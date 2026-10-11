# Proyecto de IA introductoria: clasificador Iris

Archivo: [clasificador_iris.py](clasificador_iris.py)

## Propósito

Explorar un flujo de aprendizaje automático supervisado: separar datos de entrenamiento y prueba, escalar características, entrenar un clasificador y revisar métricas.

## Preparación y ejecución

```bash
python -m pip install scikit-learn
python proyectos/ia/clasificador_iris.py
```

El conjunto Iris está incluido en scikit-learn, por lo que el ejemplo no necesita descargar datos durante la ejecución.

## Qué observar

- El modelo aprende a partir del conjunto de entrenamiento.
- Las predicciones se evalúan con datos que no se usaron para ajustar el modelo.
- La exactitud resume aciertos, pero no explica todos los errores.
- La matriz de confusión permite observar qué clases se confunden.
- El resultado depende de los datos, del modelo y de la división entre entrenamiento y prueba.

## Límites y uso responsable

Es un experimento educativo con un conjunto de datos pequeño y conocido. No demuestra que el modelo sea adecuado para decisiones reales. Antes de aplicar IA a una situación, deben evaluarse la calidad y representatividad de los datos, los errores, los sesgos, la privacidad y las consecuencias de una clasificación incorrecta.

## Retos

1. Cambia `random_state` y compara resultados.
2. Explica qué significa cada fila y columna de la matriz de confusión.
3. Compara dos modelos con la misma división de datos.
4. Documenta un caso en el que la exactitud sea una métrica insuficiente.
5. Busca un conjunto de datos apropiado y con licencia clara antes de ampliar el experimento.

**Estado:** ejemplo incorporado; requiere instalar scikit-learn y ejecutar la práctica para observar resultados reales.
