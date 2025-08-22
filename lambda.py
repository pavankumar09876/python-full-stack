max=lambda a,b:a if a>b else b
min=lambda a,b:a if a<b else b
print(max(100,200))
print(min(1,3))

a=5
square=lambda x: x**a
print(square(2))

numbers = [1, 2, 3, 4]
squares = tuple(map(lambda x: x**2, numbers))
print(squares)

words=["Veda","Teja","harathi"]
upper1=list(map(lambda x:x.upper(),words))
print(upper1)

number=[1,2,3,4]
convert=tuple(map(str,number))
print(convert)



number=1,2,3,4,5,6,7,8,9
even=tuple((filter(lambda x:x%2==0,number)))
print(even)

word=["apple","banana","pineapple","kiwi"]
longword=list(filter(lambda x:len(x)>5,word))
print(longword)

number=[-4,-3,-2,-1,0,1,2,3,4]
negative=list(filter(lambda x:x>=0,number))
print(negative)

name=["Aakhil","pavan","aple","banana"]
a=list(filter(lambda x:x.startswith("A"),name))
print(a)

d1={"name":"pavan","id":123,"company":"limited solutions"}
def m1():
    for x in d1.keys():
        print(x)
def m2():
    for x in d1.items():
        print(x)

m1()
m2()

def m3():
    l=[1,2,3,4]
    for i in l:
        print(l)
    for x in d1.values():
        print(x)
m3()


s=(1,2,3,4,5,6,7,8,9,10)
s1 = list(map(lambda x:x if x%2==0 else x+1,s))
print(s1)


#Double each number in the list
number = [1,2,3,4,5,6,7,8]
p = list(map(lambda x:x*2 ,number))
p1=list(map(lambda x:x+x,number))
print(p1)
print(p)


name=["aakhil","pavan","bhaskar"]
upper=list(map(lambda x:x.capitalize(),name))
print(upper)


number=("apple","pavan","aakhil")
lenght=list(map(lambda x:len(x),number))
print(lenght)


n=[1, 3, 5, 7]
s=list(map(lambda x:x*2,n))
print(s)


# Keep only even numbers
n=[1,2,3,4,5,6,7,8,9,10]
s=list(filter(lambda x:x%2==0,n))
print(s)


#  Filter words with more than 5 letters
names= ["apple", "banana", "kiwi", "cherry", "mango"]
s=list(filter(lambda name:len(name)>5,names))
print(s)


# Keep only positive numbers
name=[-4,-3,-2,-1,0,1,2,3,4]
p=list(filter(lambda x:x > 0,name))
print(p)


# Filter strings starting with a vowel
words = ["apple", "orange", "banana", "umbrella", "grape"]
z=list(filter(lambda x:x[0] in "AEIOUaeiou",words))
print(z)


# Filter strings starting with a vowel
words = ["apple", "orange", "banana", "umbrella", "grape"]
z=list(filter(lambda x:x[0].lower() in "aeiou",words))
print(z)



#  Keep numbers divisible by 3
num=[3, 4, 6, 8, 9, 12, 15]
a=list(filter(lambda x:x%3==0,num))
print(a)


# Reduce
#  Sum of a List
from functools import reduce
number=[1,2,3,4,5,6,7,8]
numbers=reduce(lambda x,y:x+y,number)
print(numbers)

# Product of a List
num=reduce(lambda x,y:x*y,number)
print(num)

# . Maximum Number in a List
numb=reduce(lambda x,y: x if x>y else y,number)
print(numb)


# Concatenate Strings
words = ["Python", "is", "fun"]
numbe=reduce(lambda x,y:x+" "+y,words)
print(numbe)

# Sum of Squares
num1=reduce(lambda x,y:x+y**2,number)
print(num1)


