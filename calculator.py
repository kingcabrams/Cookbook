def main():
    num_one = int(input("Enter a number: "))
    print("Enter an operator: ")
    print("'+' for addition")
    print("'-' for subtraction")
    print("'*' for multiplication")
    print("'/' for division")
    print("'**' for exponents")
    print("'%' for remainder division")
    operator = input()

    num_two = int(input("Enter a second number: "))

    if operator == "+":
        print(num_one + num_two)  # Integer addition
    elif operator == "-":
        print(num_one - num_two)  # Integer subtraction
    elif operator == "*":
        print(num_one * num_two)  # Integer multiplication
    elif operator == "/":
        print(num_one / num_two)  # Integer division
    elif operator == "**":
        print(num_one**num_two)  # Integer exponents
    else:
        print(num_one % num_two)  # Remainder division


main()
