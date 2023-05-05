class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval, end=' ')
         printval = printval.nextval
         

list = SLinkedList()
list.headval = Node("Mon") # type: ignore
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Fri")
e5 = Node("Sat")

# Link first Node to second node
list.headval.nextval = e2 # type: ignore

# Link second Node to third node
e2.nextval = e3 # type: ignore

# Link third Node to fourth node
e3.nextval = e4 # type: ignore

# Link fourth Node to fifth node
e4.nextval = e5 # type: ignore

list.listprint()