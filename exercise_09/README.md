# Exercise 09: Data Collection App

An Android app that collects sensor data from the device and uploads it to the Exercise 07 data collection service. Collected data is analyzed using a Jupyter Notebook.

## Setup

```bash
cd exercise_09
./gradlew clean
./gradlew assembleDebug
adb install app/build/outputs/apk/debug/app-debug.apk
```

Requires **JDK 24** and Android SDK with `ANDROID_HOME` set.

## Usage

1. Start the Exercise 07 Flask service (`python3 app.py` in `exercise_07/src/`)
2. Open the app on the device
3. Select sensors and start data collection
4. Upload data to the service via the app
5. Call `POST /store` to persist data to `data.json`

## Run the Jupyter analysis

```bash
cd exercise_09
jupyter notebook analysis.ipynb
```

Or open `analysis.ipynb` directly in VS Code.

## Where to find things

| What | Where |
|---|---|
| Android app source | [`app/src/`](app/src/) |
| Collected sensor data (personal data file) | [`data.json`](data.json) |
| Jupyter Notebook analysis | [`analysis.ipynb`](analysis.ipynb) |
| App screenshot | [`img/image.png`](img/image.png) |
| Accelerometer X/Y/Z plot | [`img/accelerometer_plot.png`](img/accelerometer_plot.png) |
| Magnitude plot | [`img/magnitude_plot.png`](img/magnitude_plot.png) |
| FFT frequency plot | [`img/fft_plot.png`](img/fft_plot.png) |
| Task answers & documentation | [`exercise_09.md`](exercise_09.md) |
