import random

max_row = input("Whats the amount of rows? ")
max_row = int(max_row)

max_col = input("Whats the amount of colums? ")
max_col = int(max_col)


row = random.randint(1, max_row)
print("Row: ",row)

col = random.randint(1, max_col)
print("Column: ", col)
