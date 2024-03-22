LETTERS = { 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25 }

class User:
  def __init__(self, name, next):
    self.name = name
    self.next = next

class Users:
  def __init__(self):
    self.head = None
    self.tail = None

  def isEmpty(self):
    return self.head == None

  def add(self, name):
    user = User(name, None)

    if self.isEmpty():
      self.head = user
      self.tail = user
    else:
      self.tail.next = user
      self.tail = user
  
  def print(self):
    user = self.head
    while user != None:
      print(user.name, end='')
      if user.next != None:
        print(' -> ', end='')
      user = user.next
    print('')


class FacebookUsers:
  def __init__(self):
    self.data = [ Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users(), Users() ]
  
  def create(self, name):
    firstLetter = name[0].lower()
    self.data[LETTERS[firstLetter]].add(name)

  def print(self):
    for i in range(0, len(self.data)):
      print(i, '\t', end='')
      self.data[i].print()

def main():
  users = FacebookUsers()
  users.create('Adriana')
  users.create('Valentina')
  users.create('Lorenzo')
  users.create('Armando')
  users.print()

if __name__ == '__main__':
  main()