start_letter = input()
end_letter = input()
miss_letter = input()
counter = 0

for n in range(ord(start_letter), ord(end_letter) + 1):
    for m in range(ord(start_letter), ord(end_letter) + 1):
        for k in range(ord(start_letter), ord(end_letter) + 1):
            if n != ord(miss_letter) and m != ord(miss_letter) and k != ord(miss_letter):
                counter += 1
                print(f"{chr(n)}{chr(m)}{chr(k)}", end=" ")
            else:
                pass

print(counter)