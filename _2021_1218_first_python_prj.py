print("Hello VScode")

stu = {'jim': 1, 'tom': 2, 'kate': 3}
for key in stu.keys():
    print(key, stu[key])

x = 3
y = x**2
print(y)
b = 0
print(x if b > 0 else y**2)

# for num in range(1, 101):
#     print(num)

for num in range(1, 101):
    if num % 5 == 0:
        print(num)

# score = input("輸入分數：")
# print(score)