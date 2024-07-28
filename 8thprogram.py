def print_even_squares(start, end):
    print(f"Even numbers and their squares from {start} to {end}:")
    for num in range(start, end):
        if num % 2 == 0:
            square = num ** 2
            print(f"{num}: {square}")

print_even_squares(1, 50)
print_even_squares(1, 100)


people_info = [
    {"name": "John Doe", "age": 30, "blood_group": "A+"},
    {"name": "Jane Smith", "age": 25, "blood_group": "B-"},
    {"name": "Emily Davis", "age": 40, "blood_group": "O+"},
    {"name": "Micheal Brown", "age": 35, "blood_group": "AB-"},
    {"name": "William johnson", "age": 28, "blood_group": "A-"},
    {"name": "Emma Wilson", "age": 22, "blood_group": "B+"},
    {"name": "Oliver Marthinez", "age": 33, "blood_group": "O-"},
    {"name": "Sophia Anderson", "age": 27, "blood_group": "AB+"},
    {"name": "James Thomas", "age": 45, "blood_group": "A+"},
    {"name": "Isabella Lee", "age": 38, "blood_group": "B-"}
]

def print_person_info(people):
    for person in people:
        # Print each person's information
        print(f"Name: {person['name']}")
        print(f"Age: {person['age']}")
        print(f"Blood Group: {person['blood_group']}")
        print("-" * 30)

print_person_info(people_info)