# Melanie Cornelius

# This program is an example set of functions.
# It's a learning tool for Workshop 1.

import random

def sum(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ

def magn(*vect):
    magsquared = 0
    for elements in vect:
        magsquared += elements**2
    mag = (magsquared) ** (1/2)
    return mag

def difference(int4, int5):
    result = int4 - int5
    return result

def greeting():
    name = input("Please enter your name: ")
    major = input("Please enter your major: ")
    food = input("What's your favorite food? ")
    
    print("\n\nHello, %s!" %(name))

    # now I'm going to generate a random number and have a few options
    # for the output, just for fun

    rand0 = random.randrange(0,3,1)
    
    resp1 = ", huh? Wow, that sounds interesting!"
    resp2 = "... Not sure I've heard of it.  Sounds neat, though!"
    resp3 = ", was that it?  I'm impressed!"

    if rand0 == 0:
        print(major + resp1)
    elif rand0 == 1:
        print(major + resp2)
    else:
        print(major + resp3)

    rand1 = random.randrange(0,3,1)

    resp40 = "I don't think I've eaten "
    resp41 = " at a resturant before, have you?"
    resp50 = "So you like "
    resp51 = ".  Well, someone has to! (Joking, of course.)"
    resp60 = "... Is that eaten with ketchup, by chance?"

    if rand1 == 0:
        print(resp40 + food + resp41)
    elif rand1 == 1:
        print(resp50 + food + resp51)
    else:
        print(food + resp60)

if __name__ == '__main__':
    greeting()
