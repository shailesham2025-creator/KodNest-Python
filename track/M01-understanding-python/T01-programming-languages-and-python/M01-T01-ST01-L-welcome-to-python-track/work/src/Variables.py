name = "shailesh"
age =  21
print(name)
print(id(name))
print(type(name))

print("hello python", end=" - ")
print("thank you python")

print("hello python\nthank you python")

# My name is shailesh and age is 21 
print("My name is " + name + " age is " , age)
print("My name is " + name + " age is "+ str(age))

#String Formating ()f strings
print(f"My name is {name} and age is {age}")


a=10
b=20
c=30
# a, b, c = 10,20,30
# print(a + b + c)
a=b=c=10
print(a+b+c)

a,b,c="shaii","pannag","chani"
print(b)
print(a+b+c)

x,y,z= 30,4,8
print(x+z)
print(a+str(x))
print(a,x)


a=10
print(type(a),a)


#local variable


def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# global variable

x = 300
def myfunc():
    y = 10
    x = 200
    print(x,y)
    x = x+1
    y = y+1
    print(x,y)
myfunc()
