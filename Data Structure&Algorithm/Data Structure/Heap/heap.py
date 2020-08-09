import heapq
def main():
    heap = [5,8,0,3,6,7,9,1,4,2]
    heapq.heapify(heap)
    print(heap)
    heapq.heappush(heap,-1)
    print(heap)
    temp=heapq.heappop(heap)
    print(temp)
main()