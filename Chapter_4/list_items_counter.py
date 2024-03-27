class Node:
  def __init__(self, value, next):
    self.value: int = value
    self.next: Node = next

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
  
def findMax(nodo: Node, max: int):
  if nodo == None:
    return max
  else:
    if (nodo.value > max):
      return findMax(nodo.next, nodo.value)
    else:
      return findMax(nodo.next, max)


def main():
  myList = List()
  myList.add(1)
  myList.add(5)
  myList.add(3)
  myList.add(7)
  myList.print()
  
  print(count(myList.head))
  print(findMax(myList.head, myList.head.value))

if __name__ == '__main__':
  main()
