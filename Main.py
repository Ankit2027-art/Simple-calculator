# Simple-calculator
# A simple Python calculator that performs basic arithmetic operations using match-case and handles invalid input with exception handling

try:
    a = int(input("Enter a First number:"))

    b = int(input("Enter a second number:"))

    print("What kind of opration can you Perform.\n Press + for Addition \n press - for Subtraction \n press * for Multiplication \n press / for division")

    o = input("Enter Opration:")

    match o:
        case "+":
            print(f"The result is:{a+b}")
        case "-":
            print(f"The result is:{a-b}")
        case "*":
            print(f"The result is:{a*b}")
        case "/":
            print(f"The result is:{a/b}")
        case _:
            print("Enter a valid Opration")


except Exception as e:
    print("Enter a valid value of a and b")
