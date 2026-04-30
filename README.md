# 🔐 Secure File Transfer Using Hybrid Cryptography (AES + RSA)

## 📌 Overview

This project implements a secure file transfer system using hybrid cryptography, combining AES (Advanced Encryption Standard) and RSA (Rivest–Shamir–Adleman).

The system securely transfers large files while maintaining confidentiality, integrity, and efficiency.

---

## 🎯 Objectives

* Secure large file transfers
* Ensure strong encryption and key protection
* Improve performance compared to RSA-only systems

---

## ⚙️ How It Works

1. Generate RSA key pair
2. Generate AES key
3. Encrypt file using AES
4. Encrypt AES key using RSA
5. Transfer encrypted file and key
6. Decrypt AES key
7. Decrypt file

---

## 📁 Project Structure

* main.py
* encrypt.py
* decrypt.py
* keygen.py
* crypto_utils.py
* file_handler.py
* test_performance.py
* test_files/

---

## 🚀 How to Run

Install:
pip install pycryptodome

Run:
python main.py

---

## 👤 Author

Candese McCalla
