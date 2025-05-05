try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print("Enter the required operation:\n1. For Addition +\n2. For Subtraction -\n3. For Multiplication *\n4. For Division\\")

    o = input("Enter the operation: ")

    if o == '+':
        print(f"The sum of {a} and {b} is: {a + b}")
    elif o == '-':
        print(f"The difference of {a} and {b} is: {a - b}") 
    elif o == '*':
        print(f"The product of {a} and {b} is: {a * b}")
    elif o == '/':
        if b != 0:
            print(f"The quotient of {a} and {b} is: {a / b}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, or /.")
except Exception as e:
    print(f"An error occurred: {e}")