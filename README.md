# 🔐 Secure File Transfer Using Hybrid Cryptography (AES + RSA)

## 📌 Overview

This project implements a secure file transfer system using **hybrid cryptography**, combining AES (Advanced Encryption Standard) and RSA (Rivest–Shamir–Adleman).

AES is used for fast and efficient encryption of large files, while RSA is used to securely encrypt and transfer the AES key. This approach ensures both **high performance and strong security**, addressing limitations of traditional encryption methods.

---

## 🎯 Objectives

* Secure large file transfers
* Ensure confidentiality, integrity, and secure key exchange
* Improve performance compared to RSA-only systems

---

## ⚙️ How It Works

1. Generate RSA key pair
2. Generate AES symmetric key
3. Encrypt file using AES
4. Encrypt AES key using RSA public key
5. Transfer encrypted file and key
6. Decrypt AES key using RSA private key
7. Decrypt file using AES

---

## 🧠 System Architecture

Sender → AES Encrypt File → RSA Encrypt Key → Secure Transfer → RSA Decrypt Key → AES Decrypt File → Receiver

---

## 📁 Project Structure

* main.py – Controls full workflow
* encrypt.py – Handles AES encryption + RSA key encryption
* decrypt.py – Handles AES decryption + RSA key decryption
* keygen.py – Generates RSA key pairs
* crypto_utils.py – Cryptographic helper functions
* file_handler.py – File operations
* test_performance.py – Performance testing
* test_files/ – Sample files for testing

---

## 🚀 How to Run

Install dependencies:
pip install pycryptodome

Run program:
python main.py

Run performance test:
python test_performance.py

---

## 📊 Results

The hybrid cryptographic system demonstrates:

* Fast encryption for large files using AES
* Secure key exchange using RSA
* Improved scalability compared to RSA-only systems

---

## 🚀 Future Improvements

* Add graphical user interface (GUI)
* Implement secure network transfer (TLS)
* Add digital signatures for authentication
* Integrate cloud-based storage

---

## 👤 Author

Candese McCalla
Darrell Coulibaly
