import random

arr = [1, 2, 1]

def bubbleSort(arr):
  for i in range(len(arr)):
    swapped = False
  
    for j in range(len(arr) - i - 1):
  
      print(arr, arr[i], arr[j], arr[j+1])
      
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
  
    if not swapped:
      break

  return arr

bubbleSort(arr)

def bogoSort(arr):
  sorted = True
  
  while True:

    print(arr)
    
    for i in range(len(arr)-1):
      if arr[i+1] < arr[i]:
        sorted = False

    if sorted:
      return arr
    else:
      random.shuffle(arr)

  return arr

# bogoSort(arr)