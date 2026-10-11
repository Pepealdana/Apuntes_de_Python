"""Gestor de actividades escolares con CustomTkinter y persistencia JSON.

Instalación:
    python -m pip install customtkinter

Los datos se guardan en actividades.json en el directorio de trabajo actual.
Usa datos ficticios al practicar.
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
        self.geometry("680x600")
        self.minsize(520, 500)
        self.actividades = []
        self.carga_correcta = True

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

        ctk.CTkLabel(self, text="Selecciona una actividad para eliminarla:").pack(pady=(12, 4))
        self.seleccion = ctk.CTkOptionMenu(self, values=["Sin actividades"])
        self.seleccion.pack(pady=4)
        self.lista = ctk.CTkTextbox(self, height=190)
        self.lista.pack(fill="both", expand=True, padx=18, pady=8)
        self.estado = ctk.CTkLabel(self, text="")
        self.estado.pack(pady=(0, 12))

        try:
            self.actividades = cargar_actividades()
            self.refrescar()
        except (OSError, json.JSONDecodeError, ValueError) as error:
            self.carga_correcta = False
            self.estado.configure(text=f"No se pudo leer {ARCHIVO}: {error}. Corrige el archivo antes de guardar cambios.")

    def refrescar(self):
        self.lista.configure(state="normal")
        self.lista.delete("1.0", "end")
        opciones = []
        for indice, item in enumerate(self.actividades, start=1):
            nombre = str(item.get("nombre", "(sin nombre)"))
            area = str(item.get("area", "(sin área)"))
            self.lista.insert("end", f"{indice}. {nombre} — {area}\n")
            opciones.append(f"{indice}. {nombre}")
        self.lista.configure(state="disabled")
        self.seleccion.configure(values=opciones or ["Sin actividades"])
        if opciones:
            self.seleccion.set(opciones[0])
        self.estado.configure(text=f"{len(self.actividades)} actividad(es). Archivo: {ARCHIVO.resolve()}")

    def agregar(self):
        if not self.carga_correcta:
            self.estado.configure(text="No se guardarán cambios mientras el JSON inicial tenga errores.")
            return
        nombre = self.nombre.get().strip()
        area = self.area.get().strip()
        if not nombre or not area:
            self.estado.configure(text="Escribe el nombre y el área.")
            return
        self.actividades.append({"nombre": nombre, "area": area})
        if self.persistir():
            self.nombre.delete(0, "end")
            self.area.delete(0, "end")

    def eliminar(self):
        if not self.carga_correcta or not self.actividades:
            self.estado.configure(text="No hay una lista válida para modificar.")
            return
        try:
            indice = int(self.seleccion.get().split(".", 1)[0]) - 1
            if not 0 <= indice < len(self.actividades):
                raise ValueError
        except (ValueError, IndexError):
            self.estado.configure(text="Selecciona una actividad válida.")
            return
        nombre = self.actividades[indice].get("nombre", "(sin nombre)")
        if not messagebox.askyesno("Confirmar eliminación", f"¿Eliminar la actividad «{nombre}»?"):
            return
        self.actividades.pop(indice)
        self.persistir()

    def persistir(self):
        try:
            guardar_actividades(self.actividades)
        except OSError as error:
            self.estado.configure(text=f"No se pudo guardar el archivo: {error}")
            return False
        self.refrescar()
        return True


if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    Gestor().mainloop()
