The program can be used for file encryption and file decryption. The program is used in command line interface.

The program uses Crypto.Cipher library.
pip install pycryptodome

////
to encrypt a file "hello.txt" in your current directory:
1. run the program.
\n$ python3 main.py

2. the program asks whether to encrypt or decrypt.
\n$ E

3. choose the file name
#$ hello.txt

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
