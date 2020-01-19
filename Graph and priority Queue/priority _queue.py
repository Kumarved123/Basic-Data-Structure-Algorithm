from heapq_max import heapify_max, heappop_max, heappush_max
class priority:
    def __init__ (self, arr):
        heapify_max(arr)
        self.heap = arr
    def Pop(self):
        return heappop_max(self.heap)
    def Push(self, value):
        heappush_max(self.heap, value)


