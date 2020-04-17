# Definition for a binary tree node.
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    '''前序遍历递归写法'''
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val]+self.preorderTraversal1(root.left)+self.preorderTraversal1(root.right)
    '''前序遍历递推写法'''
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack=[root]
        ans=[]
        while stack:
            cur=stack.pop()
            ans.append(cur.val)
            '''因为这个栈需要后进先出，所以先append右节点'''
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return ans
    
    '''中序遍历递归写法'''
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal1(root.left) +[root.val]+self.inorderTraversal1(root.right)
    
    '''中序遍历递推写法'''
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        stack=[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            cur=stack.pop()
            res.append(cur.val)
            root=cur.right
        return res
    
    '''颜色标记法 中序遍历'''
    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        white,gray=0,1
        res,stack=[],[(white,root)]
        while stack:
            color,node=stack.pop()
            if node is None:continue
            if color==white:
                stack.append((white,node.right))
                stack.append((gray,node))
                stack.append((white,node.left))
            else:
                res.append(node.val)
        return res
    
    '''颜色标记法优化 中序遍历'''
    def inorderTraversal4(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res,stack=[],[root]
        while stack:
            node=stack.pop()
            if isinstance(node,TreeNode):
                stack.extend([node.right,node.val,node.left])
            elif isinstance(node,int):
                res.append(node)
        return res
    '''莫里斯解法(线索二叉树) 待更'''


    '''颜色标记法优化 后序遍历'''
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res,stack=[],[root]
        while stack:
            node=stack.pop()
            if isinstance(node,TreeNode):
                stack.extend([node.val,node.right,node.left])
            elif isinstance(node,int):
                res.append(node)
        return res
    
    '''后序遍历，递归写法'''
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal2(root.left)+self.postorderTraversal2(root.right)+[root.val]

    '''后序遍历，递推写法
    因为先序遍历是root->left->right，而后序遍历是left->right->root，所以其实只要将先序遍历变为：
    root->right->left，然后将遍历后的答案逆序返回就可以了。但是中序遍历因为是left->root->right，root都在
    中间，所以无法改变'''
    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack=[root]
        ans=[]
        while stack:
            cur=stack.pop()
            ans.append(cur.val)
            '''因为这个栈需要后进先出，所以先append右节点'''
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return ans[::-1]
    
    '''层序遍历递归写法，两个参数：节点和层数，root是第0层
    这里比较重要的是根据levels列表长度和level判断层数'''
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        levels=[]
        if not root:
            return levels
        def helper(node,level):
            if len(levels)==level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
        helper(root,0)
        return levels
    
    '''层序遍历迭代写法，使用队列，相当于bfs写法，而递归相当于dfs写法。
    这边需要注意的是，queue中始终保存着这一层的所有节点，所以q_length就是
    当前层有多少节点'''
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        levels=[]
        level=0
        if root is None:
            return levels
        queue = deque([root,])
        while queue:
            levels.append([])
            q_length=len(queue)
            for i in range(q_length):
                node=queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return levels
    