x, y, z = input("Expression: ").split(" ")

x = int(x)
z = int(z)

if y == "+":
    ans = x + z
    print(f"{ans:.1f}")

elif y == "-":
    ans = x - z
    print(f"{ans:.1f}")

elif y == "/" and z == 0:
    print(f"Error, {x} cannot be divided by {z}")

elif y == "/":
    ans = x / z
    print(f"{ans:.1f}")

elif y == "*":
    ans = x * z
    print(f"{ans:.1f}")
