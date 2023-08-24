#=============================================================================
#| Encrypting a plaintext file using the Affine Cipher
#|
#| Author: Anthony Marrongelli
#| Language: Python (3.10.3)
#|
#| To Compile and Execute: python main.py X.txt Y Z
#| where X.txt is the file including text
#| and Y and Z are the numbered pair used for encryption
#|
#| Note: In order for this program to work properly the input can only consist
#|       of the 26 letters of the alphabet
#|
#+=============================================================================
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'     #Our alphabet we will use for indexing

#Arguments given by user
input_file = str(sys.argv[1])
key1 = int(sys.argv[2])
key2 = int(sys.argv[3])


inputArray = []     #Array that will hold our encrypted message
inputText = open(input_file, 'r', encoding = 'utf-8')  #Opening of intake file


#Reading encrypted message from a file into an array
try:
    i = 0
    while(1):
        char = inputText.read(1)
        
        #break when we reach end of file
        if not char:
            break
        
        #excluding spaces
        if char == ' ':
            continue
        
        inputArray.append(char.lower())
        i+=1
finally:
        if not ''.join(inputArray).isalpha: raise Exception("Message to be encrypted has illegal characters.")
        inputText.close()

#function for encrypting a message with a given key pair
def encrypt(inputArray, key1, key2):
    encryptedArray = []
    
    for item in inputArray:
        encryptedArray.append(alphabet[(key1*(alphabet.index(item)) + key2) % 26])
    
    return encryptedArray

#function for decrypting a message with a given key pair
def decrypt(encryptedArray, key1, key2):
    decryptedArray = []
    
    for item in encryptedArray:
        decryptedArray.append(alphabet[(modularInverse(key1)*(alphabet.index(item) - key2)) % 26])
    
    return decryptedArray

#function to find modular inverse for when we are decrypting
def modularInverse(key1):
    x = 1
    while x < 26:
        if (((key1 % 26) * (x % 26)) % 26 == 1): return x
        x += 1


output = open('output.txt', 'w', encoding = 'utf-8')    #Opening output file to write encryption/decryption

encryptedMessage = encrypt(inputArray, key1, key2)

output.write('Encrypted Message: \n' + ''.join(encryptedMessage) + '\n')    #Displaying after encrypted
output.write('After Decryption: \n' + ''.join(decrypt(encryptedMessage, key1, key2)) + '\n')   #Displaying after encrypted was decrypted
