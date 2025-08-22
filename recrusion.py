def countdown(n):
    if n==0:
        print("blast")
    else:
        print(n)
        countdown(n-1)
countdown(5)

def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))

def sum(n):
    if n==0:
        # print("1 base class")
        return 1
    else:
        return n+sum(n-1)
print(sum(6))


def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))



def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(6))