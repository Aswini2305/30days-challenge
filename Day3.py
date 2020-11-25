#Assigning the dictionary
captials={"Tamilnadu":"Chennai","Andhrapradesh":"Chitoor","Telgana":"Hyderbad"}
#print from dictionary
print(captials['Andhrapradesh'])
#adding new value 
captials['karnataka']='Bangalore'
print(captials)
#delete or remove key from  the dictionary
del captials['Telgana']
#using fromkeys
x={"guava","banana","apple","orange"}
y="Fruits"
dic=dict.fromkeys(x,y)
print(dic)
#using get method
z=captials.get('karnataka')
print(z)
#using items method
print(captials.items())
#merge two python dictionaries
dict1={"orange":"1","grapes":"2","guava":"3"}
dict2={"Custardapple":"4","apple":"5","banana":"6"}
dict1.update(dict2)
print(dict1)
#map two lists into a dictionary
i=['blue','orange','pink']
j=['0','1','2']
k=dict(zip(i,j))
print(k)
student={"1","2","4","8"}
teacher={"4","5","2","6"}
#print the length of set
print(len(student))
#remove the intersection of 2nd set from the 1st set
print(student-teacher)