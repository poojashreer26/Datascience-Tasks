# TUPLE DATATYPE ASSIGNMENT
# ========================

# SOLVED EXAMPLE
# --------------
# Question: Find the sum and product of all elements in a tuple
print("SOLVED EXAMPLE:")
print("Find the sum and product of all elements in a tuple")
numbers = (2, 4, 6, 8, 10)
sum_tuple = sum(numbers)
product = 1
for num in numbers:
    product *= num
print(f"Tuple: {numbers}")
print(f"Sum: {sum_tuple}")
print(f"Product: {product}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")
N_num=tuple(range(10))
print(N_num)

# Question 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("\nQuestion 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
T1=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(T1))

# Question 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')
print("\nQuestion 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')")
T2=('a', 'b', 'c', 'd', 'e')
print(T2[2])

# Question 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)
print("\nQuestion 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)")
T=(23, 45, 12, 67, 34, 89, 56)
max=max(T)
print(max)

# Question 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)
print("\nQuestion 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)")
T3=(1, 5, 2, 5, 3, 5, 4, 5, 6)
count = 0 
for i in T3:
    if i==5:
        count += 1
print(count)

# Question 6: Create a tuple of mixed data types (integer, float, string, boolean)
print("\nQuestion 6: Create a tuple of mixed data types (integer, float, string, boolean)")
Mdt= (1,1.5,"Dtype",True)
print(Mdt)

# Question 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')
print("\nQuestion 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')")
E=('java', 'python', 'c++', 'javascript')
print(E.index("python"))


# Question 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)
print("\nQuestion 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)")
X=(10, 20, 30, 40, 50)
if 25 in X:
    print("exists")
else:
    print("doesn't exists")


# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")
N = tuple(range(10))
for i in N:
    if i%2==0:
        print(i,end=",")

# Question 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)
print("\nQuestion 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)")
T=(15, 23, 31, 42, 56, 78)
Avg=(sum(T)/len(T))
print(Avg)