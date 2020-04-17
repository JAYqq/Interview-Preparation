### 字符串匹配问题

问题就是一串source="abcdabcb"，对应有一个target=“abcb”，从source中找出连续匹配target的字符串的第一个字母下标，这里的下表就是4

一般思路是循环source，找到首字母相同的，然后遍历target查看之后是否一一对应，时间复杂度是O(n*m)

KMP的优化地方是比如当：

![20180519185025412.png](https://i.loli.net/2019/08/18/x1O57syelr2ZCGu.png)

循环到这时候发现不匹配，如果按一般思路往后移一格继续循环，就会浪费时间，所以直接可以跳到：

![20180519185502368.png](https://i.loli.net/2019/08/18/pjmVtTbLc6YUPDg.png)

所以用一个**next**数组记录source中第i个字母前面是否有重复的子字符串，没有则为-1，有就记录下往前移动几个。**k**则是用来记录最长的相同子字符串长度-1。

注意寻找相同字串都是相对于从头开始的第一个字符（参考博客）

理解代码的重要点在于理解：

1. next  里面放的是第i个字符是否匹配并且需要移动的距离，所以next[i]+1=包括第i个字符前面最大相同字串长度
2. k在下面getnext的循环中，每次的next[i]=k

code：

```python
class KMP():
    def __init__(self,str1,str2):
        self.next={}
        self.k=None
        self.target=str1
        self.source=str2
    def getNext(self):
        self.next[0]=-1
        self.k=self.next[0]
        for i in range(1,len(self.target)):
            while(self.k>-1 and self.target[i]!=self.target[self.k+1]):
                self.k=self.next[self.k]
            #如果退出来就说明是k==-1或者找到匹配的了
            if self.target[i]==self.target[self.k+1]:
                self.k+=1
            self.next[i]=self.k
    def KMP(self):
        self.getNext()
        k=self.next[0]
        # print(self.next)
        for i in range(len(self.source)):
            while(k>-1 and self.target[k+1]!=self.source[i]):
                # print(k)
                k=self.next[k]
            if self.target[k+1]==self.source[i]:
                k+=1
            # print("k:",k)
            if k==len(self.target)-1:
                return i-len(self.target)+1
        return -1
if __name__=="__main__":
    kmp=KMP("abad","axadabacabad")
    ans=kmp.KMP()
    print(ans)
```

参考资料：

<https://blog.csdn.net/l577217/article/details/80373822>

<https://www.cnblogs.com/ZuoAndFutureGirl/p/9028287.html> 

