#                                                                                       1

# 1. ფუნქცია არის ჩვეულებრივი შორთქათი (shortcut).

# 2. def

# 3. Argument არის ინფორმაცია, რომელსაც ფუნქციას აძლევ, რომ თავისი საქმე გააკეთოს.

# 4. Parameter არის მაგალითად def example(x) < --- x რო წერია ეგ არის Parameter.

# 5. return აბრუნებს შედეგს.

# 6. print აჩვენებს და return ინახავს და აბრუნებს. 

# 7. დავწერთ ბოლოში ფუნქციის სახელს, და ფრჩხილებს გვერდით.

#                                                                                      2

def findMax(a, b):
    if a > b:
        print(a)
    else:
        print(b)
findMax(5, 10)

#                                                                                      3 

def checkNumber(number):
    if number % 2 == 0:
        print("ლუწია")
    else:
        print("კენტია")
checkNumber(50)

#                                                                                      4

def checkAge(age):
    if age >= 18:
        print("შეგიძლია შესვლა")
    else:
        print("შესვლა აკრძალულია")
checkAge(12)