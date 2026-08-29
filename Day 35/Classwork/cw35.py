# 1

def greet(name = "Guest"):
    print("Hello,", name)
greet("gio")

# 2

def square(number = 2):
    print(number * number)
square(5)

# 3

def calculatePrice(price, discount = 0):
    print(price - discount)
calculatePrice(100,20)

# 4

def getGrade(score=0):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
print(getGrade(95))
