# Actividad 4 - Ejercicio 6.7: Validacion de campos
# Programacion Orientada a Objetos 2026-2S - Juan Diego Toro Zuluaga

import tkinter as tk
from tkinter import messagebox


class Programador:

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:

    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.tamanio_equipo = 0
        self.programadores = [None, None, None]

    def esta_lleno(self):
        return self.tamanio_equipo == len(self.programadores)

    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores[self.tamanio_equipo] = programador
        self.tamanio_equipo += 1

    @staticmethod
    def validar_campo(campo):
        for caracter in campo:
            if caracter.isdigit():
                raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Equipo maratón de programación")
        self.resizable(False, False)
        self.equipo = None

        datos = ["Nombre del equipo", "Universidad", "Lenguaje de programación"]
        self.campos_equipo = []
        for i, nombre in enumerate(datos):
            tk.Label(self, text=nombre).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            campo = tk.Entry(self, width=24)
            campo.grid(row=i, column=1, padx=10, pady=5)
            self.campos_equipo.append(campo)

        tk.Button(self, text="Crear equipo", width=12,
                  command=self.crear_equipo).grid(row=3, column=0, columnspan=2, pady=8)

        self.campos_integrante = []
        for i, nombre in enumerate(["Nombre del integrante", "Apellidos del integrante"]):
            tk.Label(self, text=nombre).grid(row=4 + i, column=0, padx=10, pady=5, sticky="w")
            campo = tk.Entry(self, width=24)
            campo.grid(row=4 + i, column=1, padx=10, pady=5)
            self.campos_integrante.append(campo)

        tk.Button(self, text="Añadir integrante", width=16,
                  command=self.anadir_integrante).grid(row=6, column=0, columnspan=2, pady=8)

        self.area = tk.Text(self, width=44, height=6)
        self.area.grid(row=7, column=0, columnspan=2, padx=10, pady=(0, 10))

    def crear_equipo(self):
        self.equipo = EquipoMaratonProgramacion(self.campos_equipo[0].get(),
                                                self.campos_equipo[1].get(),
                                                self.campos_equipo[2].get())
        self.area.delete("1.0", tk.END)
        self.area.insert(tk.END, "Equipo = " + self.equipo.nombre_equipo + "\n")
        self.area.insert(tk.END, "Universidad = " + self.equipo.universidad + "\n")
        self.area.insert(tk.END, "Lenguaje = " + self.equipo.lenguaje_programacion + "\n")

    def anadir_integrante(self):
        if self.equipo is None:
            messagebox.showerror("Error", "Primero debe crear el equipo.")
            return

        nombre = self.campos_integrante[0].get()
        apellidos = self.campos_integrante[1].get()
        try:
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            self.equipo.anadir(Programador(nombre, apellidos))
        except Exception as error:
            messagebox.showerror("Error", str(error))
            return

        self.area.insert(tk.END, "Integrante " + str(self.equipo.tamanio_equipo) +
                         " = " + nombre + " " + apellidos + "\n")
        for campo in self.campos_integrante:
            campo.delete(0, tk.END)


ventana = VentanaPrincipal()
ventana.mainloop()
