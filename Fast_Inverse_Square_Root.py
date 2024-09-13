import struct
import numpy as np

def fast_inverse_sqrt(number):
    
    x = float(number)                               # Convert the input number to a 32-bit floating point value
    i = struct.unpack('i', struct.pack('f', x))[0]  # Interpret the input number as a 32-bit signed integer
    i = 0x5F3759DF - (i >> 1)                       # Use the magic number to estimate the square root
    y = struct.unpack('f', struct.pack('i', i))[0]  # Interpret the estimate as a 32-bit floating point value
    y = y * (1.5 - 0.5 * x * y * y)                 # Use Newton's method to refine the estimate
    
    return 1 / y                                    # Return the reciprocal square root

# Get user input for the number to calculate the inverse square root of
# number = float(input("Enter a number to calculate the inverse square root of: "))
number =  12
sqrt_num = np.sqrt(number)
# Calculate the inverse square root using the fast inverse square root algorithm
result = fast_inverse_sqrt(number)

# Print the result
print("The inverse square root of", number, "is", result,sqrt_num, result-sqrt_num)

#--------------------------------------------------------------------------------------------------------------------------
# more info: https://breq.dev/2021/03/17/5F3759DF
# https://en.wikipedia.org/wiki/Fast_inverse_square_root

#more magic numbers: https://en.wikipedia.org/wiki/Magic_number_(programming)