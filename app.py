from flask import Flask, request, jsonify

app = Flask(__name__)

# === Example Route ===
@app.route('/')
def home():
    return "GlobalBlockInc AI Bot is Running!"

# === AI Automation Endpoint (Placeholder) ===
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    # Example: extract prompt from input JSON
    prompt = data.get('prompt', '')

    # === Placeholder Response (replace with real AI logic) ===
    ai_response = f"Received prompt: {prompt}. AI bot will process this soon."

    return jsonify({
        "status": "success",
        "response": ai_response
    })

# === Run Server ===
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
