A=['a','b','c']
B=['1','2','3','4','5']
print(A[1])
print(B[2:4])
print(B[-1])
#add an item to the list
x=A.append('V')
print(A)
#extend the list
y=A.extend(B)
print(A)
#insert or delete  an item  in given index
z=B.insert(3,'6')
print(B)
del B[4]
print(B)
A.remove('c')
print(A)
#excercise 1
l=['10','26','65','24']
m=l.append('54')
print(l)
print(l.pop(0))
print(min(l))
print(max(l))
#excercise 2
n=('10','guava','34.56')
o=reversed(n)
print(tuple(o))
#excercise 3
p=list(n)
print(type(p))
print(p)