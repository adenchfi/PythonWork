#!/usr/bin/python2

#Functionality: This program is to approximate pi with Monte Carlo Methods.

import random

if __name__ == '__main__':
    rbox = 1
    rcircle = 1
    
    npoints = input("How many points do you want to estimate pi with? ")
    p_in = 0

    for point in range(0, npoints):
        x = 2*random.random() - 1
        y = 2*random.random() - 1

        if (x**2 + y**2 <= rcircle):
            p_in += 1
    my_pi = 4* (float(p_in) / npoints)
    
    print("Pi = %f" %(my_pi))


    
