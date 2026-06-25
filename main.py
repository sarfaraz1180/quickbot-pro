import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Ustaad ka bot zinda hai ✅", 200

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # WhatsApp verification ke liye
        return request.args.get('hub.challenge', 'No challenge')
    else:
        # Message aane pe yahan logic likhna hai
        print("Message aya:", request.json)
        return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
