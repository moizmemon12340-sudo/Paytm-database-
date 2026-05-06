from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "BGMI ID Checker API is Live!"

@app.route('/api/check', methods=['GET'])
def check_id():
    player_id = request.args.get('id')
    if not player_id:
        return jsonify({"error": "Please provide id parameter"}), 400

    url = f"https://id-game-checker.p.rapidapi.com/bgmi/{player_id}"
    headers = {
        "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
        "x-rapidapi-key": "4031d8fca9mshd856dbf4ba5f5e5p1ad3bejsnd6dbde6aa518"
    }

    try:
        response = requests.get(url, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ye line Vercel ke liye zaroori hai
app.run()
