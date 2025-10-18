from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import base64
import os
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import secrets

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)

# Enhanced AES Configuration
def generate_secure_key():
    return os.urandom(16)

AES_KEY = os.environ.get('AES_ENCRYPTION_KEY', generate_secure_key())
if isinstance(AES_KEY, str):
    AES_KEY = AES_KEY.encode('utf-8')[:16].ljust(16, b'\0')

# Input validation function - FIXED
def validate_input(text, max_length=10000):
    if not text or not isinstance(text, str):
        return False, "Invalid input text"
    if len(text) > max_length:
        return False, f"Text too long. Maximum {max_length} characters allowed."
    return True, "Valid"

# Caesar Cipher
def caesar_cipher_encrypt(text, shift=3):
    try:
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                encrypted_text += shifted_char
            else:
                encrypted_text += char
        return encrypted_text
    except Exception as e:
        raise Exception(f"Caesar cipher encryption failed: {str(e)}")

def caesar_cipher_decrypt(text, shift=3):
    return caesar_cipher_encrypt(text, -shift)

# Base64
def base64_encrypt(text):
    try:
        text_bytes = text.encode('utf-8')
        base64_bytes = base64.b64encode(text_bytes)
        return base64_bytes.decode('utf-8')
    except Exception as e:
        raise Exception(f"Base64 encoding failed: {str(e)}")

def base64_decrypt(encoded_text):
    try:
        base64_bytes = encoded_text.encode('utf-8')
        text_bytes = base64.b64decode(base64_bytes)
        return text_bytes.decode('utf-8')
    except Exception as e:
        raise Exception(f"Base64 decoding failed: {str(e)}")

# AES Encryption
def aes_encrypt(text):
    try:
        iv = secrets.token_bytes(16)
        cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
        padded_text = pad(text.encode('utf-8'), AES.block_size)
        encrypted_bytes = cipher.encrypt(padded_text)
        combined = iv + encrypted_bytes
        return base64.b64encode(combined).decode('utf-8')
    except Exception as e:
        raise Exception(f"AES encryption failed: {str(e)}")

def aes_decrypt(encrypted_text):
    try:
        combined = base64.b64decode(encrypted_text)
        iv = combined[:16]
        encrypted_bytes = combined[16:]
        cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
        decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
        return decrypted_bytes.decode('utf-8')
    except Exception as e:
        raise Exception(f"AES decryption failed: {str(e)}")

# SHA-256 Hash
def sha256_hash(text):
    try:
        pepper = os.environ.get('HASH_PEPPER', 'default_pepper_change_in_production')
        salted_text = text + pepper
        hash_object = hashlib.sha256()
        hash_object.update(salted_text.encode('utf-8'))
        return hash_object.hexdigest()
    except Exception as e:
        raise Exception(f"SHA-256 hashing failed: {str(e)}")

# Security headers
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.get_json()
        text = data.get('text', '')
        algorithm = data.get('algorithm', '')

        if not text:
            return jsonify({'error': 'Text is required'}), 400
        if not algorithm:
            return jsonify({'error': 'Encryption algorithm is required'}), 400

        if algorithm == 'caesar':
            encrypted_text = caesar_cipher_encrypt(text)
        elif algorithm == 'base64':
            encrypted_text = base64_encrypt(text)
        elif algorithm == 'aes':
            encrypted_text = aes_encrypt(text)
        elif algorithm == 'sha256':
            encrypted_text = sha256_hash(text)
        else:
            return jsonify({'error': 'Invalid algorithm selected'}), 400

        return jsonify({
            'encrypted_text': encrypted_text,
            'algorithm': algorithm,
            'success': True
        })

    except Exception as e:
        return jsonify({'error': f'Operation failed: {str(e)}'}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.get_json()
        encrypted_text = data.get('encrypted_text', '')
        algorithm = data.get('algorithm', '')

        if not encrypted_text:
            return jsonify({'error': 'Encrypted text is required'}), 400
        if not algorithm:
            return jsonify({'error': 'Encryption algorithm is required'}), 400

        if algorithm == 'sha256':
            return jsonify({'error': 'Cannot decrypt SHA-256 hash'}), 400

        if algorithm == 'caesar':
            decrypted_text = caesar_cipher_decrypt(encrypted_text)
        elif algorithm == 'base64':
            decrypted_text = base64_decrypt(encrypted_text)
        elif algorithm == 'aes':
            decrypted_text = aes_decrypt(encrypted_text)
        else:
            return jsonify({'error': 'Invalid algorithm selected'}), 400

        return jsonify({
            'decrypted_text': decrypted_text,
            'algorithm': algorithm,
            'success': True
        })

    except Exception as e:
        return jsonify({'error': f'Operation failed: {str(e)}'}), 500

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'Text Encryption Tool',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    print("🚀 Starting Text Encryption Tool...")
    print("📧 Access: http://127.0.0.1:5000")
    app.run(debug=True, host='127.0.0.1', port=5000)