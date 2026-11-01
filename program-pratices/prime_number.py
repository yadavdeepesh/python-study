# check if a number is prime or not 
# num = int(input("Enter a number: "))   
# if num <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# print all prime numbers in a given range
   
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):

    if num <= 1:
        continue

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")