import streamlit as st
import pandas as pd

from lectura_datos import leer_datos
from regresion import calcular_regresion
from grafica import crear_grafica


# Configuración de la página
st.set_page_config(
    page_title="Regresión Lineal",
    page_icon="📊",
    layout="wide"
)


# Título principal
st.title("Regresión Lineal por Mínimos Cuadrados")

st.write(
    "Aplicación para calcular la recta de regresión lineal "
    "a partir de archivos CSV o TXT."
)

st.divider()


# Sección para cargar archivos
st.subheader("1. Cargar archivo de datos")

st.write(
    "Selecciona un archivo CSV o TXT que contenga "
    "dos columnas numéricas: X y Y."
)

archivo = st.file_uploader(
    "Seleccionar archivo",
    type=["csv", "txt"]
)


if archivo is not None:

    try:
        # Leer los datos
        datos = leer_datos(archivo)

        # Calcular la regresión
        m, b, error, y_estimado = calcular_regresion(datos)

        st.success("Archivo cargado correctamente.")

        # Mostrar la tabla
        st.subheader("2. Datos cargados")

        st.dataframe(
            datos,
            use_container_width=True
        )

        st.write(f"Cantidad de muestras: {len(datos)}")

        st.divider()

        # Mostrar resultados
        st.subheader("3. Resultados de la regresión")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Pendiente (m)",
            f"{m:.4f}"
        )

        col2.metric(
            "Intercepto (b)",
            f"{b:.4f}"
        )

        col3.metric(
            "Error cuadrático total",
            f"{error:.4f}"
        )

        st.markdown("### Ecuación de la recta")

        st.latex(f"y = {m:.4f}x + ({b:.4f})")

        st.divider()

        # Mostrar gráfica
        st.subheader("4. Gráfica de regresión lineal")

        figura = crear_grafica(datos, m, b)

        st.pyplot(figura)

        st.divider()

        # Mostrar tabla de valores estimados
        st.subheader("5. Comparación de resultados")

        resultados = datos.copy()
        resultados["Y estimado"] = y_estimado
        resultados["Error"] = (
            resultados["y"] - resultados["Y estimado"]
        )

        st.dataframe(
            resultados,
            use_container_width=True
        )

    except (ValueError, UnicodeDecodeError, pd.errors.ParserError) as e:
        st.error(f"No se pudieron procesar los datos: {e}")

else:
    st.info("Carga un archivo CSV o TXT para comenzar.")

    st.subheader("Ejemplo de formato")

    ejemplo = pd.DataFrame({
        "x": [1, 2, 3, 4],
        "y": [2, 3, 5, 4]
    })

    st.dataframe(ejemplo, use_container_width=True)

    st.caption(
        "El archivo debe tener al menos dos columnas "
        "numéricas correspondientes a X y Y."
    )