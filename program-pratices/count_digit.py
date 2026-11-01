num = 153
count = 0
sum = 0
product = 1
original_num = num
a= 0
while num >0:
    rem = num % 10
    count = count*10 +  rem
    sum = sum + rem
    a =a+rem*rem*rem
    product = product * rem
    num = num // 10
print("Number of digits:", count)
print("Sum of digits:", sum)
print("Product of digits:", product)

if original_num == count or a == original_num:
    print("The number is a palindrome", "or an Armstrong number", "or both")
else:
    print("The number is not a palindrome")
    