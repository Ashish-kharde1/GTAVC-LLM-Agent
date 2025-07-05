import mss
import numpy as np
import cv2

sct = mss.mss()
monitor = sct.monitors[1]  # change if you need another monitor

def capture_frame():
    """
    Capture the full screen and return a BGR image.
    """
    s = sct.grab(monitor)
    img = np.array(s)
    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
