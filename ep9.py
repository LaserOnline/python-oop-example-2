
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person created: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        # * Call the constructor of the superclass (Person) to initialize its parts
        super().__init__(name, age)
        self.employee_id = employee_id
        print(f"Employee created: {self.name}, ID: {self.employee_id}")

# * สร้างอินสแตนซ์ของ Employee
emp = Employee("John Doe", 30, "E1234")