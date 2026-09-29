# Human Following Robot

An autonomous human-following robot built as part of IEEE CASS Summer of Projects 2026 at BMSIT.

## Overview

This robot uses a camera and computer vision to detect a designated marker worn by a person and autonomously follow them through a given path.

A laptop processes the camera feed using computer vision and sends movement commands to the ESP32, which controls the motors through an L298N motor driver.

## Hardware

- ESP32-S3-CAM
- L298N Motor Driver
- 2 × DC Gear Motors
- Caster Wheel
- Robot Chassis
- 3 × 3.7V Batteries
- Jumper Wires
- Smartphone Camera
- Laptop

## How It Works

The camera captures a live video feed of the person.

The laptop processes the video using computer vision to detect the designated marker and determine its position.

Based on the marker's position, movement commands are sent to the ESP32.

The ESP32 controls the motors through the L298N motor driver to move the robot towards the person.

### Basic Logic

| Marker Position | Robot Action |
|-----------------|--------------|
| Center | Move forward |
| Left | Turn left |
| Right | Turn right |
| Not detected | Stop |

## Components & Connections

<table>
  <tr>
    <td><img src="media/connections.jpeg" width="300"></td>
  </tr>
</table>

### ESP32-S3-CAM → L298N

| ESP32 Pin | L298N Pin | Function |
|-----------|-----------|----------|
| GPIO 1 | ENA | Motor A PWM |
| GPIO 2 | IN1 | Motor A direction |
| GPIO 3 | IN2 | Motor A direction |
| GPIO 14 | IN3 | Motor B direction |
| GPIO 41 | IN4 | Motor B direction |
| GPIO 42 | ENB | Motor B PWM |

## Computer Vision

The laptop processes the camera feed using Python and computer vision.

The project uses:

- OpenCV
- NumPy
- PySerial

OpenCV is used for camera and computer vision processing, NumPy for image/data processing, and PySerial for communication with the ESP32.

## Camera

A smartphone mounted on the robot is used as the camera.

The phone runs an IP Webcam application and provides a live video stream to the laptop.

The camera is positioned so that the person and designated marker remain visible in the frame.

## Software

- Python
- OpenCV
- NumPy
- PySerial
- Arduino IDE
- ESP32 board support
- C/C++

## Project Photos

<table>
  <tr>
    <td><img src="media/robo3.1.jpeg" width="300"></td>
    <td><img src="media/robo3.2.jpeg" width="300"></td>
    <td><img src="media/robo3.3.jpeg" width="300"></td>
  </tr>
</table>

## What I Learned

- Basic computer vision
- RGB and HSV colour spaces
- Colour detection and thresholding
- Contour detection
- Object position tracking
- OpenCV camera processing
- Python and NumPy
- Serial communication using PySerial
- ESP32 motor control
- Integrating computer vision with robotics

## Project Outcome

Successfully built and tested a vision-based robot designed to detect a designated marker and follow a person using computer vision and autonomous motor control.

## Future Improvements

- Improve marker detection accuracy
- Improve tracking under different lighting conditions
- Reduce camera processing delay
- Improve movement and turning response
