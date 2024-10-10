
import customtkinter as ctk

class LoginView(ctk.CTkFrame):
    def __init__(self, master, login_callback,show_register_callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.login_callback = login_callback
        self.show_register_callback = show_register_callback


        self.username_label = ctk.CTkLabel(self, text="Username")
        self.username_label.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

        self.username_entry = ctk.CTkEntry(self,placeholder_text="username",width=280)
        self.username_entry.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="w")

        self.password_entry = ctk.CTkEntry(self, show="*",placeholder_text="password")
        self.password_entry.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.grid(row=7, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.register_button = ctk.CTkButton(self, text="Register", command=self.show_register, width=50,fg_color="transparent")
        self.register_button.grid(row=8, column=0, padx=10, pady=(10, 10), sticky="e")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.login_callback(username, password)

    def show_register(self):
        self.show_register_callback()

