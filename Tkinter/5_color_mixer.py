"""Explore RGB colors with sliders and copy the resulting hex code."""

import tkinter as tk


def rgb_to_hex(red, green, blue):
    """Convert three 0-255 RGB channels to a six-digit hex color."""
    channels = (red, green, blue)
    if any(not isinstance(channel, int) or not 0 <= channel <= 255
           for channel in channels):
        raise ValueError("RGB channels must be integers from 0 to 255.")
    return "#{:02X}{:02X}{:02X}".format(*channels)


class ColorMixer:
    def __init__(self, root):
        self.root = root
        root.title("RGB Color Mixer")
        root.geometry("360x340")

        tk.Label(root, text="Move the sliders to mix a color").pack(pady=10)
        self.sliders = []
        for name, value in (("Red", 128), ("Green", 128), ("Blue", 128)):
            slider = tk.Scale(root, label=name, from_=0, to=255,
                              orient=tk.HORIZONTAL, length=280)
            slider.set(value)
            slider.pack()
            self.sliders.append(slider)

        for slider in self.sliders:
            slider.config(command=self.update_color)

        self.preview = tk.Label(root, text="Color preview", width=25, height=2)
        self.preview.pack(pady=8)
        self.hex_label = tk.Label(root, font=("TkDefaultFont", 12))
        self.hex_label.pack()
        tk.Button(root, text="Copy hex code", command=self.copy_hex).pack(pady=8)
        self.update_color()

    def update_color(self, *_):
        color = rgb_to_hex(*(slider.get() for slider in self.sliders))
        self.preview.config(bg=color)
        self.hex_label.config(text=color)

    def copy_hex(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.hex_label.cget("text"))
        self.root.update()  # Keep the clipboard available after closing the window.


if __name__ == "__main__":
    root = tk.Tk()
    ColorMixer(root)
    root.mainloop()
