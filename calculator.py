try:
    user = int(input("Enter first number: "))
    user2 = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")    
    if operation == "+":
        result = user + user2
    elif operation == "-":
        result = user - user2       
    elif operation == "*":
         result = user * user2
    elif operation == "/":
         if user2 != 0:
            result = user / user2
         else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Error: Invalid operation."
        print(result)
    print(f"The result is {result}")

except ValueError:
    print("Error: Please enter valid numbers.")

 


