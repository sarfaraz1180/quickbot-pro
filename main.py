from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Ustaad ka AI bot live hai! 🚀"

@app.route('/webhook', methods=['POST'])
def webhook():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
