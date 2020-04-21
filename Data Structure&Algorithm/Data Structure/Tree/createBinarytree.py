'''已知一个完全二叉树的前序遍历，重构这个树'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.nodeList=['A','D','E','F','G','H','K','L','B','I','M','C']
        self.index=0
    def initParam(self):
        '''初始化参数'''
        self.level=int(len(self.nodeList)**0.5)
        self.length=len(self.nodeList)
    def preorderTraversal1(self, root: TreeNode):
        '''前序遍历查看结果'''
        if not root:
            return []
        return [root.val]+self.preorderTraversal1(root.left)+self.preorderTraversal1(root.right)
    def createTree(self,val,level):
        '''****主要逻辑，递归重构*****'''
        node=TreeNode(val)
        self.index+=1
        if level>self.level or self.index>self.length-1:
            return None
        node.left=self.createTree(self.nodeList[self.index],level+1)
        self.index-=1
        node.right=self.createTree(self.nodeList[self.index],level+1)
        return node
if __name__ == "__main__":
    b=BinarySearchTree()
    b.initParam()
    root=b.createTree(b.nodeList[0],0)
    tree=b.preorderTraversal1(root)
    print(tree)


        
