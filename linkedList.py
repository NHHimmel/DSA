
# Single LinkedList, implementation
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    def insert(self,data:any)->None:
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = newNode

    def deleteKey(self,key:any)->any:
        current = self.head
        prev = None
        if (current != None and current.data == key):
            self.head = current.next
            print(f"Deleted {key}")
            return 

        while (current != None and current.data != key):
            prev = current
            current = current.next
        if current is not None:
            prev.next = current.next
            print(f"Deleted {key}")
        if current is None:
            raise Exception(f"{key} not found")

    def output(self):
        if self.head != None:
            string = ""
            current = self.head
            while (current.next != None):
                string += str(current.data) + ", "
                current = current.next
            string += str(current.data)
            return f"[{string}]"
        else: return []

    def peek(self):
        if(self.head) != None:
            current = self.head
            return current.data
        else:
            return None

    def deleteByIndex(self,idx):
        current = self.head
        prev = None
        if current!=None and idx == 0:
            self.head = current.next
            return

        i=0
        while(current!=None and i!=idx):
            prev = current
            current = current.next
            i+=1

        if(current!=None):
            prev.next = current.next
            return
        elif current is None:
            raise IndexError(f"Element not found at index {idx}")

    def size(self):
        curr = self.head
        i=0
        while(curr!=None):
           curr = curr.next
           i+=1
        return i

    def swapNode(self, x, y):
        if x == y:
            return

        # Initialize pointers
        curr = self.head
        prev = None
        var_x, var_y = None, None
        prev_x, prev_y = None, None

        # Find x and y in the linked list_1
        while curr is not None:
            if curr.data == x:
                var_x = curr
                prev_x = prev
            elif curr.data == y:
                var_y = curr
                prev_y = prev

            prev = curr
            curr = curr.next

        # If either x or y is not found, return
        if not (var_x and var_y):
            return

        # If x is not head of linked list_1
        if prev_x is not None:
            prev_x.next = var_y
        else:  # Make y the new head
            self.head = var_y

        # If y is not head of linked list_1
        if prev_y is not None:
            prev_y.next = var_x
        else:  # Make x the new head
            self.head = var_x

        # Swap next pointers
        var_x.next, var_y.next = var_y.next, var_x.next




if __name__ == "__main__":
    # list_1 = LinkedList()
    # list_1.insert(2)
    # list_1.insert(5)
    # list_1.insert(7)
    # list_1.insert(12)



    # # sorting two merged sorted list using recursion
    # def merge_sorted_list_1(a:Node, b:Node):
    #     result = None
    #     if a is None:
    #         return b
    #     if b is None:
    #         return a
    #     if a.data < b.data:
    #         result = a
    #         result.next = merge_sorted_list_1(a.next, b)
    #     else:
    #         result = b
    #         result.next = merge_sorted_list_1(a, b.next)
    #     return result

    # list_2 = LinkedList()
    # list_2.insert(1)
    # list_2.insert(3)
    # list_2.insert(9)

    # result = merge_sorted_list_1(list_1.head,list_2.head)
    # while(result is not None):
    #     print(result.data)
    #     result = result.next

    first = Node(2)
    second = Node(6)
    third = Node(8)
    fourth = Node(9)
    first.next = second
    second.next = third



    # def detectCycle(head):
    #     if not(head or head.next):
    #         return None
    #     slow = head
    #     fast = head
        
    #     while (fast and fast.next):
    #         slow = slow.next
    #         fast = fast.next.next
    #         if(slow==fast):
    #             slow = head
    #             while(slow!=fast):
    #                 slow = slow.next
    #                 fast = fast.next
    #             return slow.data

    # print(detectCycle(first))
    def getLen(head):
        len_ = 1
        curr = head
        while(curr.next!=None):
            curr = curr.next
            len_+=1
        
        middle = math.floor(len_/2)+1
        curr = head
        while(middle>1):
            curr = curr.next
            middle-=1
        return curr


    getLen(first)

    







