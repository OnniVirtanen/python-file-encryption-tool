import os
from Crypto.Cipher import AES

# key = b'16 bytes'

# Encrypt
def encrypt():
    print("This key will be needed in decryption. If the key is lost the data is lost.")
    key = os.urandom(16)
    #key.hex problematic !!!!
    print(key.hex())
    filename = input("Type a filename you want to encrypt: \n")
    with open(filename, "rb") as tieto:
        data = tieto.read()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    print("Encryption completed.")

    # Writing ciphertext, nonce and tag to a file.
    with open('nonce.txt', "wb") as f:
        f.write(nonce)
    with open('enc' + filename, "wb") as f:
        f.write(ciphertext)
    with open('tag.txt', "wb") as f:
        f.write(tag)

# Decrypt
def decrypt():
    filename = input("Type a filename you want to decrypt: \n")
    key_input = input("Type the key that was given when the file was encrypted: \n")
    #bytes.fromhex problematic
    key = bytes.fromhex(key_input)
    with open('nonce.txt', "rb") as f:
        nonce_file = f.read()
    with open(filename, "rb") as f:
        ciphertext_file = f.read()
    with open('tag.txt', "rb") as f:
        tag_file = f.read()
    print("nonce, cipher and tag files are read from the files.")

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce_file)
    plaindata = cipher.decrypt(ciphertext_file)
    try:
        cipher.verify(tag_file)
        print("The message is authentic.")
        with open(filename[3:], "wb") as f:
            f.write(plaindata)
    except ValueError:
        print("Key incorrect or message corrupted")

# User input
user_choice_enc_or_dec = input("E to encrypt. D to decrypt.\n")

if user_choice_enc_or_dec == "E":
    encrypt()
elif user_choice_enc_or_dec == "D":
    decrypt()
else:
    print("error")