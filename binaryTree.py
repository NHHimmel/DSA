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

   @staticmethod
   def addHelper(head,node):
      var = Queue()
      var.put(head)
      while not var.empty():
         curr = var.get()
         
         if curr.left: 
            var.put(curr.left)
         else: 
            curr.left = node
            break

         if curr.right: 
            var.put(curr.right)
         else: 
            curr.right = node
            break

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

   def getDeepest(self):
      var = Queue()
      r_most = self.parent
      if r_most: var.put(r_most)
      while not(var.empty()):
         r_most = var.get()
         if r_most.left:
            var.put(r_most.left)
         if r_most.right:
            var.put(r_most.right)  # Fix: use r_most.right instead of r_most.left
      return r_most

   def deleteDeepestRight(self, d_node):
      var = Queue()
      r_most = self.parent
      if not r_most: return None
      var.put(r_most)

      while not var.empty():
         r_most = var.get()
         if r_most is d_node:
            return None
         if r_most.left:
            if r_most.left == d_node:
               r_most.left = None
               return
            else:
               var.put(r_most.left)

         if r_most.right:
            if r_most.right == d_node:
               r_most.right = None
               return
            else:
               var.put(r_most.right)

   def deleteNode(self, key):
      var = Queue()
      curr = self.parent
      if not curr:
         return
      
      if curr.data == key and not curr.left and not curr.right: 
         self.parent = None
         return

      var.put(curr)

      key_node = None
      while not var.empty():
         curr = var.get()
         if curr.data == key:
            key_node = curr  # Save the node to be deleted
         if curr.left:
            var.put(curr.left)
         if curr.right:
            var.put(curr.right)

      if key_node:  # Replace the key_node's data with the deepest node's data
         d_node = self.getDeepest()
         key_node.data = d_node.data
         self.deleteDeepestRight(d_node)

   def inOrderSearch(self,key):
      return self.inOrderHelper(self.parent,key)

   @staticmethod
   def inOrderHelper(head,key):
      if head is None:
         return False

      result_left = BinaryTree.inOrderHelper(head.left,key)
      if result_left:
         return True

      if head.data == key:
         return True
      
      return BinaryTree.inOrderHelper(head.right,key)
    
   def display(self):  # Pre-order traversal
      self.displayHelper(self.parent)
      print()

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

   bt.display()  # Pre-order: 2 5 7 10 15
  
   print("After deletion:")
   bt.deleteNode(5)

   bt.display()  # Pre-order after deletion of node with value 5
