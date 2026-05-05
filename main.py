from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# आपका असली API URL
REAL_API_BASE = "https://paid.proportalx.workers.dev/number?key=Rexultron&num="

@app.route("/")
def home():
    # यह सिर्फ यह बताने के लिए है कि आपका मास्क काम कर रहा है
    return "<h1>API Mask Active</h1><p>Use: /info?num=9876543210</p>"

@app.route("/info")
def masked_api():
    # ब्राउज़र के URL से नंबर उठाना
    number = request.args.get("num")
    
    if not number:
        return jsonify({"error": "Number missing! Use /info?num=1234567890"}), 400

    try:
        # मास्क के पीछे असली कॉल
        full_url = f"{REAL_API_BASE}{number}"
        response = requests.get(full_url)
        
        # रिजल्ट वापस भेजना
        return jsonify(response.json())
    
    except Exception as e:
        return jsonify({"error": "Connection Failed", "details": str(e)}), 500

if __name__ == "__main__":
    app.run()
