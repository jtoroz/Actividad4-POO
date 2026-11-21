# Actividad 4 - Ejercicio 6.6: Catchs multiples
# Programacion Orientada a Objetos 2026-2S - Juan Diego Toro Zuluaga

import math
import tkinter as tk


class CalculosNumericos:

    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        try:
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            return "Resultado = " + str(math.log(valor))
        except ArithmeticError:
            return "El valor debe ser un número positivo para calcular el logaritmo"
        except ValueError:
            return "El valor debe ser numérico para calcular el logaritmo"

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        try:
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            return "Resultado = " + str(math.sqrt(valor))
        except ArithmeticError:
            return "El valor debe ser un número positivo para calcular la raíz cuadrada"
        except ValueError:
            return "El valor debe ser numérico para calcular la raíz cuadrada"


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Cálculos numéricos")
        self.resizable(False, False)

        tk.Label(self, text="Ingresar valor numérico").grid(row=0, column=0, padx=10,
                                                            pady=10, sticky="w")
        self.campo = tk.Entry(self, width=14)
        self.campo.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self, text="Calcular", width=10,
                  command=self.calcular).grid(row=1, column=0, columnspan=2, pady=5)

        self.etiqueta_logaritmo = tk.Label(self, text="Logaritmo neperiano =")
        self.etiqueta_logaritmo.grid(row=2, column=0, columnspan=2, padx=10, sticky="w")

        self.etiqueta_raiz = tk.Label(self, text="Raíz cuadrada =")
        self.etiqueta_raiz.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 10),
                                sticky="w")

    def calcular(self):
        try:
            valor = float(self.campo.get())
        except ValueError:
            self.etiqueta_logaritmo.config(text="El valor ingresado debe ser numérico")
            self.etiqueta_raiz.config(text="")
            return

        self.etiqueta_logaritmo.config(
            text="Logaritmo neperiano: " + CalculosNumericos.calcular_logaritmo_neperiano(valor))
        self.etiqueta_raiz.config(
            text="Raíz cuadrada: " + CalculosNumericos.calcular_raiz_cuadrada(valor))


ventana = VentanaPrincipal()
ventana.mainloop()
