
# * Multiple Inheritance

class A:
    def hello(self):
        print("Method A")

    def __die__(self):
        print("Remove")

class B(A):
    def hello(self):
        print("Method B")
        super().hello()

class C(A):
    def hello(self):
        print("Method C")
        super().hello()

class D(B,C):
    def hello(self):
        print("Method D")
        super().hello()

d = D()

d.hello()