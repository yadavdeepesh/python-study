num  = int(input("Enter the number "))

flag = False

if num <= 1:
    print("not prime number")

for x in range(2 , num):
    if num % x == 0:
        flag = True
        break


if not flag:
    print("Prime Number", num)
else:
    print("Is Not Prime Number", num)