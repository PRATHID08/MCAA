numbers = [1, 2, 3, 4, 5]

def sum_of_list(list):
    return sum(list)

def multiply_of_list(list):
    result = 1
    for number in list:
        result *= number
    return result

def largest_number(list):
    return max(list)


def smallest_number(list):
    return min(list)


print("Sum of all items:", sum_of_list(numbers))
print("Product of all items:", multiply_of_list(numbers))
print("Largest number:", largest_number(numbers))
print("Smallest number:", smallest_number(numbers))

