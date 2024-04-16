class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# Test cases
if __name__ == "__main__":
    # Create instances of Person
    person1 = Person(1, "John Doe")
    person2 = Person(2, "Jane Smith")

    # Create instances of Manager
    manager1 = Manager(3, "Alice Johnson", "HR Manager")
    manager2 = Manager(4, "Bob Brown", "Sales Manager")

    # Create instances of Employee
    employee1 = Employee(5, "Charlie Davis", "Python")
    employee2 = Employee(6, "Diana Evans", "JavaScript")

    # Print information
    person1.printInfo()
    person2.printInfo()
    manager1.printInfo()
    manager2.printInfo()
    employee1.printInfo()
    employee2.printInfo()

    # Additional test cases for Manager and Employee
    for i in range(7, 12):
        manager = Manager(i, f"Manager{i}", f"Title{i}")
        employee = Employee(i, f"Employee{i}", f"Skill{i}")
        manager.printInfo()
        employee.printInfo()
