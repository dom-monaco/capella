from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# Dictionary to store short and original URLs
url_mapping = {}

@app.route('/encode', methods=['POST'])
def encode():
    data = request.get_json()

    original_url = data['url']
    # Create a unique hash for the original URL to be used as the short version
    hash_object = hashlib.md5(original_url.encode())
    short_url = hash_object.hexdigest()[:8]

    # Store the mapping
    url_mapping[short_url] = original_url

    return jsonify({'short_url': f'http://short/{short_url}'})

@app.route('/decode/<short_url>', methods=['GET'])
def decode(short_url):
    original_url = url_mapping.get(short_url)

    if original_url is None:
        return jsonify({'error': 'Shortened URL not found'}), 404

    return jsonify({'original_url': original_url})

if __name__ == '__main__':
    app.run(debug=True)
