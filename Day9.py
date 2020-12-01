#excercise 1 lambda function that multiples two arguments
x=lambda a,b:a*b
print(x(2,3))
#excercise 2 Fibonnacci series 
from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1]) 
print(fib(10)) 
#excercise 3 multiply with list
list1=[10,54,32,14]
num=int(input("enter the number"))
print(list1)
z=list(map(lambda a:a*num,list1))
print(z)
#excercise 4
num=9
list2=[56,33,45,69,18,81,25,84]
o=list(filter(lambda a:(a%num==0),list2))
print(o)
#excercise 5
list3=[25,64,32,15,87,31,54,30,97,30]
count=0
p=len(list(filter(lambda a:(a%2==0),list3)))
print(p)