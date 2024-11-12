#ex_1
counter = 0
total = 0

# Construct the while loop
while counter <= 100:
    total += counter  # Add counter to total
    counter += 1      # Increment counter

print(total)

#ex_2
# List of names
names = ["Patel", "Qwerty", "Bond", "Asdfg", "Zxcvb"]

# Initialize the counter
index = 0

while index < len(names):
    if names[index] == "Bond":
        print("We’ve been expecting you, Mr Bond")
        break  
    index += 1  
