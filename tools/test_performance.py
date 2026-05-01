import os
import time
from core.encrypt import encrypt_file
from core.decrypt import decrypt_file

def create_dummy_file(filename, size_in_mb):
    print(f"Creating a {size_in_mb}MB test file...")

    with open(filename, "wb") as f:
        f.write(os.urandom(size_in_mb * 1024 * 1024))

def run_tests():
    sizes = [1, 50, 200]

    print("--- STARTING PERFORMANCE TEST ---")
    for size in sizes:
        filename = f"test_file_{size}MB.dat"
        create_dummy_file(filename, size)

        #Time the encryption
        start_time = time.time()
        encrypt_file(filename)
        encrypt_duration = time.time() - start_time

        #Time the decryption
        encrypted_filename = filename + ".encrypted"
        start_time = time.time()
        decrypt_file(encrypted_filename, filename)
        decrypt_duration = time.time() - start_time

        #Print the results
        print(f"\nRESULTS FOR {size}MB FILE:")
        print(f"Encryption Time: {encrypt_duration:.4f} seconds")
        print(f"Decryption Time: {decrypt_duration:.4f} seconds")
        print("-" * 40)

if __name__ == "__main__":
    run_tests()