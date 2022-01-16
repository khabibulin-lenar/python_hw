print(50+50)
print(100-10)

print(6**6)
print(6+6+6+6+6+6)

print("Hello World")

import math
#loan size
p = int(input())
#interest rate
r = float(input()) * 0.01
#months to payout
l = int(input())
#monthly payment
m = (p*(r/12))/(1-(1/((1+(r/12))**l)))
print(int(math.ceil(m)))

