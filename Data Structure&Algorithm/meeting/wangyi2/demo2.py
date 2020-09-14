res=[]
def main():
    n=int(input())
    feature=[]
    max_len=1
    for i in range(n):
        temp=input().split()
        max_len*=len(temp)
        feature.append(temp)
    if len(feature)==0:
        print(-1)
        return
    max_len//=len(feature[0])
    dfs(feature,0,[])
    for i in range(max_len):
        j=i
        while j<len(res):
            print(res[j])
            j+=max_len
def dfs(features,index,ans):
    global res
    if index==len(features):
        gfd="-".join(ans)
        res.append(gfd)
        return
    for item in features[index]:
        ans.append(item)
        dfs(features,index+1,ans)
        ans.pop()
main()