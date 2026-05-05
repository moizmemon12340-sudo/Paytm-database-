from flask import Flask, jsonify
import requests

app = Flask(__name__)

# यहाँ अपना असली Hugging Face API या कोई भी URL डालें
REAL_API = "https://paid.proportalx.workers.dev/number?key=Rexultron&num=" 

@app.route("/api")
def masked_api():
    # आप चाहें तो यहाँ अपना API Token भी छिपा सकते हैं
    r = requests.get(REAL_API)
    return jsonify(r.json())

# Vercel के लिए यह ज़रूरी है
if __name__ == "__main__":
    app.run()
