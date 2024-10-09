# pip install pycryptodome
# pip install cryptography
from Crypto.Cipher import AES
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def encrypt(text, key, iv):
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    c, t = cipher.encrypt_and_digest(text)
    return c

def sign(message, privatekey):
    return privatekey.sign(
    message,
    padding.PSS(
         mgf=padding.MGF1(hashes.SHA256()),
         salt_length=padding.PSS.MAX_LENGTH
     ),
    hashes.SHA256()
)

def validate(message, signature, publickey):
    try:
        publickey.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
    except:
        return False
    return True

def special_encrypt(text, key, iv):
    ans = []
    for i in range(10):
        temp_iv = (int.from_bytes(iv, 'big') ^ i).to_bytes(12, 'big')
        ans.append(encrypt(text, key, temp_iv))
    return ans
