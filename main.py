import tkinter
from tkinter import ttk

import sv_ttk

class RadioButtonKind(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Выберите вид уравнения", padding=15)

        self.var = tkinter.IntVar()

        self.add_widgets()

    def add_widgets(self):
        self.radio_1 = ttk.Radiobutton(self, text="Уравнение теплопроводности", variable=self.var, value=0)
        self.radio_1.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.radio_1 = ttk.Radiobutton(self, text="Волновое уравнение", variable=self.var, value=1)
        self.radio_1.grid(row=1, column=0, pady=10, sticky="w")

class RadioButtonType(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Выберите тип задачи", padding=15)

        self.var = tkinter.IntVar()

        self.add_widgets()

    def add_widgets(self):
        self.radio_1 = ttk.Radiobutton(self, text="Дирихле", variable=self.var, value=0)
        self.radio_1.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.radio_1 = ttk.Radiobutton(self, text="Нейман", variable=self.var, value=1)
        self.radio_1.grid(row=1, column=0, pady=10, sticky="w")

class InputsAndButtonsDemo(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Введите условия задачи", padding=15)

        self.columnconfigure(0, weight=1)

        self.add_widgets()

        self.bind_int_widgets()

    def add_widgets(self):
        self.label_a = ttk.Label(self, text = "A")
        self.label_a.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.int_entry_a = ttk.Entry(self)
        self.int_entry_a.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.label_l = ttk.Label(self, text="Длина стержня l")
        self.label_l.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.int_entry_l = ttk.Entry(self)
        self.int_entry_l.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.label = ttk.Label(self, text="U(X,0)")
        self.label.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.entry = ttk.Entry(self)
        self.entry.grid(row=2, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.label = ttk.Label(self, text="dU/dt(X,0)")
        self.label.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.entry = ttk.Entry(self)
        self.entry.grid(row=3, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.label = ttk.Label(self, text="Неоднородность F(X,t)")
        self.label.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.entry = ttk.Entry(self)
        self.entry.grid(row=4, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.separator = ttk.Separator(self)
        self.separator.grid(row=5, column=0, pady=10, sticky="ew", columnspan=2)

        self.accentbutton = ttk.Button(self, text="Получить результат", style="Accent.TButton")
        self.accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="ew", columnspan=2)

    def bind_int_widgets(self):
        self.int_entry_a.bind("<FocusOut>", self.validate_int)
        self.int_entry_a.bind("<FocusIn>", self.validate_int)  # Can't get the normal fosuced state
        self.int_entry_a.bind("<KeyRelease>", self.validate_int)

        self.int_entry_l.bind("<FocusOut>", self.validate_int)
        self.int_entry_l.bind("<FocusIn>", self.validate_int)  # Can't get the normal fosuced state
        self.int_entry_l.bind("<KeyRelease>", self.validate_int)

    def validate_int(self, *_):
        if self.int_entry_a.get() == "":
            self.int_entry_a.state(["!invalid"])
        else:
            try:
                int(self.int_entry_a.get())
                self.int_entry_a.state(["!invalid"])
            except ValueError:
                self.int_entry_a.state(["invalid"])

        if self.int_entry_l.get() == "":
            self.int_entry_l.state(["!invalid"])
        else:
            try:
                int(self.int_entry_l.get())
                self.int_entry_l.state(["!invalid"])
            except ValueError:
                self.int_entry_l.state(["invalid"])

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=15)

        for index in range(2):
            self.columnconfigure(index, weight=1)
            self.rowconfigure(index, weight=1)

        RadioButtonKind(self).grid(row=0, column=0, padx=(0, 10), pady=(0, 20), sticky="nsew")
        RadioButtonType(self).grid(row=1, column=0, padx=(0, 10), pady=(0, 20), sticky="nsew")
        InputsAndButtonsDemo(self).grid(row=0, column=1, padx=(0, 10), pady=(0, 20), sticky="nsew", rowspan=2)


def main():
    root = tkinter.Tk()
    root.title("math_physics")
    root.iconbitmap(r'math_integral_box_icon.ico')

    sv_ttk.set_theme("dark")

    App(root).pack(expand=True, fill="both")
    root.update_idletasks()

    width, height = root.winfo_width(), root.winfo_height()
    x = int((root.winfo_screenwidth() / 2) - (width / 2))
    y = int((root.winfo_screenheight() / 2) - (height / 2))

    root.minsize(width, height)
    root.geometry(f"+{x}+{y}")

    root.mainloop()


if __name__ == "__main__":
    main()