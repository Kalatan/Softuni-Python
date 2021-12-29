letter_input = input()
string = ""
count_n = 0
count_o = 0
count_c = 0

while letter_input != "End":
    if letter_input.encode().isalpha():
        if letter_input == "n":
            count_n += 1
            if count_n > 1:
                string += "".join(letter_input)
            letter_input = input()
        elif letter_input == "c":
            count_c += 1
            if count_c > 1:
                string += "".join(letter_input)
            letter_input = input()
        elif letter_input == "o":
            count_o += 1
            if count_o > 1:
                string += "".join(letter_input)
            letter_input = input()
        else:
            string += "".join(letter_input)
            letter_input = input()
        if count_n >= 1 and count_c >= 1 and count_o >= 1:
            print(string, end=" ")
            string = ""
            count_n = 0
            count_o = 0
            count_c = 0
    else:
        letter_input = input()