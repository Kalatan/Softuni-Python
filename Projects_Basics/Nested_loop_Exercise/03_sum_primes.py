input_text = input()
prime_sum = 0
non_prime_sum = 0

while input_text != "stop":
    current_number = int(input_text)
    prime_counter = 0
    if current_number < 0:
        print("Number is negative.")
        input_text = input()
        continue
    elif current_number == 1:
        non_prime_sum += 1
        input_text = input()
        continue
    elif current_number == 2:
        prime_sum += 2
        input_text = input()
        continue
    for num in range(2, current_number):
        if current_number % num == 0:
            non_prime_sum += current_number
            break
        else:
            prime_counter += 1
            if prime_counter == current_number - 2:
                prime_sum += current_number
    input_text = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")