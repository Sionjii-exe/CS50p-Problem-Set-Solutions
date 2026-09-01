def main():
    text = input("Input: ")
    output = ""
    for c in text:
        if c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            continue

        else:
            output = output + c

    print(f"Output: {output}")

main()