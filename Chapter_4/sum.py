def sum(arr):
  if len(arr) == 1:
    return arr[0]
  else:
    return arr[0] + sum(arr[1:])

def main():
  print(sum([2,4,6]))

if __name__ == '__main__':
  main()
