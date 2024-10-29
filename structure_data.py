"""
# Creating a list of integers
numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]

#printed all integer
print(numbers)

# Finding the largest and smallest numbers in the list
largest = max(numbers)
smallest = min(numbers)

# Printing the results
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)
"""


# Sample input: list of dictionaries
people = [
    {"name": "Lewis Hamilton", "age": 35},
    {"name": "Lando Norris", "age": 24},
    {"name": "Oscar Piastri", "age": 20}
]

# Sorting the list by age and extracting names
sorted_names = [person["name"] for person in sorted(people, key=lambda x: x["age"])]

# Printing the sorted list of names
print("Names sorted by age:", sorted_names)
