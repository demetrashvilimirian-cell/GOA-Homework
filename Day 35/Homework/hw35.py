# 1

# return აბრუნებს, და Default პარამეტრი არის ფუნქციის ცვლადი.

# 2

def welcome(name = "Guest", age = 18):
    if age >= 18:
        return "Welcome, " + name + "!"
    else:
        return "Hi, " + name + "!"
print(welcome("მირიან", 12))

# 3

def checkNumber(number = 12):
    if number > 0:
        return"Positive"
    elif number < 0:
        return"Negative"
    else:
        return"Zero"
print(checkNumber())

# 4

def sum(a = 6, b = 6):
    return a + b
print(sum())

# 5

def calculator(a, b, operator = "+"):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
print(calculator(10,5,"*"))

# 6




