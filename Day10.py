#excercise 1 string contains(A-Z)(a-z)(0-9)
import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("Python_Exercises_1_ABC"))
print(text_match("BARking_DOG_seldom_bite"))
print(text_match("hello everyone "))
# excercise 2 find all 'ab'
import re
x="abaaababbabaab"
y=re.findall('ab',x)
print(y)
#excercise 3 find string end with number
import re
def num(string):
    text=re.compile(".*?[0-9]$")
    if(text.match(string)):
        print("True")
    else:
        print("False")
num('akhfio9')
num('aliefh8fh')
txt = "8 times before 11:45 AM"
x=re.match("[0-9]",txt)
print(x)
if x:
    print("match found")
else:
    print("match not found")
#excercise 4 find string end with numbers of length 3
import re 
result=re.finditer("([0-9]{1,3})","the numbers are 5864,6897,35,347,1")
for n in result:
    print(n.group(0))
#excercise 5 string contains only the uppercase charaters
import re
def define(text):
    pattern="^[A-Z].*?$"

    if re.search(pattern,text):
        print("match found")
    else:
        print("not match")
define("Barking dog Jumps over tHe LAZy doG")
define("dcnadhiwhf")
define("dknflw23548SDF")

