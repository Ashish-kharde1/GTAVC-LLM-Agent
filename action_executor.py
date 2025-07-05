import pyautogui
import time

KEY_MAP = {
    "forward": "w",
    "backward": "s",
    "left": "a",
    "right": "d",
    "brake": "s",
    "enter": "enter",
    "stop": None
}

def execute_action(action: str, duration: float = 0.2):
    """
    Press the mapped key for `duration` seconds.
    """
    key = KEY_MAP.get(action)
    if not key:
        return
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)
