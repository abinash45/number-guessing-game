
def calculator():
    print(" Welcome to the Python Calculator! ")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            # Take user input
            choice = input("Enter choice (1/2/3/4 or q to quit): ")

            if choice.lower() == 'q':
                print("👋 Exiting Calculator. Goodbye!")
                break

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"✅ Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"✅ Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"✅ Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"✅ Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid input! Please choose 1, 2, 3, 4, or q.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the calculator
if __name__ == "__main__":
    calculator()
