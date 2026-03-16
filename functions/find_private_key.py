from extended_euclidean_algorithm import EEA

def Find_Private_Key_d(e, p, q):
    """
    Implement this function to find the decryption exponent d, 
    such that d is the modular inverse of e. 
    
    This will use the Extended Euclidean Algorithm
    
    This function should return the following:
    d: the decryption component.
    
    This is not a single action, and there are multiple methods to create this. 
    
    You may create a helper function or have all code within this function.
    
    Plan ahead before coding this.

    """
    f = (p - 1) * (q - 1) #initiate variable f and assign it the product (p-1)(q-1)
    
    gcd, bezouts = EEA(e, f) #run the EEA using e and our calculated variable f, in order to find the value for d (modular inverse of e)
        #we assign the output of EEA(e, f) to gcd,bezouts because we have two return values
        #the return value we are interested in is the second one bezouts, which is a tuple of our two Bezout's coefficients
        
    d = bezouts[0] #initiate d with the value of the first Bezout's coefficient (the one associated with e in the "s*e + t*(p-1)(q-1)" equation
    
    return (n, d) #return a tuple with the values of n and d whenever this fxn is called