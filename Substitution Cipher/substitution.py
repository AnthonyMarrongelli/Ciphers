#=============================================================================
#| Encrypting a plaintext file using the Vigenere Cipher
#|
#| Author: Anthony Marrongelli
#| Language: Python (3.10.3) 
#|
#| To Compile and Execute: python vigenere.py plaintext.txt key.txt
#| where plaintext.txt is the file including text
#| and key.txt is the file including the key
#|
#| Note: In order for this program to work properly the input can only consist
#|       of the 26 letters of the alphabet
#|
#+=============================================================================
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'     #Our alphabet we will use for indexing

#Arguments given by user
input_file = str(sys.argv[1])
key_file = str(sys.argv[2])


inputArray = []     #Array that will hold our encrypted message 
inputText = open(input_file, 'r', encoding = 'utf-8')   #Opening of intake file

keyArray = []       #Array that holds the new alphabet that will be used in the substitution
keyText = open(key_file, 'r', encoding = 'utf-8')   #Opening of key file


#Reading message to encrypt from a file into an array
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
        i += 1
finally:
    if not ''.join(inputArray).isalpha: raise Exception("Message to be encrypted has illegal characters")
    inputText.close()
    
    
#Reading key alphabet from a file into an array
try:
    i = 0
    while(1):
        char = keyText.read(1)
        
        #break when we reach end of file
        if not char:
            break
        
        #excluding spaces
        if char == ' ':
            continue
        
        keyArray.append(char.lower())
        i += 1
finally:
    if not ''.join(keyText).isalpha: raise Exception("Key has illegal characters")
    keyText.close()
    
    
#function for encrypting a message with a given key (alphabet)
def encrypt(message, key):
    
    encryptedArray = []
    
    for item in message:
        encryptedArray.append(key[alphabet.index(item)])
        
    return encryptedArray
    

#function for decrypting a message with a given key (alphabet)
def decrypt(message, key):
    
    decryptedArray = []
    
    for item in message:
        decryptedArray.append(alphabet[key.index(item)])
        
    return decryptedArray



output = open('output.txt', 'w', encoding = 'utf-8')    #Opening output file to write encryption/decryption

encryptedMessage = encrypt(inputArray, keyArray)

output.write('Encrypted Message: \n' + ''.join(encryptedMessage) + '\n')    #Displaying after encrypted
output.write('After Decryption: \n' + ''.join(decrypt(encryptedMessage, keyArray)) + '\n')   #Displaying after encrypted was decrypted