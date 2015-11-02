#!/usr/bin/python2

#***
#* Written by: Melanie Cornelius (Dooley)
#* Edited by: Adam Denchfield
#*
#* This is the incomplete version
#*
#* Note: this is written for Python2 as Python3 and Numpy/MatPlotLib require
#* 3.5, and the machines available to the group are not up-to-date.
#***

import matplotlib.pyplot
import numpy
import argparse

# Function for plot types

def get_components(inputs):
    """
    This function writes a new nested list containing the components of the
    initial velocity and acceleration values
    """
    component_inputs = [inputs[0], inputs[1], inputs[2], 
                       ['x velocity', numpy.cos((numpy.pi * 2 * inputs[4][1]) / 360) * inputs[3][1]],
                       ['y velocity', numpy.sin((numpy.pi * 2 * inputs[4][1]) / 360) * inputs[3][1]],
                       ['x acceleration', numpy.cos((numpy.pi * 2 * inputs[6][1]) / 360) * inputs[5][1]],
                       ['y acceleration', numpy.sin((numpy.pi * 2 * inputs[6][1]) / 360) * inputs[5][1]],
                       inputs[7], ['number time steps', inputs[0][1] / inputs[7][1]]]
#    print(component_inputs)

    return component_inputs


def plot_position(inputs):
    # Initializing empty storage arrays
    x_positions = []
    y_positions = []
    del_t = inputs[7][1]
    
    # Looping through all steps, incrementing the time step each time
    for i in range(0, int(inputs[8][1])):
        x_positions.append(inputs[1][1] + inputs[3][1] * del_t * i + 0.5 * inputs[5][1] * (del_t * i)**2)
        y_positions.append(inputs[2][1] + inputs[4][1] * del_t * i + 0.5 * inputs[6][1] * (del_t * i)**2)

    # Plotting
    matplotlib.pyplot.plot([0, x_positions[-1]], [0, 0])
    matplotlib.pyplot.plot(x_positions, y_positions)
    matplotlib.pyplot.show()


def velocity(inputs):

    # Initializing empty storage arrays
    x_velocities = []
    y_velocities = []
    del_t = inputs[7][1]
    times = []
    # Looping through all steps, incrementing the time step each time
    for i in range(0, int(inputs[8][1])):
        x_velocities.append(inputs[3][1] +  inputs[5][1] * del_t * i)
        y_velocities.append(inputs[4][1] +  inputs[6][1] * del_t * i)
        times.append(del_t * i)
        
    # Plotting
    matplotlib.pyplot.plot(times, x_velocities)
    matplotlib.pyplot.plot(times, y_velocities)
    matplotlib.pyplot.show()



def acceleration(inputs):

    # Initializing empty storage arrays
    x_accel = []
    y_accel = []

    times = []
    # Looping through all steps, incrementing the time step each time
    for i in range(0, int(inputs[8][1])):
        x_accel.append(inputs[5][1])
        y_accel.append(inputs[6][1])
        times.append(del_t * i)
        
    # Plotting
    matplotlib.pyplot.plot(times, x_accel)
    matplotlib.pyplot.plot(times, y_accel)
    matplotlib.pyplot.show()


# Main

if __name__ == '__main__':
    
    # Setting initial arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_values", help = "If set, uses set of test data, not prompts.",
                        action = "store_true")
    args = parser.parse_args()

    # Gather user input
    
    inputs = [['run time (in s)', 0], ['initial x position', 0], ['initial y position', 0],
             ['initial velocity', 0], ['angle of launch', 0], ['initial acceleration', 0],
             ['angle of acceleration', 0], ['time step', 0]]

    if args.test_values:
        # Use pre-made test set
        print("\nUsing test data. \n")
        to_insert = [10, 50, 50, 50, 45, -10, 90, 0.5]
        for i in range(0, len(to_insert)):
            inputs[i][1] = to_insert[i]

    else:
        # Use custom user inputs
        print("\nGathering user input. \nPlease enter all values in meters and seconds.\n")
        for element in inputs:
            element[1] = float(raw_input("Input the %s : " %element[0]))

    # Getting user inputs in component forms
    component_inputs = get_components(inputs)

    # Determine plot type
    plot_types = ['position', 'velocity vs time', 'acceleration vs time']

    done = False
    while not done:
        print("Plot options include:")
        for element in plot_types:
            print(element)
        
        print("Or press q to quit.\n")

        desired_plot = raw_input("Enter the desired plot type: ")

        # Process input

        if desired_plot.lower() == 'q':
            # Exit the loop - the user is finished
            print("\n\nThanks for stopping in! \n\n")
            done = True

        else:
            if desired_plot not in plot_types:
                # In case the user made a mistake in entry, check and repeat
                # while loop if needed
                print("Input not understood, sorry.  Please try again.")

            else:
                choice = plot_types.index(desired_plot)
                print(choice)
                print("\n\nNow processing for %s plot... \n\n" %desired_plot)

                # Now call the appropriate method depending on the user's input
                if choice == 0:
                    print("in choice")
                    plot_position(component_inputs)
                elif choice == 1:
                    velocity(component_inputs)
                else:
                    acceleration(component_inputs)
