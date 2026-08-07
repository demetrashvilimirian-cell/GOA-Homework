# 1
# elif - ი არის დამატებითი პირობა,

# 2
number = int(input("Enter a Number "))
if number > 10:
    print("დიდია")
elif number == 10:
    print("ზუსტად 10-ია")
else:
    print("პატარაა")

# 3
num = int(input("Enter Any Number "))
if num > 0:
    if num % 2 == 0:
        print("დადებითია და არის ლუწი")
    elif num % 2 != 0:
        print("დადებითია და არის კენტი")
else:
    print("უარყოფითია")
