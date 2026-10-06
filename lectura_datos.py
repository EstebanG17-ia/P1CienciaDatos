import pandas as pd
from io import StringIO


def leer_datos(archivo):
    """
    Lee un archivo CSV o TXT y obtiene las columnas X y Y.
    """
    contenido = archivo.getvalue().decode("utf-8-sig")

    # Intentar detectar automáticamente el separador
    separadores = [None, ",", ";", "\t", r"\s+"]

    for separador in separadores:
        try:
            datos = pd.read_csv(
                StringIO(contenido),
                sep=separador,
                engine="python",
                header=None
            )

            if datos.shape[1] >= 2:
                datos = datos.iloc[:, :2].copy()
                datos.columns = ["x", "y"]

                # Convertir los valores a números
                datos["x"] = pd.to_numeric(
                    datos["x"], errors="coerce"
                )
                datos["y"] = pd.to_numeric(
                    datos["y"], errors="coerce"
                )

                # Eliminar encabezados o filas incompletas
                datos = datos.dropna()

                if len(datos) >= 2:
                    return datos.reset_index(drop=True)

        except (ValueError, TypeError, pd.errors.ParserError):
            continue

    raise ValueError(
        "El archivo debe contener al menos dos columnas "
        "numéricas con los valores X y Y."
    )