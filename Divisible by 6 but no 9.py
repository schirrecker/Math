c = 0

for i in range(100, 999):
    if i % 6 == 0 and i % 9 != 0:
        print("divisible: " + str(i))
        c += 1

print("The answer is: " + str(c))
