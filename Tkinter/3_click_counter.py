#!/usr/bin/env python3
"""
Click Counter Application built with Tkinter.
Allows users to increment, decrement, and reset a tally counter.
"""

import tkinter as tk


class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Counter")
        self.root.geometry("250x200")
        self.root.resizable(False, False)

        # Initialize counter variable
        self.count = 0

        # Display label for current count
        self.count_label = tk.Label(
            root, text=str(self.count), font=("Helvetica", 36, "bold")
        )
        self.count_label.pack(pady=15)

        # Frame container for action buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Decrement button (-)
        self.btn_decrement = tk.Button(
            button_frame, text="-", width=5, font=("Helvetica", 14), command=self.decrement
        )
        self.btn_decrement.grid(row=0, column=0, padx=5)

        # Reset button (Reset)
        self.btn_reset = tk.Button(
            button_frame, text="Reset", width=6, font=("Helvetica", 12), command=self.reset
        )
        self.btn_reset.grid(row=0, column=1, padx=5)

        # Increment button (+)
        self.btn_increment = tk.Button(
            button_frame, text="+", width=5, font=("Helvetica", 14), command=self.increment
        )
        self.btn_increment.grid(row=0, column=2, padx=5)

    def update_display(self):
        """Updates the text and color of the counter display label."""
        self.count_label.config(text=str(self.count))
        if self.count > 0:
            self.count_label.config(fg="green")
        elif self.count < 0:
            self.count_label.config(fg="red")
        else:
            self.count_label.config(fg="black")

    def increment(self):
        """Increments the counter by 1."""
        self.count += 1
        self.update_display()

    def decrement(self):
        """Decrements the counter by 1."""
        self.count -= 1
        self.update_display()

    def reset(self):
        """Resets the counter to 0."""
        self.count = 0
        self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCounterApp(root)
    root.mainloop()
