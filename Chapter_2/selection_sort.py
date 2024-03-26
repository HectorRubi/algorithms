def findMax(arr):
  maxIndex = 0
  for i in range(0, len(arr)):
    if arr[i] > arr[maxIndex]:
      maxIndex = i
  return maxIndex

def selectionSort(arr):
  newArray = []
  for i in range(0, len(arr)):
    maxIndex = findMax(arr)
    newArray.append(arr.pop(maxIndex))
  return newArray

def main():
  print(selectionSort([5, 3, 6, 2, 10]))

if __name__ == "__main__":
  main()
