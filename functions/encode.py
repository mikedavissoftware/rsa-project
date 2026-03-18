from functions.convert_text import Convert_Text
from functions.fast_modular_exponentiation import FME

def Encode(n, e, message):
    """
    Here, the message will be a string of characters.
    Use the function Convert_Text from 
    the basic tool set and get a list of numbers.
    
    Encode each of these numbers using n and e and
    return the encoded cipher_text.
    """

    print("Message before conversion: ", message)

    char_codes = Convert_Text(message) #call the Convert_Text() function using our input message, and assign the returned list of ASCII codes to char_codes
    
    cipher_text = [] #initiate empty list to later receive our cipher codes
    
    for code in char_codes: #for each ASCII code (M) in char_codes
        cipher_text.append(FME(code, e, n)) #append the value of the cipher integer ((M ** e) mod n) to our cipher_text list, in the order in which it was received
    
    return cipher_text #return the list of cipher integers