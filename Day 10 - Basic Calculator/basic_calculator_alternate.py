from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# keys are operators and values are function names
operations_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    print(logo)
    first_number = float(input("What's the first number? "))

    # can use the below loop with results from previous calculations
    calculating = True
    while calculating:

        for symbol in operations_dictionary:
            print(symbol)
        operator = input("Pick an operation: ")
        second_number = float(input("What's the next number? "))
        result = operations_dictionary[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")

        continue_calculations = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or 'e' to exit ").lower()

        if continue_calculations == "y":

            # continue with previous result
            first_number = result

        elif continue_calculations == "n":

            # start new calculations
            print("\n" * 20)
            calculator()
            break # breaks recursion

        else:
            # terminates the program
            calculating = False

calculator()