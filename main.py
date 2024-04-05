#--------------------Question 1-----------------------
print("""          ____.                             
         |    |____    _____   ____   ______
         |    \__  \  /     \_/ __ \ /  ___/
     /\__|    |/ __ \|  Y Y  \  ___/ \___ \ 
     \________(____  /__|_|  /\___  >____  >
                   \/      \/     \/     \/ """)

#--------------------Question 2-----------------------
import math
a = float(input("Enter the first side length in meters:"))
b = float(input("Enter the second side length in meters:"))
c = float(input("Enter the third side length in meters:"))
S = (a+b+c)/2
A = math.sqrt(S*(S-a)*(S-b)*(S-c))

print("The S is", round(S, 2),"m")

print("The surfce area is",round(A,2),"m^2")

#--------------------Question 3----------------------- #How to make it more realistic?
import random

total = int(input("Enter your total budget this month:"))

food = round(random.uniform(0.2*total,0.25*total),2)
clothing = round(random.uniform(0.1*total,0.15*total),2)
rent = round(random.uniform(0.4*total, 0.5*total),2)
entertainment = round((total-food-clothing-rent),2)

print("The monthly food cost is, $",food,",and the percentage cost of it is, $",round(food/total*100, 0),"%")

print("The monthly clthing cost is, $",clothing,",and the percentage cost of it is, $",round(clothing/total*100, 0),"%")

print("The monthly entertainment cost is, $",entertainment,",and the percentage cost of it is, $",round(entertainment/total*100, 0),"%")

print("The monthly rent cost is, $",rent,",and the percentage cost of it is, $",round(rent/total*100, 0),"%")
