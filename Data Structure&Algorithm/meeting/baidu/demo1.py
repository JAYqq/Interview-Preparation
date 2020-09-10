# def main():
#     n=int(input())
#     while n:
#         L,m=list(map(int,input().split()))
#         res=[0 for _ in range(L+1)]
#         arg=[]
#         while m:
#             a,b=list(map(int,input().split()))
#             for i in range(a-1,b):
#                 res[i]+=1
#             m-=1
#         n-=1
#         for i in range(L):
#             if i<L-1:
#                 print(res[i],end=" ")
#             else:
#                 print(res[i])
# main()

def main():
    n=int(input())
    while n:
        L,m=list(map(int,input().split()))
        # res=[0 for _ in range(L+1)]
        arg=[]
        while m:
            a,b=list(map(int,input().split()))
            arg.append((a,b))
            m-=1
        for i in range(1,L+1):
            ans=0
            for item in arg:
                if i>=item[0] and i<=item[1]:
                    ans+=1
            print(ans,end=" ")
        n-=1
main()