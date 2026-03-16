from functions.convert_binary_string import Convert_Binary_String

def FME(b, n, m):
    """
    1. Using the fast modular exponentiation algorithm,
    the below function should return b**n mod m.
    As described on page 254. (however, you may input the exponent and 
    then convert it to a string - the book version imports the binary expansion)  
    2. You should use the function defined above Convert_Binary_String() if using the book algorithm.
    3. For this block you MUST use one of the 3 methods above.
    4. Any method using bit-shifting or copied from the internet (even changing varibale names) will result in a 0.
    
    **If you are completely stuck, you may use pow() with a 10pt penalty.**

    You may use the function you developed in your Mastery Workbook - but be sure it is your own
    work, commented, etc. and change inputs as needed.
    """
    #I will be using Sriram's algorithm from the lecture
    
    n_binary = Convert_Binary_String(n) #acquire binary version of input number n
    
    result = 1 #initiate result at 1, since it will be multiplied by the first squared result and we don't want zero
    square = b #establish number to square as the base of the exponent
    
    for i in range(len(n_binary)): #use length of binary string to establish a for loop
        bit = n_binary[-i - 1] #assign current bit to a reusable variable
        if bit == "1": #check if current bit is significant
            result = (result * square) % m #take current result and assign it to the modulo of the product of itself & current value of square
        square = (square * square) % m #establish new number to be used in the "b" spot next iteration
        
    return result #return result for value to be used when function is called