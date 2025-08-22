# class car:
#     print("Car implementation")
#     class engine:
#         print("engine emplementation")
#         def service(self):
#             print("services")
# i1=car()
# i2=i1.engine()
# i2.service()
# i1=car().engine().service()


class employee:
    def __init__(self):
        self.name="Pavan"
        self.doj=employee.Doj()
    def m1(self):
        print("Name of employe",self.name)
        self.doj.m2()
    class Doj:
        def __init__(self):
            self.date=7
            self.month=8
            self.year=2002
        def m2(self):
            print(" Date of joining:{}/{}/{}".format(self.date,self.month,self.year))
i1=employee()
i1.m1()
