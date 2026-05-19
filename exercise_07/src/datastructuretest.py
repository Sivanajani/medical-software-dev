"""Unit tests for the datastructure module."""
import unittest
import datastructure


class TestDataStructure(unittest.TestCase):
    """Tests for DataStorage, Patient, Experiment, and DataPoint."""

    def setUp(self):
        """Reset the DataStorage singleton before each test."""
        ds = datastructure.DataStorage()
        ds.patients.clear()
        ds.experiments.clear()
        ds.data.clear()

    def test_data_storage_initialization(self):
        """DataStorage should be instantiable and not None."""
        ds = datastructure.DataStorage()
        self.assertIsNotNone(ds)

    def test_data_storage_singleton(self):
        """DataStorage should return the same instance each time."""
        ds1 = datastructure.DataStorage()
        ds2 = datastructure.DataStorage()
        self.assertIs(ds1, ds2)

    def test_add_and_get_patient(self):
        """Adding a patient should make it retrievable by ID."""
        ds = datastructure.DataStorage()
        patient = datastructure.Patient("John Doe")
        ds.add_patient(patient)
        retrieved = ds.get_patient(patient.id)
        self.assertEqual("John Doe", retrieved.name)
        self.assertEqual(patient.id, retrieved.id)

    def test_get_patient_not_found(self):
        """Getting a patient with an unknown ID should return None."""
        ds = datastructure.DataStorage()
        self.assertIsNone(ds.get_patient("nonexistent-id"))

    def test_add_and_get_experiment(self):
        """Adding an experiment should make it retrievable by ID."""
        ds = datastructure.DataStorage()
        exp = datastructure.Experiment("Tremor Study")
        ds.add_experiment(exp)
        retrieved = ds.get_experiment(exp.id)
        self.assertEqual("Tremor Study", retrieved.name)
        self.assertEqual(exp.id, retrieved.id)

    def test_get_experiment_not_found(self):
        """Getting an experiment with an unknown ID should return None."""
        ds = datastructure.DataStorage()
        self.assertIsNone(ds.get_experiment("nonexistent-id"))

    def test_add_data_point(self):
        """Adding a data point should increase the data list length."""
        ds = datastructure.DataStorage()
        dp = datastructure.DataPoint("pid", "eid", {"x": 1.0})
        ds.add_data(dp)
        self.assertEqual(1, len(ds.data))
        self.assertEqual("pid", ds.data[0].patient_id)


if __name__ == '__main__':
    unittest.main()
