from flask import Flask, render_template, jsonify

app = Flask(__name__)

EPOCAS = [
    {
        "id": "prehistoria",
        "fecha": "Hace millones de años",
        "titulo": "La prehistoria",
        "periodo": "Mucho antes de las primeras ciudades",
        "emoji": "🦖",
        "color": "prehistoria",
        "descripcion": "Explorá un mundo de enormes reptiles, paisajes salvajes y los primeros seres humanos.",
        "datos": [
            "Los dinosaurios dominaron la Tierra durante millones de años.",
            "No todos los dinosaurios vivieron en la misma época.",
            "Los primeros humanos aparecieron muchísimo después de los dinosaurios no avianos."
        ],
        "mision": "Descubrí qué grupo de animales dominó la Tierra durante gran parte de la era Mesozoica.",
        "respuesta": "Los dinosaurios"
    },
    {
        "id": "egipto",
        "fecha": "c. 2600 a. C.",
        "titulo": "Antiguo Egipto",
        "periodo": "La era de los grandes faraones",
        "emoji": "🏺",
        "color": "egipto",
        "descripcion": "Caminá entre pirámides, templos y misterios de una de las civilizaciones más fascinantes.",
        "datos": [
            "Las pirámides de Guiza fueron construidas hace más de 4.500 años.",
            "El río Nilo era fundamental para la agricultura y la vida egipcia.",
            "Los antiguos egipcios utilizaban jeroglíficos como sistema de escritura."
        ],
        "mision": "¿Qué río fue fundamental para el desarrollo del Antiguo Egipto?",
        "respuesta": "El río Nilo"
    },
    {
        "id": "roma",
        "fecha": "Año 80 d. C.",
        "titulo": "Imperio romano",
        "periodo": "Una ciudad en su esplendor",
        "emoji": "🏛️",
        "color": "roma",
        "descripcion": "Conocé una ciudad de caminos, acueductos, mercados y enormes anfiteatros.",
        "datos": [
            "La red de caminos romanos conectaba territorios muy distantes.",
            "Los acueductos transportaban agua hacia las ciudades.",
            "El Coliseo fue inaugurado en el siglo I d. C."
        ],
        "mision": "¿Cómo se llamaba el famoso anfiteatro de Roma?",
        "respuesta": "El Coliseo"
    },
    {
        "id": "edad-media",
        "fecha": "Año 1200",
        "titulo": "Edad Media",
        "periodo": "Castillos, mercados y fortalezas",
        "emoji": "🏰",
        "color": "medieval",
        "descripcion": "Visitá una ciudad medieval, explorá sus murallas y descubrí cómo era la vida cotidiana.",
        "datos": [
            "Los castillos podían servir como residencias y estructuras defensivas.",
            "Los mercados eran importantes centros de intercambio.",
            "La Edad Media duró aproximadamente mil años en Europa."
        ],
        "mision": "¿Qué estructura se utilizaba para proteger muchas ciudades medievales?",
        "respuesta": "Las murallas"
    },
    {
        "id": "mayo",
        "fecha": "25 de mayo de 1810",
        "titulo": "Revolución de Mayo",
        "periodo": "Buenos Aires, 1810",
        "emoji": "🇦🇷",
        "color": "mayo",
        "descripcion": "Viajá a Buenos Aires en 1810 y conocé los acontecimientos que iniciaron el proceso revolucionario.",
        "datos": [
            "La Revolución de Mayo ocurrió en Buenos Aires.",
            "El 25 de mayo de 1810 se formó la Primera Junta de gobierno.",
            "Estos acontecimientos fueron parte del proceso que llevó a la independencia argentina."
        ],
        "mision": "¿Qué gobierno se formó el 25 de mayo de 1810?",
        "respuesta": "La Primera Junta"
    },
    {
        "id": "futuro",
        "fecha": "Año 3000",
        "titulo": "El futuro imaginado",
        "periodo": "Una posible visión del mañana",
        "emoji": "🚀",
        "color": "futuro",
        "descripcion": "Imaginá ciudades futuristas, nuevos medios de transporte y cómo podría cambiar nuestra vida.",
        "datos": [
            "Esta etapa es una ficción: nadie sabe exactamente cómo será el año 3000.",
            "La tecnología podría transformar la energía, la medicina y el transporte.",
            "Las decisiones que tomamos hoy pueden influir en el futuro."
        ],
        "mision": "¿Podemos saber con certeza cómo será la vida en el año 3000?",
        "respuesta": "No"
    }
]

@app.route("/")
def inicio():
    return render_template("index.html", epocas=EPOCAS)

@app.route("/api/epocas")
def api_epocas():
    return jsonify(EPOCAS)

@app.route("/salud")
def salud():
    return {"estado": "ok", "app": "Maquina del Tiempo"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
