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