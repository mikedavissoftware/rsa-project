from functions.extended_euclidean_algorithm import EEA
from functions.decode import Decode

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