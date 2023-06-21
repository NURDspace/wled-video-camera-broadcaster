# wled-video-camera-broadcaster
This Python script allows users to stream video content from a file or webcam directly to a WLED device. It also displays the video content in a GUI for visual reference. The script is designed for a 2D 6x26 pixel LED panel, but it can be adjusted for different setups.

# Features

Stream video files or webcam footage in real time to a WLED device.
Display the current video frame being streamed in a graphical user interface.
Control the video stream with options to start and stop.

# Requirements

    Python 3
    OpenCV
    NumPy
    Pillow
    tkinter

These can be installed via pip:

    pip install opencv-python numpy pillow

# Usage
Start the script:

    python3 wled-video.py

In the GUI, use the "Select video and start stream" button to select a video file and start the stream.
Use the "Start webcam stream" button to start streaming from the webcam.
Use the "Stop stream" button to stop the current stream.

# Configuration
Set your WLED device's IP address and port in the script.
Adjust the pixel resolution according to your LED panel setup.

# Implementation Details

The script uses the OpenCV library to capture frames from the video source and scale them down to the resolution of the LED panel.
These frames are then sent over UDP to the WLED device for display.
The script also displays the current frame in the GUI, scaled up for easier viewing.

# Limitations

The script is designed for a specific LED panel setup (2D 6x26 pixel panel). You may need to modify the script for different panel configurations.
The frame rate of the video stream depends on the processing speed of your computer and the network speed between your computer and the WLED device. You may need to adjust the delay between frames for optimal results.

# Future Work

Add support for different LED panel configurations.
Improve the frame rate of the video stream.
Add more control options in the GUI, such as adjusting the frame rate or selecting the network interface for the UDP stream.

Please feel free to contribute and make improvements to the script!
