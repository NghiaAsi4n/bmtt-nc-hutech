from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

# Khởi tạo Flask app
app = Flask(__name__)

caesar_cipher = CaesarCipher()
# API mã hóa Caesar, nhận dữ liệu JSON, trả về JSON
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt_api():
    data = request.json                          # Nhận JSON từ body request
    plain_text = data.get("plain_text", "")      # Lấy plain_text từ JSON
    key = int(data.get("key", 0))                # Lấy key từ JSON
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)  # Mã hóa
    # Trả về kết quả JSON
    return jsonify({
        "plain_text": plain_text,
        "key": key,
        "encrypted_text": encrypted_text
    })

# API giải mã Caesar, nhận dữ liệu JSON, trả về JSON
@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt_api():
    data = request.json                          # Nhận JSON từ body request
    cipher_text = data.get("cipher_text", "")    # Lấy cipher_text từ JSON
    key = int(data.get("key", 0))                # Lấy key từ JSON
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)  # Giải mã
    # Trả về kết quả JSON
    return jsonify({
        "cipher_text": cipher_text,
        "key": key,
        "decrypted_text": decrypted_text
    })

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()   

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# RAILFENCE CIPHER ALGORITHM
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# PLAYFAIR CIPHER ALGORITHM
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

#TRANSPOSITION CIPHER ALGORITHM
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})



# Chạy app API ở port 5084 (nên đổi sang port 5050 nếu chạy song song app.py)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5084, debug=True)
