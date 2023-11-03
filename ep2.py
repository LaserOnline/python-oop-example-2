
# * constructor
class Employee:
    def __init__(self, message):
        # * ใช้ double underscore ทำให้เป็น private
        self.__message = message  
    
    def show(self):
        print(f"Message Data: {self.__message}")

emp = Employee("Hello")

emp.show()