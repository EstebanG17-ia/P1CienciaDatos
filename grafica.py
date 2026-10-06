import matplotlib.pyplot as plt
import numpy as np


def crear_grafica(datos, m, b):
    """
    Crea la gráfica de dispersión y la recta
    de regresión lineal.
    """
    x = datos["x"].to_numpy()
    y = datos["y"].to_numpy()

    x_recta = np.linspace(min(x), max(x), 100)
    y_recta = m * x_recta + b

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.scatter(
        x, y,
        label="Datos originales",
        color="blue"
    )

    ax.plot(
        x_recta, y_recta,
        label="Recta de regresión",
        color="red"
    )

    ax.set_xlabel("Valores de X")
    ax.set_ylabel("Valores de Y")
    ax.set_title("Regresión Lineal por Mínimos Cuadrados")
    ax.legend()
    ax.grid(True)

    return fig