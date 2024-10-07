
import customtkinter as ctk

class LoginView(ctk.CTkFrame):
    def __init__(self, master, login_callback,show_register_callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.login_callback = login_callback
        self.show_register_callback = show_register_callback

        self.username_label = ctk.CTkLabel(self, text="Username")
        self.username_label.pack(pady=5)

        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.pack(pady=5)

        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack(pady=5)

        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        self.register_button = ctk.CTkButton(self, text="Register", command=self.show_register)
        self.register_button.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.login_callback(username, password)

    def show_register(self):
        self.show_register_callback()

class RegisterView(ctk.CTkFrame):
    def __init__(self, master, register_callback, show_login_callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.register_callback = register_callback
        self.show_login_callback = show_login_callback

        self.username_label = ctk.CTkLabel(self, text="Username")
        self.username_label.pack(pady=5)
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.pack(pady=5)

        self.name_label = ctk.CTkLabel(self, text="Nombre")
        self.name_label.pack(pady=5)
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack(pady=5)

        self.lastname_label = ctk.CTkLabel(self, text="Apellido")
        self.lastname_label.pack(pady=5)
        self.lastname_entry = ctk.CTkEntry(self)
        self.lastname_entry.pack(pady=5)

        self.email_label = ctk.CTkLabel(self, text="Email")
        self.email_label.pack(pady=5)
        self.email_entry = ctk.CTkEntry(self)
        self.email_entry.pack(pady=5)

        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=5)

        self.register_button = ctk.CTkButton(self, text="Register", command=self.register)
        self.register_button.pack(pady=5)

        self.back_button = ctk.CTkButton(self, text="Back to Login", command=self.show_login)
        self.back_button.pack(pady=5)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.register_callback(username, password)

    def show_login(self):
        self.show_login_callback()