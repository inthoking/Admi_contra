import customtkinter as ctk
from controllers.login_control import LoginController

def main():
    app = ctk.CTk()
    app.geometry("800x600")
    app.title("Login App")
    app.grid_columnconfigure((0), weight=1)
    app.grid_rowconfigure((0), weight=1)


    controller = LoginController(app)
    controller.show_login_view()

    app.mainloop()

if __name__ == "__main__":
    main()
