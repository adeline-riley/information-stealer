import pyautogui

def capture_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        print("[+] Screenshot captured successfully.")
    except Exception as e:
        print(f"[-] Error capturing screenshot: {e}")