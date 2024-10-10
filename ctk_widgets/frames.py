import customtkinter as ctk


class Login_frame(ctk.CTkFrame):
    def __init__(self, master, label, entry):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.label = label
        self.entry = entry
        self.entrys = []
        self.variable = ctk.StringVar(value="")
    
    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


        pass
class MyRadiobuttonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)