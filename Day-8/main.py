alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



def caesar(orignal_text, shift_amount, encode_or_decode):
    text = ""
    
    for letter in orignal_text:
        if letter == " ":
            text += " "
            continue
        
        if letter not in alphabet:
            text += letter
            continue
        
        if encode_or_decode == "decode": 
            shifted_position = alphabet.index(letter) - shift_amount
        elif encode_or_decode == "encode":
            shifted_position = alphabet.index(letter) + shift_amount
        
        shifted_position %= len(alphabet)
        text += alphabet[shifted_position]
    print(f"\n{text}")

should_continue = True
while should_continue:
    direction = input("Encode or Decode?\n").lower()
    text = input("Enter the Text:\n").lower()
    shift = int(input("Shift?\n"))
         
    caesar(text, shift, direction)
    
    nu = input("Do you want to continue. Yes/No? ").lower()
    if nu == "no":
        should_continue = False
        