#excercise
A=int(input("Enter the first number"))
B=int(input("enter the second number"))
def add(A,B):
    return A+B
def sub(A,B):
    return A-B
def mul(A,B):
    return A*B
def div(A,B):
    return A/B
print("Addition",add(A,B))
print("Subtraction",sub(A,B))
print("Multiplication",mul(A,B))
print("Division",div(A,B))
name=input("enter the nameof the patient")
temp=int(input("enter the temperature"))
def funct():
    if(temp>=98):
        def covid(name,temp):
            print("Your name is",name)
            print("Your temperature is",temp)
        covid(name,temp)
funct()