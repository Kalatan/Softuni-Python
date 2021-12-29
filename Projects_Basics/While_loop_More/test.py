letter_input = input()

while letter_input != "End":
    if letter_input.encode().isalpha():
        print(letter_input)
        break
    else:
        pass