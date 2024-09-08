

print('===============String================')
# test01

print("sachini")


print('===============if-else================')
 # test02 --> if-else

a,b = 1,3
if a>b :
 print("a is greater than b")
else:
    print("b is greater than or equal to a")

print('===============data type================')
# test03

mystring = "hallow"
myfloat = 10.5
myint= 20

if mystring:
    print("String: %s" % mystring)
    print("String" + mystring)

if isinstance(myfloat,float) and myfloat == 10.5:
    print("Float: %f" % myfloat )

if isinstance(myint,int) and myint == 20:
     print("Int: %i" % myint)

print('===============for loop================')
  # test04 - for loop

fruits= ["apple","mango"]
for x in fruits:
    print(x)

    # while loop
print('===============while================')

i = 1
while i < 6:
    print(i)
    i += 1

# array
print('===============array================')

fruits = ['orange', 'apple', 'mango']
print(fruits)
print(type(fruits))

# functions
print('===============function================')



def my_function():
    print("Hello from a function")
my_function()

# test06

def count(x,y):
    print(x*y)
    count(10,5)

    # test07
def count_num(a,b):
 return (a*b)

print(count_num(10,5))

print('===============type conversions================')
#type conversions
int("10")
float('10.1')
str(19)
state=bool("True")
print(state)

print('===============the type String================')
#the type String
my_name='Sachini Apsara'
my_name.capitalize()

print('===============get keyboard input================')
#get keyboard input
my_First_Name=input("Input Your First Name : ")
print(my_First_Name)

# Taking user inputs for name, age, and weight
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))

# Printing the inputs
print("name:", name)
print("age:", age)
print("weight:", weight)
print("=================")





