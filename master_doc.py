import time

from functions.fast_modular_exponentiation import FME
from functions.convert_text import Convert_Text
from functions.convert_num import Convert_Num
from functions.helper_functions import *
from functions.encode import Encode
from functions.decode import Decode


# TIME EFFICIENCY TESTING
# n, e = 2626319734066980059, 65537
# start_time = time.perf_counter()

# full_code_break(n, e, cipher_text)
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