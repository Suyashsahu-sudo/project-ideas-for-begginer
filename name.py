from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_password():
    data = request.get_json()
    length = int(data.get('length', 12))
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)