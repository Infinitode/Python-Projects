#!/usr/bin/env python3
# Made by @Ericwasepic127 - With guided comments

import tkinter as tk # Imports Tkinter module, shortcuts to tk

root = tk.Tk() # Make window

label = tk.Label( # Make Label widget
  root, # Say to THIS window
  text="Hello, World!" # Display THIS string given
)
label.pack() # Show the widget in window

button = tk.Button( # Make Button widget
  root, # Say to THIS window
  text="Quit", # Display THIS string
  command=root.destroy # Run THIS command on click
)
button.pack( # Show widget in window
  fill=tk.BOTH # Fill Left and Right
)

root.mainloop() # Run until window closes
# If you don't add root.mainloop(), the python program ends, causing window close immediately
