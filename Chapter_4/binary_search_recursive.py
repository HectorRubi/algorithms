def binary_search(list, value):
  print(list, value)
  if len(list) == 0:
    return -1
  else:
    mid = round(len(list) / 2)
    if value == list[mid]:
      return list[mid]
    elif value > list[mid]:
      return binary_search(list[mid + 1:],value)
    else:
      return binary_search(list[:mid],value)

def main():
  my_list = [1,2,3,4,5,6]
  print(binary_search(my_list, 4))
  print(binary_search(my_list, -1))

if __name__ == '__main__':
  main()
