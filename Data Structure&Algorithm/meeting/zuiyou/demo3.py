class Node:
    def __init__(self,num):
        self.left=None
        self.right=None
        self.val=num
res=0
def find(root,m):
    helper(root,m,0)
    print(res)
def helper(root,m,ans):
    global res
    if ans==m:
        res+=1
        return
    if not root:
        return
    helper(root.left,m,ans+root.val)
    helper(root.right,m,ans+root.val)
    return
def createTree():
    root=Node(3)
    # root.left=Node(2)
    # root.right=Node(2)
    return root
def main():
    root=createTree()
    m=int(input())
    find(root,m)
main()