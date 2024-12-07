import math

while (True):

    print ("This is an odd & even filter")
    num = int(input("please enter a number: "))
    
    if (num % 2 == 0):
        
        print ("This is an even number: ", num)
        
        
    else:
        
        print ("This is an odd number: ", num)
        
    repeat = input("Do you want to repeat this? Type Y for yes: ")
    
    if (repeat == "Y"):
        
        continue
    
    else:

        print("This program has ended")
        break
