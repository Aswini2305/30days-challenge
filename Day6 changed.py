#excercise 1 loop through list
list1=[10,65,345,34,98]
for i in list1:
    i=i+2
    print(i)
#excercise 2 pattern
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
#excercise 3 fibannoci series
a=0
b=1
n=int(input("enter the range of the input"))
print(a)
print(b)
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)
#excercise 4 armstrong number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
#excercise 5 Multiplication table
num = 9
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

#excercise 6 negative or positive
num=int(input("enter the number"))
if(num>0):
    print("Positive number")
elif(num<0):
    print("Negative number")
else:
    print("Number is zero")
#excercise 7 convert days to age
day=int(input("enter number of days"))
if day>365:
    age=day/365
    print("the age is ",int(age))
elif day<365:
    print("the number of days are",day)
else:
    print("your input is wrong")
#excercise 8 trigonometric problem using math
import math 
a = math.pi/6
print ("The value of sine of pi/6 is : ", end="") 
print (math.sin(a)) 
print ("The value of cosine of pi/6 is : ", end="") 
print (math.cos(a))
#excercise 9 calculator
#excercise 1
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
choice=input("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")
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


