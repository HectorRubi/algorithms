PIVOT_POSITION = 1

def quicksort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[PIVOT_POSITION]

    lower = []
    for i in range(0, len(arr)):
      if i == PIVOT_POSITION:
        continue
      if arr[i] <= pivot:
        lower.append(arr[i])

    bigger = []
    for i in range(0, len(arr)):
      if i == PIVOT_POSITION:
        continue
      if arr[i] > pivot:
        bigger.append(arr[i])

    return quicksort(lower) + [pivot] + quicksort(bigger)


def main():
  print(quicksort([10, 5, 2, 3]))

if __name__ == '__main__':
  main()
