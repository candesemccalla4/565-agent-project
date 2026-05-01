"""
Handles AES file encryption and RSA encryption of AES key
"""

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from file_handler import read_file, write_file

def encrypt_file(file_path):
    data = read_file(file_path)

    # Generate AES key
    aes_key = get_random_bytes(16)

    # AES Encryption
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    write_file("encrypted_file.bin", cipher_aes.nonce + tag + ciphertext)

    # Load RSA public key
    public_key = RSA.import_key(open("public.pem").read())
    cipher_rsa = PKCS1_OAEP.new(public_key)

    encrypted_key = cipher_rsa.encrypt(aes_key)
    write_file("encrypted_key.bin", encrypted_key)

    print("File encrypted successfully.")
