# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
import math
x = (3.14,2.718,1.618,0.577)
y = sum(x)
avg = (y/4)
print(f"average is {avg}")


# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
F=float(98.6)
c = (F-32)* (5/9) 
print(f" 98.6 Fahrenheit to Celsius is :  {c}")

# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
P = 1000
I = 5.5
T = 3
CI = P*((1+I/T)**(I*T))
print(CI)


# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
side1 = 3.5
side2 = 4.2
hypt = math.sqrt((side1*side1)+(side2*side2))
print(f"hypotenuse of a right triangle with sides 3.5 and 4.2 is :{hypt}")

# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
r=7.8
V=(4/3)*3.14*(r*r*r)
print(f"volume of sphere is :{V}")

# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
print(round(3.14159,3))


# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
a=45
b=67
percnt=(45/67)*100
print(f"percentage: 45 out of 67 is :{percnt}")

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
import math
X = math.sqrt(23.456)
print(f"square root of 23.456 is :{X}")

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
P=2500
r= 6.5
t=2.5
FA=P*(1+r*t)
print(f"Simple intrest :{FA}")

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
x=45.7
radian = x * (3.14/180)
print(f"radiant of 45.7 is :{radian}")
