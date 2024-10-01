#CodSoft Task 2 - Simple Calculator
#Code for the Simple Calculator

print("CALCULATOR \n")
def show():
    print("Choose the operation to perform \n")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print("5. Modulus/Remainder(%)")


print("Enter two numbers -")
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
show()
op=input("\nEnter arithmetic symbol : ")
match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '%':
        print(a%b)
    case _:
        print('Enter the correct option')

        
        




