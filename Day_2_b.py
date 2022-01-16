a = [1, "hello", 2.0]
print(a)

print([1, 1, [1, 2]][2][1])

d = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
print(tuple([1, [2, 3]]))

c = set('Mississippi')

c.add('X')

print(set([1, 1, 2, 3]))


for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=", ")

