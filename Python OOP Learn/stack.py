# dua _ jadi private
# contoh -> self.__stack
# contoh -> def __pushStack


class Stack:

    def __init__(self):
        self.__stack = []

    def pushStack(self, value):
        if type(value) == int:
            self.__stack.append(value)
        else:
            print("not numeric")

    def popStack(self):
        return self.__stack.pop()

    def print(self):
        for test in self.__stack:
            print(test)

    def peek(self):
        return self.__stack[-1]


stack = Stack()
stack.pushStack(50)
stack.pushStack(10)
stack.pushStack(20)
stack.pushStack(30)
stack.pushStack(100)

print(stack.peek())
stack.pushStack("test")
stack.pushStack(True)

stack.print()