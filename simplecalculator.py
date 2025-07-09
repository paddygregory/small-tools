def calculator():
    print("welcome to the simple calculator!")
    print('enter two numbers and choose an operator to perform a calculation')
    while True:
        num1 = input('enter first number: ')
        num2 = input('enter second number: ')
        operator = input('enter an operator (+, -, *, /): ')
        if operator == '+':
            print(int(num1) + int(num2))
        elif operator == '-':
            print(int(num1) - int(num2))
        elif operator == '*':
            print(int(num1) * int(num2))
        elif operator == '/':
            print(int(num1) / int(num2))
        else:
            print('Invalid operator. Please try again.')


calculator()
