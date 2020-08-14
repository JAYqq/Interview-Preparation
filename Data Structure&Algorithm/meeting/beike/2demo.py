def main():
    t=int(input())
    while t:
        t-=1
        n,m=list(map(int,input().split(" ")))
        sum_=n*m
        if sum_==1:
            print(1)
            continue
        for i in range(2,sum_+1):
            if sum_%i==0:
                print(i)
                break
main()