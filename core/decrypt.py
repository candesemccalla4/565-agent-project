import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

def decrypt_file(encrypted_filename, original_filename):
    print(f"Starting decryption for '{encrypted_filename}'...")

    #Load the Receiver's RSA Private Key
    key_path = os.path.join("keys", "private.pem")
    with open(key_path, "rb") as key_file:
        private_key = RSA.import_key(key_file.read())

    #Open the encrypted file
    with open(encrypted_filename, "rb") as file:
        #We must read the pieces in the exact same size he was written
        encrypted_aes_key = file.read(256)

        #AES Nonce is 16 bytes
        nonce = file.read(16)

        #AES tag is 16 bytes
        tag = file.read(16)

        ciphertext = file.read()

    #Decrypt the AES key using the RSA Private Key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    try:
        aes_key = cipher_rsa.decrypt(encrypted_aes_key)
    except ValueError:
        print("Error: Incorrect Private Key")
        return
    
    #Use the unlockked AES Key, the nonce, and the tag to decrypt the file data
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce)

    try:
        #This step decrypts the data and checks the tag to ensure no one tampered with it
        decrypted_data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    except ValueError:
        print("Error: The file data was modified or corrupted during transfer")
        return
    
    #Save the successfully decrypted data to a new file

    folder_path = os.path.dirname(original_filename)
    file_name = os.path.basename(original_filename)
    
    recovered_filename = os.path.join(folder_path, "recovered_" + file_name)
    with open(recovered_filename, "wb") as out_file:
        out_file.write(decrypted_data)

    print(f"The file has been unlocked and saved as '{recovered_filename}'")
