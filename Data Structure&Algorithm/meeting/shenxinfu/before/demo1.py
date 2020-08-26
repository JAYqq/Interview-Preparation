def main():
    t=int(input())
    for i in range(t):
        arr=list(map(int,input().split()))
        sr=str(arr[0])+str(arr[1])+str(arr[2])
        index=3
        while len(sr)<arr[3]:
            sr+=str(int(sr[-1])+int(sr[-2])+int(sr[-3]))
        print(sr[arr[-1]-1])
main()

