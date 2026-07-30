# text = input()

# if ":)" in text:
#     newtext = text.replace(":)", "🙂")

# if ":(" in text:
#     newtext = text.replace(":(", "🙁")

# print(newtext)

def main():
    text = input("Please enter a sentence: ")
    newtext = convert(text)
    print(newtext)

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()
