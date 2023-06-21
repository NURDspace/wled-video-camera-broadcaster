import os
import socket
import time
import cv2
import subprocess
import glob
import threading
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# You may need to install opencv-python, numpy, and pillow with pip
import numpy as np

class WLEDStreamer:
    def __init__(self, wled_ip, wled_port, label):
        self.wled_ip = wled_ip
        self.wled_port = wled_port
        self.label = label
        self.thread = None
        self.running = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self, video_path=None):
        if self.running:
            return

        self.running = True
        self.thread = threading.Thread(target=self.stream, args=(video_path,))
        self.thread.start()

    def stop(self):
        if not self.running:
            return

        self.running = False
        self.thread.join()

    def stream(self, video_path):
        if video_path is None:
            cap = cv2.VideoCapture(0)
        else:
            cap = cv2.VideoCapture(video_path)

        while self.running:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Resize the image
            frame = cv2.resize(frame, (26, 6))

            # Display the image in the GUI
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = image.resize((26*15, 6*15))  # Resize for display
            photo = ImageTk.PhotoImage(image)
            self.label.config(image=photo)
            self.label.image = photo

            # Convert frame to raw RGB data and send to WLED device
            rgb_data = frame.tobytes()
            self.sock.sendto(b'\x02\x05' + rgb_data, (self.wled_ip, self.wled_port))

            # Sleep for a bit before sending the next frame
            time.sleep(0.05)

        # When everything done, release the capture
        cap.release()

def select_video_and_start_stream(streamer):
    # Open a file dialog to select the video file
    video_path = filedialog.askopenfilename()

    # Start the video stream
    streamer.start(video_path)

# Create the GUI window
window = tk.Tk()
wled_ip = '10.208.3.3'  # replace with your WLED device's IP address
wled_port = 21324  # replace with your WLED device's port
label = tk.Label(window)
label.pack()
streamer = WLEDStreamer(wled_ip, wled_port, label)
start_video_button = tk.Button(window, text="Select video and start stream", command=lambda: select_video_and_start_stream(streamer))
start_video_button.pack()
start_webcam_button = tk.Button(window, text="Start webcam stream", command=streamer.start)
start_webcam_button.pack()
stop_button = tk.Button(window, text="Stop stream", command=streamer.stop)
stop_button.pack()
window.mainloop()
