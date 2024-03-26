def factorial(num):
  res = 1
  for x in range(num, 0, -1):
    res *= x
  return res

def main():
  print(factorial(5))

if __name__ == '__main__':
  main()
