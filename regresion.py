import numpy as np


def calcular_regresion(datos):
    """
    Calcula la pendiente, el intercepto
    y el error cuadrático total.
    """
    x = datos["x"].to_numpy()
    y = datos["y"].to_numpy()

    n = len(x)

    suma_x = np.sum(x)
    suma_y = np.sum(y)
    suma_xy = np.sum(x * y)
    suma_x2 = np.sum(x ** 2)

    denominador = n * suma_x2 - suma_x ** 2

    if denominador == 0:
        raise ValueError(
            "No se puede calcular la regresión: "
            "todos los valores de X son iguales."
        )

    # Fórmula de la pendiente
    m = (n * suma_xy - suma_x * suma_y) / denominador

    # Fórmula del intercepto
    b = (suma_y - m * suma_x) / n

    # Calcular valores estimados
    y_estimado = m * x + b

    # Calcular el error cuadrático total
    error = np.sum((y - y_estimado) ** 2)

    return m, b, error, y_estimado