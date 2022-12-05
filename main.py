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
    print("The key is required for decryption. If lost, the data will be irrecoverable.")
    print("key:", key.hex())

    # Asking user if the key should be saved in the current directory.
    save_key = input(
        "Write the key to a file in your current directory? Y/N\n")
    if save_key == "Y" or save_key== "y":
        with open(f'key_{filename}.txt', "w") as f:
            f.write("key: " + key.hex())

    # Writing ciphertext to file.
    with open('enc_' + filename, "wb") as f:
        f.write(ciphertext)
    # Writing nonce to the file.
    with open('enc_' + filename, "a") as f:
        f.write(nonce.hex())
    # Writing tag to the file.
    with open('enc_' + filename, "a") as f:
        f.write(tag.hex())
    print("The file was successfully encrypted.")


# Decrypt file
def decrypt():
    filename = input("Type a filename you want to decrypt: \n")

    # Finding nonce and tag from the encrypted file.
    with open(filename, "r") as f:
        # NONCE
        f.seek(0, 2)
        position = f.tell()
        f.seek(position - 64, 0)
        bytes64_32 = f.read(32)
        nonce_in_end_of_file = bytes64_32

        # TAG
        bytes32_16 = f.read()
        f.seek(position - 32, 0)
        bytes32_16 = f.read()
        tag_in_end_of_file = bytes32_16

        nonce = bytes.fromhex(nonce_in_end_of_file)

    with open(filename, 'r+b') as f:
        # Move to the position 64 bytes from the end of the file
        f.seek(-64, 2)
        # Truncate the file at the current position
        f.truncate()

    key_input = input(
        "Type the key that was given when the file was encrypted: \n")
    key = bytes.fromhex(key_input)
    with open(filename, "rb") as f:
        ciphertext_file = f.read()

    tag_file = bytes.fromhex(tag_in_end_of_file)

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
    print("Closing program.")
else:
    print("Wrong input.\nClosing program.")