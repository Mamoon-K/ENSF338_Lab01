import sys
import math
def do_stuff():
    a = float(sys.argv[1]) 
    b = float(sys.argv[2])
    c = float(sys.argv[3]) 
    d = b**2 - 4*a*c 
    try:
        if d > 0:
            root1 = (-b + math.sqrt(d)) / (2*a)
            root2 = (-b - math.sqrt(d)) / (2*a)
            print(f'The solutions are: {root1}, {root2}')
        elif d == 0:
            root = -b/(2*a) 
            print(f'The solution is: {root}')
        else:
            print('There are no real solutions.') 
    except ZeroDivisionError:                 #There was no error handling if dividing by zero
        print('float division by zero')
    except ValueError:           # or if putting a value 
        print('could not convert string to float')  
        
    
do_stuff()

# The code above is a function that takes in three arguments from the command line and calculates the roots of a quadratic equation.
