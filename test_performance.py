"""
Measures encryption performance for different file sizes
"""

import time
from encrypt import encrypt_file

def test():
    files = [
        "test_files/small.txt",
        "test_files/medium.txt",
        "test_files/large.txt"
    ]

    for file in files:
        start = time.time()
        encrypt_file(file)
        end = time.time()

        print(f"{file} encryption time: {end - start:.4f} seconds")

if __name__ == "__main__":
    test()
