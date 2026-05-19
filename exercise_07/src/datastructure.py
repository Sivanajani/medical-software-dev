"""Data structures for patients, experiments, and sensor data points."""
import json
import os

import idgenerator


class Patient:  # pylint: disable=too-few-public-methods
    """Represents a patient in an experiment."""

    def __init__(self, name, patient_id=None):
        self.name = name
        if patient_id is None:
            id_gen = idgenerator.AlphaNumericIDGenerator()
            self.id = id_gen.get_id()
        else:
            self.id = patient_id


class PatientEncoder(json.JSONEncoder):
    """JSON encoder for Patient objects."""

    def default(self, o):
        """Serialize object to a dict."""
        return o.__dict__


class Experiment:  # pylint: disable=too-few-public-methods
    """Represents an experiment."""

    def __init__(self, name, experiment_id=None):
        self.name = name
        if experiment_id is None:
            id_gen = idgenerator.AlphaNumericIDGenerator()
            self.id = id_gen.get_id()
        else:
            self.id = experiment_id


class ExperimentEncoder(json.JSONEncoder):
    """JSON encoder for Experiment objects."""

    def default(self, o):
        """Serialize object to a dict."""
        return o.__dict__


class DataPoint:  # pylint: disable=too-few-public-methods
    """Represents a single sensor data point linked to a patient and experiment."""

    def __init__(self, patient_id, experiment_id, data):
        id_gen = idgenerator.AlphaNumericIDGenerator()
        self.id = id_gen.get_id()
        self.patient_id = patient_id
        self.experiment_id = experiment_id
        self.data = data


class DataPointEncoder(json.JSONEncoder):
    """JSON encoder for DataPoint objects."""

    def default(self, o):
        """Serialize object to a dict."""
        return o.__dict__


class DataStorage:
    """Singleton storage for patients, experiments, and data points."""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.instance.experiments = {}
            cls.instance.patients = {}
            cls.instance.data = []
        return cls.instance

    def add_patient(self, obj):
        """Add a patient to storage."""
        self.patients[obj.id] = obj

    def get_patient(self, patient_id):
        """Return patient by ID, or None if not found."""
        return self.patients.get(patient_id)

    def add_experiment(self, obj):
        """Add an experiment to storage."""
        self.experiments[obj.id] = obj

    def get_experiment(self, experiment_id):
        """Return experiment by ID, or None if not found."""
        return self.experiments.get(experiment_id)

    def add_data(self, obj):
        """Add a data point to storage."""
        self.data.append(obj)

    def store_data(self):
        """Persist patients, experiments, and data points to JSON files."""
        with open('patients.json', 'w', encoding='utf-8') as pf:
            pf.write(json.dumps(self.patients, cls=PatientEncoder))
        with open('experiments.json', 'w', encoding='utf-8') as ef:
            ef.write(json.dumps(self.experiments, cls=ExperimentEncoder))
        with open('data.json', 'w', encoding='utf-8') as df:
            df.write(json.dumps(self.data, cls=DataPointEncoder))
        self.data.clear()

    def load_data(self):
        """Load patients and experiments from JSON files if they exist."""
        if os.path.exists('patients.json'):
            with open('patients.json', 'r', encoding='utf-8') as file:
                for val in json.load(file).values():
                    obj = Patient(val['name'], val['id'])
                    self.patients[val['id']] = obj

        if os.path.exists('experiments.json'):
            with open('experiments.json', 'r', encoding='utf-8') as file:
                for val in json.load(file).values():
                    obj = Experiment(val['name'], val['id'])
                    self.experiments[val['id']] = obj
