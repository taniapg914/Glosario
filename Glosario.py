from flask import Flask

app = Flask(__name__)

GLOSARIO = {
    "Algoritmo:": {
        "definicion": "un conjunto de instrucciones paso a paso para realizar una tarea o resolver un problema. En IA, un algoritmo puede aprender de los datos para mejorar su ejecución.",
        "imagen": "Algoritmo.jpg"
    },
    "Alucinaciones": {
        "definicion": "Los sistemas de IA generativa pueden generar respuestas inexactas (alucinaciones o confabulaciones) debido a que no distinguen entre lo real y lo falso, o porque carecen de información actualizada tras su entrenamiento. Para solucionar esto y mejorar la precisión sobre un tema específico, los desarrolladores utilizan la «conexión a tierra», un proceso que consiste en proveer al sistema información adicional proveniente de fuentes confiables. ",
        "imagen": "Alucinaciones.jpg"
    },
    "html": {
        "definicion": "El lenguaje de marcado estándar utilizado para crear y estructurar páginas web.",
        "imagen": "Algoritmo.jpg"
    }
}

@app.route("/")
def mostrar_glosario():
    html_content = """
    <html>
    <head>
        <title> Glosario Conceptos de IA</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f9; margin: 40px; color: #333; }
            h1 { text-align: center; color: #2c3e50; }
            .contenedor { max-width: 800px; margin: 0 auto; }
            .tarjeta { background: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; 
                       box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: flex; align-items: center; }
            .texto { flex: 1; padding-right: 20px; }
            .palabra { font-size: 24px; color: #2980b9; text-transform: capitalize; margin: 0 0 10px 0; }
            .definicion { font-size: 16px; line-height: 1.5; color: #555; }
            .imagen-contenedor img { width: 120px; height: 120px; object-fit: contain; border-radius: 4px; }
        </style>
    </head>
    <body>
        <div class="contenedor">
            <h1>📖 Mi Glosario en la Web</h1>
    """
    for palabra, datos in GLOSARIO.items():
        html_content += f"""
            <div class="tarjeta">
                <div class="texto">
                    <h2 class="palabra">{palabra}</h2>
                    <p class="definicion">{datos['definicion']}</p>
                </div>
                <div class="imagen-contenedor">
                    <img src="/static/{datos['imagen']}" alt="{palabra}">
                </div>
            </div>
        """   
    html_content += """
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(debug=True)

