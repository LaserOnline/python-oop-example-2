
class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} แมว"

class Dog(Animal):
    def speak(self):
        return f"{self.name} หมา"

# * สร้างอ็อบเจ็กต์จากคลาสต่าง ๆ
dog = Dog("มิว")
cat = Cat("ดัค")

animals = [dog,cat]
# * ใช้ Polymorphism ในการเรียกเมทอด speak ของอ็อบเจ็กต์ต่าง ๆ
for i in animals:
    print(i.speak())