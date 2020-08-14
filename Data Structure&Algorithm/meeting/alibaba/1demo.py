def main():
    def dfs(k,level,order):
        if level==m:
            for i in range(len(order)):
                if i==len(order)-1:
                    print(order[i])
                else:
                    print(order[i],end=" ")
            return
        for i in range(k,n+1):
            order.append(i)
            dfs(i+1,level+1,order)
            order.pop()
    n,m=list(map(int,input().split(" ")))
    order=[]
    dfs(1,0,order)
main()