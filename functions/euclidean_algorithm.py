def Euclidean_Alg(a, b):
    """
    1. Calculate the Greatest Common Divisor of a and b.
    
    2. This version should have only positive inputs and outputs.
    
    3. The function must return a single integer ('x') which is
    the gcd of a and b.
    
    
    """
    while b > 0: #run following loop while the second integer is greater than 0, since any number modulo 0 is undefined
        k = a % b #initiate variable k, which determines whether b is a factor of a -- if so, it is the gcd of the two numbers
        a = b #assign the value of b to the value of a for the next loop, or return value if this is the final loop
        b = k #assign the remainder k to b, to be checked if greater than zero to determine if another loop is necessary

    return a #return the gcd, which happens to be the final value of a