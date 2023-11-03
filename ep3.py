
class Employee:
    def __init__(self):
        self.__message = None

    def printer(self,message):
        # * เรียกฟังชัน ของ object ตัวเอง
        self.update(message)
        print(f"Data {self.__message}")

    def update(self,message :str):
        self.__message = message
        return self.__message

emp = Employee()

emp.printer("JoJo")