from flask import Flask, render_template, jsonify, request
import speech_recognition as sr

app = Flask(__name__)
nombres = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escuchar', methods=['POST'])
def escuchar():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Escuchando...")
        try:
            audio = recognizer.listen(source, timeout=5)
            nombre = recognizer.recognize_google(audio, language='es-ES')
            print(f"✅ Nombre detectado: {nombre}")
            nombres.append(nombre)
            return jsonify({"status": "ok", "nombre": nombre, "nombres": nombres})
        except sr.WaitTimeoutError:
            return jsonify({"status": "error", "message": "No se detectó voz. Intenta de nuevo."})
        except sr.UnknownValueError:
            return jsonify({"status": "error", "message": "No entendí lo que dijiste."})
        except sr.RequestError as e:
            return jsonify({"status": "error", "message": f"Error del servicio de reconocimiento: {e}"})

@app.route('/nombres')
def obtener_nombres():
    return jsonify(nombres)

if __name__ == '__main__':
    app.run(debug=True)


