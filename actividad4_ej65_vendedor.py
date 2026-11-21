# Actividad 4 - Ejercicio 6.5: Lanzamiento de excepciones
# Programacion Orientada a Objetos 2026-2S - Juan Diego Toro Zuluaga

import tkinter as tk
from tkinter import messagebox


class Vendedor:

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def verificar_edad(self, edad):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if 0 <= edad < 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

    def imprimir(self):
        return ["Nombre del vendedor = " + self.nombre,
                "Apellidos del vendedor = " + self.apellidos,
                "Edad del vendedor = " + str(self.edad)]


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Vendedor")
        self.resizable(False, False)

        self.campos = []
        for i, nombre in enumerate(["Nombre", "Apellidos", "Edad"]):
            tk.Label(self, text=nombre).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            campo = tk.Entry(self, width=18)
            campo.grid(row=i, column=1, padx=10, pady=5)
            self.campos.append(campo)

        tk.Button(self, text="Registrar", width=10,
                  command=self.registrar).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self, text="Limpiar", width=10,
                  command=self.limpiar).grid(row=3, column=1, padx=10, pady=10)

        self.etiquetas = []
        for i in range(3):
            etiqueta = tk.Label(self, text="")
            etiqueta.grid(row=4 + i, column=0, columnspan=2, padx=10, sticky="w")
            self.etiquetas.append(etiqueta)

        tk.Label(self, text="").grid(row=7, column=0)

    def registrar(self):
        try:
            edad = int(self.campos[2].get())
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return

        vendedor = Vendedor(self.campos[0].get(), self.campos[1].get())
        try:
            vendedor.verificar_edad(edad)
        except ValueError as error:
            messagebox.showerror("Error", str(error))
            return

        for etiqueta, texto in zip(self.etiquetas, vendedor.imprimir()):
            etiqueta.config(text=texto)

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)
        for etiqueta in self.etiquetas:
            etiqueta.config(text="")


ventana = VentanaPrincipal()
ventana.mainloop()
