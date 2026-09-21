from flask import Flask

app = Flask(__name__)

GLOSARIO = {
    "Agentes de IA": {
        "definicion": "Un agente de inteligencia artificial (IA) se refiere a un sistema o programa que es capaz de realizar tareas de forma autónoma en nombre de un usuario o de otro sistema mediante el diseño de su flujo de trabajo y el uso de las herramientas disponibles. Los agentes de IA pueden abarcar una amplia gama de funcionalidades más allá del procesamiento de lenguaje natural e incluyen la toma de decisiones, la resolución de problemas, la interacción con entornos externos y la ejecución de acciones.",
        "imagen": "AgentesIA.jpeg"
    },
    "Ajuste Fino (Fine-Tuning)": {
        "definicion": "El proceso de tomar un modelo de IA que ya fue preentrenado con datos masivos y entrenarlo un poco más con un conjunto de datos pequeño y muy específico para adaptarlo a una tarea particular. El ajuste fino permite que el modelo se especialice en un dominio o tarea concreta, mejorando su rendimiento en ese contexto.",
        "imagen": "FT.jpg"
    },
    "Algoritmo": {
        "definicion": "Un conjunto de instrucciones paso a paso para realizar una tarea o resolver un problema. En IA, un algoritmo puede aprender de los datos para mejorar su ejecución.",
        "imagen": "Algoritmo.jpg"
    },
    "Alucinaciones": {
        "definicion": "Los sistemas de IA generativa pueden generar respuestas inexactas (alucinaciones o confabulaciones) debido a que no distinguen entre lo real y lo falso, o porque carecen de información actualizada tras su entrenamiento. Para solucionar esto y mejorar la precisión sobre un tema específico, los desarrolladores utilizan la «conexión a tierra», un proceso que consiste en proveer al sistema información adicional proveniente de fuentes confiables.",
        "imagen": "Alucinaciones.jpg"
    },
    "Aprendizaje No Supervisado (Unsupervised Learning)": {
        "definicion": "Un enfoque de Machine Learning donde el algoritmo recibe datos que no están etiquetados ni clasificados. La IA debe explorar la información por sí misma para descubrir patrones ocultos, agrupaciones naturales (clustering) o estructuras internas sin intervención humana.",
        "imagen": "NoSupervisado.png"
    },
    "Aprendizaje Supervisado (Supervised Learning)": {
        "definicion": "Un enfoque de desarrollo donde el modelo se entrena utilizando un conjunto de datos previamente etiquetados por humanos. El sistema aprende la relación entre los datos de entrada y la respuesta correcta esperada. Este enfoque es útil para tareas como clasificación y regresión, donde se busca predecir resultados basados en ejemplos conocidos.",
        "imagen": "Supervisado.png"
    },
    "Aprendizaje automático": {
        "definicion": "El aprendizaje automático (o machine learning) es un área de la informática que entrena a los sistemas informáticos para identificar patrones y hacer predicciones a través de la repetición constante de datos y algoritmos. Es una tecnología ideal para desafíos que la programación tradicional no puede resolver fácilmente, tales como el reconocimiento de imágenes y la traducción de idiomas.",
        "imagen": "Aprendizajeautomatico.jpg"
    },
    "Aprendizaje profundo (Deep Learning)": {
        "definicion": "Los modelos de aprendizaje profundo son un subconjunto de las redes neuronales. Con múltiples capas ocultas, los algoritmos de aprendizaje profundo pueden reconocer patrones más sutiles y complejos. Al igual que las redes neuronales, los algoritmos de aprendizaje profundo involucran nodos interconectados donde se ajustan los pesos, pero, como se mencionó anteriormente, hay más capas y más cálculos que pueden realizar ajustes a la salida para determinar cada decisión. Las decisiones de los modelos de aprendizaje profundo suelen ser muy difíciles de interpretar, ya que hay muchas capas ocultas que realizan diferentes cálculos que no se traducen fácilmente a reglas en inglés (u otro idioma legible para humanos).",
        "imagen": "AprendizajeProfundo.png"
    },
    "AutoGen": {
        "definicion": "Microsoft AutoGen es una infraestructura de código abierto para crear agentes de IA y otras aplicaciones de inteligencia artificial código abierto para crear agentes de IA. Es el resultado de la incursión de Microsoft Research en la IA agéntica, que simplifica la creación de sistemas de multi-agente usando modelos de lenguaje grande (LLMs).",
        "imagen": "AutoGen.jpg"
    },
    "Cajas negras": {
        "definicion": "Llamamos cajas negras a aquello que no comprendemos porque lo que ocurre en su interior es invisible. Muchos algoritmos de aprendizaje automático son cajas negras, lo que significa que no entendemos cómo un sistema utiliza las características de los datos al tomar decisiones (generalmente, sabemos qué características se utilizan, pero no cómo se utilizan). Actualmente existen dos formas principales de desvelar el funcionamiento interno de los algoritmos de IA: el aprendizaje automático interpretable y el aprendizaje automático explicable.",
        "imagen": "CajasNegras.jpg"
    },
    "Computación Cognitiva": {
        "definicion": "Enfoque de IA que busca imitar la forma en que los humanos piensan, razonan y procesan información, con el objetivo de lograr un procesamiento más similar al humano.",
        "imagen": "ComputacionCognitiva.jpg"
    },
    "Datos de entrenamiento": {
        "definicion": "Estos son los datos utilizados para entrenar el algoritmo o modelo de aprendizaje automático. Han sido generados por humanos en su trabajo u otros contextos en el pasado. Aunque parezca sencillo, los datos de entrenamiento son cruciales porque los datos incorrectos pueden perpetuar sesgos sistémicos.",
        "imagen": "DatosEntrenamiento.png"
    },
    "Generación Aumentada por Recuperación (RAG)": {
        "definicion": "Una técnica de arquitectura que permite a un modelo de lenguaje consultar una base de datos externa de confianza para responder preguntas, reduciendo drásticamente las alucinaciones sin necesidad de reentrenar todo el modelo.",
        "imagen": "RAG.jpg"
    },
    "Modelos multimodales": {
        "definicion": "Un modelo multimodal es un sistema de inteligencia artificial que puede trabajar con diferentes tipos o modos de datos de manera simultánea. Puede mirar imágenes, escuchar sonidos y leer palabras. ¡Es la multitarea definitiva! Puede combinar toda esta información para hacer cosas como responder preguntas sobre imágenes.",
        "imagen": "Multimodales.jpg"
    },
    "Pesos y Sesgos (Weights and Biases)": {
        "definicion": "Los parámetros internos que la IA ajusta durante su entrenamiento. Los pesos determinan la importancia o fuerza que tiene una conexión de datos específica, mientras que el sesgo es un valor numérico fijo que ayuda a ajustar la predicción general del modelo.",
        "imagen": "Sesgos.jpg"
    },
    "Procesamiento del Lenguaje Natural (PLN / NLP)": {
        "definicion": "El procesamiento del lenguaje natural (PLN) es un campo de la inteligencia artificial que se centra en la interacción entre las computadoras y el lenguaje humano. Su objetivo es permitir que las máquinas comprendan, interpreten y generen lenguaje de manera que sea natural para los humanos. El PLN combina la lingüística computacional con algoritmos de aprendizaje automático para analizar y modelar el lenguaje, permitiendo aplicaciones como chatbots, traducción automática, análisis de sentimientos y reconocimiento de voz.",
        "imagen": "NPL.png"
    },
    "Redes neuronales (RN)": {
        "definicion": "Las redes neuronales, también llamadas redes neuronales artificiales (RNA), son un subconjunto de los algoritmos de aprendizaje automático (ML). Se inspiraron en las interconexiones de las neuronas y las sinapsis del cerebro humano. En una red neuronal, después de que los datos ingresan a la primera capa, pasan por una capa oculta de nodos donde se realizan cálculos que ajustan la fuerza de las conexiones entre ellos, para luego llegar a una capa de salida. Las redes neuronales son la base de los modelos de aprendizaje profundo (deep learning) y se utilizan para tareas como el reconocimiento de imágenes, la traducción automática y la generación de texto.",
        "imagen": "RedesNeuronales.jpg"
    },
    "Sobreajuste (Overfitting)": {
        "definicion": "Un error de entrenamiento que ocurre cuando un modelo memoriza los datos de entrenamiento de forma tan estricta que es incapaz de generalizar o funcionar correctamente con datos nuevos. El sobreajuste puede ser mitigado mediante técnicas como la regularización, la validación cruzada y el aumento de datos.",
        "imagen": "Sobreajuste.jpg"
    },
    "Tokenización": {
        "definicion": "El proceso de dividir el texto en fragmentos más pequeños llamados tokens (que pueden ser palabras completas, sílabas o caracteres) antes de que un modelo de lenguaje los procese. Es la unidad básica de medida que los modelos de lenguaje utilizan para leer y calcular el costo de uso de sus sistemas.",
        "imagen": "Tkenizacion.jpg"
    },
    "Visión por Computadora": {
        "definicion": "La visión por computadora es un conjunto de desafíos computacionales que buscan enseñar a las computadoras a comprender la información visual, incluyendo objetos, imágenes, escenas y movimiento (incluido el video). La visión por computadora (a menudo considerada un problema de IA) utiliza técnicas como el aprendizaje automático para lograr este objetivo.",
        "imagen": "VisionComputadora.jpg"
    }
}

@app.route("/")
def mostrar_glosario():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Portal de Inteligencia Artificial</title>
        <style>
            html {
                scroll-padding-top: 80px;
                scroll-behavior: smooth;
            }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                background-color: #f4f4f9; 
                margin: 0;
                padding-top: 70px;
                color: #333; 
            }

            .navbar {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                background-color: #2c3e50;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 12px 30px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.2);
                z-index: 1000;
                box-sizing: border-box;
            }
            .navbar .logo {
                color: #ecf0f1;
                font-size: 20px;
                font-weight: bold;
                text-decoration: none;
            }
            .navbar .menu {
                list-style: none;
                margin: 0;
                padding: 0;
                display: flex;
                gap: 20px;
            }
            .navbar .menu a {
                color: #ecf0f1;
                text-decoration: none;
                font-size: 15px;
                transition: color 0.3s;
            }
            .navbar .menu a:hover {
                color: #3498db;
            }
            .buscador {
                padding: 8px 15px;
                border-radius: 20px;
                border: none;
                outline: none;
                font-size: 14px;
                width: 200px;
            }

            h1, h2 { text-align: center; color: #2c3e50; }
            h1 { margin-top: 30px; }
            .contenedor { max-width: 900px; margin: 20px auto; padding: 0 20px; }
            
            .seccion-bloque {
                background: white;
                padding: 30px;
                margin-bottom: 30px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                line-height: 1.6;
            }
            .seccion-bloque p { text-align: justify; color: #555; }

            .grid-tipos {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 20px;
            }
            .tarjeta-tipo {
                background: #f8f9fa;
                border-left: 4px solid #3498db;
                padding: 15px;
                border-radius: 4px;
            }
            .tarjeta-tipo h3 { margin-top: 0; color: #2980b9; }

            .tarjeta { 
                background: white; 
                padding: 20px; 
                margin-bottom: 20px; 
                border-radius: 8px; 
                box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
                display: flex; 
                align-items: center; 
            }
            .texto { flex: 1; padding-right: 20px; }
            .palabra { font-size: 24px; color: #2980b9; margin: 0 0 10px 0; text-align: left; }
            .definicion { font-size: 16px; line-height: 1.5; color: #555; text-align: justify; } 
            .imagen-contenedor img { width: 200px; height: 200px; object-fit: contain; border-radius: 4px; }

            footer {
                background-color: #2c3e50;
                color: #ecf0f1;
                padding: 15px 20px;
                margin-top: 40px;
                font-size: 14px;
            }
            .footer-contenido {
                max-width: 900px;
                margin: 0 auto;
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                gap: 10px;
            }
            .footer-info a {
                color: #3498db;
                text-decoration: none;
            }
            .footer-info a:hover {
                text-decoration: underline;
            }
            .copyright {
                font-size: 12px;
                color: #bdc3c7;
            }
        </style>
    </head>
    <body>
        <nav class="navbar">
            <a href="#" class="logo">Portal IA</a>
            <ul class="menu">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="#antecedentes">Antecedentes</a></li>
                <li><a href="#evaluacion">Evaluación</a></li>
                <li><a href="#tipos">Tipos de IA</a></li>
                <li><a href="#glosario">Glosario</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
            <input type="text" id="inputBuscar" class="buscador" placeholder="Buscar concepto..." onkeyup="filtrarPorPalabra()">
        </nav>

        <div class="contenedor">
            <!-- Sección Inicio -->
            <section id="inicio" class="seccion-bloque">
                <h1>Inteligencia Artificial: Transformando el Futuro</h1>
                <p>Bienvenido al portal educativo de Inteligencia Artificial. Este espacio está diseñado para explorar los fundamentos, historia, arquitecturas y conceptos clave que definen la tecnología moderna. La Inteligencia Artificial es el campo de la informática dedicado a resolver problemas cognitivos comúnmente asociados con la inteligencia humana, como el aprendizaje, la creación y el reconocimiento de patrones.</p>
            </section>

            <!-- Sección Antecedentes -->
            <section id="antecedentes" class="seccion-bloque">
                <h2>Antecedentes Históricos</h2>
                <p>La IA tiene sus raíces en la antigüedad con mitos y automatismos, pero su era formal comenzó en el siglo XX. En 1950, <strong>Alan Turing</strong> propuso la famosa "Prueba de Turing" para determinar si una máquina puede pensar. Posteriormente, en 1956, la Conferencia de Dartmouth marcó el nacimiento oficial del campo como disciplina académica.</p>
                <p>A lo largo de las décadas, la IA ha pasado por ciclos de gran optimismo seguidos de períodos de desinterés y falta de financiamiento conocidos como "Inviernos de la IA". Sin embargo, el aumento exponencial en el poder de cómputo, la disponibilidad de Big Data y el avance del Aprendizaje Profundo (Deep Learning) han impulsado una revolución sin precedentes en el siglo XXI.</p>
            </section>

            <!-- Sección Evaluación de IA -->
            <section id="evaluacion" class="seccion-bloque">
                <h2>Evaluación y Métricas de IA</h2>
                <p>Medir el desempeño de los modelos de Inteligencia Artificial es crucial para garantizar su precisión, equidad y confiabilidad. Dependiendo del tipo de tarea, se utilizan diferentes enfoques y métricas:</p>
                <ul>
                    <li><strong>Clasificación:</strong> Métricas como <em>Precisión (Accuracy)</em>, <em>Exhaustividad (Recall)</em>, <em>Precision</em> y la puntuación <em>F1-Score</em> evalúan la capacidad de categorizar datos correctamente.</li>
                    <li><strong>Regresión:</strong> Se utilizan métricas de error como el Error Cuadrático Medio (MSE) y el Error Absoluto Medio (MAE).</li>
                    <li><strong>Modelos de Lenguaje (LLMs):</strong> Se evalúan con pruebas especializadas de alucinación, coherencia y referencias cruzadas mediante técnicas como RAG o métricas como BLEU y ROUGE.</li>
                </ul>
            </section>

            <!-- Sección Tipos de IA -->
            <section id="tipos" class="seccion-bloque">
                <h2>Tipos de Inteligencia Artificial</h2>
                <div class="grid-tipos">
                    <div class="tarjeta-tipo">
                        <h3>IA Estrecha (ANI)</h3>
                        <p>Diseñada para realizar una tarea específica (como reconocimiento facial o ajedrez). Es el único tipo de IA existente en la actualidad.</p>
                    </div>
                    <div class="tarjeta-tipo">
                        <h3>IA General (AGI)</h3>
                        <p>Sistemas hipotéticos que poseerían la capacidad de comprender, aprender y aplicar conocimiento en cualquier disciplina, al nivel de un ser humano.</p>
                    </div>
                    <div class="tarjeta-tipo">
                        <h3>Superinteligencia (ASI)</h3>
                        <p>Concepto teórico que describe una IA que supera ampliamente el intelecto humano en todos los aspectos, incluyendo la creatividad y las relaciones sociales.</p>
                    </div>
                </div>
            </section>

            <!-- Sección Glosario -->
            <div id="glosario">
                <h2>Glosario de Conceptos</h2>
    """
    
    for palabra, datos in GLOSARIO.items():
        html_content += f"""
                <div class="tarjeta">
                    <div class="texto">
                        <h3 class="palabra">{palabra}</h3>
                        <p class="definicion">{datos['definicion']}</p>
                    </div>
                    <div class="imagen-contenedor">
                        <img src="/static/{datos['imagen']}" alt="{palabra}">
                    </div>
                </div>
        """
        
    html_content += """
            </div>
        </div>

        <footer id="contacto">
            <div class="footer-contenido">
                <div class="footer-info">
                    <strong>Contacto:</strong> <a href="mailto:utp0211991@alumno.utpuebla.edu.mx">utp0211991@alumno.utpuebla.edu.mx</a>
                </div>
                <div class="copyright">
                    &copy; Glosario de IA. Todos los derechos reservados.
                </div>
            </div>
        </footer>

        <script>
            function filtrarPorPalabra() {
                let input = document.getElementById('inputBuscar').value.toLowerCase();
                let tarjetas = document.getElementsByClassName('tarjeta');

                for (let i = 0; i < tarjetas.length; i++) {
                    let palabra = tarjetas[i].getElementsByClassName('palabra')[0].innerText.toLowerCase();

                    if (palabra.includes(input)) {
                        tarjetas[i].style.display = "flex";
                    } else {
                        tarjetas[i].style.display = "none";
                    }
                }
            }
        </script>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(debug=False)