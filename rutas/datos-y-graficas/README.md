# Ruta: datos, estadísticas y gráficas

## Propósito

Aprender a leer conjuntos pequeños de datos, hacer preguntas sobre ellos y comunicar resultados mediante tablas y gráficas.

## Secuencia

1. Usar listas, diccionarios, ciclos y funciones.
2. Leer y validar datos CSV y JSON.
3. Calcular conteos, promedios, mínimos, máximos y otras estadísticas sencillas.
4. Crear gráficas con Matplotlib.
5. Incorporar pandas solo si las tablas crecen o las operaciones lo justifican.
6. Construir un informe breve que explique los resultados, no solo que muestre una gráfica.

## Proyecto inicial

Analiza un archivo CSV con datos ficticios de una encuesta o mediciones escolares. El programa debe:
- validar que existan las columnas esperadas;
- detectar datos vacíos o inválidos;
- calcular al menos tres indicadores;
- producir una gráfica etiquetada;
- explicar qué se puede y qué no se puede concluir de los datos.

## Instalación de Matplotlib

En el entorno virtual del proyecto:

```bash
python -m pip install matplotlib
```

Instala pandas únicamente en una fase posterior si necesitas sus herramientas de tablas:

```bash
python -m pip install pandas
```

## Buenas prácticas

- Usa datos ficticios o debidamente anonimizados.
- Etiqueta ejes, unidades y título de las gráficas.
- No presentes correlación como prueba automática de causalidad.
- Comprueba valores atípicos y datos faltantes.
- Conserva el archivo original y genera resultados en una carpeta separada.

## Retos

1. Cambia los datos y predice cómo cambiará la gráfica.
2. Compara dos categorías.
3. Añade una validación para valores vacíos.
4. Exporta un resumen CSV.
5. Escribe tres conclusiones justificadas por los datos.

## Referencias

- [Módulo csv de Python](https://docs.python.org/es/3/library/csv.html)
- [Matplotlib](https://matplotlib.org/stable/)
- [pandas](https://pandas.pydata.org/docs/)
