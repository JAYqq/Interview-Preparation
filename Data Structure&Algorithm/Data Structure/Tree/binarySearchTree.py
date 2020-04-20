'''如果有重复数据那么有两种解决方案：
1.每个节点储存的不是单个数据，而是一个链表
2.如果在插入数据的时候碰到和自己相同的，那么就统一规定都放到自己的右边或者左边，然后
查找或者删除的时候按照这个规则来，当找到一个节点后，继续往右或者往左继续查找'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self._root=None
    
    def find(self,val:int):
        cur=self._root
        if not cur:
            return None
        while cur and cur.val!=val:
            cur=cur.right if cur.val<val else cur.left
        return cur

    '''二叉搜索树都是插入到叶子节点'''
    def insert(self,val:int):
        if not self._root:
            self._root=TreeNode(val)
            return
        cur=self._root
        while cur:
            parent=cur
            cur=cur.left if cur.val>val else cur.right
        node=TreeNode(val)
        if parent.val>val:
            parent.left=node
        else:
            parent.right=node
    
    def delete(self,val:int):
        cur=self._root
        parent=None
        if not self._root:
            return None
        while cur and cur.val!=val:
            parent=cur
            cur=cur.left if cur.val>val else cur.right
        child=cur.left if cur.left else cur.right
        if not parent:
            self._root=parent
        elif parent.left==cur:#如果但当前节点是父节点的左节点
            parent.left=child
        else:
            parent.right=child
    
    #层序遍历打印
    def _print(self):
        levels=[]
        if not self._root:
            return levels
        def helper(node,level):
            if len(levels)==level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
        helper(self._root,0)
        print(levels)
    
    #求二叉树的最大深度
    def maxDepth(self, root: TreeNode) -> int: 
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 
            



