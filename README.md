## 👥 Authors
* **Candese McCalla** (GitHub: https://github.com/Darius72C)
* **Darrell Coulibaly** (GitHub: https://github.com/candesemccalla4)

# 🔐 Secure File Transfer Tool: Hybrid Cryptography

## 📖 Project Overview
It is a command-line application that demonstrates the power and efficiency of **Hybrid Cryptography** for secure file transfers. 

By combining the lightning-fast processing speed of symmetric encryption (**AES-256**) with the secure key-exchange capabilities of asymmetric encryption (**RSA-2048**), this tool allows users to safely encrypt massive data payloads without suffering the severe performance bottlenecks of using RSA alone.

## ✨ Features
* **RSA Key Generation:** Automatically generates and locally stores 2048-bit public and private `.pem` keys.
* **Hybrid Encryption (Sender):** Secures files using AES-256 and securely wraps the temporary AES key using the receiver's RSA Public Key.
* **Hybrid Decryption (Receiver):** Unlocks the AES key using the RSA Private Key, verifies data integrity, and recovers the original file.
* **Live Demo Generator:** Includes a tool to instantly generate a 200MB readable text file for live presentation purposes.
* **Automated Performance Testing:** Includes a testing suite to measure AES processing speeds under moderate and stress loads.
