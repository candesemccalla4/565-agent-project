"""
Handles RSA decryption of AES key and AES file decryption
"""

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from file_handler import read_file, write_file

def decrypt_file(file_path):
    encrypted_data = read_file(file_path)

    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]

    # Load RSA private key
    private_key = RSA.import_key(open("private.pem").read())
    cipher_rsa = PKCS1_OAEP.new(private_key)

    encrypted_key = read_file("encrypted_key.bin")
    aes_key = cipher_rsa.decrypt(encrypted_key)

    # AES Decryption
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    write_file("decrypted_file.txt", data)

    print("File decrypted successfully.")
