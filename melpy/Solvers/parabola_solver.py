#!/usr/bin/python2
# Parabola solver; plots it too
# Adam Denchfield

# Functionality: 
# This will take in variables from the user and solve the parabolic motion equations It will then plot the desired data.

import numpy
import matplotlib.pyplot as m

if __name__ == '__main__':
    desired_inputs = [['initial x', 0] , ['initial y', 0] , ['initial v', 0] , ['angle of launch', 0], ['acceleration constant', 0], ['angle of acceleration', 0], ['time of flight', 0] , ['number of subdivisions', 0]]
    print ("This function will ask for parabolic motion inputs and then solve. Plots can be given in the end.")
    print ("You will need the following variables in meters and seconds: ")

    for i in range (0, len (desired_inputs)):
        print (desired_inputs [i] [0])

    for i in range (0, len (desired_inputs)):
        desired_inputs [i] [1] = input ("Please input the value for %s :" %(desired_inputs [i] [0]))

        # ASK THE USER WHAT PLOT
    desired_plot = ['position', 'velocity vs time', 'acceleration vs time']
    print ('\nYour plot options include:')
    for i in range (0, len (desired_plot)):
        print (desired_plot [i])

    print ("\n ")

    plot_type = raw_input ("Enter the desired plot type as it appears above, or enter 'done' when done: ")

    finished = False

    while finished == False:
        # do all the things
        if plot_type == 'done':
            finished = True
        elif plot_type == desired_plot [0]:
            # user wants a position plot
            pass
        elif plot_type == desired_plot [1]:
            # user wants a velocity vs time plot
            total_time = desired_inputs [6] [1]
            time_change = desired_inputs [6] [1] / desired_inputs [7] [1]
            xpos = ypos = []
            current_time = 0
            
            while (current_time <= desired_inputs [6] [1]):
                # calcs go here
                xvel = numpy.cos (desired_inputs [3] [1] * (desired_inputs [1] [1]))
                yvel = numpy.sin (desired_inputs [3] [1] * (desired_inputs [1] [1]))
                current_time += time_change
                


        elif plot_type == desired_plot [2]:
            pass
        else:
            print ("Sorry, your input wasn't understood.")
    # ask the user what plot?
    # do the calculations
        # loop over time (subdivisions)
        # calculate the desired values
    # plot the values

            a = b = list (range (0, 100, 5))
            print (a)

            matplotlib.pyplot.plot (a, b)
            matplotlib.pyplot.show ()
