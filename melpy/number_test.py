# Melanie Dooley

# For use with Workshop 2 activity
# This program will manupilate some numbers

# We will use a random number to make the values change slightly
# each time the program is used
import random

if __name__ == '__main__':

    a = random.randrange(1,10,1)
    b = random.randrange(5,15,1)
    
    print("Number a is %f and number b is %f.\nWe will manipulate these values." %(a,b))

    c = a*b
    d = b/a
    e = a-b
    f = a**b
    g = b**a

    print("a*b is : %f" %(c))
    print("b/a is : %f" %(d))
    print("a-b is : %f" %(e))
    print("a**b is : %f" %(f))
    print("b**a is : %f" %(g))

    print("Now we're done!  Good job.")
