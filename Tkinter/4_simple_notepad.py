#!/usr/bin/env python3
"""
Simple Notepad Application built with Tkinter.
Features text editing, file opening, file saving, and clearing capabilities.
"""

import tkinter as tk
from tkinter import filedialog, messagebox


class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad - Untitled")
        self.root.geometry("600x400")

        # Keep track of current open file path
        self.current_filepath = None

        # Create main frame
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        # Create scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create multi-line text widget
        self.text_area = tk.Text(
            frame,
            wrap=tk.WORD,
            undo=True,
            yscrollcommand=scrollbar.set,
            font=("Courier New", 11)
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text_area.yview)

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=False)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)

        self.menu_bar.add_cascade(label="File", menu=file_menu)

    def new_file(self):
        """Clears the text area and resets file path."""
        self.text_area.delete("1.0", tk.END)
        self.current_filepath = None
        self.root.title("Simple Notepad - Untitled")

    def open_file(self):
        """Prompts user to select and open a text file."""
        filepath = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", content)
                self.current_filepath = filepath
                self.root.title(f"Simple Notepad - {filepath}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file:\n{e}")

    def save_file(self):
        """Saves current content to current file or triggers Save As if new."""
        if self.current_filepath:
            try:
                content = self.text_area.get("1.0", tk.END)
                with open(self.current_filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("Saved", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        """Prompts user for file location and saves text content."""
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            try:
                content = self.text_area.get("1.0", tk.END)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                self.current_filepath = filepath
                self.root.title(f"Simple Notepad - {filepath}")
                messagebox.showinfo("Saved", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
