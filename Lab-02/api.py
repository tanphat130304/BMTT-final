from flask import Flask, request, jsonify
from cipher.vigenere import VigenereCipher
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

vigenere_cipher = VigenereCipher()
caesar_cipher = CaesarCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()

@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    try:
        data = request.json
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        plain_text = data['plain_text']
        key = str(data['key'])  # Vigenere key should be string
        
        if not plain_text or not key:
            return jsonify({'error': 'Empty text or key not allowed'}), 400
            
        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    try:
        data = request.json
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        cipher_text = data['cipher_text']
        key = str(data['key'])  # Vigenere key should be string
        
        if not cipher_text or not key:
            return jsonify({'error': 'Empty text or key not allowed'}), 400
            
        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.json
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        plain_text = data['plain_text']
        key = int(data['key'])  # Caesar key should be integer
        
        if not plain_text:
            return jsonify({'error': 'Empty text not allowed'}), 400
            
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = request.json
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        cipher_text = data['cipher_text']
        key = int(data['key'])  # Caesar key should be integer
        
        if not cipher_text:
            return jsonify({'error': 'Empty text not allowed'}), 400
            
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    try:
        data = request.json
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        plain_text = data['plain_text']
        key = int(data['key'])  # Rail fence key should be integer (number of rails)
        
        if not plain_text:
            return jsonify({'error': 'Empty text not allowed'}), 400
            
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    try:
        data = request.json
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        cipher_text = data['cipher_text']
        key = int(data['key'])  # Rail fence key should be integer (number of rails)
        
        if not cipher_text:
            return jsonify({'error': 'Empty text not allowed'}), 400
            
        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    try:
        data = request.json
        if not data or 'key' not in data:
            return jsonify({'error': 'Missing key field'}), 400
            
        key = data['key']
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        return jsonify({'playfair_matrix': playfair_matrix})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    try:
        data = request.json
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        plain_text = data['plain_text']
        key = data['key']
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    try:
        data = request.json
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        cipher_text = data['cipher_text']
        key = data['key']
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    try:
        data = request.json
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        plain_text = data['plain_text']
        key = int(data['key'])  # Transposition key should be integer
        
        if not plain_text:
            return jsonify({'error': 'Empty text not allowed'}), 400
            
        encrypted_text = transposition_cipher.encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    try:
        data = request.json
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        cipher_text = data['cipher_text']
        key = int(data['key'])  # Transposition key should be integer
        
        if not cipher_text:
            return jsonify({'error': 'Empty text not allowed'}), 400
            
        decrypted_text = transposition_cipher.decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
