class Node:
   def __init__(self,data):
      self.data = data
      self.prev = None
      self.next = None
   
class CircularDoublyLinkedList:
   def __init__(self):
      self.head = None

   def appendAtBeginning(self, data):
      node = Node(data)

      if self.head is None:
         self.head = node
         self.head.next = self.head
         self.head.prev = self.head

      else:
         tail = self.head.prev
         tail.next = node
         node.prev = tail
         self.head.prev = node
         node.next = self.head
         #update head node
         self.head = node

   def display(self):
      if self.head is not None:
         curr = self.head
         # print(curr.data)
         # # traversing left to right
         # while(curr:=curr.next)!=self.head:
         #    print(curr.data)

         #display reversely
         tail = curr.prev
         print(tail.data)
         while (tail:=tail.prev)!=self.head.prev:
            print(tail.data)

   def insert(self, data, pos):
      #left to right direction
      node = Node(data)
      if 0<pos<=self.size():
         if self.head:
            i=1
            curr = self.head
            while(i!=pos):
               curr = curr.next
               i+=1
            node.prev = curr.prev
            node.next = curr
            curr.prev.next = node
            curr.prev = node
         
            if pos==1:
               self.head = node
            # self.head.next = self.head
            # self.head.prev = self.head
      elif pos == 1 and self.head is None:
        self.head = node
        self.head.next = self.head
        self.head.prev = self.head
      else:
         print("Position out of bound!")
      
         
         
   def size(self):
      if not(self.head):
         return 0

      else:
         curr = self.head
         i=1
         while((curr:=curr.next)!=self.head):
            i+=1
         return i

   def deletion(self,pos):
      #left to right direction
      #--<-2-><-11-><-5-><-8->--
      if 0<pos<=self.size():
         if self.head:
            curr = self.head
            i = 1
            while(i!=pos):
               curr = curr.next
               i+=1
            if curr == self.head and curr.next == self.head:
                self.head = None
            else:
                # If deleting the head
                if curr == self.head:
                    self.head = curr.next

            curr.prev.next = curr.next 
            curr.next.prev = curr.prev 
         else:
            print("No element to delete")
      else: print("Position out of bound")
            
         


         



   


         


if __name__ == "__main__":
   cdll_1 = CircularDoublyLinkedList()

   cdll_1.appendAtBeginning(2)
   cdll_1.appendAtBeginning(5)
   cdll_1.appendAtBeginning(8)

   # cdll_1.display()
   # print(cdll_1.size())
   # print()
   cdll_1.insert(11,2)
   # cdll_1.display()
   cdll_1.deletion(1)
   cdll_1.display()



   



