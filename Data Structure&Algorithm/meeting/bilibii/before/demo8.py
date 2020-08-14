class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s,index):
            res,num="",0
            while index<len(s):
                if s[index]<='9' and s[index]>='0':
                    num=num*10+int(s[index])
                elif s[index]=='[':
                    index,str1=dfs(s,index+1)
                    res+=num*str1
                    num=0
                elif s[index]==']':
                    return index,res
                else:
                    res+=s[index]
                index+=1
            return res
        return dfs(s,0)