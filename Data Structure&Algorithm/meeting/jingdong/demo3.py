class UnionFind:
    def __init__(self,names):
        self.parent={}
        for item in names:
            self.parent[item]=item
    def union(self,name_a,name_b):
        if name_a not in self.parent or name_b not in self.parent:
            return
        root_a=self.find(name_a)
        root_b=self.find(name_b)
        if root_a<root_b:
            self.parent[root_b]=root_a
        else:
            self.parent[root_a]=root_b
    
    def find(self,name):
        while self.parent[name]!=name:
            self.parent[name]=self.parent[self.parent[name]]
            name=self.parent[name]
        return name
def main():
    n,m,q=list(map(int,input().split()))
    dic={}
    for i in range(m):
        x,y=list(map(int,input().split()))
        dic[x]=y
        dic[y]=x
    uni=UnionFind(dic)
    # print(uni.parent)
    res=[]
    for i in range(q):
        x,y=list(map(int,input().split()))
        res.append((x,y))
        uni.union(x,y)
    for item in res:
        a=uni.find(item[0])
        b=uni.find(item[1])
        if a==b:
            print("YES")
        else:
            print("NO")
main()