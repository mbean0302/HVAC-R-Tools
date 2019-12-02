from tabulate import tabulate
name1 = input("What is your name? ")
name2 = input("What is your name? ")
name3 = input("What is your name? ")
table = [[name1, 32, 0], [name2, 30, 0], [name3, 7, 1]]

print(tabulate(table, headers=["Name", "Age", "0 or 1"]))
