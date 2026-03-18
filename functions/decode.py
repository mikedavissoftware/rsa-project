from functions.fast_modular_exponentiation import FME
from functions.convert_num import Convert_Num

def Decode(n, d, cipher_text):
    """
    Here, the cipher_text will be a list of integers.
    First, you will decrypt each of those integers using 
    n and d.
    
    Later, you will need to use the function Convert_Num from the 
    basic toolset to recover the original message as a string. 
    
    """
    codes = [] #initiate empty list, to later receive the ASCII codes for our message
    
    for num in cipher_text: #for each integer in our list cipher_text
        codes.append(FME(num, d, n)) #append the value of the modular inverse ((C ** d) mod n) to our codes list
    print("Character codes: ", codes)
    message = Convert_Num(codes) #call the Convert_Num() function on the list of codes we created, and...
        #assign it to variable message, which will be a string of readable characters
    
    return message #return the string of characters we created, wherever this fxn is called