while (True):
    print ("This is a triangle filter")
    
    sideAdj = float(input("Please input side A (base/adj): "))
    sideByp = float(input("Please input side B (side/hyp): "))
    sideCop = float(input("Please input side C (side/opp): "))
    
    if (sideAdj == sideByp) and (sideByp == sideCop) and (sideCop == sideAdj):
        print ("This is an equilateral triangle")
        
    elif (sideAdj > sideByp) and (sideAdj > sideCop) and (sideByp == sideCop):
        print ("This is an isosceles triangle")
        
    elif (sideAdj > sideByp) and (sideCop < sideByp) and (sideAdj > sideCop):
        print ("This is a scalene triangle")
        
    elif (sideAdj < sideByp) and (sideByp > sideCop) and (sideAdj >= sideCop) or (sideCop >= sideAdj):
        print ("This is a right side of triangle")
        
    else:
        print ("This is NOT a triangle")
        
        
    repeat = input("Do you want to repeat this? Type Y for yes: ")
    
    if (repeat == "Y"):
        
        continue
    
    else:
        
        print ("Program has ended")
        break
