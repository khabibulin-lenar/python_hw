def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("under", end=" ")
    elif 18.5 <= bmi < 25.0:
        print("normal", end=" ")
    elif 25.0 <= bmi < 30.0:
        print("over", end=" ")
    else:
        print("obese", end=" ")


def start():
    case_num = int(input())
    cases = []
    for case in range(case_num):
        cases.append((weight := float(input()), height := float(input())))
    for case in cases:
        bmi_calculator(case[0], case[1])


start()