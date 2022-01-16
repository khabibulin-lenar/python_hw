bookstore_inventory = [["34587", "Learning Python, Mark Lutz", 4, 40.95],
                       ["98762", "Programming Python, Mark Lutz", 5, 56.80],
                       ["77226", "Head First Python, Paul Barry", 3, 32.95],
                       ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]]

order_invoice = list(map(lambda x: x if x[1] >= 100 else (x[0], x[1] + 10), map(lambda x: (x[0], x[2] * x[3]),
                                                                                bookstore_inventory)))
print(order_invoice)

