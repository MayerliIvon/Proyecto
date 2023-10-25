import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import avatar.image_processing  # Adjusted import statement


class ClickableImageCanvas(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, width=200, height=200, **kwargs)
        self.config(highlightthickness=0)  # Set background color to white, remove border
        self.bind("<Button-1>", self.on_click)  # Bind left mouse button click
        self.bind("<Enter>", self.on_enter)  # Bind mouse enter event
        self.bind("<Leave>", self.on_leave)  # Bind mouse leave event
        self.create_oval(0, 0, 199, 199, tags='circle')  # Create a filled circle with tag 'circle'

    def on_click(self, event):
        # Only respond to clicks within the circle
        if (event.x - 100)**2 + (event.y - 100)**2 <= 100**2:
            self.upload_and_display_image()

    def on_enter(self, event):
        self.itemconfig('circle', fill='gray')  # Change color to gray on hover
        self.create_text(100, 100, text='Añadir foto', tags='hover_text')  # Create text with tag 'hover_text'

    def on_leave(self, event):
        self.itemconfig('circle', fill='lightgray')  # Change color back to light gray on mouse leave
        self.delete('hover_text')  # Delete text on mouse leave

    def upload_and_display_image(self):
        file_path = filedialog.askopenfilename(title='Select Image', filetypes=[("All files", "*.*")])
        if file_path:
            processed_image = image_processing.process_image(file_path)  # Call the function from image_processing module
            self.display_image(processed_image)

    def display_image(self, image):
        self.delete("all")  # Delete previous image and circle
        self.create_oval(0, 0, 200, 200, fill='lightgray', tags='circle')  # Re-create the filled circle
        photo = ImageTk.PhotoImage(image)
        self.create_image(100, 100, image=photo)  # Assumes the canvas is at least 200x200 pixels
        self.photo = photo  # Keep
