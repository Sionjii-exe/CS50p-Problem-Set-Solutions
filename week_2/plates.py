# First it has to check whether the plate is 2 to 6 characters long
# Is it less than 2 or greater than 6? If true, then it will return FALSE

# The first two characters must be letters
# It will check if the first and second characters are letters
# If either are not, then it will return FALSE

# No punctuation or space, only letters and numbers
# If there is, it will return false

# Once the first number appears, every character after it must also be a number

# The first number cannot be 0

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1
    if not (2 <= len(s) <= 6):
        return False
    
    # Rule 2
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3
    for c in s:
        if not c.isalnum():
            return False

    # Rule 4
    # Rule 5
    seen_number = False

    for c in s[2:]:
        if c.isdigit():
            if not seen_number:
                if c == "0":
                    return False
            seen_number = True  
        elif c.isalpha() and seen_number:
            return False

    return True

main()
