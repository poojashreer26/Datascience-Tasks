# DICTIONARY DATATYPE ASSIGNMENT - 50 QUESTIONS
# ============================================

# SOLVED EXAMPLE
# --------------
# Question: Find the key with maximum value in a dictionary
print("SOLVED EXAMPLE:")
print("Find the key with maximum value in a dictionary")
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88}
max_key = max(scores, key=scores.get)
max_value = scores[max_key]
print(f"Dictionary: {scores}")
print(f"Key with maximum value: {max_key}")
print(f"Maximum value: {max_value}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a dictionary of student names and their ages
print("Question 1: Create a dictionary of student names and their ages")
D=dict({'name': 'John', 'age': 25})
print(D)

# Question 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}
print("\nQuestion 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}")
S={'a': 1, 'b': 2, 'c': 3}
S.update({'d':4})
print(S)

# Question 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}
print("\nQuestion 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}")
X=dict({'name': 'John', 'age': 25, 'city': 'New York'})
print(X.keys())
      
# Question 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}
print("\nQuestion 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}")
Y={'python': 3, 'java': 2, 'c++': 1}
print(Y.values())

# Question 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}
print("\nQuestion 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}")
z={'name': 'Alice', 'age': 30, 'city': 'London'}
Z=z.keys()
if 'age' in Z:
    print('True')
else:
    print('false')


# Question 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
print("\nQuestion 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}")
D={'a': 1, 'b': 2, 'temp': 3, 'c': 4}
D.pop('temp')
print(D)

# Question 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}
print("\nQuestion 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}")
P={'math': 85, 'science': 92, 'english': 78}
p=P.values()
print(sum(p))

# Question 8: Create a dictionary with squares of numbers 1 to 5
print("\nQuestion 8: Create a dictionary with squares of numbers 1 to 5")
a={X:X**2  for X in range(1,6)}
print(a)


# Question 9: Count frequency of each character in string "hello"
print("\nQuestion 9: Count frequency of each character in string 'hello'")
Str='hello'
E={}
for i in Str:
    if i in E:
        E[i]+=1
    else:
        E[i]=1
print(E)

# Question 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4} 
print("\nQuestion 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}")
E=dict({'a': 1, 'b': 2})
F=dict({'c': 3, 'd': 4})
print(E|F ,end="")


# Question 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}")
L=dict({'person': {'name': 'Alice', 'age': 25}})
print(L)

# Question 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}")
M=L['person']['name']
print(M) 


# Question 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print("\nQuestion 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}")
D=dict({'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']})
print(D)

# Question 14: Add 'orange' to the 'fruits' list in nested dictionary
print("\nQuestion 14: Add 'orange' to the 'fruits' list in nested dictionary")
D['fruits'].append('orange')
print(D)

# Question 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print("\nQuestion 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}")
d=({'coordinates': (10, 20), 'rgb': (255, 0, 0)})
print(d)

# Question 16: Extract first coordinate from nested tuple
print("\nQuestion 16: Extract first coordinate from nested tuple")
K=d['coordinates'][0]
print(K)

# Question 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print("\nQuestion 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}")
S=dict({'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}})
print(S)

# Question 18: Add 'o' to vowels set in nested dictionary
print("\nQuestion 18: Add 'o' to vowels set in nested dictionary")
S['vowels'].update('o')
print(S)

# Question 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print("\nQuestion 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}")
NL={'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print(NL)

# Question 20: Access employee name from 3-level nested dictionary
print("\nQuestion 20: Access employee name from 3-level nested dictionary")
L=NL['company']['department']['employee']['name']
print(L)

# Question 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print("\nQuestion 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}")
C={'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print(C)

# Question 22: Check data type of each value in mixed dictionary
print("\nQuestion 22: Check data type of each value in mixed dictionary")
L=C.values()
N=[]
for i in L:
    M=type(i)
    N.append(M)
print(N)


# Question 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}
print("\nQuestion 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}")
Z={'len': len, 'str': str, 'int': int}
print(Z)

# Question 24: Apply each function to "123" using dictionary
print("\nQuestion 24: Apply each function to '123' using dictionary")
Z.update({'len': 123, 'str': 123, 'int': 123})
print(Z)

# Question 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}
print("\nQuestion 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}")
d={'double': lambda x: x*2, 'square': lambda x: x**2}
print(d)

# Question 26: Apply each lambda function to 5
print("\nQuestion 26: Apply each lambda function to 5")
##



# Question 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}
print("\nQuestion 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}")
CV={'list': list, 'dict': dict, 'set': set}
print(CV)

# Question 28: Create instances using class dictionary
print("\nQuestion 28: Create instances using class dictionary")
##

# Question 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}
print("\nQuestion 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}")
N={'a': None, 'b': None, 'c': None}
print(N)

# Question 30: Replace all None values with 0
print("\nQuestion 30: Replace all None values with 0")
M=N.update({'a': 0, 'b': 0, 'c': 0})

# Question 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}
print("\nQuestion 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}")
A={'is_active': True, 'is_admin': False}
print(A)

# Question 32: Count True values in boolean dictionary
print("\nQuestion 32: Count True values in boolean dictionary")
a=A.values()
count=0
for i in  a:
    if i==True:
        count+=1
print(count)

# Question 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}
print("\nQuestion 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}")
v={'z1': 3+4j, 'z2': 1+2j}
print(v)

# Question 34: Find magnitude of each complex number
print("\nQuestion 34: Find magnitude of each complex number")
A=v.values()
D=[]
for i in A:
    b=abs(i)
    D.append(b)
print(D)



# Question 35: Create a 4-level nested dictionary
print("\nQuestion 35: Create a 4-level nested dictionary")
ND={'company': {'department': {'employee': {'name':'alex'}}}}
print(ND)

# Question 36: Access deepest value in 4-level nested dictionary
print("\nQuestion 36: Access deepest value in 4-level nested dictionary")
print(ND['company']['department']['employee']['name'])


# Question 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}
print("\nQuestion 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}")
A={'r1': range(3), 'r2': range(5)}
print(A)

# Question 38: Convert each range to list
print("\nQuestion 38: Convert each range to list")
I=list(range(0,3))
U=list(range(0,5))
R={'r1': I, 'r2': U} 
print(R)

# Question 39: Create a dictionary with generator values
print("\nQuestion 39: Create a dictionary with generator values")
D={'a':1,'b':2,'c':3}
d={i for i in D.values()}
print(d)


# Question 40: Convert each generator to list
print("\nQuestion 40: Convert each generator to list")
print([d])

# Question 41: Create a dictionary with iterator values
print("\nQuestion 41: Create a dictionary with iterator values")
R=iter(range(1,6))
Y={i:next(R) for i in range(5)}
print(Y)

# Question 42: Extract all elements from each iterator
print("\nQuestion 42: Extract all elements from each iterator")
print(Y.items())

# Question 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print("\nQuestion 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}")
Y= {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print(Y)

# Question 44: Find sum of each nested list
print("\nQuestion 44: Find sum of each nested list")
A=Y['matrix']
B=[]
C=[]
for i in A:
    a=sum(i)
    B.append(a)

D=Y['vector']
c=sum(D)
C.append(c)
print(B,C)

# Question 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print("\nQuestion 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}")
ND={'config': {'db': {'host': 'localhost', 'port': 5432}}}
print(ND)

# Question 46: Access database port from nested configuration
print("\nQuestion 46: Access database port from nested configuration")
L=ND['config']['db']['port']
print(L)

# Question 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print("\nQuestion 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}")
NT={'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print(NT)

# Question 48: Extract first point coordinates
print("\nQuestion 48: Extract first point coordinates")
print(NT['points'][0])

# Question 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
print("\nQuestion 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}")
A={'groups': {frozenset({1, 2, 3}), frozenset({4, 5, 6})}, 'categories': {frozenset({'a', 'b'}), frozenset({'c', 'd'})}}
print(A)

# Question 50: Find union of all nested sets
print("\nQuestion 50: Find union of all nested sets")
D=A['groups']
F=A['categories']
un=set().union(*D)
print(un)
uc=set().union(*F)
print(uc)
