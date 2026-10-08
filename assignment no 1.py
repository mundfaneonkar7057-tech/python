# Introduction to Python
# Simple Calculator

print("===== Python Calculator =====")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (**)")
    print("6. Modulus (%)")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        result = num1 + num2
        print("Addition =", result)

    elif choice == "2":
        result = num1 - num2
        print("Subtraction =", result)

    elif choice == "3":
        result = num1 * num2
        print("Multiplication =", result)

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Division =", result)

    elif choice == "5":
        result = num1 ** num2
        print("Exponentiation =", result)

    elif choice == "6":
        if num2 == 0:
            print("Error: Cannot find modulus with zero.")
        else:
            result = num1 % num2
            print("Modulus =", result)

    else:
        print("Invalid choice. Please select 1 to 6.")

except ValueError:
    print("Invalid input! Please enter numbers only.")

except Exception as e:
    print("An error occurred:", e)