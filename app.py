import tkinter as tk
from datetime import datetime

logging_active = False
log_file = None

def start_logging():
    global logging_active, log_file
    logging_active = True
    log_file = open("keystrokes.txt", "a")
    log_file.write(f"\n--- Logging Started: {datetime.now()} ---\n")
    status_label.config(text="Status: Logging Started", fg="green")

def stop_logging():
    global logging_active, log_file
    logging_active = False
    if log_file:
        log_file.write(f"--- Logging Stopped: {datetime.now()} ---\n")
        log_file.close()
    status_label.config(text="Status: Logging Stopped", fg="red")

def key_pressed(event):
    if logging_active:
        key = event.keysym
        log_file.write(key + " ")

# GUI
root = tk.Tk()
root.title("Ethical Key Logger (Educational)")
root.geometry("400x300")

info = tk.Label(
    root,
    text="This program logs keys ONLY inside this window\nFor educational use only",
    fg="blue"
)
info.pack(pady=10)

start_btn = tk.Button(root, text="Start Logging", command=start_logging, bg="green", fg="white")
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop Logging", command=stop_logging, bg="red", fg="white")
stop_btn.pack(pady=5)

status_label = tk.Label(root, text="Status: Idle", fg="black")
status_label.pack(pady=10)

typing_area = tk.Label(root, text="Click here and type...", relief="solid", height=5)
typing_area.pack(fill="x", padx=20, pady=10)

root.bind("<Key>", key_pressed)

root.mainloop()
