class Order:
  def __init__(self, value, next):
    self.value = value
    self.next = next


class OrdersList:
  def __init__(self):
    self.head = None

  def addOrder(self, value):
    order = Order(value, None)
    if self.head == None:
      self.head = order
    else:
      self.head.next = order

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

  orderList.print()

if __name__ == "__main__":
  main()
