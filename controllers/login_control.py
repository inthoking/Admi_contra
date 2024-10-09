from models.login_model import User
from views.login_view import LoginView, RegisterView
import customtkinter as ctk

class LoginController:
    def __init__(self, root):
        self.root = root
        self.user = User("admin", "password")  # Usuario de ejemplo

    def show_login_view(self):
        self.clear_frame()
        self.login_frame = LoginView(self.root, self.authenticate,self.show_register_view )
        self.login_frame.pack(fill="both", expand=True)

    def show_register_view(self):
        self.clear_frame()
        self.register_frame = RegisterView(self.root, self.register_user, self.show_login_view)
        self.register_frame.pack(fill="both", expand=True)


    def authenticate(self, username, password):
        if self.user.username == username and self.user.check_password(password):
            print("Login successful")
        else:
            print("Login failed")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register_user(self, User,):
        if self.api_client.create_user(User):
            print("User registered successfully")
            self.show_login_view()
        else:
            print("Registration failed")
    
