'''散列表+双向链表
因为链表的增删操作是O(1)时间复杂度，而查询需要O(N),
所以我们使用散列表优化，让它的查询也为O(1)'''
class DbListNode(object):
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.hashList={}
        self.head=DbListNode(None,-1)
        self.tail=DbListNode(None,-1)
        self.head.next=self.tail
        self.tail.prev=self.head

    def put(self,key,value)->None:
        if key in self.hashList.keys():
            cur=self.hashList[key]
            cur.val=value #update the cache
            #skip out
            cur.prev.next=cur.next
            cur.next.prev=cur.prev
            #the latest used node should be put on the head
            head_node=self.head.next
            self.head.next=cur
            cur.prev=self.head
            head_node.prev=cur
            cur.next=head_node
        else:
            cur=DbListNode(key,value)
            self.hashList[key]=cur

            head_node=self.head.next
            self.head.next=cur
            cur.prev=self.head
            head_node.prev=cur
            cur.next=head_node
            if len(self.hashList.keys())>self.capacity:
                self.hashList.pop(self.tail.prev.key)
                self.tail.prev.prev.next=self.tail
                self.tail.prev=self.tail.prev.prev
    
    def get(self,key:int)->int:
        if key in self.hashList.keys():
            cur=self.hashList[key]
            #skip out
            cur.prev.next=cur.next
            cur.next.prev=cur.prev
            
            top_node = self.head.next
            self.head.next = cur
            cur.prev = self.head
            cur.next = top_node
            top_node.prev = cur

            return self.hashList[key].val
        return -1

    
    def __repr__(self):
        vals = []
        p = self.head.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  
    cache.put(3, 3)  
    print(cache)
    cache.get(2)  
    cache.put(4, 4)  
    print(cache)
    cache.get(1)  
    cache.get(3)  
    print(cache)
    cache.get(4)  
    print(cache)

