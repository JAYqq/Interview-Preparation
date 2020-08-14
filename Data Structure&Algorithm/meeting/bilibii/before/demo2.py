import sys
ans=sys.maxsize*sys.maxsize
arr=[]
def main():
    global arr
    arr=input().split(",")
    ls=[]
    dfs(ls)
    print(ans)
def dfs(temp_list):
    global ans,arr
    if len(temp_list)==len(arr):
        sr="".join(temp_list)
        ans=min(ans,int(sr))
        return
    for i in range(len(arr)):
        if(arr[i] in temp_list):
            continue
        temp_list.append(arr[i])
        dfs(temp_list)
        temp_list.pop()
main()
