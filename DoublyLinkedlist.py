class Node:
   def __init__(self,data):
      self.data = data
      self.next = None
      self.prev = None

class DoublyLinkedList:
   
   def forward_traversal(self,head):
      curr = head
      while curr is not None:
         print(curr.data, end=' ')
         curr = curr.next

      print()

   def backward_traversal(self,tail):
      curr = tail
      while curr is not None:
         print(curr.data, end=" ")
         curr = curr.prev

      print()

   def find_length(self,head):
      curr = head 
      count = 0
      while curr is not None:
         count+=1
         curr = curr.next
      return count

   def insertBegin(self,head, data):
    
    # Create a new node
    new_node = Node(data)
    
    # Make next of it as head
    new_node.next = head
    
    # Set previous of head as new node
    if head is not None:
        head.prev = new_node
    
    # Return new node as new head
    return new_node

   def insert_end(self,head, new_data):
      
    # Create a new node
    new_node = Node(new_data)
    
    # If the linked list is empty, set the new node
    #as the head
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        
        # Set the next of the last node to the new node
        curr.next = new_node
        
        # Set the prev of the new node to the last node
        new_node.prev = curr
    
    return head

   


if __name__=="__main__":
   dll = DoublyLinkedList()

   head = Node(1)
   second = Node(2)
   third = Node(3)

   head.next = second
   second.prev = head
   second.next = third
   third.prev = second

   print("Forward Traversal:")
   dll.forward_traversal(head)
   
   print("Backward Traversal:")
   dll.backward_traversal(third)

   print(dll.find_length(head))   