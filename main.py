# Program made by Onni Virtanen 05/12/2022.

import os
from Crypto.Cipher import AES


# Encrypt file
def encrypt():
    key = os.urandom(16)
    filename = input("Enter the filename you want to encrypt: \n")

    print(f'Encrypting file "{filename}"...')
    with open(filename, "rb") as tieto:
        data = tieto.read()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    print("The key and nonce are required for decryption. If they are lost, the data will be irrecoverable.")
    print("The tag is used to verify the authenticity of the file.")
    print("Please make sure to save these values:\n")
    print("key:", key.hex())
    print("nonce:", nonce.hex())
    print("tag:", tag.hex() + "\n")

    # Asking user if it is necessary to write a file containing key, nonce and tag in current directory.
    save_important_values_to_file = input(
        "Write these values to a file in your current directory? Y/N\n")
    if save_important_values_to_file == "Y" or save_important_values_to_file == "y":
        with open(f'important_values_{filename}.txt', "w") as f:
            f.write("key: " + key.hex() + "\n")
            f.write("nonce: " + nonce.hex() + "\n")
            f.write("tag: " + tag.hex() + "\n")

    # Writing ciphertext to file.
    with open('enc_' + filename, "wb") as f:
        f.write(ciphertext)
    print("The file was successfully encrypted.")


# Decrypt file
def decrypt():
    filename = input("Type a filename you want to decrypt: \n")
    key_input = input(
        "Type the key that was given when the file was encrypted: \n")
    key = bytes.fromhex(key_input)
    with open(filename, "rb") as f:
        ciphertext_file = f.read()
    nonce_input = input("Type the nonce: \n")
    nonce = bytes.fromhex(nonce_input)

    verify_authenticity = input("Verify file's authenticity Y/N\n")
    if verify_authenticity == "Y" or verify_authenticity == "y":
        tag_input = input(
            "Type the tag that was given when the file was encrypted: \n")
        tag_file = bytes.fromhex(tag_input)

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaindata = cipher.decrypt(ciphertext_file)
    try:
        try:
            cipher.verify(tag_file)
            print("The file is authentic.")
        except:
            print("The file's authenticity cannot be verified.")

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