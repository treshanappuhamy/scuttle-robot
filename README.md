# Scuttle Robot

Scuttle is a programmable robot designed for educational purposes and experimentation in robotics. It is a four-legged robot with a modular design that allows users to customize its functionality and behavior. This project details the setup and configuration of the Scuttle Robot, including flashing the Raspberry Pi SD card, configuring the robot, and using various sensors and components.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Flashing the Raspberry Pi SD Card](#flashing-the-raspberry-pi-sd-card)
  - [Initial Configuration](#initial-configuration)
  - [Cloud9 IDE Setup](#cloud9-ide-setup)
  - [Node-RED Setup](#node-red-setup)
- [Components and Modules](#components-and-modules)
  - [Camera](#camera)
  - [Encoders](#encoders)
  - [Gamepad](#gamepad)
- [Fault Diagnosis](#fault-diagnosis)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Scuttle Robot is designed for easy customization with add-ons such as cameras, ultrasonic sensors, and servo motors. This allows for a wide range of functionalities and behaviors to be implemented, making it a versatile platform for learning and experimentation.

## Prerequisites

Before starting, ensure you have the following:
- Scuttle Robot Full Kit
- Raspberry Pi with accessories (SD card, power supply, etc.)
- SD card flashed with Scuttle Raspbian OS
- Access to a computer on the same network as the Raspberry Pi

## Setup

### Flashing the Raspberry Pi SD Card

1. **Download Scuttle Raspbian OS Image:**
   Download the Scuttle Raspbian OS image from [this link](https://drive.google.com/file/d/1xwpaLW83OHBvmmy3Hy2JRXO0YdhzJjme/view).

2. **Flash the SD Card:**
   Use Raspberry Pi Imager or a similar tool to flash the downloaded OS image onto the SD card.

### Initial Configuration

1. **Boot the Raspberry Pi:**
   Insert the SD card into the Raspberry Pi, connect it to an external display and keyboard, and power it on.

2. **Enable SSH and WiFi:**
   Add an `ssh` file and a `wpa_supplicant.conf` file to the boot directory of the SD card to enable SSH and configure WiFi.

3. **Connect via SSH:**
   Once the Raspberry Pi is connected to the network, SSH into it from your computer using the default credentials (username: `pi`, password: `scuttle`).

4. **Configure Raspberry Pi:**
   Use `raspi-config` to enable necessary interfaces such as GPIO, I2C, and SPI.

### Cloud9 IDE Setup

1. **Install Cloud9 IDE:**
   Configure Cloud9 IDE on the Raspberry Pi OS to access it from any PC on the same network. Cloud9 allows building, launching, and debugging programs directly from the browser.

2. **Access Cloud9:**
   Open a web browser and navigate to `http://scuttle.local:8080` to access Cloud9.

### Node-RED Setup

1. **Install Node-RED:**
   Install Node-RED on the Raspbian OS and access it using `http://scuttle.local:1880` from any PC on the same network.

## Components and Modules

### Camera

1. **Setup Camera:**
   Attach a USB camera to the front of the SCUTTLE to take pictures of the scene.

2. **Stream Images:**
   Use Node-RED and a Python script to stream and filter images for object tracking.

   - Run in Cloud9 terminal:
     ```bash
     cd Module1-Camera
     bash start_mjpg_streamer_pi.sh L3_image_filter.py
     ```
   - Adjust colors using Node-RED dashboard:
     `http://scuttle.local:1880/ui/#!/2?socketid=O4di0kaVc15snu4uAAAA`
   - View livestream:
     `http://scuttle.local:8090/stream.html`

### Encoders

1. **Setup Encoders:**
   Encoders track the location of the axles and transform wheel speeds into distance and angle measurements.

   - Run in Cloud9 terminal:
     ```bash
     cd Module2-Encoder
     python3 L1_encoder.py
     ```
   - View encoder changes on Node-RED dashboard:
     `http://scuttle.local:1880/ui/#!/0?socketid=e7uwXb08-HVQvzQYAAAD`

### Gamepad

1. **Setup Gamepad:**
   Use a gamepad for manually controlling the SCUTTLE's motion and visualize the changes using Node-RED.

   - Run in Cloud9 terminal:
     ```bash
     cd Module3-Gamepad
     python3 L3_gpDemo.py
     ```
   - View live changes on Node-RED dashboard:
     `http://scuttle.local:1880/ui/#!/1?socketid=DXLHVH2nIdf4nZmDAAAC`

## Fault Diagnosis

1. **Encoder Replacement:**
   If an encoder is detected as defective, contact the local support team for a replacement and rewire according to the official SCUTTLE wiring guide.

2. **Joystick and Motor Testing:**
   Test the joystick using a Python script, and if movements are inverse, check the motor drive with a multimeter and reverse the wiring if necessary.

3. **LiDAR Visualization:**
   Install ROS Noetic on Ubuntu 20.04 in a VM to visualize the YD LiDAR X2 sensor.

   - Install YDLidar-SDK:
     ```bash
     git clone https://github.com/YDLIDAR/YDLidar-SDK
     cd YDLIDAR-SDK
     mkdir build
     cd build
     cmake ..
     make
     sudo make install
     ```
   - Install ydlidar ros drivers:
     ```bash
     git clone https://github.com/YDLIDAR/ydlidar_ros_driver
     cd ydlidar_ros_driver
     catkin_make
     ```
   - Visualize LiDAR data:
     ```bash
     roslaunch ydlidar_ros_driver lidar_view.launch
     ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or enhancements.

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.
