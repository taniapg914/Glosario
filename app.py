from collections import deque
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL de la API asignada
ML4K_API_URL = "https://machinelearningforkids.co.uk/api/scratch/e52db8c0-d89d-11f1-9dd6-979fe2bdb61cf7ce1819-521f-44bc-abf3-67afb9aab976/classify"

GLOSARIO = {
    "Agentes de IA": {
        "definicion": "Un agente de inteligencia artificial (IA) se refiere a un sistema o programa que es capaz de realizar tareas de forma autónoma en nombre de un usuario o de otro sistema mediante el diseño de su flujo de trabajo y el uso de las herramientas disponibles.",
        "imagen": "AgentesIA.jpeg"
    },
    "Ajuste Fino (Fine-Tuning)": {
        "definicion": "El proceso de tomar un modelo de IA que ya fue preentrenado con datos masivos y entrenarlo un poco más con un conjunto de datos pequeño y muy específico para adaptarlo a una tarea particular.",
        "imagen": "FT.jpg"
    },
    "Algoritmo": {
        "definicion": "Un conjunto de instrucciones paso a paso para realizar una tarea o resolver un problema. En IA, un algoritmo puede aprender de los datos para mejorar su ejecución.",
        "imagen": "Algoritmo.jpg"
    },
    "Alucinaciones": {
        "definicion": "Los sistemas de IA generativa pueden generar respuestas inexactas debido a que no distinguen entre lo real y lo falso, o porque carecen de información actualizada tras su entrenamiento.",
        "imagen": "Alucinaciones.jpg"
    },
    "Aprendizaje No Supervisado (Unsupervised Learning)": {
        "definicion": "Un enfoque de Machine Learning donde el algoritmo recibe datos que no están etiquetados ni clasificados.",
        "imagen": "NoSupervisado.png"
    },
    "Aprendizaje Supervisado (Supervised Learning)": {
        "definicion": "Un enfoque de desarrollo donde el modelo se entrena utilizando un conjunto de datos previamente etiquetados por humanos.",
        "imagen": "Supervisado.png"
    },
    "Aprendizaje automático": {
        "definicion": "El aprendizaje automático (o machine learning) es un área de la informática que entrena a los sistemas informáticos para identificar patrones y hacer predicciones.",
        "imagen": "Aprendizajeautomatico.jpg"
    },
    "Aprendizaje profundo (Deep Learning)": {
        "definicion": "Los modelos de aprendizaje profundo son un subconjunto de las redes neuronales con múltiples capas ocultas.",
        "imagen": "AprendizajeProfundo.png"
    },
    "AutoGen": {
        "definicion": "Microsoft AutoGen es una infraestructura de código abierto para crear agentes de IA y aplicaciones multi-agente usando LLMs.",
        "imagen": "AutoGen.jpg"
    },
    "Cajas negras": {
        "definicion": "Llamamos cajas negras a aquello que no comprendemos porque lo que ocurre en su interior es invisible en algoritmos de ML.",
        "imagen": "CajasNegras.jpg"
    },
    "Computación Cognitiva": {
        "definicion": "Enfoque de IA que busca imitar la forma en que los humanos piensan, razonan y procesan información.",
        "imagen": "ComputacionCognitiva.jpg"
    },
    "Datos de entrenamiento": {
        "definicion": "Datos utilizados para entrenar el algoritmo o modelo de aprendizaje automático.",
        "imagen": "DatosEntrenamiento.png"
    },
    "Generación Aumentada por Recuperación (RAG)": {
        "definicion": "Técnica de arquitectura que permite a un modelo de lenguaje consultar una base de datos externa de confianza.",
        "imagen": "RAG.jpg"
    },
    "Modelos multimodales": {
        "definicion": "Sistema de IA que puede trabajar con diferentes tipos o modos de datos de manera simultánea.",
        "imagen": "Multimodales.jpg"
    },
    "Pesos y Sesgos (Weights and Biases)": {
        "definicion": "Parámetros internos que la IA ajusta durante su entrenamiento para perfeccionar las predicciones.",
        "imagen": "Sesgos.jpg"
    },
    "Procesamiento del Lenguaje Natural (PLN / NLP)": {
        "definicion": "Campo de la IA centrado en la interacción entre las computadoras y el lenguaje humano.",
        "imagen": "NPL.png"
    },
    "Redes neuronales (RN)": {
        "definicion": "Algoritmos de ML inspirados en las interconexiones de las neuronas del cerebro humano.",
        "imagen": "RedesNeuronales.jpg"
    },
    "Sistema Inteligente": {
        "definicion": "Sistemas capaces de aprender, adaptarse y tomar decisiones de manera autónoma.",
        "imagen": "Sistemainteligente.jpg"
    },
    "Sobreajuste (Overfitting)": {
        "definicion": "Error de entrenamiento que ocurre cuando un modelo memoriza los datos de entrenamiento.",
        "imagen": "Sobreajuste.jpg"
    },
    "Tokenización": {
        "definicion": "Proceso de dividir el texto en fragmentos más pequeños llamados tokens.",
        "imagen": "Tkenizacion.jpg"
    },
    "Visión por Computadora": {
        "definicion": "Conjunto de técnicas para enseñar a las computadoras a comprender la información visual.",
        "imagen": "VisionComputadora.jpg"
    }
}

MAPA_HOTEL = {
    "Recepción": ["Habitación 101", "Habitación 102"],
    "Habitación 101": ["Habitación 201", "Habitación 202"],
    "Habitación 102": ["Habitación 203"],
    "Habitación 201": [],
    "Habitación 202": [],
    "Habitación 203": [],
}



# --- Algoritmos de búsqueda ---
def buscar_amigo_bfs(hotel, amigo_buscado):
    cola_de_busqueda = deque(["Recepción"])
    visitados = set()
    pasos = []

    while cola_de_busqueda:
        lugar_actual = cola_de_busqueda.popleft()

        if lugar_actual in visitados:
            continue

        pasos.append(f"🚪 Abriendo puerta en: {lugar_actual}")
        visitados.add(lugar_actual)

        if lugar_actual == amigo_buscado:
            pasos.append(f"🎉 ¡Encontré a {amigo_buscado} en {lugar_actual}!")
            return pasos, True

        for siguiente_lugar in hotel.get(lugar_actual, []):
            if siguiente_lugar not in visitados:
                cola_de_busqueda.append(siguiente_lugar)
                pasos.append(f"   📋 Agregado a la lista de espera: {siguiente_lugar}")

    return pasos, False



# --- Rutas de Flask ---
@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/antecedentes")
def antecedentes():
    return render_template("antecedentes.html")

@app.route("/evaluacion")
def evaluacion():
    return render_template("evaluacion.html")

@app.route("/tipos")
def tipos():
    return render_template("tipos.html")

@app.route("/glosario")
def glosario():
    return render_template("glosario.html", glosario=GLOSARIO)

@app.route('/machine-learning')
def machine_learning():
    return render_template('machine_learning.html')

@app.route('/sistema-inteligente')
def sistema_inteligente():
    info_sistema = GLOSARIO.get("Sistema Inteligente", {})
    return render_template('sistema_inteligente.html', info=info_sistema)

@app.route('/ensayo')
def ensayo():
    return render_template('ensayo.html')

@app.route("/Abusqueda")
def algoritmo_busqueda():
    info_algoritmo = GLOSARIO.get("Algoritmo", {})
    return render_template("Abusqueda.html", info=info_algoritmo)

@app.route("/Cbusqueda", methods=["GET", "POST"])
def clasificar_busqueda():
    info_algoritmo = GLOSARIO.get("Algoritmo", {})
    resultado = None

    if request.method == "POST":
        texto_usuario = request.form.get("texto_busqueda", "").strip()
        if texto_usuario:
            try:
                response = requests.get(ML4K_API_URL, params={"data": texto_usuario})
                if response.ok:
                    data = response.json()
                    if data:
                        top = data[0]
                        resultado = {
                            "etiqueta": top.get("class_name"),
                            "confianza": top.get("confidence"),
                            "texto": texto_usuario
                        }
                else:
                    resultado = {"error": "Error de conexión con el modelo de IA."}
            except Exception as e:
                resultado = {"error": f"Ocurrió un detalle técnico: {str(e)}"}

    return render_template("Cbusqueda.html", info=info_algoritmo, resultado=resultado)

@app.route("/Ebusqueda", methods=["GET", "POST"])
def Ebusqueda():
    info_algoritmo = GLOSARIO.get("Algoritmo", {})
    pasos_ejecucion = []
    tipo_busqueda = None

    if request.method == "POST":
        tipo_busqueda = "bfs"
        objetivo_raw = request.form.get("objetivo", "").strip()

        # Si el usuario solo escribe un número (ej. "201"), se le antepone "Habitación "
        if objetivo_raw.isdigit():
            objetivo = f"Habitación {objetivo_raw}"
        else:
            objetivo = objetivo_raw if objetivo_raw else "Habitación 203"

        pasos_ejecucion, _ = buscar_amigo_bfs(MAPA_HOTEL, objetivo)

    return render_template(
        "Ebusqueda.html", 
        info=info_algoritmo, 
        pasos=pasos_ejecucion, 
        tipo=tipo_busqueda
    )

if __name__ == "__main__":
    app.run(debug=True)