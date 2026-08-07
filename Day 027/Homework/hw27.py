# 1

name = "Giorgi"

print(name[0:3])
print(name[2:]) 
print(name[:4]) 
print(name[-1])

# (1) პირველი წამოიღებს მარტო "Gio" - ს. 
# (2) მეორე წამოიღებს "orgi" - ს. 
# (3) მესამე წამოიღებს მარტო "gi" - ს.
# (4) მეოთხე წამოიღებს 5 სიტყვას, "Giorg" - ის.

# ის მიუთითებს თუ საიდან უნდა დაიწყოს.
# ის მიუთითებს სადამდე უნდა იმუშაოს. 
# უარყოფითი ინდექსი მოდის უკნიდან.

# 2

#            0          1          2          3        4        5         6
cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Gori", "Zugdidi", "Poti"]
print(cities[2:7])

# 3

namee = input("Enter Your Name "  )
print(namee[2::])

# 4

nameee = input("Enter Your Name " )
if nameee[-1] == "ა":
    print(nameee[:-1])
else:
    print(nameee[1:])

# 5

password = input("Enter Your Password " )
if password[0] == "A":
    print("Correct")
else:
    print("Wrong")

# 6

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers[3:-1])