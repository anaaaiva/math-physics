import tkinter
from tkinter import ttk
import sv_ttk

import sympy
from sympy.plotting.plot import plot3d

import solution

class RadioButtonKind(ttk.LabelFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, text="Выберите вид уравнения", padding=15)

        self.var = tkinter.IntVar()
        self.var.set(0)

        self.controller = controller
        self.controller['kind'] = 0

        self.add_widgets()
    def update_controller(self):
        self.controller['kind'] = int(self.var.get())
        #print(self.controller)
    def add_widgets(self):
        self.radio_1 = ttk.Radiobutton(self, text="Уравнение теплопроводности", variable=self.var, value=0,
                                       command = self.update_controller)
        self.radio_1.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.radio_1 = ttk.Radiobutton(self, text="Волновое уравнение", variable=self.var, value=1,
                                       command = self.update_controller)
        self.radio_1.grid(row=1, column=0, pady=10, sticky="w")

class RadioButtonType(ttk.LabelFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, text="Выберите тип задачи", padding=15)

        self.var = tkinter.IntVar()
        self.var.set(0)

        self.controller = controller
        self.controller['type'] = 0

        self.add_widgets()
    def update_controller(self):
        self.controller['type'] = int(self.var.get())
        #print(self.controller)

    def add_widgets(self):
        self.radio_1 = ttk.Radiobutton(self, text="Дирихле", variable=self.var, value=0,
                                       command = self.update_controller)
        self.radio_1.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.radio_1 = ttk.Radiobutton(self, text="Нейман", variable=self.var, value=1,
                                       command = self.update_controller)
        self.radio_1.grid(row=1, column=0, pady=10, sticky="w")

class InputsAndButtonsDemo(ttk.LabelFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, text="Введите условия задачи", padding=15)
        self.controller = controller

        self.columnconfigure(0, weight=1)

        self.add_widgets()

    def update_controller(self):

        self.controller['a'] = self.entry_a.get()
        self.controller['l'] = self.entry_l.get()
        self.controller['phi1'] =  self.entry_phi1.get()
        self.controller['phi2'] = self.entry_phi2.get()
        self.controller['f'] = self.entry_f.get()

        print('Данные обновлены:  ', self.controller)

        x, t = sympy.symbols('x t')
        u, dict = solution.get_result(self.controller)

        print(f'Результат: U(X,t) = {u}')

        if self.controller['type'] == 0:
            plot3d(u, (x, 0, dict['l']), (t, 0, 5), title=f"U(X, t) = {u}", )
        else:
            plot3d(u.diff(x), (x, 0, dict['l']), (t, 0, 5), title=f"U(X, t) = {u}")

    def add_widgets(self):
        self.label_a = ttk.Label(self, text = "A")
        self.label_a.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.entry_a = ttk.Entry(self)
        self.entry_a.insert(0, 0)
        self.entry_a.grid(row=0, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.label_l = ttk.Label(self, text="Длина стержня l")
        self.label_l.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.entry_l = ttk.Entry(self)
        self.entry_l.insert(0, 0)
        self.entry_l.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.label_phi1 = ttk.Label(self, text="U(X,0)")
        self.label_phi1.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.entry_phi1 = ttk.Entry(self)
        self.entry_phi1.insert(0, 0)
        self.entry_phi1.grid(row=2, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.label_phi2 = ttk.Label(self, text="dU/dt(X,0)")
        self.label_phi2.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.entry_phi2 = ttk.Entry(self)
        self.entry_phi2.insert(0, 0)
        self.entry_phi2.grid(row=3, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.label_f = ttk.Label(self, text="Неоднородность F(X,t)")
        self.label_f.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.entry_f = ttk.Entry(self)
        self.entry_f.insert(0, 0)
        self.entry_f.grid(row=4, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.separator = ttk.Separator(self)
        self.separator.grid(row=5, column=0, pady=10, sticky="ew", columnspan=2)

        self.accentbutton = ttk.Button(self, text="Получить результат", style="Accent.TButton", command = self.update_controller)
        self.accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="ew", columnspan=2)

class App(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=15)
        self.controller = controller

        for index in range(2):
            self.columnconfigure(index, weight=1)
            self.rowconfigure(index, weight=1)

        RadioButtonKind(self, controller = self.controller).grid(row=0, column=0, padx=(0, 10), pady=(0, 20), sticky="nsew")
        RadioButtonType(self, controller = self.controller).grid(row=1, column=0, padx=(0, 10), pady=(0, 20), sticky="nsew")
        InputsAndButtonsDemo(self, controller = self.controller).grid(row=0, column=1, padx=(0, 10), pady=(0, 20), sticky="nsew", rowspan=2)
def main():
    root = tkinter.Tk()
    root.title("math_physics")
    root.iconbitmap(r'math_integral_box_icon.ico')

    sv_ttk.set_theme("dark")

    app_data = {"kind": tkinter.IntVar(),
                "type": tkinter.IntVar(),
                "a": tkinter.StringVar(),
                "l": tkinter.StringVar(),
                "phi1": tkinter.StringVar(),
                "phi2": tkinter.StringVar(),
                "f": tkinter.StringVar()}

    app = App(root, controller = app_data)
    app.pack(expand=True, fill="both")
    root.update_idletasks()

    width, height = root.winfo_width(), root.winfo_height()
    x = int((root.winfo_screenwidth() / 2) - (width / 2))
    y = int((root.winfo_screenheight() / 2) - (height / 2))

    root.minsize(width, height)
    root.geometry(f"+{x}+{y}")

    root.mainloop()


if __name__ == "__main__":
    main()