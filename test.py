try:
    x = int(input("What is x? "))
except ValueError:
    print("x is not an integer, please enter an integer!")
else:
    print(f"x is {x}")