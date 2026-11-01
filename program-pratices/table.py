num = int(input("Enter a number: "))    

# for i in range(1, 11):
#     print(num, 'x', i, '=', num*i)  

a = 0
b = 1

for i in range(num):
    print(a, end=' ')
    c = a + b
    a = b
    b = c
    

    