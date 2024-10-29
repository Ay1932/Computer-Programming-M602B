# Take user input
value = input("Enter a value: ")

number = float(value)

    # Check if the value is an integer
if number.is_integer():
        print("The entered value is an integer.")
else:
        # If it's a float, calculate and display the decimal component
        decimal_component = number - int(number)
        print(f"The entered value is a float. Decimal component: {decimal_component}")

