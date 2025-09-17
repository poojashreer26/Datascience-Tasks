# COMPLEX DATATYPE ASSIGNMENT
# ==========================

# SOLVED EXAMPLE
# --------------
# Question: Create a complex number and find its conjugate
print("SOLVED EXAMPLE:")
print("Create a complex number and find its conjugate")
z = 3 + 4j
conjugate = z.conjugate()
magnitude = abs(z)
print(f"Complex number: {z}")
print(f"Conjugate: {conjugate}")
print(f"Magnitude: {magnitude}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create complex number 5 + 3j
print("Question 1: Create complex number 5 + 3j")
C= complex(5,3)
print(C)

# Question 2: Find the real part of complex number 7 - 2j
print("\nQuestion 2: Find the real part of complex number 7 - 2j")
C1= (7 - 2j)
C=C1.real
print(C)

# Question 3: Find the imaginary part of complex number 4 + 6j
print("\nQuestion 3: Find the imaginary part of complex number 4 + 6j")
C2=(4 + 6j)
c=C2.imag
print(c)


# Question 4: Add two complex numbers: (3 + 2j) and (1 + 4j)
print("\nQuestion 4: Add two complex numbers: (3 + 2j) and (1 + 4j)")
A=(3 + 2j) + (1 + 4j)
print(A)

# Question 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)
print("\nQuestion 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)")
A= (2 + 3j) 
B=(1 + 2j)
C=A*B
print(C)

# Question 6: Find the magnitude of complex number 6 + 8j
print("\nQuestion 6: Find the magnitude of complex number 6 + 8j")
P=(6 + 8j)
E=abs(P)
print(E)

# Question 7: Find the conjugate of complex number 5 - 7j
print("\nQuestion 7: Find the conjugate of complex number 5 - 7j")
C= 5 - 7j
W=c.conjugate()
print(W)

# Question 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)
print("\nQuestion 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)")
B=(10 + 5j) - (3 + 2j)
print(B)

# Question 9: Divide complex numbers: (8 + 6j) / (2 + 1j)
print("\nQuestion 9: Divide complex numbers: (8 + 6j) / (2 + 1j)")
C=(8 + 6j) / (2 + 1j)
print(c)

# Question 10: Find the phase angle of complex number 1 + 1j
print("\nQuestion 10: Find the phase angle of complex number 1 + 1j")
import cmath
A=1 + 1j
print(cmath.phase(A))