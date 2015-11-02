#!/usr/bin

# Adam Denchfield
# 10/9/15

# OBJECTIVE:
# Asks for needed variable in Ohm's law, V = IR
# Then solves given the other two
# Done in SI units (base 0)

if __name__ == '__main__': 
    print("You must use SI units base 0, i.e., Volts, Ohms, Amps")
    
    needed = input("What variable is needed? Specify V, I, or R\nNeeded variable: ")
    inputbad = False
    
    while (inputbad == True):

        if (needed == 'V'):

            print("You are solving for voltage.")
            inp_curr = input("Current: ")
            inp_res = input("Resistance: ")

            current = float(inp_curr)
            res = float(inp_res)

            ret_volt = current * res
            print("From a current of %f and resistance of %f you have a voltage drop of %f across the resistor" %(current, res, ret_volt))
            
        elif (needed == 'I'):

            print("You are solving for current.")
            inp_volt = input("Voltage: ")
            inp_res = input("Resistance: ")
            volt = float(inp_volt)
            res = float(inp_res)

            current = volt * res
            print("From a voltage of %f and resistance of %f you have a current of %f across the resistor" %(volt, res, current))
            

        elif (needed == 'R'):

        else:
            print("Input not recognized. Try again.")
            inputbad = True
        
