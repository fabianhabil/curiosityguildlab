# override vs overload

class A:

    def methodA(self):
        print("Method A")


class B(A):

    def methodA(self):
        print("Method B")


class C(B, A):
    pass


a = A()
b = B()
c = C()

a.methodA()
b.methodA()
c.methodA()