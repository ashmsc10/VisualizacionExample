import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Configurar la página de Streamlit
st.set_page_config(page_title="Visualización de Penguins", layout="wide")

# Cargar un conjunto de datos de ejemplo
data = sns.load_dataset("penguins")

# Configurar el estilo de la gráfica
sns.set_theme()

# Crear la gráfica
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data=data, x="flipper_length_mm", hue="species", multiple="stack", ax=ax)

# Añadir títulos
ax.set_title("Distribución de la longitud de aletas por especie")
ax.set_xlabel("Longitud de aleta (mm)")
ax.set_ylabel("Frecuencia")

# Mostrar la gráfica en Streamlit
st.pyplot(fig)

# Opcional: Agregar texto explicativo
st.markdown("### Información sobre la visualización")
st.write("Este histograma muestra la distribución de la longitud de las aletas de diferentes especies de pingüinos.")

# Opcional: Agregar un selector para cambiar el eje X
opcion_x = st.selectbox("Selecciona la variable de análisis", ["flipper_length_mm", "bill_length_mm", "bill_depth_mm"])
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data=data, x=opcion_x, hue="species", multiple="stack", ax=ax)
st.pyplot(fig)
