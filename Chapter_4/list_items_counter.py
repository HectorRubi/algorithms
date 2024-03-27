class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next

class List:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def isEmpty(self):
    return self.head == None
  
  def add(self, value):
    order = Node(value, None)

    if self.isEmpty():
      self.head = order
      self.tail = order
    else:
      self.tail.next = order
      self.tail = order

  def print(self):
    order = self.head
    while order != None:
      print(order.value, ' -> ', end="")
      order = order.next
    print('')


def count(nodo):
  if nodo == None:
    return 0
  else:
    return 1 + count(nodo.next)


def main():
  myList = List()
  myList.add("first")
  myList.add("second")
  myList.add("third")
  myList.add("last")
  myList.print()
  
  print(count(myList.head))

if __name__ == '__main__':
  main()
