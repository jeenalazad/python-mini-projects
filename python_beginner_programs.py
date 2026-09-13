# Python Beginner Programs
# Easy programs for practice

# 1. Hello World
print("Hello, World!")

# 2. Add two numbers
a = 10
b = 20
print("Sum =", a + b)

# 3. Take input from user
name = input("Enter your name: ")
print("Hello", name)

# 4. Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 5. Check positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 6. Find the largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)

# 7. Find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest =", max(a, b, c))

# 8. Calculate area of a circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area =", area)

# 9. Calculate simple interest
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)

# 10. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 11. Print multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 12. Find sum of first N natural numbers
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)

# 13. Find factorial
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)

# 14. Check whether a number is prime
n = int(input("Enter a number: "))
if n < 2:
    print("Not Prime")
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Not Prime")

# 15. Reverse a string
text = input("Enter a string: ")
print("Reverse =", text[::-1])

# 16. Count vowels in a string
text = input("Enter a string: ")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Number of vowels =", count)

# 17. Find sum of list elements
numbers = [10, 20, 30, 40, 50]
print("List =", numbers)
print("Sum =", sum(numbers))

# 18. Find maximum in a list
numbers = [12, 45, 7, 89, 23]
print("Maximum =", max(numbers))

# 19. Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9 / 5) + 32
print("Fahrenheit =", f)

# 20. Swap two numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)
