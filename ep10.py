
# * Don’t Repeat Yourself
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person created: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        # * โค้ดซ้ำ - ควรใช้ super() แทนการตั้งค่า name และ age อีกครั้ง
        self.name = name
        self.age = age
        self.employee_id = employee_id
        print(f"Employee created: {self.name}, ID: {self.employee_id}")

emp = Employee("John Doe", 30, "E1234")
