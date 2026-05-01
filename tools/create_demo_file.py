import os

def generate_large_text_file(filename, target_size_mb):
    print(f"Generating a {target_size_mb}MB readable text file. Please wait...")
    
    # Calculate exactly how many bytes we need
    target_bytes = target_size_mb * 1024 * 1024
    
    # This is the paragraph we will repeat thousands of times!
    base_text = (
        "CONFIDENTIAL DATA LOG:\n"
        "This file is being used to demonstrate the power of Hybrid Cryptography. "
        "By combining the speed of the Advanced Encryption Standard (AES) with the "
        "secure key-exchange of Rivest-Shamir-Adleman (RSA) asymmetric encryption, "
        "we can safely transmit large amounts of data across vulnerable networks.\n\n"
    )
    
    # We open the file and keep writing the paragraph until it reaches the target size
    with open(filename, "w", encoding="utf-8") as f:
        current_bytes = 0
        while current_bytes < target_bytes:
            f.write(base_text)
            # Update our byte counter
            current_bytes += len(base_text.encode("utf-8"))
            
    print(f"Success! '{filename}' has been created.")
    print(f"Actual size: {os.path.getsize(filename) / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    # Let's generate a 10MB text file (Perfect for a live presentation!)
    generate_large_text_file("demo2.txt", 200)