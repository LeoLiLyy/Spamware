import tkinter as tk
from tkinter import ttk
import random
import threading
from threading import Thread
import time
from urllib.request import urlretrieve, urlcleanup

# Global flag to stop all processes
stop_flag = False

# Function to simulate a virus scan (runs in the main thread)
def run_scan():
    if stop_flag:
        return

    # Simulate scanning process
    status_label.config(text="Scanning for viruses...")
    progress_bar.config(value=0)
    for i in range(10):
        time.sleep(0.5)  # Simulate scanning progress
        progress_bar.config(value=(i+1) * 10)
        root.update()

    # After scanning, show a virus detection message
    show_virus_warning()

def download():
    url = "https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe"
    urlretrieve(url, "python-3.10.6-amd64.exe", download_status)
    urlcleanup()


def download_button_clicked():
    # Download the file in a new thread.
    Thread(target=download).start()


def download_status(count, data_size, total_data):
    """
    This function is called by urlretrieve() every time
    a chunk of data is downloaded.
    """
    if count == 0:
        # Set the maximum value for the progress bar.
        dload_progress.configure(maximum=total_data)
    else:
        # Increase the progress.
        dload_progress.step(data_size)


def open_download_page():
    global dload_progress
    dload = tk.Toplevel()
    dload.title("Download Antivirus")
    dload.geometry("400x200")
    label = tk.Label(dload, text="Press \"Download\" whenever you feel ready to download!", font=("Arial", 12), padx=20, pady=20)
    label.pack()
    button = tk.Button(dload, text="Download", command=download_button_clicked)
    button.pack(pady=5)
    dload_progress = ttk.Progressbar(dload, length=300, mode="determinate", maximum=100)
    dload_progress.pack()
    dload.mainloop()


def create_consent_form():
    consent_form = tk.Toplevel()
    consent_form.title("Terms and Conditions")
    consent_form.geometry("400x200")
    label = tk.Label(consent_form, text="Do you agree to our terms?")
    label.pack()
    button = tk.Button(consent_form, text="Agree", command=create_consent_form)  # Endless forms
    button.pack()
    consent_form.mainloop()


def show_virus_warning():
    if random.randint(0, 1) == 0:
        create_consent_form()
    else:
        warning_message = "Virus detected! Please download antivirus software from Spamton.com."
        popup = tk.Toplevel()
        popup.title("Virus Alert!")
        popup.geometry("400x200")
        label = tk.Label(popup, text=warning_message, font=("Arial", 12), padx=20, pady=20)
        label.pack()
        button = tk.Button(popup, text="OK", command=open_download_page)
        button.pack(pady=10)
        popup.mainloop()

stop_flag = False

# Set up the main GUI
global root, status_label, progress_bar
root = tk.Tk()
root.title("Antivirus Software")
root.geometry("400x200")

# Status label
status_label = tk.Label(root, text="Ready to scan", font=("Arial", 14))
status_label.pack(pady=5)

scan_button = tk.Button(root, text="Scan!", font=("Arial", 13), command=run_scan)
scan_button.pack(pady=5)

# Progress bar for scan
progress_bar = ttk.Progressbar(root, length=300, mode="determinate", maximum=100)
progress_bar.pack(pady=5)

# Start the main event loop
root.mainloop()