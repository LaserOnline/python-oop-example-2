
# * Destructor
class MyClass:
    def __init__(self):
        print("Hello Python Programming")

    def __del__(self):
        print("Remove Object")


m = MyClass()