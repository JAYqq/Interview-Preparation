def main():
    n=int(input())
    tn=n//4
    res=[]
    for num in range(1,tn):
        temp=num*4
        if judge(num,temp):
            res.append((num,temp))
    if len(res)==0:
        print(0)
    else:
        print(len(res))
        for item in res:
            print(item[0],item[1])
def judge(num,temp):
    num,temp=str(num),str(temp)
    if len(num)!=len(temp):
        return False
    length=len(num)
    for i in range(length):
        if num[i]!=temp[length-i-1]:
            return False
    return True
main()

    

def main():
    n,a,b=list(map(int,input().split()))
    arr=[]
    ans=0
    for i in range(n):
        k1,k2=list(map(int,input().split()))
        arr.append((k1,k2))
    arr.sort(key=lambda x:x[0],reverse=True)
    for i in range(a):
        ans+=arr[i][0]
    brr=arr[a:]
    brr.sort(key=lambda x:x[1],reverse=True)
    for i in range(b):
        ans+=brr[i][1]
    print(ans)
main()