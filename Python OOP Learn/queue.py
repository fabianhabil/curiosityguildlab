class Queue:

    def __init__(self):
        self.__queue = []

    def pushQueue(self, value):
        if type(value) == int:
            self.__queue.append(value)
        else:
            print("invalid value")

    def popQueue(self):
        return self.__queue.pop(0)

    def peek(self):
        return self.__queue[0]

    def printQueue(self):
        print(self.__queue)


queue = Queue()

queue.pushQueue(5)
queue.pushQueue(4)
queue.pushQueue(3)
queue.pushQueue(2)
queue.pushQueue(1)

queue.printQueue()

queue.popQueue()
queue.popQueue()

queue.printQueue()
print(queue.peek())
