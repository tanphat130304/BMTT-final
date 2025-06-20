from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Initialize cipher objects
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()

# Home page
@app.route("/")
def home():
    return render_template('index.html')

# Caesar Cipher routes
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return render_template('caesar.html', encrypted_text=encrypted_text)

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return render_template('caesar.html', decrypted_text=decrypted_text)

# Vigenere Cipher routes
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere_encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)
    return render_template('vigenere.html', encrypted_text=encrypted_text)

@app.route("/vigenere_decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)
    return render_template('vigenere.html', decrypted_text=decrypted_text)

# Rail Fence Cipher routes
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence_encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
    return render_template('railfence.html', encrypted_text=encrypted_text)

@app.route("/railfence_decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)
    return render_template('railfence.html', decrypted_text=decrypted_text)

# Playfair Cipher routes
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair_encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
    return render_template('playfair.html', encrypted_text=encrypted_text)

@app.route("/playfair_decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
    return render_template('playfair.html', decrypted_text=decrypted_text)

# Transposition Cipher routes
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition_encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = transposition_cipher.encrypt(text, key)
    return render_template('transposition.html', encrypted_text=encrypted_text)

@app.route("/transposition_decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = transposition_cipher.decrypt(text, key)
    return render_template('transposition.html', decrypted_text=decrypted_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True) 