"""Crea una gráfica con datos ficticios.

Preparación:
    python -m pip install matplotlib

Este ejemplo no necesita descargar datos ni acceder a internet.
"""

import matplotlib.pyplot as plt


dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
minutos = [20, 35, 25, 40, 30]

plt.figure(figsize=(8, 4.5))
plt.plot(dias, minutos, marker="o")
plt.title("Tiempo de práctica por día")
plt.xlabel("Día")
plt.ylabel("Minutos de práctica")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
