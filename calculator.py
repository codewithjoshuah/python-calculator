print("Welcome to the Calculator")
print("Select any operation of your choice from the list below -")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = input("Enter the serial number of your desired operation - ")
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter the first number - "))
    num2 = float(input("Enter the second number - "))


    if choice == '1':
        print(num1 + num2)
    elif choice == '2':
        print(num1-num2)
    elif choice == '3':
        print(num1*num2)
    elif choice == '4':
        if num2 != 0:
            print(f"Result =", num1/num2)
        else:
            print("Error")
