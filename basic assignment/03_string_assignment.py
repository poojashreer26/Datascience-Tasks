# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================
import string 
import math
# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")
A="Python Programming"
B=A[::-1]
print(B)

# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
a="racecar"
b=a[::-1]
if a==b:
    print("is palindrome")
else:
    print("is not palindrome") 


# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
a="Python is a great programming language"
print(len(a))

# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
sting1="hello world" 
print(sting1.title())

# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
S2="Data Science"
print(len(S2))

# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
A = "Machine Learning"
RA=A.replace(" ","_")
print(RA)

# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
Srting= "Python Programming Language"
String1 = "Python"
if String1 in Srting:
    print(True)
else:
    print(False)    
# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
A="Artificial Intelligence"
print(A[0:6])

# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
S="UPPERCASE"
P=S.lower()
print(P)

# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
S1="Computer Science"
V=("aeiou")
for E in S1:
    if E not in V:
        print(E,end="")


# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
S='mississippi'
Max=max(S)
print(Max)


# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
A="listen"
B="silent"
if sorted(A) not in sorted(B):
    print("True")
else:
    print("False")

# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
A="python programming language"
print(A.title())

# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
v="Hello World"
S3=("aeiou")
count = 0
for i in v:
    if i not in S3 and i !=' ':
        count +=1
print(count)

# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
A=  "Python is a programming language"
B=A.split()
C = max(B)
print(C)

# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
import string
Str="Hello, World! How are you?"
for i in Str:
    if i not in string.punctuation:
        print(i,end="")

# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
S="Python"
print(S.startswith("Python"))

# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
A="Hello World"
P=A.index("o")
print(P)

# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
A="apple,banana,orange"
B=A.split(",")
print(B)

# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
P=['Python', 'is', 'awesome']
for i in P:
    if i != " ":
        print(i,end=" ")


# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
print('12345' is string)

# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
print('Helloworld'.isalpha() )

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
Z="hello world"
A=""
for i in range(len(Z)) :
    if i%2==0 :
        A +=Z[i].upper()
    else:
        A +=Z [i].lower()
print(A)

# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
Str1='banana' 
position= []
for i in range(0,len(Str1)):
    if Str1[i] == "a":
        position.append(i)
print(position)

# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
A="  Hello World  "
print(A.lstrip())

# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
Str="programming"
print(Str.endswith('ing'))

# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
l="Hello World"
P=l.replace("o","0",1)
print(P)
   
# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
import string 
O= "Python is a programming language"
Q=O.split()
print(min(Q))

# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
X="Python programming is powerful"
count=0
for i in X and X.lower():
    if i=='p':
        count+=1
print(count)

# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
W='Hello World Python'
D=W[::-1]
print(D)

# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
mail="user@example.com"
if '@' in mail and '.' in mail and mail.index('@') < mail.index('.'):
    print('valid')
else:
    print('not valid')

# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
link="https://www.example.com/path"
domain=link.split('//')[-1].split('/')[0]
print(domain)

# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
A='''The rain falls soft,
A gentle, whispered beat.
Washing the world clean,
A melody so sweet'''
B=A.split(",")
print(len(B))

# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
Str1="hello" 
Str2="World"
Unq=set(Str1) & set(Str2)
print(Unq)


# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
N="+1-555-123-4567"
Num=N.replace("-","")
if Num.startswith('+1') and len(Num)==12:
    print('vaild')
else:
    print('invalid')

# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
L="abc123def456ghi789"
for i in L :
    if i.isnumeric():
        print(i,end=",")

# Question 37: Convert "snake_case" to "camelCase"
print("\n\nQuestion 37: Convert 'snake_case' to 'camelCase'")
A="snake_case"
B=A.replace('_',"")
print(B)

# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
A="A man a plan a canal Panama".lower()
a=A.replace(" ","")
b=a[::-1]
if a == b:
    print("is palandrome")
else:
    print("Not palandrome")


# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
text = "the quick brown fox jumps over the lazy dog"
words = text.split() 
word_count  = 0
word_text  = ' '
for i in words:
    count  = words.count(i)
    if count > word_count:
        word_count  = count
        word_text  = i
        print(word_text)

# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
S="National Aeronautics and Space Administration"
s=S.split()
for i in s:
    if len(i)>3:
        print(i[0:1],end="")

# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
X="((()))"
if len(X)%2 == 0:
    print("is equal")
else:
    print("not equal")

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
N=[]
morse =dict({'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',' ':'/'})
s = "hello world"
for i in s:
        N.append(morse[i])
print(N)


# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
str1="programming"
str2="grammar"
l=""
for i in range(len(str1)):
    for j in range(i,len(str1)+1):
        a=str1[i:j]
        if a in str2 and len(a)>len(l):
            l=a
print(l)

# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
link='https://www.google.com'
if link.startswith('http://')and link.endswith('.com' ):
    print('valid')
else:
    print('not valid')


# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
A="Python programming is amazing and powerful"
B=A.split()
for i in B:
    if len(i)>5:
        print(i,end=",")

# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
# Your code here

# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
Ip="192.168.1.1"
ip=Ip.split('.')
for i in ip:
    if int(i) in range(0,255):
        print('vaild')
    else:
        print('invalid')


# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
A='abc' 
for i in range(len(A)):
    for j in range(i,len(A)+1):
        print(A[i:j],end=" ")


# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
# Your code here

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
N="4532015112830366"
if len(N)==16:
    print(True)
else:
    print(False)