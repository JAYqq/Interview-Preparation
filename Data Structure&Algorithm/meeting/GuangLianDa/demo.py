import heapq as hq
def main():
    input1=list(map(int,input().strip().split(" ")))
    input2=list(map(int,input().strip().split(" ")))
    heap=[]
    for item in input2:
        hq.heappush(heap,item)
    m=input1[1]
    while m:
        temp=hq.heappop(heap)
        hq.heappush(heap,temp+input1[2])
        m-=1
    print(hq.heappop(heap))
main()
    