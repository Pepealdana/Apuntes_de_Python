"""Calculadora básica de escritorio con CustomTkinter.

Instalación:
    python -m pip install customtkinter

Permite sumar, restar, multiplicar y dividir dos números.
"""

import math
import customtkinter as ctk


def calcular_operacion(a, b, operacion):
    """Calcula una operación validada; separa la lógica de la interfaz."""
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Los números deben ser valores finitos.")
    if operacion == "+":
        return a + b
    if operacion == "−":
        return a - b
    if operacion == "×":
        return a * b
    if operacion == "÷":
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return a / b
    raise ValueError(f"Operación no reconocida: {operacion}")


class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora básica")
        self.geometry("420x390")
        self.minsize(360, 350)

        ctk.CTkLabel(self, text="Calculadora", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(22, 12))
        self.entrada_a = ctk.CTkEntry(self, placeholder_text="Primer número", width=280)
        self.entrada_a.pack(pady=7)
        self.entrada_b = ctk.CTkEntry(self, placeholder_text="Segundo número", width=280)
        self.entrada_b.pack(pady=7)

        fila = ctk.CTkFrame(self, fg_color="transparent")
        fila.pack(pady=14)
        for simbolo in ("+", "−", "×", "÷"):
            ctk.CTkButton(fila, text=simbolo, width=55, command=lambda op=simbolo: self.calcular(op)).pack(side="left", padx=4)

        self.resultado = ctk.CTkLabel(self, text="El resultado aparecerá aquí.", wraplength=340)
        self.resultado.pack(pady=14)
        ctk.CTkButton(self, text="Limpiar", fg_color="gray", command=self.limpiar).pack(pady=4)

    def calcular(self, operacion):
        try:
            a = float(self.entrada_a.get().replace(",", "."))
            b = float(self.entrada_b.get().replace(",", "."))
            valor = calcular_operacion(a, b, operacion)
        except ZeroDivisionError:
            self.resultado.configure(text="No se puede dividir entre cero.")
            return
        except ValueError:
            self.resultado.configure(text="Escribe dos números válidos y finitos. Puedes usar coma o punto decimal.")
            return

        self.resultado.configure(text=f"Resultado: {valor:g}")

    def limpiar(self):
        self.entrada_a.delete(0, "end")
        self.entrada_b.delete(0, "end")
        self.resultado.configure(text="El resultado aparecerá aquí.")


if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    Calculadora().mainloop()
