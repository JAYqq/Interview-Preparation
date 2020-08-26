class Solution:
    def process(self,sr):
        res=[]
        for ch in sr:
            res.append(ch)
        return res
    def commonChars(self , chars ):
        # write code here
        minl=float('INF')
        res=[]
        target=""
        after_arr=[]
        for item in chars:
            after_arr.append(self.process(item))
        for item in after_arr:
            l=len(item)
            if l<minl:
                minl=l
                target=item[::]
        for char in target:
            flag=True
            for i in range(len(after_arr)):
                if char not in after_arr[i]:
                    flag=False
                    break
                index=after_arr[i].index(char)
                after_arr[i].pop(index)
            if flag:
                res.append(char)
        res.sort()
        return "".join(res)
so=Solution()
print(so.commonChars(["bella","labe","roller"]))