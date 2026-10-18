num  = int(input("Enter the number of range limit end point :: "))

flag = False

if num <= 1:
    print("not prime number")
count = 0
for y in range(2, num+1):
    flag = False
    for x in range(2 , y):
        # print(y,x)
        if y % x == 0:
            flag = True
            
    if not flag:
        count += 1
            
            
print("total prime number is given list : ",count)

 