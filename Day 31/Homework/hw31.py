# 1

favorite_hobby = ["Fishing", "Programming", "Boxing",]
print(len(favorite_hobby))

# 2

favorite_hobby.append("CSGO")
print(favorite_hobby)

# 3

favorite_hobby.insert(0,"Minecraft")
print(favorite_hobby)

# 4

removed_game = ["CSGO"]
favorite_hobby.pop(4)
print("წაშლილი ელემენტია", removed_game)

# 5

fruits = ["apple", 93, "bannana",  23, "mango", True, 15, False, 3.1, "Hello World!"]
res = []
for i in fruits:
    if type(i) == int:
        res.append(i)
print(res)

# 6

words = ["cat", "elephant", "dog", "hippopotamus", "ox", "python", "a"]
result = []
for ii in words:
    if len(ii) > 3:
        result.append(ii)
print(result)

# 7

data = [12, "15", 8.5, "text", 30, None, 7, True, 45]

sum_numbers = 0
count = 0

for i in data:
    if type(i) == int or type(i) == float:
        sum_numbers += i
        count += 1


print(sum_numbers)

print(sum_numbers / count)

# 8

nums = [4, 7, 12, 3.5, "9", 21, 8, "eleven", 16, 0]

odd = []
even = []


for i in nums:
    if type(i) == int:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
print(even)