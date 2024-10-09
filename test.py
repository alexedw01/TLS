import crypto
import answer
import os
from cryptography.hazmat.primitives.asymmetric import rsa

for i in range(10):
    message = os.urandom(16)
    key = os.urandom(16)
    iv = os.urandom(12)
    if crypto.encrypt(message,key,iv) == answer.encrypt(message,key,iv):
        print(f"Encrypt test {i} passed")
    else:
        print(f"Encrypt test {i} failed")

for i in range(10):
    private_key = rsa.generate_private_key(public_exponent = 65537, key_size=2048)
    public_key = private_key.public_key()
    message = os.urandom(16)
    sig1 = crypto.sign(message, private_key)
    sig2 = answer.sign(message, private_key)
    if crypto.validate(message, sig1, public_key) and answer.validate(message, sig1, public_key):
        print(f"Signature test {i} passed")
    else:
        print(f"Signature test {i} failed")

for i in range(10):
    message = os.urandom(16)
    key = os.urandom(16)
    iv = os.urandom(12)
    if crypto.encrypt(message,key,iv) == answer.encrypt(message,key,iv):
        print(f"Special Encrypt test {i} passed")
    else:
        print(f"Special Encrypt test {i} failed")