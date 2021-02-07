import nltk
# from nltk.corpus import words

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
            encrypted_text += char

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
            decrypted_text += char

    return decrypted_text   
    
    # 3. Create a `crack` function that will decode the cipher so that an 
    # encrypted message can be transformed into its original state WITHOUT 
    # access to the key.
    
    # 4. Devise a method for the computer to determine if code was broken 
    # with minimal human guidance.
    
    def crack(encrypted):
        """ Shifts an encrypted message into its original state WITHOUT access to the key.
        hacked = True or False when crack() is successful/fails"""
        
        # plaintext = 'It was the best of times, it was the worst of times.'
        # encrypted = 'Yj mqi jxu ruij ev jycui, yj mqi jxu mehij ev jycui.'
        
        plaintext = ''
        hacked = True
        key = 0
        
        nltk.corpus.download('words', quiet=True)
        
        for key in range(26):
            plaintext += decrypt(encrypted, key)
            word_list = plaintext.words(plaintext)
            

        for word in range(word_list):
            if word in word_list:
                hacked = True
            else:
                hacked = False
            
        return(f'Hacking key: {key} gives {plaintext}. Did I do it right?? {hacked}')

        
# reference on ascii -- https://www.tutorialspoint.com/count-uppercase-lowercase-special-character-and-numeric-values-in-cplusplus#:~:text=Uppercase%20Letters%20%E2%88%92%20A%20%2D%20Z%20having,48%20and%2057%20are%20inclusive