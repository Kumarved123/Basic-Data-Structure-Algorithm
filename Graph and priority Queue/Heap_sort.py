def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i],arr[largest]
        heapify(arr, n, largest)

arr = [5,3,1,4,6]
for i in range(5, -1, -1):
    heapify(arr, 5, i)
for i in range(4, 0, -1):
    arr[i], arr[0] = arr[0], arr[i] # swap
    heapify(arr, i, 0)
print(arr)

