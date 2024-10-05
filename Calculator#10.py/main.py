from art import logo

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def calculator():
    print(logo)
    n1=float(input("Enter your number:-"))
    operation={
        "+":add,
        "*":multiply,
        "/":div,
        "-":sub
    }
    for i in operation:
        print(i)


    flow=True
    while flow==True:
        operation_symbol=input("Enter the operation from above:-")
        n2=float(input("Whats the next number?: "))
        cal=operation[operation_symbol]
        ans=cal(n1,n2)
        print(f"{n1}{operation_symbol}{n2}={ans}")
        a=input("Enter 'y' to continue calculating with {ans}, or type 'n' to start a new calculation and 'e' to exit: ")
        if a=="y":
            num1=ans
        elif a=="e":
            print("Goodbye!!!!!!!")
            flow=False
        else:
            flow=False
            calculator()
calculator()

