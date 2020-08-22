def main():
    n=int(input())
    arr=get_arr(n)
    res=[[0 for _ in range(n)] for _ in range(n)]
    h,left,right=n,0,n-1
    index=n*n-1
    while h>0:
        
            
        

def get_arr(n):
    n*=n
    ans=[1 for _ in range(n)]
    for i in range(2,n):
        ans[i]=ans[i-1]+ans[i-2]
    return ans