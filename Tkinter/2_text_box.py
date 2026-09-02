#!/usr/bin/env python3
# Made by @Ericwasepic127 - with Helpful comments

import tkinter as tk # Imports Tkinter module shortcuting as tk

root = tk.Tk() # Make window object

button = tk.Button( # Make Button
  root, # to this window
  text="Disable" # Display this string
)
button.pack(fill=tk.BOTH) # Show button

text = tk.Text( # Make text box
  root # to this window
)
text.pack(fill=tk.BOTH) # Show text box

def toggle(btn, txt): # Let's make function to toggle
  # To avoid any local and global thing mess up, 
  # let's make a wrapper-like function
  def func():
    if btn["text"] == "Disable": # Get text from button, and if it's Disable
      # Instead using dict-like setting, you can use .config method 
      # I prefer dict-like setting 
      # You can see usage below 
      btn["text"] = "Enable"
      txt["state"] = "disabled"
    else: # in case disabled 
      btn["text"] = "Disable"
      txt["state"] = "normal" # means editable
  return func

# instead dict-like setting
button.config(command=toggle(button, text))

root.mainloop()
