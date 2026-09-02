#!/usr/bin/env python3
# Made by @Ericwasepic127 - With guided comments

import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("Hello World App")

# Create and position a simple text label
label = tk.Label(root, text="Hello, World!")
label.pack(padx=10, pady=10)

# Create a quit button that closes the window when clicked
# Note: Assign the function reference (root.destroy), do not call it with ()
button = tk.Button(root, text="Quit", command=root.destroy)
button.pack(fill=tk.X, padx=10, pady=5)

# Start the Tkinter event loop
# Keeps the application running and listening for user interactions (clicks, keypresses)
root.mainloop()
