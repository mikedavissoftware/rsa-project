import random #we use this package to randomly determine the value of e for our public key

def Convert_Binary_String(_int):
    """
    Here, you need to define a function that converts an integer to
    a string of its binary expansion. You may or may not need this function. 
    
    For example:
    _int = 345
    bits = 101011001
    """
    binary = "" #initiate empty string to receive bits, to later be converted to an integer since strings make things more straightforward in the conversion process
    while _int > 0: #while we have a remainder in our binary conversion
        if _int % 2 == 1: #modulo 2 indicates if the current bit indicates a "utilized" bit / power of 2
            binary = "1" + binary #add to the front because the bits go from least significant to most significant in this process
        else: #if modulo 2 returns 0, this is not a "utilized" bit / power of 2
            binary = "0" + binary #again, add to the front due to increasing bit significance
        _int = _int // 2 #floor division of the number by a factor of 2, to be used next iteration
    return binary #return the value, to be used wherever this function is called

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

def Find_Public_Key_e(p, q, max_e):
    """
    Implement this function such that
    it takes 2 primes p and q.
    
    Use the gcd function that you have 
    defined before.
    
    The function should return 2 elements as follows:
    public key: n
    public key: e
    
    HINT: this function will run a loop to find e such 
    that e is relatively prime to (p - 1) (q - 1) 
    and not equal to p or q.
    
    NOTE: There are a number of ways to implement this key feature. 
    You, as the coder, can choose to how to acheive this goal.
    
    """
    n = p * q #per RSA, n is equal to the product of our chosen p and q values
    
    f = (p - 1) * (q - 1) #initiate variable f and assign it the product (p-1)(q-1)
    
    e_list = [] #initiate an empty list to receive the possible values of e
    for num in range(2, max_e): #scan a range of integers
        if Euclidean_Alg(num, f) == 1: #condition checking for relative primeness of the current number and (p-1)(q-1)
            e_list.append(num) #append number to the list of possible e's if condition is satisfied
    
    e = e_list[random.randint(0, len(e_list) - 1)] #pick a random value from the list of possible e's, to become our e-value whenever this fxn is called
        
    return (n, e) #return a tuple with the values of both n and e whenever this fxn is called

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

def Convert_Text(_string):
    """
    Define this function such that it takes in a simple 
    string such as "hello" and outputs the corresponding
    standard list of integers (ascii) for each letter in the word hello.
    For example:
    _string = hello
    integer_list = [104, 101, 108, 108, 111]
    
    You may use "ord()"
    """
    integer_list = [] #initiate empty list which will later receive the ASCII codes for the characters in the string
    
    for char in _string: #for each character in our input string
        integer_list.append(ord(char)) #using the ord() method, translate the character to an ASCII code, and...
            #add the resulting character code to the list in the order in which it was received
    
    return integer_list #return the list of ASCII codes wherever this fxn is called

def Convert_Num(_list):
    """
    Do the opposite of what you did in the Convert_Text
    function defined above.
    
    Define this function such that it takes in a list of integers
    and outputs the corresponding string (ascii).
    
    For example:
    _list = [104, 101, 108, 108, 111]
    _string = hello
    """
    _string = '' #initiate empty string, to later receive the characters that make up our message
    
    for i in _list: #for each number in the input list
        _string += chr(i) #using the chr() method, translate the ASCII code to an actual character, and...
            #add the resulting character to the string in the order in which it was received
    
    return _string #return the string that was translated from ASCII codes, wherever this fxn is called

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

def factorize(n):
    for i in range(2, n-1):
        if n % i == 0:
            return [(i, int(n / i))]
    return "n is prime"

def pair_factorize(n):
    factor_pairs = []
    p = 2
    q = n // 2
    while p < q:
        if n % p == 0:
            q = int(n / p)
            print("p = ", p)
            print("q = ", q)
            factor_pairs.append((p, q))
        p += 1

    if len(factor_pairs) > 0:
        return factor_pairs
    else:
        return "n is prime"
    
def check_rel_prime(pairs, e):
    d_vals = []
    for pair in pairs:
        p,q = pair
        f = (p - 1) * (q - 1)
        eea = EEA(e, f)
        if eea[0] == 1:
            d_vals.append(int(eea[1][0]))
        
    d_set = set(d_vals)
    d_list = list(d_set)
    return d_list

def multi_decode(d_list, cipher):
    for d in d_list:
        print(Decode(n, d, cipher))  
        
def full_code_break(n, e, cipher):
    pairs = pair_factorize(n)
    print(pairs)
    # pairs = factorize(n)
    d_list = check_rel_prime(pairs, e)
    multi_decode(d_list, cipher)

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