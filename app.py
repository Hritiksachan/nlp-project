
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Load translation models
en_to_hi_translator = pipeline("translation_en_to_hi", model="/Users/mac/Documents/model")
hi_to_en_translator = pipeline("translation_hi_to_en", model="/Users/mac/Documents/model")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate/en-hi', methods=['POST'])
def translate_en_to_hi():
    data = request.json
    text = data.get('text', '')
    translation = en_to_hi_translator(text)
    return jsonify({'translation': translation[0]['translation_text']})

@app.route('/translate/hi-en', methods=['POST'])
def translate_hi_to_en():
    data = request.json
    text = data.get('text', '')
    translation = hi_to_en_translator(text)
    return jsonify({'translation': translation[0]['translation_text']})

if __name__ == '__main__':
    app.run(debug=True)

