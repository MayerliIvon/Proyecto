# overview.py
import tkinter as tk
from main_view import MainView
 # Vistas de Registro
from registro.personal_data import PersonalDataView 
from registro.user_data import UserDataView
from registro.contact_data import ContactDataView
from registro.success import SuccessView

class AppController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Academia USAC")
        self.attributes('-fullscreen', True)
        self.current_view = None
        self.view_classes = {
            'MainView': MainView,
            'PersonalDataView': PersonalDataView,
            'UserDataView': UserDataView,
            'ContactDataView': ContactDataView,
            'SuccessView': SuccessView
        }
        self.switch_view('MainView')

    def switch_view(self, view_name):
        view_class = self.view_classes.get(view_name)
        if view_class:
            new_view = view_class(self, self.switch_view)
            if self.current_view:
                print('1')
                self.current_view.pack_forget()
                print('2')
            self.current_view = new_view
            self.current_view.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = AppController()
    app.mainloop()