def print_even_squares(start, end):
    for num in range(start, end):
        if num % 2 == 0:
            square = num ** 2
            print(f"Number: {num}, Square: {square}")


print("Even numbers and their squares in range(1, 50):")
print_even_squares(1, 50)


print("\nEven numbers and their squares in range(1, 100):")
print_even_squares(1, 100)