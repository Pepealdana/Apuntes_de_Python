"""Gestor de actividades escolares con CustomTkinter y persistencia JSON.

Instalación:
    python -m pip install customtkinter

Los datos se guardan en actividades.json junto a la carpeta desde la que
se ejecuta el programa. Los registros de ejemplo deben ser ficticios.
"""

import json
from pathlib import Path
import tkinter.messagebox as messagebox

import customtkinter as ctk


ARCHIVO = Path("actividades.json")


def cargar_actividades():
    if not ARCHIVO.exists():
        return []
    with ARCHIVO.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list) or not all(isinstance(item, dict) for item in datos):
        raise ValueError("El JSON debe contener una lista de actividades.")
    return datos


def guardar_actividades(actividades):
    temporal = ARCHIVO.with_suffix(".json.tmp")
    with temporal.open("w", encoding="utf-8") as archivo:
        json.dump(actividades, archivo, ensure_ascii=False, indent=2)
    temporal.replace(ARCHIVO)


class Gestor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de actividades")
        self.geometry("680x560")
        self.minsize(520, 450)
        self.actividades = []

        ctk.CTkLabel(self, text="Actividades escolares", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(18, 10))
        formulario = ctk.CTkFrame(self)
        formulario.pack(fill="x", padx=18, pady=8)

        self.nombre = ctk.CTkEntry(formulario, placeholder_text="Nombre de la actividad")
        self.nombre.pack(fill="x", padx=12, pady=(12, 6))
        self.area = ctk.CTkEntry(formulario, placeholder_text="Área o asignatura")
        self.area.pack(fill="x", padx=12, pady=6)

        botones = ctk.CTkFrame(formulario, fg_color="transparent")
        botones.pack(pady=8)
        ctk.CTkButton(botones, text="Agregar", command=self.agregar).pack(side="left", padx=4)
        ctk.CTkButton(botones, text="Eliminar seleccionada", fg_color="#9b3b3b", command=self.eliminar).pack(side="left", padx=4)

        self.lista = ctk.CTkTextbox(self, height=220)
        self.lista.pack(fill="both", expand=True, padx=18, pady=8)
        self.estado = ctk.CTkLabel(self, text="")
        self.estado.pack(pady=(0, 12))

        try:
            self.actividades = cargar_actividades()
            self.refrescar()
        except (OSError, json.JSONDecodeError, ValueError) as error:
            self.estado.configure(text=f"No se pudo leer {ARCHIVO}: {error}")

    def refrescar(self):
        self.lista.configure(state="normal")
        self.lista.delete("1.0", "end")
        for indice, item in enumerate(self.actividades, start=1):
            self.lista.insert("end", f"{indice}. {item.get('nombre', '(sin nombre)')} — {item.get('area', '(sin área)')}\n")
        self.lista.configure(state="disabled")
        self.estado.configure(text=f"{len(self.actividades)} actividad(es). Archivo: {ARCHIVO.resolve()}")

    def agregar(self):
        nombre = self.nombre.get().strip()
        area = self.area.get().strip()
        if not nombre or not area:
            self.estado.configure(text="Escribe el nombre y el área.")
            return
        self.actividades.append({"nombre": nombre, "area": area})
        self.persistir()
        self.nombre.delete(0, "end")
        self.area.delete(0, "end")

    def eliminar(self):
        seleccion = self.lista.tag_ranges("sel")
        if not seleccion:
            self.estado.configure(text="Selecciona el texto de una actividad antes de eliminar.")
            return
        texto = self.lista.get(seleccion[0], seleccion[1]).strip()
        try:
            indice = int(texto.split(".", 1)[0]) - 1
            if not 0 <= indice < len(self.actividades):
                raise ValueError
        except (ValueError, IndexError):
            self.estado.configure(text="Selecciona una línea que comience con el número de la actividad.")
            return
        self.actividades.pop(indice)
        self.persistir()

    def persistir(self):
        try:
            guardar_actividades(self.actividades)
        except OSError as error:
            self.estado.configure(text=f"No se pudo guardar el archivo: {error}")
            return
        self.refrescar()


if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    Gestor().mainloop()
