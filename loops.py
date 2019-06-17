colors = ["red", "green", "blue", "orange", "pink", "yellow"]
count = 0
for color in colors:
    print(color)

while count < 10:
    print(color[count])
    count++

number_list = [x for x in range(10)]
print(number_list)

number_list2 = [x for x in range(10) if x % 2 == 0]
print(number_list)