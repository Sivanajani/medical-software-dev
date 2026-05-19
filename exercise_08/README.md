# Exercise 08 – Android Sensor Overview

An Android app that displays device information and all available sensors on the device.

## Setup

Clone the source code from FHNW GitLab:

```
https://gitlab.fhnw.ch/david.herzig/androidsensoroverview
```

Android Studio and JDK 17 are required.

## Usage

Build the app using the Gradle Wrapper on Windows:

```powershell
.\gradlew.bat clean
.\gradlew.bat assembleDebug
```

Then open the project in Android Studio, connect an Android device via USB with USB debugging enabled, and run the app directly from the IDE.

## Output

The app shows two sections:

- **Device Information**: manufacturer, model, Android version, API level, screen resolution, screen density, total RAM
- **Available Sensors**: a list of all sensors present on the device

## Where to find things

| What | Where |
|---|---|
| Android project | `app/` |
| APK output | `app/build/outputs/apk/debug/app-debug.apk` |
| Screenshots | `screenshots/` |
| Discussion & answers | [`exercise_08.md`](exercise_08.md) |

## Data source

Source code cloned from:

```
https://gitlab.fhnw.ch/david.herzig/androidsensoroverview
```
