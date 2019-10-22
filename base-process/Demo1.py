happy = 0

while happy < 10:
    print("学习使我快乐，快乐 + 1，当前快乐值为：", happy)
    happy += 1

print("我不快乐了")


# happy = 0
#
# while True:
#     print("学习使大佬快乐，快乐 + 1，当前快乐值为：", happy)
#     happy += 1

for index in "Python":
    print(index)

for index in range(5):
    print(index)

for index in range(0, 10, 3):
    print(index)

happy = 0

while happy < 10:
    happy += 1
    if happy == 5:
        break
    print("学习使我快乐，快乐 + 1，当前快乐值为：", happy)

print("还是开黑更快乐一些~~~")

happy = 0

while happy < 10:
    happy += 1
    if happy == 5:
        continue
    print("学习使我快乐，快乐 + 1，当前快乐值为：", happy)

print("还是学习会更快乐~~~")