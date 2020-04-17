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
        while cur.val!=val:
            cur=cur.right if cur.val<val else cur.left
        return cur
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

