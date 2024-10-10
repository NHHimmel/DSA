from queue import Queue
class Node:
   def __init__(self,data):
      self.data = data
      self.left = None
      self.right = None

class BinaryTree:
   def __init__(self):
      self.parent = None

   def add(self, data):
      node = Node(data)
      if not(self.parent):
         self.parent = node
      else:
         self.addHelper(self.parent, node)
         #       2
         #      / \
         #      3 4
         #     /\ /\

   @staticmethod
   def addHelper(head,node):
      var = Queue()
      var.put(head)
      while not var.empty():
         curr = var.get()
         if curr.left: var.put(curr.left)
         else: curr.left = node; break
         if curr.right: var.put(curr.right)
         else: curr.right = node;break


   def breadthSearch(self,key): 
      var = Queue()
      curr = self.parent
      if curr: var.put(curr)
      while not var.empty():
         curr = var.get()
         if curr.data == key: return True
         if curr.left: var.put(curr.left)
         if curr.right: var.put(curr.right)
      return False

   def inOrderSearch(self,key):
      return self.inOrderHelper(self.parent,key)

   @staticmethod
   def inOrderHelper(head,key):
      
      if head is None:
         return False

      result_left = BinaryTree.inOrderHelper(head.left,key)
      if result_left:
         return True

      if head.data==key:
         return True
      
      return BinaryTree.inOrderHelper(head.right,key)
    

   
   def display(self): #pre Order traversal
      self.displayHelper(self.parent) #or, displayHelper().__func__()

   @staticmethod
   def displayHelper(node):
      if node is None:
         return
      else:
         print(node.data,end=" ")
         BinaryTree.displayHelper(node.left) 
         BinaryTree.displayHelper(node.right)

   

if __name__ == "__main__":
   bt = BinaryTree()
   bt.add(2)
   bt.add(5)
   bt.add(7)
   bt.add(10)
   bt.add(15)

   bt.display()

   print(bt.inOrderSearch(15))
   




      
      