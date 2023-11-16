from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/encode', methods=['POST'])
def encode():


@app.route('/decode/<short_url>', methods=['GET'])
def decode(short_url):


if __name__ == '__main__':
    app.run(debug=True)
