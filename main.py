import os
import time
from core.keygen import generate_rsa_keys
from core.encrypt import encrypt_file
from core.decrypt import decrypt_file

def show_menu():
    print("\n" + "="*40)
    print("  HYBRID CRYPTOGRAPHY FILE TRANSFER TOOL")
    print("="*40)
    print("1. Generate RSA Keys (Setup)")
    print("2. Encrypt a File (Sender)")
    print("3. Decrypt a File (Receiver)")
    print("4. Exit")
    print("="*40)

def main():

    target_folder = "test_files"

    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':
            start_time = time.time() 
            generate_rsa_keys()
            elapsed_time = time.time() - start_time
            print(f"\nTime taken to generate RSA keys: {elapsed_time:.2f} sec")
        
        elif choice == '2':
            filename = input("Enter the exact name of the file to encrypt (e.g. secret.txt): ")
            file_path = os.path.join(target_folder, filename)
            if os.path.exists(file_path):
                start_time = time.time()  
                encrypt_file(file_path)
                elapsed_time = time.time() - start_time 
                print(f"\nTime taken to encrypt file: {elapsed_time:.2f} sec")
            else:
                print("Error: File not found! Make sure it is in same folder.")

        elif choice == '3':
            encrypted_filename = input("Enter the name of the encrypted file (e.g., secret.txt.encrypted): ")
            original_filename = input("Enter what the original name was (e.g., secret.txt): ")

            encrypted_file_path = os.path.join(target_folder, encrypted_filename)
            original_file_path = os.path.join(target_folder, original_filename)

            if os.path.exists(encrypted_file_path):
                start_time = time.time()  
                decrypt_file(encrypted_file_path, original_file_path)
                elapsed_time = time.time() - start_time 
                print(f"\nTime taken to decrypt file: {elapsed_time:.2f} sec")
            else:
                print("Error: Encrypted file not found!")
            
        elif choice == '4':
            print("Exiting tool. Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()