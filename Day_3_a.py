for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        print(x)

print("60°C is", int((60*9/5)+32), "in Fahrenheit")
print("45°F is", int((45-32)*(5/9)), "in Celsius")

import random
num = random.randint(1, 9)
while True:
    x = int(input("Guess a number from 1 to 9: "))
    if x == num:
        print("Well guessed!")
        break

for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()
for i in range(5, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print()

word = input()
print(word[::-1])

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = odd = 0
for num in nums:
    if num % 2 == 0:
        even += 1
    elif num % 2 == 1:
        odd += 1
print("Number of even numbers :", even)
print("Number of odd numbers :", odd)

datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for i in datalist:
    print(type(i))

for i in range(7):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end=' ')
