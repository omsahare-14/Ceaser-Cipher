
# Day 8: Ceaser Cipher

import math

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo, "\n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ciphered_alphabet = []

def caeser(todo, some_text, shift_amount):

    ciphered_alphabet.clear()
    for i in range(0, len(alphabet)):
        new_index = int(math.fmod(i+shift_amount, 26))
        ciphered_alphabet.append(alphabet[new_index])
    
    if todo == "encode":
        ciphertext = ""
        for i in some_text:
            if i in alphabet:
                shifted_index = alphabet.index(i)
                ciphertext += ciphered_alphabet[shifted_index]
            else:
                ciphertext += i    
        print(f"\nThe encoded message is: {ciphertext}")
    
    elif todo == "decode":
        plaintext = ""
        for i in some_text:
            if i in alphabet:
                shifted_index = ciphered_alphabet.index(i)
                plaintext += alphabet[shifted_index]
            else:
                plaintext += i
        print(f"\nThe decoded message is: {plaintext}")

should_continue = True
while should_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    caeser(todo=direction, some_text=text, shift_amount=shift)

    ask = input("\nWant to do it again? yes or no?\n").lower()
    if ask == "no":
        should_continue = False
        print("\nThank You!\n")