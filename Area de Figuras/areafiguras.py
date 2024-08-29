import tkinter as tk
import math
from tkinter import END, messagebox, ttk


class triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = 0

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

    def getArea(self):
        return self.area


class cuadrado:
    def __init__(self, lado):
        self.lado = lado
        self.area = 0

    def calcular_area(self):
        self.area = self.lado ** 2

    def getArea(self):
        return self.area


class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = 0

    def calcular_area(self):
        self.area = self.base * self.altura

    def getArea(self):
        return self.area


class poligono:
    def __init__(self, lado, lados):
        self.lado = lado
        self.lados = lados
        #self.angulo = angulo
        self.area = 0

    def calcular_area(self):
        #apo = base/(2*math.tan(math.pi/lados))
        #area = 0.5 * lados * lado * apo
        #lado = longitud
        #lados = numero de lados
        apo = self.lado/(2*math.tan(math.pi/self.lados))
        self.area = 0.5 * self.lados * self.lado * apo
        # area de un solo triangulo
        #area_triangulo = 0.5 * self.lado * self.lado * math.sin(math.radians(self.angulo))
        # numero de triangulos que forman el poligono
        #self.area = area_triangulo * self.lados

    def getArea(self):
        return self.area


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(width=400, height=300)
        self.title("Área Figuras")

        self.lbFigura = tk.Label(self, text="Seleccione Figura:")
        self.lbFigura.place(x=10, y=10)
        self.cbFigura = ttk.Combobox(self, state="readonly", values=["Triángulo", "Cuadrado", "Rectángulo", "Polígono"])
        self.cbFigura.place(x=10, y=30)
        self.cbFigura.bind("<<ComboboxSelected>>", self.actualizar_campos)

        self.lbBase = tk.Label(self, text="Ingrese Base:")
        self.lbBase.place(x=10, y=60)
        self.txBase = tk.Entry(self)
        self.txBase.place(x=10, y=80)

        self.lbAltura = tk.Label(self, text="Ingrese Altura:")
        self.lbAltura.place(x=10, y=110)
        self.txAltura = tk.Entry(self)
        self.txAltura.place(x=10, y=130)

        self.lbLados = tk.Label(self, text="Ingrese Número de Lados:")
        self.lbLados.place(x=10, y=160)
        self.txLados = tk.Entry(self)
        self.txLados.place(x=10, y=180)
        self.lbLados.place_forget()
        self.txLados.place_forget()

        self.btCalcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btCalcular.place(x=10, y=210)

    def actualizar_campos(self, event):
        figura = self.cbFigura.get()
        if figura == "Cuadrado":
            self.lbBase.config(text="Ingrese Lado:")
            self.lbAltura.place_forget()
            self.txAltura.place_forget()
            self.lbLados.place_forget()
            self.txLados.place_forget()
        elif figura == "Polígono":
            self.lbBase.config(text="Ingrese Lado:")
            self.lbAltura.place_forget()
            self.txAltura.place_forget()
            self.lbLados.place(x=10, y=110)
            self.txLados.place(x=10, y=130)
        else:
            self.lbBase.config(text="Ingrese Base:")
            self.lbAltura.place(x=10, y=110)
            self.txAltura.place(x=10, y=130)
            self.lbLados.place_forget()
            self.txLados.place_forget()

    def calcular(self):
        try:
            figura = self.cbFigura.get()
            if figura == "Triángulo":
                base = float(self.txBase.get())
                altura = float(self.txAltura.get())
                t = triangulo(base, altura)
                t.calcular_area()
                area = t.getArea()
            elif figura == "Cuadrado":
                lado = float(self.txBase.get())
                c = cuadrado(lado)
                c.calcular_area()
                area = c.getArea()
            elif figura == "Rectángulo":
                base = float(self.txBase.get())
                altura = float(self.txAltura.get())
                r = rectangulo(base, altura)
                r.calcular_area()
                area = r.getArea()
            elif figura == "Polígono":
                lado = float(self.txBase.get())
                lados = int(self.txLados.get())
                p = poligono(lado, lados)
                p.calcular_area()
                area = p.getArea()
            else:
                raise ValueError("Seleccione una figura válida")
            messagebox.showinfo(message="Área: " + str(area), title="Info")
        except ValueError as e:
            messagebox.showerror(message=str(e), title="Error")

if __name__ == "__main__":
    app = App()
    app.mainloop()