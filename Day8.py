#excercise 1 some type of try and exceptions
#assert error
x=0
y=1
assert y!=1, "y is 0"
#environment error
import sys
try:
    file=open("environment","r")
except EnvironmentError:
    print("file not found")
#excercise 2
try:
    A=int(input("Enter the first number"))
    B=int(input("enter the second number"))
except:
    print("Enter only the numeric datatype")
  
try:
    def add(A,B):
        return A+B
except FloatingPointError:
    print("invalid number")
except ArithmeticError:
    print("error occured")
except OverflowError:
    print("exceeds the maximum limit")
except TypeError:
    print("enter the correct datatype")
except ValueError:
    print("enter the correct value")
try:
    def sub(A,B):
        return A-B
except FloatingPointError:
    print("invalid number")
except ArithmeticError:
    print("error occured")
except OverflowError:
    print("exceeds the maximum limit")
except TypeError:
    print("enter the correct datatype")
except ValueError:
    print("enter the correct value")
try:
    def mul(A,B):
        return A*B
except FloatingPointError:
    print("invalid number")
except ArithmeticError:
    print("error occured")
except OverflowError:
    print("exceeds the maximum limit")
except TypeError:
    print("enter the correct datatype")
except ValueError:
    print("enter the correct value")
try:
    def div(A,B):
        return A/B
except ZeroDivisionError:
    print("Division by zero")
except OverflowError:
    print("exceeds the maximum limit")
except FloatingPointError:
    print("invalid number")
except ArithmeticError:
    print("error occured")
except OverflowError:
    print("exceeds the maximum limit")
except TypeError:
    print("enter the correct datatype")
except ValueError:
    print("enter the correct value")

try:
    choice=input("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")
except:
    print("enter only the numeric value")

if choice =='1':
    print("Addition",add(A,B))
elif choice =='2':
    print("Subtraction",sub(A,B))
elif choice =='3':
    print("Multiplication",mul(A,B))
elif choice =='4':
    print("Division",div(A,B))
else:
    print("enter the correct choice")

#excercise 3
try:
    print(x)
except NameError:
    print("X is not defined")
except:
    print("something went wrong")

#excercise 5
try:
    a=int(input("enter the number"))
    print("inside the try block")
except:
    b=input("enter the number")
    print("in the except block")
