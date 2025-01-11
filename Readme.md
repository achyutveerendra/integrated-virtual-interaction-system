# Integrated Virtual Interaction System: Virtual Mouse, Keyboard, and Assistant

## Overview
This project integrates three virtual applications into a single cohesive system: a **Virtual Mouse**, **Virtual Keyboard**, and **Virtual Assistant**. These applications utilize cutting-edge technologies such as **computer vision**, **speech recognition**, and **machine learning** to provide innovative functionalities that enhance user experience through natural user interfaces. 

The system allows users to interact with their computer using hand gestures and voice commands, enabling seamless control of various functions like moving the cursor, typing, opening applications, and controlling system volume.

## Features
- **Virtual Mouse**: Control the mouse pointer, click, and adjust volume using hand gestures.
- **Virtual Keyboard**: Type on a virtual keyboard using hand gestures.
- **Virtual Assistant**: Interact with the system using voice commands to execute tasks like opening applications, fetching information, and controlling the virtual mouse and keyboard.
- **Multimodal Interaction**: Supports both **gesture** and **voice**-based inputs.
- **Seamless Integration**: The virtual mouse, keyboard, and assistant work together in one unified system.

## System Architecture
- **Virtual Mouse**: Built using the Mediapipe library for hand tracking and gesture recognition.
- **Virtual Keyboard**: Uses Mediapipe for gesture recognition and displays a virtual keyboard on the screen.
- **Virtual Assistant**: Developed using Python’s Pyttsx3 for text-to-speech and SpeechRecognition for speech-to-text functionality.

## Requirements

Before running the system, make sure you have the following dependencies installed:

- **Mediapipe**: For hand tracking and gesture recognition.
- **OpenCV**: For image processing and handling webcam feeds.
- **PyAutoGUI**: For controlling the mouse cursor programmatically.
- **Pyttsx3**: For text-to-speech functionalities in the virtual assistant.
- **SpeechRecognition**: For converting spoken language into text commands.
- **Psutil**: For process management and controlling subprocesses.
- **Flask**: For serving the web interface of the virtual mouse.

You can install these dependencies by running the following command:

```bash
pip install -r requirements.txt

# To run the Application
python nova.py
