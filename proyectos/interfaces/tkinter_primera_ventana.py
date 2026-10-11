"""Primera ventana con Tkinter.

Ejecuta este archivo con Python 3 en un entorno de escritorio.
No necesita instalar una biblioteca externa cuando Tkinter está disponible.
"""

import tkinter as tk


def cambiar_mensaje():
    """Actualiza el texto cuando se pulsa el botón."""
    etiqueta.config(text="¡Ya ejecutaste una acción desde la interfaz!")


ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("420x220")

etiqueta = tk.Label(
    ventana,
    text="Estoy aprendiendo Python",
    font=("Arial", 14),
    wraplength=360,
)
etiqueta.pack(pady=25)

boton = tk.Button(
    ventana,
    text="Probar botón",
    command=cambiar_mensaje,
)
boton.pack()

ventana.mainloop()
