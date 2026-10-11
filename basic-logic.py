# Basic (Syntax and Logic)
# 1. Hello World and taking user input
# 2. Add, subtract, multiply, divide (simple calculator)
# 3. Even or odd number check
# 4. Largest of three numbers
# 5. Swap two variables
# 6. Factorial of a number
# 7. Fibonacci series
# 8. Prime number check and prime numbers in a range
# 9. Reverse a number or string
# 10. Palindrome check
# 11. Sum of digits and Armstrong number
# 12. Multiplication table
# 13. Leap year check
# 14. Count vowels in a string
# 15. Temperature converter (Celsius to Fahrenheit)

# answers:1

# print("Hello World!")

# answers:2 

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))

# operator = input("enter operator (+, -, *, / ) :")

# def calculator(a , b, operator):
#     match operator:
#         case "+":
#             return a + b
#         case "-":
#             return a - b
#         case "*":
#             return a * b
#         case "/":
#             if b!=0:
#                 return a / b
#             return "Cannot divide by zero" 
#         case _:
#             return "Invalid operator ::"

# print(calculator(a,b,operator))

# answers:3

# num = int(input("enter the number "))

# def check_even_odd(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
    
# print(check_even_odd(num)) 

# answers:4

# a = int(input("enter the first number :"))
# b = int(input("enter the second number :"))
# c = int(input("enter the third number :"))

# def largest_three_num(a , b , c):
#     if a > b and a > c:
#         return f"a is largest number {a}"
#     elif b > a and b > c:
#         return f"b is largest number {b}"
#     else:
#         return f"c is largest number {c}"
        
        
# print(largest_three_num(a ,b ,c))
    
# answers:5

# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# print(f" before the swap a , b values {a , b}")
# a = a + b
# b = a - b
# a = a - b
# print(f" After the swap a , b values {a , b}")

# answers:6

# a = 0
# b = 1

# num = int(input("enter the number: "))
# print(a, b, end=" ")

# for x in range(num):
#     t = a + b
#     b = a
#     a = t
#     print(a ,end=" ")
 
 
# a = 0
# b = 1

# num = int(input("Enter the number: "))

# if num <= 0:
#     print("Please enter a positive number")
# elif num == 1:
#     print(a)
# else:
#     print(a, b, end=" ")

#     for x in range(num - 2):
#         t = a + b
#         b = a
#         a = t
#         print(a, end=" ")






    

