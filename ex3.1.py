def hello_world(number):
 print("Hello, world! My group number is", number)
hello_world("3")



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


import matplotlib.pyplot as plt
import json 
with open('internetdata.json') as id:
    content = json.load(id)




for n in content:
    if n["incomeperperson"] == None:
        n["incomeperperson"] = 0
        
    else:
        n["incomeperperson"] = n["incomeperperson"]
        
    if n["internetuserate"] == None:
        n["internetuserate"] = 0
        

x1 = [n["internetuserate"]  for n in content if n["incomeperperson"] <10000]

x2 = [n["internetuserate"] for n in content if n["incomeperperson"] >= 10000]


plt.hist(x1, bins=20, alpha=0.5, label='Income < 10,000',edgecolor='black')  

plt.xlabel('Internet Use Rate')
plt.ylabel('frequency')
plt.legend()

plt.title('Income per Person < 10,000 - Internet Usage Rate')
plt.savefig('hist1.png')
plt.show()



plt.hist(x2, bins=20, alpha=0.5, label='Income >= 10,000',edgecolor='black')  

plt.xlabel('Internet Use Rate')
plt.ylabel('frequency')
plt.legend()

plt.title('Income per Person >= 10,000 - Internet Usage Rate')
plt.savefig('hist2.png')
plt.show()

 
