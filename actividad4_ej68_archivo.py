# Actividad 4 - Ejercicio 6.8: Lectura de archivos
# Programacion Orientada a Objetos 2026-2S - Juan Diego Toro Zuluaga

import tkinter as tk


class LeerArchivo:

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer(self):
        lineas = []
        archivo = open(self.nombre_archivo, "r", encoding="utf-8")
        linea = archivo.readline()
        while linea != "":
            lineas.append(linea.rstrip("\n"))
            linea = archivo.readline()
        archivo.close()
        return lineas


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Leer archivo")
        self.resizable(False, False)

        tk.Label(self, text="Nombre del archivo").grid(row=0, column=0, padx=10,
                                                       pady=10, sticky="w")
        self.campo = tk.Entry(self, width=30)
        self.campo.grid(row=0, column=1, padx=10, pady=10)
        self.campo.insert(0, "prueba.txt")

        tk.Button(self, text="Leer", width=10,
                  command=self.leer).grid(row=1, column=0, columnspan=2, pady=5)

        self.area = tk.Text(self, width=46, height=8)
        self.area.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10))

    def leer(self):
        archivo = LeerArchivo(self.campo.get())
        self.area.delete("1.0", tk.END)
        try:
            for linea in archivo.leer():
                self.area.insert(tk.END, linea + "\n")
        except IOError:
            self.area.insert(tk.END, "No se pudo leer el archivo.")


ventana = VentanaPrincipal()
ventana.mainloop()
