num_1 = int(input("Enter a number: "))
p = 0
num_1 += 1
for i in range(2, int(num_1 ** 0.5) + 2):
    if num_1 % i == 0:
        p = 0
        break
    else:
        p = 1
if p == 1:
    print(num_1, " is the next Prime number")
else:
    print(num_1, " the only Prime number")

