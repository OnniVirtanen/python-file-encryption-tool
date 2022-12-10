import os
import shutil
from Crypto.Cipher import AES

# Encrypt file
def encrypt():
    # Create a random secure key.
    # Ask user to enter the filename to encrypt.
    key = os.urandom(16)

    while True:
        # Asking the user for key input.
        filename = input("Enter the filename you want to encrypt: \n")
        try:
            # Read bytes of the file.
            # Encrypt the file's bytes and assign it to a variable ciphertext.
            # Create a nonce and a tag.

            with open(filename, "rb") as f:
                data = f.read()
            cipher = AES.new(key, AES.MODE_EAX)
            nonce = cipher.nonce
            ciphertext, tag = cipher.encrypt_and_digest(data)
        except:
            print("Key is not in hexadecimal format.")
            continue
        else:
            print(f'Encrypting file "{filename}"...')
            break
    
    # User must save the printed key for decryption.
    print("The key is required for decryption. If lost, the data will be irrecoverable.")
    print("key:", key.hex())

    # Asking user if the key should be saved in the current directory.
    # If true, creating a file containing the key.
    
  
    save_key = input("Write the key to a file in your current directory? Y/N\n")

    if save_key == "Y" or save_key == "y":
        with open(f'secret_key.txt', "w") as f:
            f.write("key: " + key.hex() + "\n")

    # Creating a file that contains the encrypted data.
    with open('enc_' + filename, "wb") as f:
        f.write(ciphertext)
    # Writing nonce to end of the file.
    with open('enc_' + filename, "a") as f:
        f.write(nonce.hex())
    # Writing tag to end of the file.
    with open('enc_' + filename, "a") as f:
        f.write(tag.hex())

    print("The file was successfully encrypted.")


# Decrypt file
def decrypt():
    filename = input("Type a filename you want to decrypt: \n")

    # Make a copy of the encrypted file. Keep the original encrypted file safe if user inputs wrong secret key.
    shutil.copy(filename, "copy" + filename)
    filename = "copy" + filename

    # Reading nonce and tag from the file that is to be decrypted.
    # Assigning variables to nonce and tag.
    with open(filename, "r") as f:
        # Nonce
        f.seek(0, 2)
        position = f.tell()
        f.seek(position - 64, 0)
        nonce = f.read(32)
        nonce = bytes.fromhex(nonce)

        # Tag
        tag = f.read()
        f.seek(position - 32, 0)
        tag = f.read()
        tag = bytes.fromhex(tag)

    # Remove nonce and tag from end of the file that is to be decrypted.
    with open(filename, 'r+b') as f:
        f.seek(-64, 2)
        f.truncate()

    # Ask the user for key if the key is not in hex format.
    while True:
        # Asking the user for key input.
        key_input = input("Type the key for decryption: \n")
        try:
            key = bytes.fromhex(key_input)
            print(f'Decrypting file "{filename}"...')
        except:
            print("Key is not in hexadecimal format.")
            continue
        else:
            break

    # Reading bytes of the encrypted file and assigning it to a variable.
    with open(filename, "rb") as f:
        ciphertext_file = f.read()

    # Decrypting the encrypted file using the key provided by user.
    try:
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaindata = cipher.decrypt(ciphertext_file)
    except:
        print("Error in decryption.")

    # Veryfying the file's authenticity by using the tag.
    try:
        cipher.verify(tag)
        print("The file is authentic.")
                # Creating a file from the decrypted data.
        try:
            with open("dec_" + filename[8:], "wb") as f:
                f.write(plaindata)
            print("The file was successfully decrypted.")
            
            # Delete encrypted files since they are no longer needed.
            os.remove(filename)
            os.remove(filename[4:])
        except:
            print("Error when writing decrypted data to a file.")
    except:
        print("The file's authenticity cannot be verified.")
        decrypt()

# Introduction to the program.
print("Welcome to VionCrypt! ©Onni Virtanen")
print("This program is used for file encryption and decryption.")
print("The program uses AES256 algorithm.")

# Asking the user how the program will be used. It can be used for encryption or decryption.
user_choice = input("Type in E or D, E=Encrypt, D=Decrypt.\n")

if user_choice == "E" or user_choice == "e":
    encrypt()
elif user_choice == "D" or user_choice == "d":
    decrypt()
else:
    print("Error in user input when providing choice on whether to encrypt or decrypt.")
