import random
def main():
    m,n=list(map(int,input().split()))
    dic={}
    ans=0
    for i in range(n):
        arr=input().split()
        if dic.get(arr[0]):
            dic[arr[0]].append(arr[2])
        else:
            dic[arr[0]]=[arr[2]]
    print(dic)
    for key,val in dic.items():
        if len(val)==2:
            flag=0
            for item in val:
                if not dic.get(item):
                    flag+=1
            if flag==2:
                ans+=1
    print(ans)
main()
