import tkinter as tk
from tkinter import messagebox
import os
import subprocess

def run_batch_file(filename):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    cleaners_path = os.path.join(current_directory, 'Cleaners')
    batch_file_path = os.path.join(cleaners_path, filename)

    if not os.path.exists(batch_file_path):
        messagebox.showerror("ForeCleaner", f"{filename} not found!")
        return

    try:
        subprocess.run(batch_file_path, shell=True)
        messagebox.showinfo("ForeCleaner", f"Executed {filename} successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not execute {filename}. Reason: {e}")

app = tk.Tk()
app.title("ForeCleaner")

# Define colors
BLACK = "#000000"
DARK_GREY = "#222222"
LIGHT_GREY = "#AAAAAA"
WHITE = "#FFFFFF"

# Set app theme
app.configure(bg=BLACK)

# App title
title = tk.Label(app, text="ForeCleaner", font=("Arial", 24, "bold"), fg=LIGHT_GREY, bg=BLACK)
title.pack(pady=20)

# App tagline
tagline = tk.Label(app, text="The Ultimate Fortnite Trace Cleaner", font=("Arial", 14), fg=LIGHT_GREY, bg=BLACK)
tagline.pack(pady=10)

# Standard Cleaners
clean_light_button = tk.Button(app, text="Clean Light", font=("Arial", 16), command=lambda: run_batch_file('light.bat'), bg=DARK_GREY, fg=WHITE, borderwidth=0)
clean_light_button.pack(pady=10)

clean_basic_button = tk.Button(app, text="Clean Basic", font=("Arial", 16), command=lambda: run_batch_file('Cleaner.bat'), bg=DARK_GREY, fg=WHITE, borderwidth=0)
clean_basic_button.pack(pady=10)

clean_moderate_button = tk.Button(app, text="Clean Moderate", font=("Arial", 16), command=lambda: run_batch_file('cleaner_1.bat'), bg=DARK_GREY, fg=WHITE, borderwidth=0)
clean_moderate_button.pack(pady=10)

clean_advanced_button = tk.Button(app, text="Clean Advanced", font=("Arial", 16), command=lambda: run_batch_file('cleaner_2.bat'), bg=DARK_GREY, fg=WHITE, borderwidth=0)
clean_advanced_button.pack(pady=10)

# Break section
break_label = tk.Label(app, text="Advanced Cleaners", font=("Arial", 18, "underline"), fg=LIGHT_GREY, bg=BLACK)
break_label.pack(pady=20)

deep_cleaner_button = tk.Button(app, text="Deep Cleaner", font=("Arial", 16), command=lambda: run_batch_file('Deep.bat'), bg=DARK_GREY, fg=WHITE, borderwidth=0)
deep_cleaner_button.pack(pady=10)

adv_deep_cleaner_button = tk.Button(app, text="Advanced Deep Clean", font=("Arial", 16), command=lambda: run_batch_file('Deepcleaner.bat'), bg=DARK_GREY, fg=WHITE, borderwidth=0)
adv_deep_cleaner_button.pack(pady=10)

app.mainloop()
