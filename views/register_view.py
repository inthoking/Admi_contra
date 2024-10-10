import customtkinter as ctk
import json


class RegisterView(ctk.CTkFrame): #esto es un pantalla con dos columnas 
    
    def __init__(self, master, register_callback, show_login_callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.register_callback = register_callback
        self.show_login_callback = show_login_callback

        self.name_label = ctk.CTkLabel(self, text="Nombre")
        self.name_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.lastname_label = ctk.CTkLabel(self, text="Apellido")
        self.lastname_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        self.lastname_entry = ctk.CTkEntry(self)
        self.lastname_entry.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

        self.email_label = ctk.CTkLabel(self, text="Email")
        self.email_label.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")
        self.email_entry = ctk.CTkEntry(self)
        self.email_entry.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="w")




        self.username_label = ctk.CTkLabel(self, text="Username")
        self.username_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="w")

        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w")
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="w")

        self.repassword_label = ctk.CTkLabel(self, text="Check password")
        self.repassword_label.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="w")
        self.repassword_entry = ctk.CTkEntry(self, show="*")
        self.repassword_entry.grid(row=5, column=1, padx=10, pady=(10, 0), sticky="w")
        self.repassword_entry.bind("<Control-v>", self.disable_paste)     #esto bloquea el pegado de texto, la funcion que utiliza solo hace un break  



        self.register_button = ctk.CTkButton(self, text="Register", command=self.register)
        self.register_button.grid(row=9, column=1, padx=10, pady=(10, 10), sticky="w")

        self.back_button = ctk.CTkButton(self, text="Back", command=self.show_login,fg_color="transparent")
        self.back_button.grid(row=9, column=0, padx=10, pady=(10, 10), sticky="w")

    def disable_paste(self, event):
        return "break"

    def register(self):
        User_name = self.username_entry.get()
        Name = self.name_entry.get()
        Last_name=self.lastname_entry.get()
        Email_add=self.email_entry.get()
        password= self.password_entry.get()

        data = {
                "User_name": User_name,
                "Name": Name,
                "Last_name": Last_name,
                "Email_add": Email_add,
                "password": password,
            }
        json_data = json.dumps(data)
        
        self.register_callback(json_data)

    def show_login(self):
        self.show_login_callback()
