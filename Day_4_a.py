def func():
    print("Hello World")


def func1(name):
    print(f'Hi My name is {name}')


def func3(x, y, z):
    if z:
        return x
    elif not z:
        return y


def func4(x, y):
    return x*y


def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 == 1:
        return False


def func5(num1, num2):
    if num1 > num2:
        return True
    else:
        return False


def func6(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


def func7(*args):
    even = []
    for x in args:
        if x % 2 == 0:
            even.append(x)
    return even


def func8(word):
    new_word = ""
    count = 0
    for c in word:
        if count % 2 == 0:
            new_word += c.upper()
        else:
            new_word += c.lower()
        count += 1
    return new_word


def func9(s1, s2):
    if s1[0].lower() == s2[0].lower():
        return True
    else:
        return False


def func10(s3):
    new_s3 = ""
    count = 0
    for c in s3:
        if count == 0:
            new_s3 += c.upper()
        elif count == 3:
            new_s3 += c.upper()
        else:
            new_s3 += c.lower()
        count += 1
    return new_s3

