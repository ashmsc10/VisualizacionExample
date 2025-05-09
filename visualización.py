from flask import Flask, Response
import seaborn as sns
import matplotlib.pyplot as plt
import io

# Crear la aplicación Flask
app = Flask(__name__)

@app.route("/grafica")
def generar_grafica():
    # Cargar el dataset
    data = sns.load_dataset("penguins")

    # Crear la gráfica
    sns.set_theme()
    plt.figure(figsize=(8, 6))
    sns.histplot(data=data, x="flipper_length_mm", hue="species", multiple="stack")

    # Guardar la imagen en un objeto de memoria
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)

    # Devolver la imagen como respuesta HTTP
    return Response(img.getvalue(), mimetype="image/png")

# Ejecutar la API en Google Colab
app.run()
