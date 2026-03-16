def EEA(a, b):
    """
    This is a helper function utilizing Bezout's theorem as discussed in your MW.
    You will follow these same steps closely to construct this function.
    
    This version will return both: 
    1. the GCD of a, b 
    2. Bezout's coefficients in any form you wish. We recommend returning your coefficients as a list or a tuple. 
    HINT: return GCD, (s1, t1)
    
    * Ensure that your inputs are positive integers. Implement these kinds of checks.
    * It might also behoove you to consider reassigning a, b to new coefficients depending on which is greater.
    
    """
    s1, t1 = 1, 0 #assign the values of 1,0 to s1,t1 respectively, per the setup of the Extended Euclid's Algorithm
    s2, t2 = 0, 1 #assign the values of 0,1 to s2,t2 respectively, per the setup of the Extended Euclid's Algorithm

    while b > 0: #similarly to the regular Euclid's Algo, run following loop while the second integer is greater than 0, since any number modulo 0 is undefined
        k = a % b #initiate variable k at the value of a mod b, which is the same as k from Euclid's (the remainder)
        q = a // b #initiate variable q at the value of the integer division of a // b, which is the number of times b divides a before a remainder is reached

        a = b #replace the value of a with the value of b, per Euclid's Algo
        b = k #replace the value of b with the remainder k, per Euclid's Algo

        s3, t3 = (s1 - q * s2), (t1 - q * t2) #initiate s3,t3 (essentially ŝ,t̂ from algo, but python doesn't recognize these symbols) as the calculated values using q...
            #...so that we can still reference the original values of s2,t2 in reassignment later

        s1, t1 = s2, t2 #reassign value of s1,t1 to that of s2,t2 per the Extended Euclid's Algo -- these are our new values for the next loop (if b is still > 0)
        s2, t2 = s3, t3 #reassign value of s2,t2 to the newly calculated values we assigned to s3,t3 -- these are our new values for the next loop (if b is still > 0)

    gcd = a #for clarity, assign the value of a to variable gcd, since once we reach b = 0, we have found our GCD in variable a
    
    return gcd, (s1, t1) #return the GCD, as well as a tuple containing s1,t1 (our Bezout's coefficients)