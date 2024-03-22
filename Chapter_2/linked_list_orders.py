class Order:
  def __init__(self, value, next):
    self.value = value
    self.next = next


class OrdersList:
  def __init__(self):
    self.head = None
    self.last = None

  def isEmpty(self):
    return self.head == None

  def addOrder(self, value):
    # Create order
    order = Order(value, None)

    if self.isEmpty():
      self.head = order
      self.last = order
    else:
      # New last order
      self.last.next = order
      self.last = order

  def pullOrder(self):
    if self.isEmpty():
      return
    
    # Remove head changing head to the next order
    self.head = self.head.next

    # All elements has been removed
    if self.head == None:
      self.last = None

  def print(self):
    order = self.head
    while order != None:
      print(order.value, ' -> ', end="")
      order = order.next
    print('')


def main():
  orderList = OrdersList()

  # Server add orders to the back
  print('Adding orders...')
  orderList.addOrder('Burger')
  orderList.addOrder('Fries')
  orderList.addOrder('Pay')
  orderList.print()

  # Chef pull orders off the front
  print('Pulling orders...')
  orderList.pullOrder()
  orderList.print()

  # Server add orders to the back
  print('Adding orders...')
  orderList.addOrder('Orange Juice')
  orderList.print()

  # Chef pull orders off the front
  print('Pulling orders...')
  orderList.pullOrder()
  orderList.print()

if __name__ == "__main__":
  main()
