try:
    BinaryNum = bin(int(input("Enter a number: ")))
except ValueError:
    print("That is not a valid number")
else:
    print("The binary value of that number is " + BinaryNum)
    print("")
