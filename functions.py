def pavan(name):
    print(f"Hello,{name}")
pavan("pavan11")

def m1(name,age,id): 
    print(name,age,id)
m1("pavan",22,123456)

def product():
    pid=int(input("Enter a id:"))
    pname=input("Enter a name:")
    price=int(input("Enter a price:"))
    # print(pid,pname,price)

    return "aakhil"
    
print(product())

def pavan1():
    name=input("Enter a name:")
    id=int(input("Enter a id:"))
    company=input("Enter a company:")
    return f"name: {name},ID:{id},Company:{company}"
print(pavan1())



def sum(a,b,c):
   return  a+b+c,a*b*c

print(sum(1,8,3))


def sum(a, b, c):
    print("Sum:", a + b + c)
    print("Product:", a * b * c)

sum(1, 2, 3)


def test(a,b):
    return(a+b,a-b,a*b)
print(test(5,5))
x1=test(5,5)
for i in x1:
    print(i)

def numbers(n):
    for i in range(1,n):
        print(i)
numbers(5)



def number(n):
    total=0
    for num in n:
        total+=num
    return total
print(number([1,2,3,4,5]))




def pavan():
    id=int(input("Enter a number:"))
    name=input("Enter a number:")
    phno=int(input("Enter a number:"))
    return id,name,phno
print(pavan())


def pavan(id,name,phno=37485):
    return id,name,phno
print(pavan(11,"pavan"))


def pavan(a,b,c):
    print("value of a:",a)
    print("value of b:",b)
    print("value of c",c)
    # print(a+b+c)
    return a+b+c
print(pavan(1,2,5))



def pavan(name,price,pid):
    print(pid,name,price)
pavan("pavan",98765,45667)

def pavan1(name,age,id=1223):
    print(id,name,age)
pavan1(12345,23,"pavan")


def default(name,age,id):
    print(id,name,age)
default("pavan",22,567)

def number(*pavan):
    return f"given values:{pavan} , sum:{sum(pavan)}"
    
print(number(1,2,3))

def test(*pavan):
    s=0
    for x in pavan:
        s+=x
    print("sum of arguments:",s)
test()
test(100)
test(100,200)
test(100,200,300)

import time
def pavan(*var):
    time.sleep(1)
    print(var)
pavan(100)
pavan(100,200)
pavan(100,200,300)


def pavan(**var):
    for x,y in var.items():
        print(x,":",y)
pavan(name="pavan",age=33,id=123456)


def pavan(**var):
    print(var)
pavan(name="pavan",age=33,id=123456)


def pavan1(*var):
    print(var)
print()
def pavan2(**var1):
    print(var1)
pavan1(name="pavan",id=1234,age=22)
pavan2(name="pavan",id=1234,age=22)

def pavan1(*var, **var1):
    print("Positional:", var)
    print("Keyword:", var1)

pavan1(10, 20, name="pavan", id=1234, age=22)

def pavan():
    s=0
    for i in range(1,10):
        s+=i
    print(s)
pavan()


def test1():
    print("pavan")
    def test2():
        print("Aakhil")
    test2()
test1()



def test():
    print(" BRo")
    def test1():
        print("Brooo")
    return test1
inner=test()
inner()

def test():
    print(" BRo")
    def test1():
        print("Brooo")
    return test1()
test()

def test_case1(name):
    print("name of language:",name)
    print()
    def test_case2(date,month,year):
        print("date of release is:{}/{}/{}".format(date,month,year))
    test_case2(7,8,2002)
test_case1("python")


import time
def test_case1(city):
    print( f"my city is:{city}")
    time.sleep(1)
    def test_case2(state):
        print(f"my state is :{state}")
    test_case2("Andhra")
    time.sleep(1)
    def test_case3(country):
        print(f"my country is:{country}")
    test_case3("India")
    time.sleep(1)
test_case1("Gudivada")

def outer(name):
    def inner():
        print(f"Hello, {name}!")
    inner()

outer("Pavan")

def math(num):
    def square(x):
        return x*x
    print("square:",square(num))
    def cude(x):
        return x**x
    print("Cude:",cude(num))
math(3)
    

# positional
def person1(name,age,id):
    print (f"The person name is {name} and age: {age} and company id: {id} ")
person1("pavan",22,1)
print("---")

# keyword
def person2(name,age,id):
    print(" The person name is {} and age: {} and company id: {}".format(name,age,id))
person2(name="pavan2",age=23,id=2)
print("----")

# Default
def person3(name,age=26,id=5):
    print(name,id,age)
person3("pavan2",24,3)
print("----")

# Variable Length arguments
# Positional variable length argument
def person4(*var):
    print(var)
person4(100)
person4(100,200)
person4(100,200,300)
print("-----")

# Keyword variable length arguments

def person5(**var1):
    print(var1.values())
person5(name="pavan",age=22,id=5)


total = 100  # Global

for i in range(3):  # i is local to the loop
    print("Inside loop: i =", i)

print("Outside loop: total =", total)
print(i)

