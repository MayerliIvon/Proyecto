import tkinter as tk
#from main_view import MainView  # Import the MainView class


class RegisterView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)
        self.switch_view = switch_view
        # ... other initialization code ...
        self.back_button = tk.Button(self, text="Back", command=self.come_back)  # Import the MainView class from main_view.py later in the controller
        self.back_button.pack()

    def come_back(self):
        from main_view import MainView  # Conditional import
        self.switch_view('MainView')
