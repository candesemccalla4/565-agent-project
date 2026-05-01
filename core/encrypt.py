import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

def encrypt_file(filename):
    print(f"Starting encryption for '{filename}'...")

    #Load the Receiver's RSA Public Key
    key_path = os.path.join("keys", "public.pem")
    with open(key_path, "rb") as key_file:
        public_key = RSA.import_key(key_file.read())
    
    #Generate a random AES key
    aes_key = get_random_bytes(32)

    #Read the original file's data
    with open(filename, "rb") as file:
        file_data = file.read()
    
    #Encrypt the file data using AES
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(file_data)

    #Encrypt the AES key itself using the RSA Public Key
    #We use PKCS1_OAEP, which is the standard padding scheme for RSA
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    #Save the bundled package to a new file
    encrypted_filename = filename + ".encrypted"
    with open(encrypted_filename, "wb") as out_file:
        #We must write these pieces in this exact order so we can reverse it later
        out_file.write(encrypted_aes_key)      #The locked AES key
        out_file.write(cipher_aes.nonce)       #A random number used by AES
        out_file.write(tag)                    #The integrity tag
        out_file.write(ciphertext)             #The actual scrambled file data

    print(f"Success! The file has been secured and saved as '{encrypted_filename}'")

