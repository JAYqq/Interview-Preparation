def main():
    arr=[]
    res=[]
    a=int(input())
    b=int(input())
    k=int(input())
    arr.append(a)
    arr.append(b)
    arr.sort()
    for i in range(k,-1,-1):
        res.append(i*arr[0]+(k-i)*arr[1])
    res=list(set(res))
    res.sort()
    if res==[0]:
        print([])
    else:
        print(res)
main()
# def dfs(k,ans):
#     if k==0:
#         res.append(ans)
#         return
#     for item in arr:
#         dfs(k-1,ans+item)