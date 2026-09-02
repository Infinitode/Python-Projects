#!/usr/bin/env python3
# Made by @Ericwasepic127 - with Helpful comments

import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("Text Toggle App")

# Create the toggle button
button = tk.Button(root, text="Disable")
button.pack(fill=tk.X, padx=10, pady=(10, 5))

# Create a multi-line text input field
text = tk.Text(root, height=10, width=40)
text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))


def toggle(btn, txt):
    """
    Higher-order function that creates a closure binding the button and text widgets.
    Returns a handler function that toggles the text box state and button text.
    """
    def func():
        # Check current button label to determine action
        if btn["text"] == "Disable":
            btn["text"] = "Enable"
            txt["state"] = "disabled"  # Locks the text box from editing
        else:
            btn["text"] = "Disable"
            txt["state"] = "normal"    # Restores text box editability

    return func


# Assign the generated closure function to the button's click event
button.config(command=toggle(button, text))

# Start the Tkinter event loop
root.mainloop()
