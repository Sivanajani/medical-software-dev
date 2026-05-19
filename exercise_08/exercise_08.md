# Exercise 08 – Android Sensor Overview

## Build & Run

The app was built on Windows using the Gradle Wrapper (`gradlew.bat`) with JDK 17, since Gradle was not installed system-wide:

```powershell
.\gradlew.bat clean
.\gradlew.bat assembleDebug
```

The APK is generated at `app/build/outputs/apk/debug/app-debug.apk`.

The app was deployed and run from Android Studio. The device (Samsung SM-S928B) was connected via USB with USB debugging enabled.

![Android Studio Build](screenshots/image.png)

## Questions

### 1. Screenshot of the app output

Device: Samsung SM-S928B, Android 16, API Level 36

![Sensor Overview Part 1](screenshots/01_sensor_overview.jpeg)
![Sensor Overview Part 2](screenshots/02_sensor_overview.jpeg)

### 2. Which sensor could be used to measure Parkinson's disease?

Parkinson's is known for tremors, which is involuntary shaking mostly in the hands.

The Accelerometer measures acceleration and movement. When holding the phone in the hand, it can detect the shaking as small rapid movements. This makes it useful for tracking Parkinson's symptoms.

There are many studies using smartphones with accelerometers to track and measure Parkinson's symptoms. In the app, the sensor `lsm6dsv LSM6DSV Accelerometer` is visible, which is exactly the accelerometer on the Samsung device used for this exercise.