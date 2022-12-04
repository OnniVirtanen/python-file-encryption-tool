import os
from Crypto.Cipher import AES
import time

# Encrypt file
def encrypt():
    key = os.urandom(16)
    filename = input("Type a filename you want to encrypt: \n")

    print(f'Encrypting file "{filename}"...')
    with open(filename, "rb") as tieto:
        data = tieto.read()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    print("The key is needed for decryption. If lost, the data cannot be retrieved!")
    print("The tag is needed to check the file authenticity.\n")
    print("Save this key:", key.hex() + "\n")
    print("Save this tag:", tag.hex() + "\n")

    # Writing ciphertext, nonce and tag to a file.
    with open('nonce.txt', "wb") as f:
        f.write(nonce)
    with open('enc_' + filename, "wb") as f:
        f.write(ciphertext)
    with open('tag.txt', "wb") as f:
        f.write(tag)
    print("The file was successfully encrypted.")

# Decrypt file
def decrypt():
    filename = input("Type a filename you want to decrypt: \n")
    key_input = input("Type the key that was given when the file was encrypted: \n")
    #bytes.fromhex problematic
    key = bytes.fromhex(key_input)
    with open('nonce.txt', "rb") as f:
        nonce_file = f.read()
    with open(filename, "rb") as f:
        ciphertext_file = f.read()

    tag_input = input("Type the tag that was given when the file was encrypted: \n")
    tag_file = bytes.fromhex(tag_input)

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce_file)
    plaindata = cipher.decrypt(ciphertext_file)
    try:
        cipher.verify(tag_file)
        print("The file is authentic.")
        with open("dec_" + filename[4:], "wb") as f:
            f.write(plaindata)
        print("The file was successfully decrypted.")
    except ValueError:
        print("Key incorrect or message corrupted")

# User input
print("Welcome to ViCrypt!")
print("This program is used for file encryption and decryption.")
print("The program uses AES 256 algorithm to encrypt files.")

proceed = str(input("Proceed: Y/N\n"))

if proceed == "Y" or proceed == "y":
    user_choice_enc_or_dec = input("Type in E or D, E=Encrypt, D=Decrypt.\n")

    if user_choice_enc_or_dec == "E":
        encrypt()
    elif user_choice_enc_or_dec == "D":
        decrypt()
    else:
        print("error")
elif proceed == "N" or proceed == "n":
    print("Closing program.\nDone")
else:
    print("Wrong input.\nClosing program.")