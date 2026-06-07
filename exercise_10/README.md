# Exercise 10 – Digital Biomarker Scientific Question

A data analytics task exploring whether a smartphone accelerometer can detect Parkinson's disease tremor.

## Scientific Question

*Can a consumer smartphone's built-in accelerometer reliably detect the characteristic 4–6 Hz resting tremor associated with Parkinson's disease?*

## Files

| File | Description |
|---|---|
| [`exercise_10.md`](exercise_10.md) | Discussion and analysis writeup |
| [`exercise_10.pptx`](exercise_10.pptx) | 3-slide presentation |
| [`exercise_10.pdf`](exercise_10.pdf) | 3-slide presentation (PDF export) |
| [`../exercise_09/analysis.ipynb`](../exercise_09/analysis.ipynb) | Jupyter Notebook with full analysis |
| [`../exercise_09/data.json`](../exercise_09/data.json) | Raw sensor data (414 data points) |

## Data

Collected with the Sensor Data Collection App (Exercise 09) on a Samsung SM-S928B using the LSM6DSV accelerometer at ~116 Hz.

## Analysis

Three analyses in the Jupyter Notebook:

1. **X/Y/Z time-series:** raw accelerometer values over time
2. **Magnitude:** `sqrt(x² + y² + z²)`, mean ~9.86 m/s² (~1g, device stationary)
3. **FFT:** frequency spectrum with Parkinson tremor range (4–6 Hz) highlighted

No 4–6 Hz peak detected, which is the expected baseline result for a healthy subject.
