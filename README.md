#VionCrypt\
##The program is capable of both file encryption and file decryption and is accessed through a command line interface.

######The program uses Crypto.Cipher library.\
######pip install pycryptodome

##To encrypt the file "hello.txt" in your current directory, use the following commands:\
1. run the program.\
$ python3 main.py

2. the program asks whether to encrypt or decrypt.\
$ E

3. choose the file name\
$ hello.txt

4. Do you want the key to be printed only or also saved to a txt file in your current directory.\
$ Y

5. File named "enc_hello.txt" is in your current directory.\

![image](https://user-images.githubusercontent.com/116679314/206299596-15777dbd-b790-41ab-805e-fac5ac1ff2e0.png)

--------------------------

##to decrypt a file "enc_hello.txt" in your current directory.\
1. run the program\
$ python3 main.py

2. the program asks whether to encrypt or decrypt.\
$ D

3. choose the file name.\
$ enc_hello.txt

4. Input key: (use your own key).\
$ 0af1f1d481535874034b18e625f739b3

5. File named "dec_hello.txt" is in your current directory.\

![image](https://user-images.githubusercontent.com/116679314/206299916-0f1e2393-5d5a-4a8b-9180-a7c399750f57.png)
 

