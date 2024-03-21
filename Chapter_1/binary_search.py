def binary_search(list, value):
  low = 0
  high = len(list) - 1
  
  while low <= high:
    # Calculate the middle element into the distance between low and high,
    # and then move it the number of steps needed.
    middle = round(((high - low ) / 2) + low)
    middle_value = list[middle]

    if middle_value == value:
      return middle

    elif middle_value < value:
      low = middle + 1

    else:
      high = middle - 1

  return None

def main():
  my_list = [1,2,3,4,5,6]
  print(binary_search(my_list, 4))
  print(binary_search(my_list, -1))

if __name__ == '__main__':
  main()
