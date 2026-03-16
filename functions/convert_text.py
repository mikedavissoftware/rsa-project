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