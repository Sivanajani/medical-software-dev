# Exercise 07 – Data Collection Service

A Flask REST API that collects sensor data from patients and experiments. The service stores patients, experiments, and data points in memory and persists them to JSON files on disk.

## Setup

```bash
cd exercise_07/src
pip install -r requirements.txt
```

## Usage

Start the service:

```bash
python3 app.py
```

The service runs on `http://localhost:5000`.

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Service info |
| POST | `/patient` | Create a patient |
| GET | `/patient?id=` | Get patient by ID |
| GET | `/patients` | Get all patients |
| POST | `/experiment` | Create an experiment |
| GET | `/experiment?id=` | Get experiment by ID |
| GET | `/experiments` | Get all experiments |
| POST | `/upload` | Upload a sensor data point |
| POST | `/store` | Persist data to JSON files |

## Run unit tests

```bash
cd exercise_07/src
python3 -m unittest datastructuretest.py -v
```

## Run performance tests

Start the service first, then in a second terminal:

```bash
cd exercise_07/src
python3 performance_test.py
```

## Where to find things

| What | Where |
|---|---|
| Flask API | [`src/app.py`](src/app.py) |
| Data classes (Patient, Experiment, DataPoint, DataStorage) | [`src/datastructure.py`](src/datastructure.py) |
| ID generator | [`src/idgenerator.py`](src/idgenerator.py) |
| Unit tests | [`src/datastructuretest.py`](src/datastructuretest.py) |
| Performance test script | [`src/performance_test.py`](src/performance_test.py) |
| Dependencies | [`src/requirements.txt`](src/requirements.txt) |
| Log file (generated at runtime) | `src/backendservice.log` |
| Persisted data (generated at runtime) | `src/patients.json`, `src/experiments.json`, `src/data.json` |
| Task answers & documentation | [`exercise_07.md`](exercise_07.md) |
| Postman screenshots | [`screenshots/`](screenshots/) |
