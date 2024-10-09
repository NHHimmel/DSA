class Stack:
    def __init__(self)->None:
        self.list = []
    def push(self, data:any)->None:
        self.list.append(data)

    def pop(self) -> any:
        if self.isEmpty():
            raise IndexError("pop from an empty stack")
        return self.list.pop(-1)

    def peek(self) -> any:
        if self.isEmpty():
            raise IndexError("peek from an empty stack")
        return self.list[-1]

    def search(self, data:any)->any:
        for i in range(len(self.list)):
            if self.list[i] ==  data:
                return i
            return -1

    def isEmpty(self)->bool:
        return self.list == []

    def clear(self)->None:
        self.list = []


    def __str__(self):
        return str(self.list[::-1])



var = Stack()
var.push(2)
var.push(7)
var.push(9)

print(var)

var.pop()
print(var)
print(var.peek())
var.push("Hi")
var.push("Ho")

print(var.search("Hi"))

print(var.isEmpty())
var.clear()
print(var.isEmpty())