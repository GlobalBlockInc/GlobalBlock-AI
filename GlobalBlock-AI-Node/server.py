from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')

    output = subprocess.run(
        ['./main', '-m', './models/7B/ggml-model-q4.bin', '-p', prompt],
        stdout=subprocess.PIPE
    )
    result = output.stdout.decode()

    return jsonify({
        "status": "success",
        "response": result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
