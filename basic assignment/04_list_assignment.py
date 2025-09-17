# LIST DATATYPE ASSIGNMENT - 50 QUESTIONS
# ======================================
import math
# SOLVED EXAMPLE
# --------------
# Question: Find the maximum and minimum values in a list
print("SOLVED EXAMPLE:")
print("Find the maximum and minimum values in a list")
numbers = [23, 45, 12, 67, 34, 89, 56]
max_val = max(numbers)
min_val = min(numbers)
print(f"List: {numbers}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a list of first 10 square numbers
print("Question 1: Create a list of first 10 square numbers")

x=list(range(0,10))
for i in x:
    X=i*i
    print(X,end=",")

# Question 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n\nQuestion 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
L=list(range(1,11,2))
print(sum(L))


# Question 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("\nQuestion 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]")
A=[1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
B=[]
for i in A:
    if i not in B:
        B.append(i)
print(B)

# Question 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order
print("\nQuestion 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order")
A=[64, 34, 25, 12, 22, 11, 90]
A.sort(reverse=True)
print(A)
# Question 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]
print("\nQuestion 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]")
A=[15, 23, 31, 42, 56, 78, 91]
B=sum(A)/len(A)
print(B)

# Question 6: Create a list of first 15 Fibonacci numbers
print("\nQuestion 6: Create a list of first 15 Fibonacci numbers")
# Your code here

# Question 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]
print("\nQuestion 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]")
Q= [45, 67, 23, 89, 12, 34, 78]
Q.sort(reverse=True)
print(Q[1])

# Question 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
R=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
R.reverse()
print(R)

# Question 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]
print("\nQuestion 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]")
A=[1, 5, 2, 5, 3, 5, 4, 5, 6]
count=0
for i in A:
    if i==5:
        count+=1
print(count)

# Question 10: Create a list of prime numbers between 1 and 50
print("\nQuestion 10: Create a list of prime numbers between 1 and 50")
A=list(range(2,51))
count=[2]
for i in A:
    if i%i==0 and i%2!=0:
        count.append(i)
print(count)

# Question 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
C=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
D=[]
for i in C:
    for j in i:
        D.append(j)
print(D)

# Question 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]
print("\nQuestion 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]")
A=[1, 2, 3, 4, 5]
B=[4, 5, 6, 7, 8]
count=[]
for i in A:
    for j in B:
        if i==j:
            count.append(i)
print(count)

       

# Question 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]
print("\nQuestion 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]")
P=[[1, 2], [3, 4], [5, 6]]
Q=[]
for i in P:
    for j in i:
        Q.append(j)
print(list(Q))



# Question 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
P=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
F=[]
for i in P:
    Q=sum(i)
    F.append(Q)
print(F)

# Question 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
##

# Question 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
print("\nQuestion 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]")
Y=[[1, 5, 3], [9, 2, 7], [4, 8, 6]]
D=[]
for i in Y:
    Z=max(i)
    D.append(Z)
print(D)   


# Question 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
M=[[1, 2], [3, 4]]
N=[[5, 6], [7, 8]]
L=(M,N)
print(list(L))


# Question 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
z=[]
for i in L:
    for j in i:
        for h in j:
            z.append(h)
print(sum(z))


# Question 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B=[]
for i in A:
    for j in i:
        if j%2==0:
            B.append(j)
print(B)


# Question 20: Create a list of mixed data types: [1, "hello", 3.14, True, [1, 2, 3]]
print("\nQuestion 20: Create a list of mixed data types: [1, 'hello', 3.14, True, [1, 2, 3]]")
A=[1, "hello", 3.14, True, [1, 2, 3]]
print(list(A))

# Question 21: Find the length of each string in ["apple", "banana", "cherry", "date"]
print("\nQuestion 21: Find the length of each string in ['apple', 'banana', 'cherry', 'date']")
A=["apple", "banana", "cherry", "date"]
B=[]
for i in A:
   Z=len(i)
   B.append(Z)
print(B)
# Question 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]")
P=[(1, 'a'), (2, 'b'), (3, 'c')]
F=[]
for i in P:
    for j in i:
        F.append(j)
print(tuple(F))

# Question 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]")
P=[(1, 'a'), (2, 'b'), (3, 'c')]
F=[]
for i in P:
        F.append(i[0])
print((F))

# Question 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print("\nQuestion 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]")
M=[{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
N=dict(M)
print(N)

# Question 25: Extract all 'name' values from list of dictionaries
print("\nQuestion 25: Extract all 'name' values from list of dictionaries")
Q=[]
for i in M:
    Q.append(i['name'])
print(Q)

# Question 26: Find the person with maximum age in list of dictionaries
print("\nQuestion 26: Find the person with maximum age in list of dictionaries")
L=[]
for i in M:
        L.append(i['age'])
print(max(L))

# Question 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print("\nQuestion 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]")
A=[[1, 2], [3, 4]]
B=[[5, 6], [7, 8]]
C=[[9, 10], [11, 12]]
D=[[13, 14], [15, 16]]
e=A,B,C,D
print(e)

# Question 28: Find the maximum value in 4D list
print("\nQuestion 28: Find the maximum value in 4D list")
u=[]
for i in e:
    for j in i:
        for k in j:
                u.append(Q)
print(max(Q))


# Question 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print("\nQuestion 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]")
L=[{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print(L)

# Question 30: Find the union of all sets in list of sets
print("\nQuestion 30: Find the union of all sets in list of sets")
p=set.union(*L)
print(p)

# Question 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]
print("\nQuestion 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]")
S=list([1+2j, 3+4j, 5+6j])
print(S)

# Question 32: Find the magnitude of each complex number in list
print("\nQuestion 32: Find the magnitude of each complex number in list")
mag=[]
for i in S:
    mag.append(i)
print(i)

# Question 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]")
l=[1, [2, 3], [4, [5, 6]], 7]
print(l)


# Question 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]")
o=range(len(l))
print(o)

# Question 35: Create a list of functions: [len, str, int, float]
print("\nQuestion 35: Create a list of functions: [len, str, int, float]")
print(0,'123',96,8.8)

# Question 36: Apply each function in list to string "123"
print("\nQuestion 36: Apply each function in list to string '123'")
print('123')
result=()

# Question 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]
print("\nQuestion 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]")
K=[lambda x: x*2, lambda x: x**2, lambda x: x+1]
print(K)

# Question 38: Apply each lambda function to 5
print("\nQuestion 38: Apply each lambda function to 5")
for i in K:
    print(i(5))
       

# Question 39: Create a list of classes: [list, dict, set, tuple]
print("\nQuestion 39: Create a list of classes: [list, dict, set, tuple]")
O=list(range(0,7))
P=dict({'harish':'male'})
Q=set(range(0,4))
R=tuple(range(0,7))
print([O,P,Q,R])

# Question 40: Create instances of each class in list
print("\nQuestion 40: Create instances of each class in list")


# Question 41: Create a list of None values: [None, None, None, None]
print("\nQuestion 41: Create a list of None values: [None, None, None, None]")
N=[None, None, None, None]
print(N)


# Question 42: Replace all None values with 0 in list
print("\nQuestion 42: Replace all None values with 0 in list")
z=[]
for i in N:
    i=0
    z.append(i)
print(z)


# Question 43: Create a list of boolean values: [True, False, True, False]
print("\nQuestion 43: Create a list of boolean values: [True, False, True, False]")
P=[True, False, True, False]
print(P)



# Question 44: Count True values in boolean list
print("\nQuestion 44: Count True values in boolean list")
count=0
for i in P:
    if i == True:
        count+=1
print(count)
        

# Question 45: Create a list of ranges: [range(3), range(5), range(2)]
print("\nQuestion 45: Create a list of ranges: [range(3), range(5), range(2)]")
S=list(range(0,3))
F=list(range(0,5))
G=list(range(0,2))
O=[S,F,G]
print(O)

# Question 46: Convert each range to list
print("\nQuestion 46: Convert each range to list")
C=[]
for i in O:
    P=len(i)
    C.append(P)
print(C)

# Question 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]
print("\nQuestion 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]")


# Question 48: Convert each generator to list
print("\nQuestion 48: Convert each generator to list")
# Your code here

# Question 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]
print("\nQuestion 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]")


# Question 50: Extract all elements from each iterator
print("\nQuestion 50: Extract all elements from each iterator")
# Your code here 