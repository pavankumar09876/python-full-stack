#Defining & Declaring
# class pavan:
#     def __init__(self):
#         self.A=1200
#         self.B=1300
#         self.C=1400
#     def m1(self):
#         self.x="A"
#         self.y="B"
#         self.z="C"
#     @classmethod
#     def m2(self):
#         pass
#     @staticmethod
#     def m3():
#         pass
# t1=pavan()
# print(t1.__dict__)
# t1.m1()
# print(t1.__dict__)
# t1.c1="a"
# t1.c2="b"
# t1.c3="c"
# print(t1.__dict__)



#Accessing  & printing

# class pavan1:
#     def __init__(self):
#         self.A=1
#         self.B=2
#         self.C=3
#         print(self.A,self.B,self.C)
#     def m1(self):
#         self.x1="A"
#         self.x2="B"
#         self.x3="C"
#         print(self.x1,self.x2,self.x3)
# p1=pavan1()
# p1.m1()
# print(p1.__dict__)
# p1.a=101
# p1.b=102
# p1.c=103
# print(p1.a,p1.b,p1.c)
# print(p1.__dict__)


#Deleting an instance variable
# class pavan:
#     def __init__(self):
#         self.A=100
#         self.B=200
#         self.C=300
#         del self.A
#         del self.B
        
#     def m1(self):
#         self.x1=400
#         self.x2=500
#         self.x3=600
#     @classmethod
#     def m2(self):
#         pass
# p1=pavan()
# print(p1.__dict__)
# p1.m1()
# print(p1.__dict__)
# p1.m2()
# p1.d1=111
# p1.d2=122
# p1.d3=133
# del p1.d1
# del p1.d2
# print(p1.__dict__)


#updating an instance variable
# class pavan:
#     def __init__(self):
#         self.eid=100
#         print("eid is:",self.eid)
#     def m1(self):
#         self.eid=200
#         print("Eid is:",self.eid)
# i1=pavan()
# i1.m1()
# i1.eid=300
# print("Eid is",i1.eid)



# # static variable
# class pavan:
#     company="Cloud"
#     def __init__(self):
#         pass
#     def m1(self):
#         pass
# i1=pavan() 


# class pavan:
#     def __init__(self):
#         self.name="pavan"
#         self.s1=50
#         self.s2=60
#         self.s3=70
#     def m1(self):
#         print(self.name)
#         print(self.s1+self.s2+self.s3/3)
# i1=pavan()
# i1.m1()
# print(i1.__dict__)


# class pavan:
#     def __init__(self,name,s1,s2,s3):
#         self.name=name
#         self.s1=s1
#         self.s2=s2
#         self.s3=s3
#     def m1(self):
#         # print(self.name)
#         print(self.name,self.s1+self.s2+self.s3/3)
# i1=pavan("pavan",50,60,70)
# print(i1.__dict__)

# i1.m1()

# print()

# i2=pavan("Aakhil",60,70,80)
# print(i2.__dict__)
# i2.m1()



# class pavan:
#     company= "Cloudy"
#     def __init__(self):
#         pass
#     def m1(self):
#         pass
# i1=pavan()
# print(i1.company)


# class student:
#     company="infosis"
#     def __init__(self,name):
#         self.name=name
#     def m1(self):
#         return f"name {self.name},company: {student.company}"
# i1=student("Aakhil")
# i2=student("Pavan")
# print(i1.m1())
# print(i2.m1())
# print(i1.__dict__)
# print(i2.__dict__)
# print(student.company)
# student.company="tcl"
# print(student.company)
# i1.m1()
# i2.m1()
# print(i1.m1())
# print(i2.m1())


# class ihub:

#     def __init__(self):
#         ihub.a=10
#         ihub.b=20
#         print(ihub.a,ihub.b)
#     def m1(self):
#         ihub.c=30
#         print(ihub.c,ihub.a)
#     @classmethod
#     def m3(self):
#         ihub.u=60
#         print(ihub.u)
#     @staticmethod
#     def m2():
#         ihub.d=40
# i1=ihub()
# i1.m1()
# i1.m3()
# i1.h=80
# ihub.y=90
# print(i1.h,ihub.y)
# print(ihub.c)



class company1:
    def __init__(self):
        company1.company="Startup"
        print(company1.company)
    def m1(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
        print("Company :",company1.company)
        print (f" Name is {self.name}, age is {self.age}, and id is {self.id}")
i1=company1()
i1.m1("Aakhil",22,7802)
i1.m1("Pavan",22,4765)


class ihub:
    s1=100
    def __init__(self):
        self.s2=200 #Default variable
        s3=300
        print(ihub.s1) 
        print(self.s2)
        print(s3)  #Local variable
    def m1(self):
        print(ihub.s1)
        print(self.s2)
i1=ihub()
print("*")
i1.m1()
print()
print(i1.s2)
print("*")
print(ihub.s1)
