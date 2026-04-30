# Secure File Transfer Using Hybrid Cryptography (AES + RSA)

## Overview

This project implements a secure file transfer system using hybrid cryptography by combining AES (Advanced Encryption Standard) and RSA (Rivest–Shamir–Adleman).

## Features

* Secure large file encryption
* Efficient performance using AES
* Secure key exchange using RSA
* Modular Python implementation

## How It Works

1. Generate RSA keys
2. Generate AES key
3. Encrypt file using AES
4. Encrypt AES key using RSA
5. Decrypt AES key
6. Decrypt file

## Project Structure

* main.py
* encrypt.py
* decrypt.py
* keygen.py
* crypto_utils.py
* file_handler.py
* test_performance.py
* test_files/

## How to Run

Install dependencies:
pip install pycryptodome

Run program:
python main.py

## Author

Candese McCalla
