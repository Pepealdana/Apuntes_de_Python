"""Experimento introductorio: clasificar flores Iris con scikit-learn.

Instalación:
    python -m pip install scikit-learn

Usa un conjunto de datos incluido con scikit-learn; no descarga archivos.
Este ejemplo es didáctico y no debe presentarse como un sistema crítico.
"""
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main():
    datos = load_iris()
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
        datos.data,
        datos.target,
        test_size=0.25,
        random_state=42,
        stratify=datos.target,
    )

    modelo = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1000, random_state=42),
    )
    modelo.fit(X_entrenamiento, y_entrenamiento)
    predicciones = modelo.predict(X_prueba)

    print("EXPERIMENTO EDUCATIVO: CLASIFICACIÓN IRIS")
    print(f"Ejemplos de entrenamiento: {len(X_entrenamiento)}")
    print(f"Ejemplos de prueba: {len(X_prueba)}")
    print(f"Exactitud en este conjunto de prueba: {accuracy_score(y_prueba, predicciones):.3f}")
    print("\nMatriz de confusión (filas = real, columnas = predicción):")
    print(confusion_matrix(y_prueba, predicciones))
    print("\nReporte por clase:")
    print(classification_report(y_prueba, predicciones, target_names=datos.target_names, zero_division=0))
    print("La exactitud depende de la división de datos y no garantiza buen rendimiento en otros datos.")


if __name__ == "__main__":
    main()
