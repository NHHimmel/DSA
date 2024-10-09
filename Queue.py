from linkedList import LinkedList


class Queue:
    def __init__(self):
        self._array = LinkedList()

    def offer(self, data: any) -> None:
        """Adds an element to the end of the queue."""
        self._array.insert(data)

    def poll(self) -> any:
        """Removes and returns the element from the front of the queue."""
        if self.isEmpty():
            raise IndexError("poll from an empty queue")
        front = self._array.peek()  # Get the front element before deletion
        self._array.deleteByIndex(0)
        return front

    def peek(self) -> any:
        """Returns the front element without removing it from the queue."""
        if self.isEmpty():
            raise IndexError("peek from an empty queue")
        return self._array.peek()

    def isEmpty(self) -> bool:
        """Checks if the queue is empty."""
        return self._array.size() == 0

    def __str__(self) -> str:
        """Returns a string representation of the queue."""
        return self._array.output()


if __name__ == "__main__":
    var = Queue()

    var.offer(12)
    var.offer(34)
    var.offer(1)

    print(var)  # Output: [12, 34, 1]

    print(var.poll())  # Output: 12
    print(var)  # Output: [34, 1]

    print(var.peek())  # Output: 34
    print(var.isEmpty())  # Output: False

    # Testing empty conditions
    var.poll()
    var.poll()
    print(var.isEmpty())  # Output: True
    # print(var.poll())  # This will raise an IndexError
    # print(var.peek())  # This will raise an IndexError
