import nltk

# 1. Create an `encrypt` function that takes in a plain text phrase and a numeric shift.
#     - the phrase will then be shifted that many letters
#     - shifts that exceed 26 should wrap around

    
def encrypt(plain, key):
    """ shifts plaintext input to the letter indicated by key = shift steps when key is known """
    
    encrypted_text = ''
    # find ascii, add key, % for alpha wrap, back into upper/lower case match input
    for char in plain:
        # lowercase ascii 97-122 inclusive
        if ord(char) >= 97 and ord(char) <= 122:
            convert = (ord(char)+ key - 97) %26 + 97
            encrypted_text += chr(convert)
            
        # uppercase ascii 65-90 inclusive
        elif ord(char) >= 65 and ord(char) <= 90:
            convert = (ord(char)+ key - 65) %26 + 65
            encrypted_text += chr(convert)
        else:
            encrypted_text += ''

    return encrypted_text   
    
# 2. Create a `decrypt` function that takes in encrypted text and numeric 
# shift which will restore the encrypted text back to its original form 
# when correct key is supplied.

def decrypt(encrypted, key):
    """ shifts encrypted input to the letter indicated by key = shift steps when key is known """
    
    decrypted_text = ''
    # find ascii, subtract previous steps taken (key), % for alpha wrap, 
    # back into upper/lower case match input
    for char in encrypted:
        # lowercase ascii 97-122 inclusive
        if ord(char) >= 97 and ord(char) <= 122:
            convert = (ord(char) - key - 97) %26 + 97
            decrypted_text += chr(convert)
            
        # uppercase ascii 65-90 inclusive
        elif ord(char) >= 65 and ord(char) <= 90:
            convert = (ord(char) - key - 65) %26 + 65
            decrypted_text += chr(convert)
        else:
            decrypted_text += ''

    return decrypted_text   
        
# reference on ascii -- https://www.tutorialspoint.com/count-uppercase-lowercase-special-character-and-numeric-values-in-cplusplus#:~:text=Uppercase%20Letters%20%E2%88%92%20A%20%2D%20Z%20having,48%20and%2057%20are%20inclusive