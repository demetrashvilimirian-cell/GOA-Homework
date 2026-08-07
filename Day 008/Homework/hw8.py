#1
text = "123" #string
number = int(text)
print(number)
print(type(number))

#2
text_number = "3.7"
text_float = float(text_number)
num = int(text_float)
print(type(text_float))
print(type(num))

#3
age = "25"
if type(age) == str :
    age = int(age)
print(type(age))

#4
a = input("შემოიყვანეთ რიცხვი:")
b = input("შემოიყვანეთ მეორე რიცხვი:")
c = int(a)
d = int(b)
print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c//d)


