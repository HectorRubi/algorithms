class Order:
  def __init__(self, value, next):
    self.value = value
    self.next = next


class OrdersList:
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def searchLast(self):
    if self.isEmpty():
      return None

    last = self.head
    while last.next != None:
      last = last.next
    
    return last
    

  def addOrder(self, value):
    # Create order
    order = Order(value, None)

    if self.isEmpty():
      self.head = order
    else:
      # Search last order
      last = self.searchLast()
      # New last order
      last.next = order

  def print(self):
    order = self.head
    while order != None:
      print(order.value, ' -> ', end="")
      order = order.next
    print('')


def main():
  orderList = OrdersList()

  # Server add orders to the back
  orderList.addOrder('Burger')
  orderList.addOrder('Fries')
  orderList.addOrder('Pay')

  orderList.print()

if __name__ == "__main__":
  main()
