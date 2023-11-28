class node:
  def __init__(self,data):
    self.data = data
    self.next = None
def display():
  pass

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1 = node2.next
node2 = node3.next

display(node1)
