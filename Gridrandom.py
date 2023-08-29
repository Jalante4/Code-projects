import random
print("welcome to your random grid tile picker!")
name = input("Welcome, what is your name? ")
max_row = input("Whats the amount of rows? ")
max_row = int(max_row)

max_col = input("Whats the amount of colums? ")
max_col = int(max_col)


row = random.randint(1, max_row)
print("Your randomized Row is: ",row)

col = random.randint(1, max_col)
print("Your randomized Column is: ", col)
print("Have a nice day", name, "!")