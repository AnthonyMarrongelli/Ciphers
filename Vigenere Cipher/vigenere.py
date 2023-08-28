#=============================================================================
#| Encrypting a plaintext file using the Caesar Cipher
#|
#| Author: Anthony Marrongelli
#| Language: Python (3.10.3) 
#|
#| To Compile and Execute: python caesar.py X.txt Y
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
key_file = str(sys.argv[2])


inputArray = []     #Array that will hold our encrypted message
inputText = open(input_file, 'r', encoding = 'utf-8')  #Opening of intake file

keyArray = []       #Array that will hold our key message
keyText = open(key_file, 'r', encoding='utf-8') #Opening of key file


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
        i+=1
finally:
        if not ''.join(inputArray).isalpha: raise Exception("Message to be encrypted has illegal characters.")
        inputText.close()


#Reading message used for key from a file into an array
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
        i+=1
finally:
    if not ''.join(keyText).isalpha: raise Exception("Message for key has illegal characters.")
    keyText.close()


#Encryption funtion for a Vigenere Cipher
def encrypt(message, key):
    
    encryptedArray = []
    
    #Place holder values for indexes
    x = 0
    y = 0
    z = 0
    
    key_num = 0
    
    for letter in message:
        
        #Making sure we do not go past the array length
        if(z >= len(message)):
            break
        
        #Finding number value associated with the letter of the current index in key
        while key[y % len(key)] != alphabet[x]:
            x += 1
            
        #Resseting x and storing the number associated with the letter
        key_num = x
        x = 0
        
        #Finding number value associated with the letter of the message to be encrypted
        while message[z] != alphabet[x]:
            x += 1
            
        #Adding the encrypted letter to output array
        encryptedArray.append(alphabet[(x + key_num) % 26])
        
        #Resseting x and moving forward to the next letter in the message and key
        x = 0
        y += 1
        z += 1
        
    return encryptedArray
    
    
def decrypt(message, key):
    
    decryptedArray = []
    
    #Place holder values for indexes
    x = 0
    y = 0
    z = 0
    
    key_num = 0
    
    for letter in message:
        
        #Making sure we do not go past the array length
        if(z >= len(message)):
            break
        
        #Finding number value associated with the letter of the current index in key
        while key[y % len(key)] != alphabet[x]:
            x += 1
            
        #Resseting x and storing the number associated with the letter
        key_num = x
        x = 0
        
        #Finding number value associated with the letter of the message to be decrypted
        while message[z] != alphabet[x]:
            x += 1
            
        #Adding the decrypted letter to output array
        decryptedArray.append(alphabet[(x - key_num) % 26])
        
        #Resseting x and moving forward to the next letter in the message and key
        x = 0
        y += 1
        z += 1
        
    return decryptedArray


output = open('output.txt', 'w', encoding = 'utf-8')    #Opening output file to write encryption/decryption

encryptedMessage = encrypt(inputArray, keyArray)

output.write('Encrypted Message: \n' + ''.join(encryptedMessage) + '\n')    #Displaying after encrypted
output.write('After Decryption: \n' + ''.join(decrypt(encryptedMessage, keyArray)) + '\n')   #Displaying after encrypted was decrypted