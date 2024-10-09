class Node:
   def __init__(self,data):
      self.data = data
      self.next = None


class CLinkedList:
   def __init__(self):
      self.head = None

   def insertEnd(self, data):
      newNode = Node(data)
      if not self.head:
         self.head = newNode
         newNode.next = self.head
      else:
         current = self.head
         while current.next!=self.head:
            current = current.next
         newNode.next = self.head
         current.next = newNode
   
   def insertAny(self,node, pos):
      
      if self.head is not None:
         
         #insert at beginning or end
         if pos==1:
            current = self.head
            while(current.next!=self.head):
               current = current.next
            current.next = node
            node.next = self.head
            self.head = node # remove this part to add the node at te end
         else:
            i=1
            current=self.head; prev=None
            while(current.next!=self.head):
               prev = current
               current = current.next
               i+=1
               if(i==pos):
                  prev.next = node
                  node.next = current


   def traverse(self):
      if self.head is not None:
         current = self.head
         while(current.next!=self.head):
            print(current.data)
            current = current.next
         print(current.data)
      else:
         print("No elements")



c1 = CLinkedList()

c1.insertEnd(4)
c1.insertEnd(7)
c1.insertEnd(8)
c1.insertAny(Node(10),1)

c1.traverse()



   


