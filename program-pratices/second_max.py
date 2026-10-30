numbers = [12, 5, 8, 20, 15, 20, 3]

first = float('-inf')
second = float('-inf')

for i in range(len(numbers)):
    
    if numbers[i] > first:
        second = first
        first = numbers[i]
    if second < numbers[i] and first > numbers[i]:
        second = numbers[i]
        
print("Second Max = ",second)