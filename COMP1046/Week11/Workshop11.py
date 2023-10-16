from abc import ABC, abstractmethod

class InvalidLevelError(Exception):
    pass

class InvalidCategoryError(Exception):
    pass

class Employee(ABC):

    # No potential error
    def __init__(self, firstName, lastName, employeeID):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__employeeID = employeeID
        self.salary = 0

    # No potential error
    @abstractmethod
    def setSalary(self, salary):
        pass

    # No potential error
    def getFirstName(self):
        return self.__firstName

    # No potential error
    def getLastName(self):
        return self.__lastName

    # No potential error
    def getEmployeeID(self):
        return self.__employeeID

    # No potential error
    @abstractmethod
    def getInformation(self):
        pass


class TeachingStaff(Employee):

    def __init__(self, firstName, lastName, employeeID, teachingArea, category):
        super().__init__(firstName, lastName, employeeID)
        self.teachingArea = teachingArea

        # Potential type error
        self.category = 0
        try:
            if category >= 1 and category <= 5:
                self.category = category
            else:
                raise InvalidCategoryError("The category of a teaching staff must be between 1 and 5.")
        except TypeError:
            print("Type Error: The category attribute must be a number.")

    # Potential type error
    def setSalary(self, newSalary):
        try:
            self.salary += ((self.category * 10) + newSalary)
        except TypeError:
            print('Type Error: The salary argument must be a number.')

    # Potential type error at self.getEmployeeID() and self.category, potential syntax error
    def getInformation(self):
        try:
            return "-Staff Information-\nID: " + self.getEmployeeID() + "\nName: " + self.getFirstName() + \
            " " + self.getLastName() + "nArea of Expertise: " + self.teachingArea + "\nCategory: " \
                + self.category + "\nSalary: " + self.salary
        except TypeError:
            return 'Type Error: One of the Teaching Staff attributes is not a string. (All attributes must be converted into strings when using concatenation)'


class AdministrativeStaff(Employee):

    def __init__(self, firstName, lastName, employeeID, level):
        super().__init__(firstName, lastName, employeeID)

        self.level = 0

        # Potential type error
        try:
            if level >= 1 and level <= 3:
                self.level = level
            else:
                raise InvalidLevelError("The level of an administrative staff must be between 1 and 3.")
        except TypeError:
            print('Type Error: The level attribute must be a number.')

    # Potential type error and attribute error
    def setSalary(self, newSalary):
        try:
            self.salary += ((self.level * 15) + newSalary)
        except TypeError:
            print('Type Error: The salary argument must be a number.')

    # Potential type error at self.getEmployeeID() and self.level
    def getInformation(self):
        try:
            return "-Staff Information-\nID: " + self.getEmployeeID() + "\nName: " + self.getFirstName() + \
                " " + self.getLastName() + "\nLevel:" + self.level + "\nSalary:" + self.salary
        except TypeError:
            return "Type Error: One of the Administrative Staff attributes is not a string. (All attributes must be converted into strings when using concatenation)"


# Testing Part

# teacherA = TeachingStaff(1, "Dallas", 991074, "Law", "4") 
# teacherA.setSalary(30000) 
# print(teacherA.getInformation())
# print("This message should appear on your screen.") 
# teacherB = TeachingStaff("Leeloo", "Dallas", 10095912, "English", 5) 
# teacherB.setSalary(22500) 
# print(teacherB.getInformation())
# print("This message should appear if exceptions are all handled correctly.")

try:
    teacherB = TeachingStaff("Leeloo", "Dallas", 10095912, "English", 11) 
    teacherB.setSalary(22500) 
    print(teacherB.getInformation())
    print("This line should not be printed on the screen if exception is not handled.")
except InvalidCategoryError:
    print("Error: The category of a teaching staff must be between 1 and 5.")

try:
    adminB = AdministrativeStaff("Ruby", "Rhod", "10095518", -1) 
    print(adminB.getInformation())
    adminB.setSalary(11100) 
    print("This line should also not be printed on the screen if exception is not handled.") 
except InvalidLevelError:
    print("Error: The level of an administrative staff must be between 1 and 3.")