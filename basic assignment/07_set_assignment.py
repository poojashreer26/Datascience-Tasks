# SET DATATYPE ASSIGNMENT
# ======================

# SOLVED EXAMPLE
# --------------
# Question: Find the union of two sets
print("SOLVED EXAMPLE:")
print("Find the union of two sets")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {union_set}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a set of first 10 natural numbers
print("Question 1: Create a set of first 10 natural numbers")
N=set(range(10))
print(N)

# Question 2: Add element 11 to set {1, 2, 3, 4, 5}
print("\nQuestion 2: Add element 11 to set {1, 2, 3, 4, 5}")
M={1, 2, 3, 4, 5}
M.add(11)
print(M)

# Question 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}
print("\nQuestion 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}")
O={1, 2, 3, 4, 5, 6}
O.remove(3)
print(O)

# Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
A={1, 2, 3, 4, 5}
B ={4, 5, 6, 7, 8}
C=A.intersection(B)
print(C)

# Question 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
a= {1, 2, 3, 4, 5} 
b= {4, 5, 6, 7, 8}
c= a.difference(b)
print(c)

# Question 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}
print("\nQuestion 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}")
A1={1, 2, 3, 4, 6, 7, 8}
if 5 in A1:
    print("Present")
else:
    print("Not Present")

# Question 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}
print("\nQuestion 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}")
Set2 = {'a', 'b', 'c', 'd', 'e'}
print(len(Set2))

# Question 8: Create a set of vowels from string "hello world"
print("\nQuestion 8: Create a set of vowels from string 'hello world'")
Str = "hello world"
V ={'a','e','i','o','u'}
M = set()
for i in Str:
    if i in V:
        M.add(i)
print(M,end=".")

# Question 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set
print("\nQuestion 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set")
Set3=[1, 2, 2, 3, 4, 4, 5, 6, 6, 7] 
S=set(Set3)
print(S)

# Question 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}
print("\nQuestion 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}")
L={1, 2, 3}
M={1, 2, 3, 4, 5, 6}
N= L.issubset(M)
print(N)