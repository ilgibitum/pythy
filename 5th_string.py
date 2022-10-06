# f = open("5th_string.txt").read().split('\n')[4]
# print("Пятая строчка:", f)


with open("5th_string.txt") as f:
    for index, line in enumerate(f):
        if index == 4:
            a = line
            break
print("The fifth string is ", a)