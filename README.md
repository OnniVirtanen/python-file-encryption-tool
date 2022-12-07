The program can be used for file encryption and file decryption. The program is used in command line interface.

The program uses Crypto.Cipher library.
pip install pycryptodome

////
to encrypt a file "hello.txt" in your current directory:
1. run the program.
$ python3 main.py

2. the program asks whether to encrypt or decrypt.
$ E

3. choose the file name
$ hello.txt

4. Do you want the key to be printed only or also saved to a txt file in your current directory.
$ Y

5. File named "enc_hello.txt" is in your current directory.

////

to decrypt a file "enc_hello.txt" in your current directory.
1. run the program
$ python3 main.py

2. the program asks whether to encrypt or decrypt.
$ D

3. choose the file name.
$ enc_hello.txt

4. Input key: (use your own key).
$ 0af1f1d481535874034b18e625f739b3

5. File named "dec_hello.txt" is in your current directory.

![image](https://user-images.githubusercontent.com/116679314/206282786-0878fbe7-eabb-4d89-b334-7b2c4bc425f2.png)
![image](https://user-images.githubusercontent.com/116679314/206282985-67309c02-cd49-4dad-b586-eaa88e55ea65.png)


