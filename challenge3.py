
class Student:
    def __init__(self,name, rollNumber):
        self.__name = name
        self.__rollNumber = rollNumber
    #def setname(self,x):
        #self.__name = x
    def  stud_name(self):
        return self.__name
    #def setrollNumber(self,y):
        self.__rollNumber = y
    #def getrollNumber(self):
        return self.__rollNumber
obj = Student("Shweta", 1234)
print(obj.stud_name())
#obj.setname("Shweta")   
#obj.setrollNumber(12456)
#print(obj.getname())
#print(obj.getrollNumber())