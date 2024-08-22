array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10000]
searchingFor = 6


def linearSearch(array, searchingFor):
  for i in array:
    if i == searchingFor:
      return array.index(i)


def binarySearch(array, searchingFor):
  start = 0
  end = len(array) - 1
  while (start <= end):
    mid = (start + end) // 2
    if (array[mid] == searchingFor):
      return mid
    elif (array[mid] < searchingFor):  
      # target is to the right of mid
      start = mid + 1
    else:  #array[mid] > searchingFor
      # target is to the left of mid
      end = mid - 1


def jumpSearch(arr, searchingFor):
  jump_amount = int(len(arr)**(0.5))

  i = 0
  prev = 0

  while arr[i] < searchingFor:
    prev = i
    i += jump_amount

    if i > len(arr) - 1:
      i = len(arr) - 1
    if prev == arr[i]:
      return -1

  while i >= prev:
    if arr[i] == searchingFor:
      return i

    i -= 1

  return -1

print(jumpSearch([1, 2, 3, 4, 5, 6, 7, 8], 8))
