import os
import json
import logging
from flask import Flask, render_template, request, jsonify
import requests
import csv

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get your OpenRouter API key from environment variable
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set.")


# Function to load upvotes from the CSV file
def read_models():
    models = []
    with open('models.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            models.append({'model_name': row['model_name'], 'upvotes': int(row['upvotes'])})
    return models

# Function to save upvotes to the CSV file
def update_upvotes(model_name):
    models = read_models()
    for model in models:
        if model['model_name'] == model_name:
            model['upvotes'] += 1
            break
    with open('models.csv', mode='w', newline='') as file:
        fieldnames = ['model_name', 'upvotes']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(models)
    return models

# Home route to render the page with current vote counts
@app.route('/')
def index():
    models = read_models()  # Load votes from CSV
    return render_template('index.html',  models=models)

# API route to handle vote updates
@app.route('/upvote', methods=['POST'])
def upvote():
    model_name = request.form['model_name']
    models = update_upvotes(model_name)
    return jsonify(models)

# Endpoint to handle user requests
@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get form data
        model = request.form.get('model')
        user_input = request.form.get('user_input')
        option = request.form.get('option')
        tone = request.form.get('tone')
        language = request.form.get('language')

        # Input validation
        if not user_input or not model:
            return jsonify({"error": "User input and model selection are required."}), 400

        # Create a prompt based on the user's options
        prompt = (
            "You are an advanced programming assistant designed to generate high-quality code snippets based on user specifications.\n"
            "Your responses should adhere to the following guidelines:\n"
            "- Provide code examples that are accurate, efficient, and easy to understand.\n"
            "- Use clear and concise comments within the code to explain key sections and logic.\n"
            "- Ensure that the code follows best practices and industry standards relevant to the programming language specified.\n"
            "- If applicable, include information about libraries, dependencies, or frameworks that are necessary for running the code.\n"
            "- Format the output code properly for readability.\n"
            f"\nUser Input: {user_input}\n"
            f"Requirement: {option}\n"
            f"Desired Tone: {tone}\n"
            f"Output Language: {language}\n"
            "Based on this information, please generate the requested code. Also make sure that include some explanation before writing the code don't only focus on writing the code"
        )
        # Make request to OpenRouter API
        headers = {
            'Authorization': f'Bearer {OPENROUTER_API_KEY}',
            'Content-Type': 'application/json'
        }

        data = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": "You are an advanced programming assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5,
        })

        response = requests.post(
            'https://openrouter.ai/api/v1/chat/completions',
            headers=headers,
            data=data
        )

        response.raise_for_status()
        response_data = response.json()
        # Extract the assistant's reply
        output_text = response_data.get('choices', [{}])[0].get('message', {}).get('content', 'No output received')
        logger.info('Successfully generated code.')
        return jsonify({"output": output_text})

    except requests.exceptions.HTTPError as http_err:
        error_message = response.json().get('error', {}).get('message', str(http_err))
        logger.error(f'HTTP error occurred: {error_message}')
        return jsonify({"error": f"HTTP error occurred: {error_message}"}), response.status_code
    except Exception as err:
        logger.error(f'An error occurred: {str(err)}')
        return jsonify({"error": f"An error occurred: {str(err)}"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5003))
    app.run(port=port, debug=False)