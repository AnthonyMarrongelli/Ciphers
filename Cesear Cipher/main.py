#=============================================================================
#| Encrypting a plaintext file using the Cesear Cipher
#|
#| Author: Anthony Marrongelli
#| Language: Python (3.10.3) 
#|
#| To Compile and Execute: python main.py X.txt Y
#| where X.txt is the file including text
#| and Y is the number that represents the key
#|
#| Note: In order for this program to work properly the input can only consist
#|       of the 26 letters of the alphabet
#|
#+=============================================================================
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'     #Our alphabet we will use for indexing

#Arguments given by user
input_file = str(sys.argv[1])
key = int(sys.argv[2])


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



#function for encrypting a message with a given key (shift value)
def encrypt(inputArray, key):
    encryptedArray = []
    
    for item in inputArray:
        encryptedArray.append(alphabet[(alphabet.index(item) + key) % 26])
        
    return encryptedArray

#function for decrypting a message with a given key (shift value)
def decrypt(encryptedArray, key):
    decryptedArray = []
    
    for item in encryptedArray:
        decryptedArray.append(alphabet[(alphabet.index(item) - key) % 26])

    return decryptedArray


output = open('output.txt', 'w', encoding = 'utf-8')    #Opening output file to write encryption/decryption

encryptedMessage = encrypt(inputArray, key)

output.write('Encrypted Message: \n' + ''.join(encryptedMessage) + '\n')    #Displaying after encrypted
output.write('After Decryption: \n' + ''.join(decrypt(encryptedMessage, key)) + '\n')   #Displaying after encrypted was decrypted
    