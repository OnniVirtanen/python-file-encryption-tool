import rsa

publicKey, privateKey = rsa.newkeys(512)

# User can choose (1) to encrypt or (2) to decrypt
user_choise = str(input("Choose (1) to encrypt a string or (2) to decrypt string: \n"))

# Encrypts user input. Writes ciphertext and privatekey to files.
if user_choise == "1":
    message = input("Give a message to encrypt: ")

    encMessage = rsa.encrypt(message.encode(), publicKey)

    # Delete later these two prints
    print(encMessage)
    print(privateKey)

    try:
        filename = 'privatekey_msg.txt'
        file = open(filename, "w")
        file.write(str(privateKey))
        file.close()
        print("Privatekey is successfully written in a file.")
        encoded_message_filename = 'encoded_message.txt'
        file_encoded_message = open(encoded_message_filename, "w")
        file_encoded_message.write(str(encMessage))
        file_encoded_message.close()
        print("Encoded message is successufully written in a file.")
    except:
        print("Error occured while writing the file.")

# Decrypts user input. A message and a privatekey is needed.
elif user_choise == "2":
    encMessageInput = input("Give a message to decrypt: \n")
    privateKeyInput = input("GIve a private key that was given when the data was encrypted: \n ")
    decMessage = rsa.decrypt(encMessageInput, privateKeyInput).decode()
    print("decrypted string: ", decMessage)
# User input wasn't correct in line 10.
else:
    print("Error. Try choosing 1 or 2.")