customer_list = ["customer1" , "customer2" , "customer3"]
for x in customer_list:
    if x == "customer2":
        continue
    print(x)
    
    
#ex_1
names = ["Qwe" , "Asd" , "Zxc" , "Vbn" , "Mkl" , "Rty" , "Uio"]

#for loop for congratulations
for x in names:
    print(f"Congratulation {x}!")
    
#ex_2
#example stirng is Abcdefghijklmnopqrstuvwxyz
text = "Abcdefghijklmnopqrstuvwxyz"

#for loop
for letter in text:
    print(letter)
    
#ex_3
#given list is 3 7 6 8 9 11 15 25
lst1 = [3,7,6,8,9,11,15,25]
lst2 = []

for num in lst1:
    lst2.append(num ** 2)
print(lst2)

#ex_4
#given list is 3 7 6 8 9 11 15 25
lst1 = [3,7,6,"Qwerty",9,11,15,25]
lst2 = []

for num in lst1:
    lst2.append(num ** 2)
print(lst2)