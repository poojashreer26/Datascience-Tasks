# INTEGER DATATYPE ASSIGNMENT
# ===========================
import math.lib
# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
x=[0,1,2,3,4,5,6,7,8,9,10]
sum_of_10_natural_numbers = math.prod(x)
print(sum_of_10_natural_numbers)

# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
x=(156%7)
print(f"remainder when 156 is divided by 7 :{x}")



# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
x=25
square_of_x=(x*x)
print(f"square of 25 is : {square_of_x} ")

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
x=125
cube_root_of_125=(x**(1/3))
print(f"cube of 125 is :{cube_root_of_125}")

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
x=(1,2,3,4,5)
sum_of_digits=sum(x)
print(f"sum of digits in number 12345 is :{sum_of_digits} ")

# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
   


# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
x=(8*7*6*5*4*3*2*1)
print(f"factorial of 8 is:{x}")


# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
x=(15,23,31,42,56)
y=sum(x)
z=(y/5)
print(f"average of numbers: 15, 23, 31, 42, 56 is : {z}")

# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
a=48
b=36
c = math.gcd(a,b)         
print(c)

# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
x=(1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39)
N=sum(x)
print(f"odd numbers 20:{N}")
