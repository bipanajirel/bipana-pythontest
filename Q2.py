#input from the user
def takeInput():
    number1 = int(input("Enter first number"))
    number2 = int(input("Enter second number"))
    operator = input("Enter operator (+,-,*,/)")
    print( number1,operator, number2, "=", displayResult(number1, number2, operator))
    
def displayResult(number1, number2, operator):
    
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    else:
        print("Invalid operator!")
        
takeInput()


    