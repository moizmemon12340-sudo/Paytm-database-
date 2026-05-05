# Paytm-database-from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Original API yahan डालो
REAL_API = "https://paid.proportalx.workers.dev/number?key=Rexultron&num="

@app.route("/")
def home():
    return jsonify({
        "status": "API Mask Running"
    })

# Masked endpoint
@app.route("/api")
def masked_api():

    # Original API call
    response = requests.get(REAL_API)

    try:
        data = response.json()
    except:
        return jsonify({"error": "API response invalid"})

    # Example masking
    if "mobile" in data:
        mobile = str(data["mobile"])
        data["mobile"] = mobile[:2] + "******"

    return jsonify(data)

# Vercel entry
app = app
