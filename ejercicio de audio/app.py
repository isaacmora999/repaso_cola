from flask import Flask, request, jsonify, render_template
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    try:
        # Check if audio file is in the request
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400

        audio_file = request.files['audio']
        
        # Save the audio file temporarily
        temp_path = 'temp_audio.wav'
        audio_file.save(temp_path)
        
        # Log file size
        file_size = os.path.getsize(temp_path)
        print(f"Received audio file size: {file_size} bytes")  # Debug log

        # Initialize recognizer
        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_path) as source:
            audio = recognizer.record(source)

        # Transcribe audio to text
        text = recognizer.recognize_google(audio)
        
        # Clean up temporary file
        os.remove(temp_path)
        
        return jsonify({'text': text})
    
    except sr.UnknownValueError:
        return jsonify({'error': 'Could not understand audio'}), 400
    except sr.RequestError as e:
        return jsonify({'error': f'Speech recognition error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)