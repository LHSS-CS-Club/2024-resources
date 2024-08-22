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
