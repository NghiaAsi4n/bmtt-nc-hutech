from flask import Flask, request, render_template
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.transposition import TranspositionCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

# Khởi tạo Flask app và các đối tượng cipher
app = Flask(__name__)
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
transposition_cipher = TranspositionCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()

# ===============================
# Trang chủ - route cho địa chỉ "/"
# ===============================
@app.route("/", methods=["GET"])
def home():
    """Hiển thị trang chủ sử dụng file index.html (trong folder templates)"""
    return render_template("index.html")

# ====================================================
# Route cho Caesar Cipher - nhận và trả kết quả mã hóa
# ====================================================
@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    encrypt_result = ""
    decrypt_result = ""
    if request.method == "POST":
        if "encrypt" in request.form:
            plain_text = request.form.get("plain_text", "")
            key = int(request.form.get("key_encrypt", "0"))
            encrypt_result = caesar_cipher.encrypt_text(plain_text, key)
        elif "decrypt" in request.form:
            cipher_text = request.form.get("cipher_text", "")
            key = int(request.form.get("key_decrypt", "0"))
            decrypt_result = caesar_cipher.decrypt_text(cipher_text, key)
    return render_template("caesar.html", encrypt_result=encrypt_result, decrypt_result=decrypt_result)

# ====================================================
# Route cho Vigenère Cipher
# ====================================================
@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    encrypt_result = ""
    decrypt_result = ""
    if request.method == "POST":
        if "encrypt" in request.form:
            plain_text = request.form.get("plain_text", "")
            key = request.form.get("key_encrypt", "")
            encrypt_result = vigenere_cipher.vigenere_encrypt(plain_text, key)
        elif "decrypt" in request.form:
            cipher_text = request.form.get("cipher_text", "")
            key = request.form.get("key_decrypt", "")
            decrypt_result = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return render_template("vigenere.html", encrypt_result=encrypt_result, decrypt_result=decrypt_result)

# ====================================================
# Route cho Transposition Cipher
# ====================================================
@app.route("/transposition", methods=["GET", "POST"])
def transposition():
    encrypt_result = ""
    decrypt_result = ""
    if request.method == "POST":
        if "encrypt" in request.form:
            plain_text = request.form.get("plain_text", "")
            key = int(request.form.get("key_encrypt", "0"))
            encrypt_result = transposition_cipher.encrypt(plain_text, key)
        elif "decrypt" in request.form:
            cipher_text = request.form.get("cipher_text", "")
            key = int(request.form.get("key_decrypt", "0"))
            decrypt_result = transposition_cipher.decrypt(cipher_text, key)
    return render_template("transposition.html", encrypt_result=encrypt_result, decrypt_result=decrypt_result)

# ====================================================
# Route cho Rail Fence Cipher
# ====================================================
@app.route("/railfence", methods=["GET", "POST"])
def railfence():
    encrypt_result = ""
    decrypt_result = ""
    if request.method == "POST":
        if "encrypt" in request.form:
            plain_text = request.form.get("plain_text", "")
            key = int(request.form.get("key_encrypt", "0"))
            encrypt_result = railfence_cipher.rail_fence_encrypt(plain_text, key)
        elif "decrypt" in request.form:
            cipher_text = request.form.get("cipher_text", "")
            key = int(request.form.get("key_decrypt", "0"))
            decrypt_result = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return render_template("railfence.html", encrypt_result=encrypt_result, decrypt_result=decrypt_result)

# ====================================================
# Route cho Playfair Cipher
# ====================================================
@app.route("/playfair", methods=["GET", "POST"])
def playfair():
    encrypt_result = ""
    decrypt_result = ""
    if request.method == "POST":
        if "encrypt" in request.form:
            plain_text = request.form.get("plain_text", "")
            key = request.form.get("key_encrypt", "")
            matrix = playfair_cipher.create_playfair_matrix(key)
            encrypt_result = playfair_cipher.playfair_encrypt(plain_text, matrix)
        elif "decrypt" in request.form:
            cipher_text = request.form.get("cipher_text", "")
            key = request.form.get("key_decrypt", "")
            matrix = playfair_cipher.create_playfair_matrix(key)
            decrypt_result = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return render_template("playfair.html", encrypt_result=encrypt_result, decrypt_result=decrypt_result)

# ===================================
# Khởi động server Flask nếu chạy file này
# ===================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5084, debug=True)
