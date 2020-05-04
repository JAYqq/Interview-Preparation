"""堆有以下特性：
1.是一个完全二叉树
2.基于数组，而不是链式的，因为完全二叉树需要i*2和i*2+1来确定左右子树

堆的应用：
1.堆排序：时间是O(nlogn),并且是原地排序，比较稳定
2.TOPk，选取前几的数据可以使用堆排序。
  
3.优先队列"""
from typing import List
import math
class BinaryHeap:
    def __init__(self,data:List):
        self._data=data
        self.length=len(data)
    
    def heapfy(self):
        self._heapfy(self.length-1)
    def _heapfy(self,tail):
        lp=(self.length-1)>>1
        for i in range(lp,-1,-1):#循环所有的非叶子节点，也就是倒数第二层最右边的节点开始
            self._heapdown(i,tail)
    def _heapdown(self,root,tail):
        '''向下调整'''
        lp=(tail-1)>>1
        while root<=lp:
            left=root*2+1
            right=left+1
            if right<=tail:
                tmp=right if self._data[right]>self._data[left] else left
            else:
                tmp=left
            if self._data[root]<self._data[tmp]:
                self._data[root],self._data[tmp]=self._data[tmp],self._data[root]
                root=tmp
            else:
                break
    def insert(self,val):
        if self._insert(val):
            self.length+=1
            return True
        return False
    

    def _insert(self,val):
        '''向上调整'''
        self._data.append(val)
        length=len(self._data)
        nn=length-1
        while nn>=0:
            p=(nn-1)>>1
            if self._data[nn]<self._data[p]:
                self._data[nn],self._data[p]=self._data[p],self._data[nn]
                nn=p
            else:
                break
        return True
    

    def get_top(self):
        if self._data:
            return self._data[0]
        return None
    

    def remove_top(self):
        ret=None
        if self._data:
            ret=self._remove_top()
        return ret


    def _remove_top(self):
        self._data[0],self._data[-1]=self._data[-1],self._data[0]
        res=self._data.pop()
        self.length-=1
        if self.length>0:
            self._heapdown(0,self.length-1)
        return res

    def _draw_heap(self):
        """
        格式化打印
        :param data:
        :return:
        """
        length = len(self._data)

        if length == 0:
            return 'empty heap'

        ret = ''
        for i, n in enumerate(self._data):
            ret += str(n)
            # 每行最后一个换行
            if i == 2**int(math.log(i+1, 2)+1) - 2 or i == len(self._data) - 1:
                ret += '\n'
            else:
                ret += ', '

        return ret

data=[7,4,5,1,8,15,54,3,45]
heap=BinaryHeap(data)
print(heap._draw_heap())
heap.heapfy()
print(heap._draw_heap())

print('-------')
print(heap.remove_top())
print(heap.remove_top())
print(heap.remove_top())
print(heap.remove_top())
print(heap.remove_top())
print(heap.remove_top())
