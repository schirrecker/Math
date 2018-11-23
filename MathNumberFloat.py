ValidNumber = False

while not ValidNumber:
    try:
        a = float(input("Enter a number: "))
        ValidNumber = True
    except ValueError:
        print("You entered an invalid number, try again.")
        ValidNumber = False
print(a)
