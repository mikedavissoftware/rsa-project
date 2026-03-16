import time

from functions.fast_modular_exponentiation import FME
from functions.convert_text import Convert_Text
from functions.convert_num import Convert_Num
from functions.helper_functions import *

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



# n = 2626319734066980059
# start_time = time.perf_counter()

# # full_code_break(n, e, cipher_text)
# print(factorize(n))

# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time:.4f} seconds")

# message = "Love this one. Your spot looks amazing, sort of reminds me of the shore in northwest Oregon a bit. Here's mine: 37.74934019629359, -105.53266866769236"
# print(Encode(n, e, message))

p, q = 173, 307
n, e = 53111, 175
d = 17143


cipher = Encode(n, e, "This is a message from the other side... BOO!")
print()
print("Cipher: ", cipher)
print()
print("Decoded message: ", Decode(n, d, cipher))