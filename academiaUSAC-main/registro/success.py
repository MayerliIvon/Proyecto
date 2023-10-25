import globals
import tkinter as tk
from tkinter import Label, Button


class SuccessView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)

        self.master = master
        self.switch_view = switch_view

        # Container frame with padding
        self.container = tk.Frame(self)
        self.container.pack(padx=50, pady=50, expand=True)

        # Configure grid to expand
        self.container.grid_columnconfigure(0, weight=1)  # Allow column to expand
        self.container.grid_rowconfigure((1, 2), weight=1)  # Allow rows to expand

        # Title
        self.title_label = Label(self.container, text="Registrado Exitoso", font=("Helvetica", 50))
        self.title_label.grid(row=1, column=0, pady=(0, 20), sticky='nsew')  # Centered alignment

        # Buttons
        self.left_button = Button(self.container, text="Back", font=("Helvetica", 16), command=self.come_back)
        self.left_button.grid(row=2, column=0, pady=20, sticky='nsew')  # Centered alignment

    def come_back(self):
        import sys
        import os
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        from main_view import MainView  # Conditional import
        self.switch_view('MainView')