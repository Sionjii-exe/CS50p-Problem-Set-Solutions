def main():
    owed = 50
    while owed > 0:
        print(f"Amount due: {owed}")
        money = int(input("Insert coin: "))
        if money in [25, 10, 5]:
            owed = owed - money
            if owed <= 0:
                owed = abs(owed)
                print("")
                print(f"Change owed: {owed}")
                break
        else:
            print("Enter denominations: 25 sents, 10 cents, 5 cents")

        print("")

main()