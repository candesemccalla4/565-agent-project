"""
Main file for Secure File Transfer System
"""

from keygen import generate_keys
from encrypt import encrypt_file
from decrypt import decrypt_file

def main():
    print("Generating RSA keys...")
    generate_keys()

    print("Encrypting file...")
    encrypt_file("test_files/small.txt")

    print("Decrypting file...")
    decrypt_file("encrypted_file.bin")

if __name__ == "__main__":
    main()
