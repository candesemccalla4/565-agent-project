import os
from Crypto.PublicKey import RSA

def generate_rsa_keys():
    print("Generating RSA keys... this might take a second.")

    # 1. Create the 'key' folder if it does not exist
    key_folder = "keys"
    if not os.path.exists(key_folder):
        os.makedirs(key_folder)

    #Generate a new RSA key pair
    key = RSA.generate(2048)

    #Extract the Private Key and save it to keys file
    private_key = key.export_key()
    private_path = os.path.join(key_folder, "private.pem")
    with open(private_path, "wb") as file_out:
        file_out.write(private_key)
    print(f"Private Key saved as '{private_path}'")

    #Extract the Public Key and save it to keys file
    public_key = key.publickey().export_key()
    public_path = os.path.join(key_folder, "public.pem")
    with open(public_path, "wb") as file_out:
        file_out.write(public_key)
    print(f"Public Key saved as '{public_path}'")

if __name__ == "__main__":
    generate_rsa_keys()