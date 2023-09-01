from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModel
import torch
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='Text Vectorization Server')

# Add an argument for the model name with a default value
parser.add_argument('--model-name', type=str, default='sentence-transformers/all-MiniLM-L6-v2',
                    help='Name of the Hugging Face model to use')

# Parse the command-line arguments
args = parser.parse_args()

# Use args.model_name to access the model name
model_name = args.model_name

app = Flask(__name__)

# Load the pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200

@app.route('/vectorize', methods=['POST'])
def vectorize_text():
    try:
        data = request.get_json()
        query = data.get('query')

        if not query:
            return jsonify({'error': 'Query is required'}), 400

        # Tokenize the text and obtain embeddings
        inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)

        # Extract embeddings from the output
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()

        return jsonify({'vector': embeddings}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)
