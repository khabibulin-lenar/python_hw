def crowd_test(names):
    if len(names) > 3:
        print("Crowded")
    else:
        print("The room is not that crowded")


names = ["Bob", "Whitney", "Houston", "Jerry"]

crowd_test(names)
del names[2:]
crowd_test(names)


def crowd_test(names):
    if len(names) > 5:
        print("There is a mob in the room")
    elif len(names) > 3:
        print("The room is crowded")
    elif len(names) >= 1 and len(names) <= 2:
        print("The room is not that crowded")
    else:
        print("The room is empty")


names.extend(["Marty", "Larry", "Frederick", "Laura"])

crowd_test(names)