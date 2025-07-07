# Just adding the comments from testing Purpose
# Adding one more comment for testing Github Actions
import math

def basic_operations():
    print("\nChoose operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    
    choice = input("Enter choice (1-6): ")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Numbers required.")
        return
    
    result = None
    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
    elif choice == '5':
        result = num1 % num2
    elif choice == '6':
        result = num1 ** num2
    else:
        print("Invalid choice.")
        return

    print(f"Result: {result}")

def scientific_operations():
    print("\nChoose operation:")
    print("1. sin(x)")
    print("2. cos(x)")
    print("3. tan(x)")
    print("4. log(x) [base 10]")
    print("5. natural log (ln(x))")
    print("6. exp(x)")
    print("7. sqrt(x)")
    print("8. factorial(x)")
    
    choice = input("Enter choice (1-8): ")
    try:
        num = float(input("Enter number: "))
    except ValueError:
        print("Invalid input!")
        return

    result = None
    if choice == '1':
        result = math.sin(math.radians(num))
    elif choice == '2':
        result = math.cos(math.radians(num))
    elif choice == '3':
        result = math.tan(math.radians(num))
    elif choice == '4':
        if num > 0:
            result = math.log10(num)
        else:
            print("Logarithm undefined for <= 0.")
    elif choice == '5':
        if num > 0:
            result = math.log(num)
        else:
            print("Natural log undefined for <= 0.")
    elif choice == '6':
        result = math.exp(num)
    elif choice == '7':
        if num >= 0:
            result = math.sqrt(num)
        else:
            print("Square root of negative number is not real.")
    elif choice == '8':
        if num.is_integer() and num >= 0:
            result = math.factorial(int(num))
        else:
            print("Factorial only defined for non-negative integers.")
    else:
        print("Invalid choice.")
        return

    if result is not None:
        print(f"Result: {result}")

def calculator():
    print("🔢 Welcome to the Advanced Python Calculator!")
    while True:
        print("\nSelect Mode:")
        print("1. Basic Operations")
        print("2. Scientific Operations")
        print("3. Exit")

        mode = input("Enter choice (1-3): ")
        if mode == '1':
            basic_operations()
        elif mode == '2':
            scientific_operations()
        elif mode == '3':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    calculator()
