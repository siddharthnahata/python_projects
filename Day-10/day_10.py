def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiple(x, y):
    return x * y

def divide(x, y):
    return x / y

mathmatical_operation = {
    "+": add,
    "-": sub,
    "*": multiple,
    "/": divide
    }


def calculator():
    re_operate = True
    n1 = float(input("What is the first number: "))
    
    while re_operate:
       
        for symbol in mathmatical_operation:
            print(symbol)
        operation = input("Please enter the following: ")
        n2 = float(input("Please enter the secound number: "))
        answer = mathmatical_operation[operation](n1, n2)
        print(answer)
        
        further_cal = input("do you want to further calculate with result or with new nums. y/n? ").lower()
        if further_cal == "y":
            n1 = answer
        else:
            print("\n"*20)
            re_operate = False
            calculator()

calculator()