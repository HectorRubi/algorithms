def recursive_countdown(num):
  print(num)
  if num <= 1:
    return
  else:
    recursive_countdown(num - 1)

def main():
  recursive_countdown(5)

if __name__ == '__main__':
  main()