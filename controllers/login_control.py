from models.login_model import User, APIClient
from views.login_view import LoginView
from  views.register_view import RegisterView
import customtkinter as ctk

class LoginController:
    def __init__(self, root):
        self.root = root
        self.user = User("admin", "password")  # Usuario de ejemplo

    def show_login_view(self):
        self.clear_frame()
        self.login_frame = LoginView(self.root, self.authenticate,self.show_register_view )
        self.login_frame.grid(row=0, column=0, padx=10, pady=10)

    def show_register_view(self):
        self.clear_frame()
        self.register_frame = RegisterView(self.root, self.register_user, self.show_login_view)
        self.register_frame.pack(fill="both", expand=True)
        self.register_frame.grid(row=0, column=0, padx=10, pady=10)


    def authenticate(self, username, password):
        if self.user.username == username and self.user.check_password(password):
            print("Login successful")
        else:
            print("Login failed")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register_user(self, data_new_user:User):
        new_user=APIClient.create_user(data_new_user)
        return new_user