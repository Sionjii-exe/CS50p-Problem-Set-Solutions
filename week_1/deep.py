deep = input("What is the Answer to Great Question of Life, the Universe, and Everything? ")
match deep:
    case "42":
        print("Yes")

    case "forty-two":
        print("Yes")

    case "forty two":
        print("Yes")

    case _:
        print("No")
