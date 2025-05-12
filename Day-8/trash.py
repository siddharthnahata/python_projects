# -*- coding: utf-8 -*-
"""
Created on Mon May 12 17:45:36 2025

@author: siddh
"""

def encrypt(orignal_text, orignal_shift):
    cipher_text = ""

    for letter in orignal_text:
        if letter == " ":
            cipher_text += " "
            continue
        
        shifted_position = alphabet.index(letter) + orignal_shift
        shifted_position %= len(alphabet)
     
        cipher_text += alphabet[shifted_position]
    print(f"Encode!!\n{cipher_text}")
        
    
def decode(orignal_text, orignal_shift):
    text = ""
    
    for letter in orignal_text:
        if letter == " ":
            text += " "
            continue
        
        shifted_position = alphabet.index(letter) - orignal_shift
        shifted_position %= len(alphabet)
        
        text += alphabet[shifted_position]
    print(f"Decode!!\n{text}")