def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def reverse_number(number):
    return int(str(number)[::-1])

try:
    num = int(input("Enter a four-digit number: "))

    if 1000 <= num <= 9999:
        digit_sum = sum_of_digits(num)
        print(f"Sum of digits: {digit_sum}")

        reversed_num = reverse_number(num)
        print(f"Reverse of the number: {reversed_num}")
    else:
        print("Error: Please enter a four-digit number.")
except ValueError:
    print("Error: Invalid input. Please enter a valid four-digit number.")
