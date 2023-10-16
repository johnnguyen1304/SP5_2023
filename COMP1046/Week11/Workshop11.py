from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, firstName, lastName, employeeID):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__employeeID = employeeID
        self.salary = 0
    @abstractmethod
    def setSalary(self, salary):
        pass
    
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getEmployeeID(self):
        return self.__employeeID
    
    @abstractmethod
    def getInformation(self):
        pass

class TeachingStaff(Employee):
    def __init__(self, firstName, lastName, employeeID, teachingArea, category):
        super().__init__(firstName, lastName, employeeID)
        self.teachingArea = teachingArea
        self.category = 0
        #Potential TypeError if category is not an integer
        try:
            if 1<= category <= 5:
                self.category = category
            else:
                print("Error: The category of a teaching staff must be between 1 and 5.")
        except TypeError:
            print("Type Error: The category attribute must be a number")    
    
    def setSalary(self, newSalary):
        self.salary += ((self.category *10) + newSalary)
    
    def getInformation(self): 
        try: 
            info = "-Staff Information-\nID: " + self.getEmployeeID() + "\nName: " + self.getFirstName() + \
        " " + self.getLastName() + "nArea of Expertise: " + self.teachingArea + "\nCategory: " \
+ self.category + "\nSalary: " + self.salary
            print(info) 
        except TypeError : 
            return "Type Error: One of the Teaching Staff attributes is not a string."
        #potential type error : this line may rise a TypeError when trying to perform arithmetic operations


class AdministrativeStaff(Employee):
    def __init__(self, firstName, lastName, employeeID, level):
        super().__init__(firstName, lastName, employeeID)
        self.level = 0
        #Potential TypeError if level is not an integer
        if level >= 1 and level <= 3:
            self.level = level
        else:
            print("Error: The level of an administrative staff must be between 1 and 3.")
    
    def setSalary(self, newSalary):
        self.salary += ((self.level * 15) + newSalary)
        #potential type error : this line may rise a TypeError when trying to perform arithmetic operations


    def getInformation(self):
        #Potential TypeError: this line may rise a TypeError if salary is not a string, or level is not a string
        return "-Staff Information-\nID: " + self.getEmployeeID() + "\nName: " + self.getFirstName() + \
" " + self.getLastName() + "\nLevel:" + self.level + "\nSalary:" + self.salary


teacherA = TeachingStaff(1, "Dallas", 991074, "Law", "4")
teacherA.setSalary(30000)
print(teacherA.getInformation())
print("This message should appear on your screen.")
teacherB = TeachingStaff("Leeloo", "Dallas", 10095912, "English", 5)
teacherB.setSalary(22500)
print(teacherB.getInformation())
print("This message should appear if exceptions are all handled correctly.")