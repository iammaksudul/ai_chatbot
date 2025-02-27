from flask import render_template, request, jsonify
from app import create_app
from models.load_model.py import generate_response

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form['input_text']
    response = generate_response(input_text)
    return jsonify({'response': response})