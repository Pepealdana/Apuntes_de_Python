"""Primera aplicación con CustomTkinter.

Preparación:
    python -m pip install customtkinter

Ejecuta este archivo desde el entorno en el que instalaste el paquete.
"""

import customtkinter as ctk


def mostrar_saludo():
    nombre = campo_nombre.get().strip()

    if not nombre:
        etiqueta_resultado.configure(text="Escribe un nombre primero.")
        return

    etiqueta_resultado.configure(text=f"Hola, {nombre}. ¡La aplicación funciona!")


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Mi primera aplicación")
ventana.geometry("460x300")
ventana.minsize(360, 260)

titulo = ctk.CTkLabel(
    ventana,
    text="Explorando CustomTkinter",
    font=ctk.CTkFont(size=20, weight="bold"),
)
titulo.pack(pady=(24, 12))

campo_nombre = ctk.CTkEntry(
    ventana,
    placeholder_text="Escribe tu nombre",
    width=280,
)
campo_nombre.pack(pady=8)

boton_saludar = ctk.CTkButton(
    ventana,
    text="Saludar",
    command=mostrar_saludo,
)
boton_saludar.pack(pady=8)

etiqueta_resultado = ctk.CTkLabel(ventana, text="El resultado aparecerá aquí.")
etiqueta_resultado.pack(pady=12)

ventana.mainloop()
