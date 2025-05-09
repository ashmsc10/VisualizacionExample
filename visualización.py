import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
data = sns.load_dataset("penguins")

# Configurar el estilo de la gráfica
sns.set_theme()

# Crear la gráfica: Histograma de la longitud de la aleta según la especie
plt.figure(figsize=(8, 6))
sns.histplot(data=data, x="flipper_length_mm", hue="species", multiple="stack")

# Mostrar la gráfica
plt.title("Distribución de la longitud de aletas por especie")
plt.xlabel("Longitud de aleta (mm)")
plt.ylabel("Frecuencia")
plt.show()
