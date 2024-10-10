# pip install pycryptodome
# pip install cryptography
from Crypto.Cipher import AES
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


# Encrypt using AES-GCM and return just the ciphertext (Hint: https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#gcm-mode)
def encrypt(text, key, iv):
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    ciphertext, t = cipher.encrypt_and_digest(text)
    return ciphertext

# Sign using the RSA signature (Hint: use the example in the documentation "https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/")
def sign(message, privatekey):
    return privatekey.sign(
        message, 
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

# Validate the above signature. Return True if valid and False if not
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


# In TLS, we will need to encrypt a series of messages with only slight changes between encryptions
# Create an array of length 10 where the ith value is encrypted with iv ^ i rather than iv
# But the text and key stay the same (feel free to use your encrypt function)
def special_encrypt(text, key, iv):
    ans = []
    for i in range(10):
        temp_iv = (int.from_bytes(iv, 'big') ^ i).to_bytes(12, 'big')
        ans.append(encrypt(text, key, temp_iv))
    return ans