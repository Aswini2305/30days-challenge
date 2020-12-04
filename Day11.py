#excercise 1 merged list of tuples from two lists
list1=["Python","java","cprogramming"]
list2=['1','2','3']
x=zip(list1,list2)
print(tuple(x))
#excercise 2 merge the given list and range to create new list of tuples
x=list(range(1,8))
y=['A','B','C','D','E','F','G','H']
Z=zip(x,y)
print(tuple(Z))
#excercise 3 sorted list 
list1=[21,8,65,1,7,32]
x=sorted(list1)
print(x)
#excercise 4 using filter function filter the even numbers 
def fun(num):
    if(num%2!=0):
        return True
    else:
        return False
seq=[31,46,36,54,16,63,9,42,81]
filtered_list=filter(fun,seq)
print("The filter  odd numbers are",list(filtered_list))
    