class Student:
    def __init__(self):
        
        self.__name = ""
        self.__rollNumber = ""

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber


student = Student()
name = input("Enter student name :")
rollno = int(input(f"Enter roll number of {name}:"))

student.setName(name)
student.setRollNumber(rollno)

print("Name:", student.getName())
print("Roll Number:", student.getRollNumber())
