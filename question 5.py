from flask import Flask, request, jsonify, make_response
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# Predefined user credentials (for demo purposes only)
USER_DATA = {
    "username": "testuser",
    "password": "testpassword"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        return make_response(jsonify({"error": "Username or password is missing"}), 400)

    # Check credentials
    if data['username'] == USER_DATA['username'] and data['password'] == USER_DATA['password']:
        return jsonify({"message": "Login successful!"})
    else:
        return make_response(jsonify({"error": "Invalid credentials"}), 401)

@app.route('/')
def index():
    return "Welcome to the user validation app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

