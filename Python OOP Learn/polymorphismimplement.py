class Stack:

    def __init__(self):
        # gak bisa private kalo inherit
        self.stack = []

    def push(self, value):
        if type(value) == int:
            self.stack.append(value)
        else:
            print("not numeric")

    def pop(self):
        val = self.stack[-1]
        del self.stack[-1]
        return val

    def print(self):
        print(self.stack)

    def peek(self):
        return self.stack[-1]


class Queue(Stack):

    def pop(self):
        val = self.stack[0]
        del self.stack[0]
        return val

    def peek(self):
        return self.stack[0]


que = Queue()
que.push(1)
que.push(2)
que.push(3)
que.push(4)

print(que.peek())
que.print()
