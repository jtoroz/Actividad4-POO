# Actividad 4 - Ejercicio 6.4: Excepciones
# Programacion Orientada a Objetos 2026-2S - Juan Diego Toro Zuluaga

import tkinter as tk


class PruebaExcepciones:

    def __init__(self):
        self.mensajes = []

    def primer_bloque(self):
        try:
            self.mensajes.append("Ingresando al primer try")
            cociente = 10000 / 0
            self.mensajes.append("Después de la división")
        except ArithmeticError:
            self.mensajes.append("División por cero")
        finally:
            self.mensajes.append("Ingresando al primer finally")

    def segundo_bloque(self):
        try:
            self.mensajes.append("Ingresando al segundo try")
            objeto = None
            objeto.to_string()
            self.mensajes.append("Después de la asignación")
        except Exception:
            self.mensajes.append("Ocurrió una excepción")
        finally:
            self.mensajes.append("Ingresando al segundo finally")

    def ejecutar(self):
        self.mensajes = []
        self.primer_bloque()
        self.segundo_bloque()
        return self.mensajes


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Prueba de excepciones")
        self.resizable(False, False)

        tk.Label(self, text="Resultado de la ejecución").pack(padx=10, pady=(10, 5))

        self.area = tk.Text(self, width=40, height=8)
        self.area.pack(padx=10)

        tk.Button(self, text="Ejecutar", width=10,
                  command=self.ejecutar).pack(padx=10, pady=5)
        tk.Button(self, text="Limpiar", width=10,
                  command=self.limpiar).pack(padx=10, pady=(0, 10))

    def ejecutar(self):
        prueba = PruebaExcepciones()
        self.area.delete("1.0", tk.END)
        for mensaje in prueba.ejecutar():
            self.area.insert(tk.END, mensaje + "\n")

    def limpiar(self):
        self.area.delete("1.0", tk.END)


ventana = VentanaPrincipal()
ventana.mainloop()
