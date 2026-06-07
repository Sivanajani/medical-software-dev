# Exercise 10 – Scientific Question

**Sources:** [`exercise_10.pptx`](exercise_10.pptx) · [`exercise_10.pdf`](exercise_10.pdf) · [`../exercise_09/analysis.ipynb`](../exercise_09/analysis.ipynb) · [`../exercise_09/data.json`](../exercise_09/data.json)

---

## Scientific Question

*Can a consumer smartphone's built-in accelerometer reliably detect the characteristic 4–6 Hz resting tremor associated with Parkinson's disease?*

Parkinson's disease is characterised by a resting tremor at 4 to 6 Hz, which occurs when the muscles are relaxed. The accelerometer in a smartphone measures linear acceleration along three axes (X, Y, Z). When the phone is held in the hand, tremors appear as periodic oscillations in the sensor signal. FFT frequency analysis can identify the characteristic 4 to 6 Hz tremor pattern.

---

## Data Collection

Sensor data was collected using the Sensor Data Collection App developed in Exercise 09. The data was uploaded to the Flask backend service from Exercise 07 and stored as `data.json`.

The analysis from Exercise 09 is reused directly as the data basis for this presentation. No separate data collection was performed for Exercise 10.

| Metric | Value |
|---|---|
| Device | Samsung SM-S928B |
| Sensor | lsm6dsv LSM6DSV Accelerometer Non-wakeup |
| Data points | 414 |
| Duration | ~3.55 seconds |
| Sampling rate | ~116 Hz |
| Patient ID | 3 |
| Experiment ID | 3 |

---

## Analysis

The Jupyter Notebook `exercise_09/analysis.ipynb` was used to analyze the collected data. The following analyses were performed:

**1. X / Y / Z axes over time**
Time-series plot showing raw accelerometer values including gravity. Two brief movement events are visible around sample 180 and sample 420.

**2. Total acceleration magnitude**
`magnitude = sqrt(x² + y² + z²)`
Mean magnitude of 9.8602 m/s² confirms the device was mostly stationary during the measurement.

**3. FFT frequency analysis**
The DC offset was removed by subtracting the mean per axis. FFT was applied to the detrended magnitude to identify dominant movement frequencies. The Parkinson tremor range (4 to 6 Hz) is highlighted.

**Result:** No significant peak was found in the 4 to 6 Hz range. The dominant energy is concentrated below 2 Hz, corresponding to the brief movement events. No tremor activity was detected during this measurement, as expected for a healthy subject.

---

## Presentation

The 3-slide presentation `exercise_10.pptx` covers:

| Slide | Content |
|---|---|
| 1 | Scientific question and motivation |
| 2 | Sensor used for data collection |
| 3 | Analytics results with all three plots |

The presentation is available as [`exercise_10.pptx`](exercise_10.pptx) and [`exercise_10.pdf`](exercise_10.pdf).