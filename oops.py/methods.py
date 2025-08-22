# class pavan:
#     def __init__(self):
#         print("Constructor")
# i1=pavan()

# class x1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#         print(self.a+self.b)
# i1=x1()

# class x2:
#     def __init__(m):
#         m.a=2
#         m.b=2
#         print(m.a*m.b)
# i2=x2()

# class pavan3:
#     def __init__(self):
#         print("Constructor")
# i1=pavan3()

# class pavan2:
#     def m1(self):
#         print("Instance")
# i3=pavan2()
# i3.m1()

# class pavan2:
#     def m1(m):
#         print("Instance")
# i3=pavan2()
# i3.m1()

# class pavan2:
#     @classmethod
#     def m1(self):
#         print("classmethod")
# obj=pavan2()
# obj.m1()
# pavan2.m1()


# class pavan4:
#     @staticmethod
#     def m4():
#         print("Static method")
# i1=pavan4()
# pavan4.m4()

# class pavan:
#     @staticmethod
#     def m1(x1,x2,x3):
#         print(x1+x2+x3)
# i1=pavan()
# pavan.m1(100,200,300)




class pavan:
    def __init__(m):
        print("Constructor")
    def func_name1(n):
        print("Instance")
    @classmethod
    def func_name2(self):
        print("classmethod")
    @staticmethod
    def func_name3():
        print("Static")
    def func_name5(n):
        print("Instance")
obj=pavan() #constructor
obj.func_name1()  #instance
obj.func_name2()   #classmethod
pavan.func_name2()  #classmethod
obj.func_name3()    #staticmethod
pavan.func_name3()    #staticmethod
obj.func_name5()
