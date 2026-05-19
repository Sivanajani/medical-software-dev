"""Flask REST API for the data collection service."""
import json
import logging
import os

from flask import Flask, jsonify, make_response, request

import datastructure

app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("backendservice.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def load_environment():
    """Load environment variables from a JSON config file."""
    env_var = os.environ.get('WORKING_ENV', 'dev_env.json')
    assert os.path.exists(env_var), f"Environment file not found: {env_var}"
    with open(env_var, encoding='utf-8') as f:
        env_values = json.loads(f.read())
    logger.info("Loaded environment from %s", env_var)
    return env_values


@app.route('/', methods=['GET'])
def index():
    """Return basic service information."""
    logger.debug("GET /")
    return json.dumps({
        'name': 'David',
        'mail': 'fhnw@roche.ch',
        'System': 'Digital Biomarker Course Project',
        'Server Component': 'v1_0_0',
        'Date': '7-Apr-2026'
    })


@app.route('/experiment', methods=['POST', 'GET'])
def experiment_action():
    """Create or retrieve an experiment."""
    ds = datastructure.DataStorage()
    if request.method == 'POST':
        body = request.get_json()
        assert body is not None, "Request body must be JSON"
        assert 'name' in body, "Field 'name' is required"
        name = body['name']
        assert isinstance(name, str) and name.strip(), "Experiment name must be a non-empty string"
        experiment_obj = datastructure.Experiment(name)
        ds.add_experiment(experiment_obj)
        logger.info("Created experiment: id=%s name=%s", experiment_obj.id, name)
        return jsonify(experiment_obj.__dict__)
    if request.method == 'GET':
        exp_id = request.args.get('id')
        result = ds.get_experiment(exp_id)
        if result is None:
            logger.warning("Experiment not found: id=%s", exp_id)
            return make_response(jsonify('experiment not found'), 404)
        logger.debug("Retrieved experiment: id=%s", exp_id)
        return make_response(jsonify(result.__dict__), 200)
    return make_response(jsonify('method not allowed'), 405)


@app.route('/patient', methods=['POST', 'GET'])
def patient_action():
    """Create or retrieve a patient."""
    ds = datastructure.DataStorage()
    if request.method == 'POST':
        body = request.get_json()
        assert body is not None, "Request body must be JSON"
        assert 'name' in body, "Field 'name' is required"
        name = body['name']
        assert isinstance(name, str) and name.strip(), "Patient name must be a non-empty string"
        patient_obj = datastructure.Patient(name)
        ds.add_patient(patient_obj)
        logger.info("Created patient: id=%s name=%s", patient_obj.id, name)
        return jsonify(patient_obj.__dict__)
    if request.method == 'GET':
        patient_id = request.args.get('id')
        result = ds.get_patient(patient_id)
        if result is None:
            logger.warning("Patient not found: id=%s", patient_id)
            return make_response(jsonify('patient not found'), 404)
        logger.debug("Retrieved patient: id=%s", patient_id)
        return make_response(jsonify(result.__dict__), 200)
    return make_response(jsonify('method not allowed'), 405)


@app.route('/patients', methods=['GET'])
def patients_action():
    """Return all patients."""
    ds = datastructure.DataStorage()
    logger.debug("GET /patients – count=%d", len(ds.patients))
    return json.dumps(ds.patients, cls=datastructure.PatientEncoder)


@app.route('/experiments', methods=['GET'])
def experiments_action():
    """Return all experiments."""
    ds = datastructure.DataStorage()
    logger.debug("GET /experiments – count=%d", len(ds.experiments))
    return json.dumps(ds.experiments, cls=datastructure.ExperimentEncoder)


@app.route('/store', methods=['POST'])
def store_data():
    """Persist current data to JSON files."""
    ds = datastructure.DataStorage()
    ds.store_data()
    logger.info("Data stored to disk")
    return make_response(jsonify("True"), 200)


@app.route('/upload', methods=['POST'])
def upload_data():
    """Upload a sensor data point linked to a patient and experiment."""
    ds = datastructure.DataStorage()
    body = request.get_json()
    assert body is not None, "Request body must be JSON"
    assert 'patientId' in body, "Field 'patientId' is required"
    assert 'experimentId' in body, "Field 'experimentId' is required"
    patient_id = body['patientId']
    experiment_id = body['experimentId']
    data_obj = datastructure.DataPoint(patient_id, experiment_id, body)
    ds.add_data(data_obj)
    logger.info("Uploaded data: patient=%s experiment=%s", patient_id, experiment_id)
    return make_response('', 200)


if __name__ == '__main__':
    logger.debug('Starting service...')
    load_environment()
    storage = datastructure.DataStorage()
    storage.load_data()
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
