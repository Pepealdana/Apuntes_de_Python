"""Formulario de registro de ejemplo con CustomTkinter.

Los registros son ficticios y se guardan en registros_formulario.csv.
Instalación: python -m pip install customtkinter
"""

import csv
from pathlib import Path
import tkinter.messagebox as messagebox

import customtkinter as ctk


ARCHIVO = Path("registros_formulario.csv")
CAMPOS = ["nombre", "curso", "interes"]


def guardar_registro(registro):
    """Agrega un registro sin reemplazar los anteriores."""
    existe = ARCHIVO.exists()
    with ARCHIVO.open("a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        if not existe or ARCHIVO.stat().st_size == 0:
            escritor.writeheader()
        escritor.writerow(registro)


class Formulario(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Formulario de intereses")
        self.geometry("460x420")
        self.minsize(360, 380)

        ctk.CTkLabel(self, text="Registro de intereses", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=(20, 14))
        self.nombre = ctk.CTkEntry(self, placeholder_text="Nombre ficticio", width=300)
        self.nombre.pack(pady=7)
        self.curso = ctk.CTkEntry(self, placeholder_text="Curso o grupo", width=300)
        self.curso.pack(pady=7)
        self.interes = ctk.CTkOptionMenu(self, values=["Robótica", "Programación", "Ciencia", "Arte"])
        self.interes.pack(pady=10)

        ctk.CTkButton(self, text="Guardar registro", command=self.guardar).pack(pady=12)
        self.estado = ctk.CTkLabel(self, text="Completa los campos obligatorios.", wraplength=350)
        self.estado.pack(pady=8)

    def guardar(self):
        nombre = self.nombre.get().strip()
        curso = self.curso.get().strip()
        if not nombre or not curso:
            self.estado.configure(text="El nombre y el curso son obligatorios.")
            return

        registro = {"nombre": nombre, "curso": curso, "interes": self.interes.get()}
        try:
            guardar_registro(registro)
        except OSError as error:
            self.estado.configure(text=f"No se pudo guardar el archivo: {error}")
            return

        self.estado.configure(text=f"Registro guardado en {ARCHIVO.resolve()}.")
        self.nombre.delete(0, "end")
        self.curso.delete(0, "end")


if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    Formulario().mainloop()
