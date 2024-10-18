from queue import Queue
class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

class BinarySearchTree:
   def __init__(self):
      self.root = None

   def insertKey(self,data):
      node = Node(data)
      curr = self.root
      if not self.root:
         self.root = node
      else:
         var = Queue()
         var.put(curr)
         while not var.empty():
            curr = var.get()
            if curr.data > data:
               if not curr.left:
                  curr.left = node
               else: var.put(curr.left)

            elif curr.data<data:
               if not curr.right:
                  curr.right = node
               else: var.put(curr.right)
            else: return self.root

# insertion using recursion
   def insertRecur(self, data):
      self.iRHelper(self.root, data)

   @staticmethod
   def iRHelper(root, data):
      if not root:
         return Node(data)
      if root.data == data:
         return root
      elif root.data > data:
         root.left = BinarySearchTree.iRHelper(root.left,data)
      else:
         root.right = BinarySearchTree.iRHelper(root.right, data)
      return root

   def display(self):
      self.displayHelper(self.root)
      print()

   @staticmethod
   def displayHelper(root): #inorder traverse
      if root:
         BinarySearchTree.displayHelper(root.left)
         print(root.data,end=" ")
         BinarySearchTree.displayHelper(root.right)

   def successor(self, node):
      curr = node.right
      while curr and curr.left:
         curr = curr.left
      return curr

   def predecessor(self, node):
      curr = node.left
      while curr and curr.right:
         curr = curr.right
      return curr

   def delete(self, key):
      self.deleteHelper(self.root,key)

   @staticmethod
   def deleteHelper(root,key):
      # base case 1 - finished searching, no similar key found
      if not root:
         return root
      #
      elif key < root.data:
         root.left = BinarySearchTree.deleteHelper(root.left, key)
      elif key > root.data:
         root.right = BinarySearchTree.deleteHelper(root.right, key)
      else:
         if not root.left: return root.right
         elif not root.right: return root.left
         else:
            successor = self.successor(root)
            root.data = successor.data
            root.right = BinarySearchTree.deleteHelper(root.right,successor.data)
      return None
         

if __name__ == "__main__":
   bst = BinarySearchTree()
   bst.insertKey(11)
   bst.insertKey(5)
   bst.insertKey(9)
   bst.insertKey(17)
   bst.insertKey(5)
   bst.insertRecur(8)

   bst.delete(17)

   bst.display()
