# Filename: main.py

import tkinter as tk
from avatar.add_profile_picture import ClickableImageCanvas  # Import the ClickableImageCanvas class

root = tk.Tk()
root.title("Profile Image Uploader")

canvas = ClickableImageCanvas(root)
canvas.pack(pady=20)

root.mainloop()
