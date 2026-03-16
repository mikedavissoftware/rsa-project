from euclidean_algorithm import Euclidean_Alg

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