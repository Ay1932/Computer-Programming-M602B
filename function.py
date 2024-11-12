#ex1
def square(number):
    return number ** 2

result = square(5)
print(result) 

#ex_2
print("Excercise no.2")
def max_num(a, b):
    if a > b:
        return a
    else:
        return b
result = max_num(100, 20)
print(result)  

"""
#ex_3
print("Excersie no.3")
def calculate_tax(salary):
    if salary <= 20000:
        tax = 0
    elif salary => 20001 and salary <= 50000:
        tax = (salary)
"""

#ex_reveerse function
print("Ex no. 4")
def reverse_string(s):
    return s[::-1]


input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)


#ex no.5
def find_average(numbers):
    if not numbers: 
        return 0  
    return sum(numbers) / len(numbers)

num_list = [10, 20, 30, 40, 50]
average = find_average(num_list)
print(f"The average is: {average}") 


#ex no.5

