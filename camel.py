def main():
    camel = input("camelCase: ")
    result = ""
    for c in camel:
        if c.islower():
            result = result + c

        elif c.isupper():
            c = c.lower()
            result = result + "_" + c

    print(f"snake_case: {result}")
    
main()