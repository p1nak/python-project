# CLI

def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b  # this line is watched for ZeroDivisionError
        elif op == "%":
            return a % b
        elif op == "**":
            return a ** b
        else:
            return "Invalid operator"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def main():
    while True:
        a = float(input("enter first number : "))
        op = (input("enter operations like( + , - , / , * ,... ) : "))
        b = float(input("enter second number : "))

        result = calculate(a,b,op)
        print("Result:", result)

        choice = input("Do you want to calculate again? (y/n): ").lower()
        if choice != 'y':
            print("Goodbye! 👋")
            break  # exit the loop

if __name__ == "__main__":
    main()
