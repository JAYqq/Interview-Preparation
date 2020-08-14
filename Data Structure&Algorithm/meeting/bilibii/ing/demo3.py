class Solution:
    def Game24Points(self , arr ):
        self.arr=arr
        self.simbles=['+','-','*','/']
        temp=[]
        self.dfs(temp)
    def dfs(self,temp):
        if len(temp)==3:
            return self.calcu(temp)
        for item in self.simbles:
            temp.append(item)
            return self.dfs(temp)
    def calcu(self,temp):
        ans=0
        if temp[0] in ['+','-'] and temp[1] in ['+','-']:
            if temp[0]=='+':
                ans+=self.arr[0]+self.arr[1]
            else:
                ans+=self.arr[0]-self.arr[1]
            if temp[2] in ['*','/']:
                if temp[2]=='*':
                    ans+=self.arr[2]*self.arr[3]
                else:
                    ans+=self.arr[2]/self.arr[3]
                if ans==24:
                    return True
                return False
        if temp[0] in ['+','-'] and temp[1] in ['*','/']:
            if temp[2] in ['*','/']:
                if temp[1]=='*' and temp[2]=='/':
                    ans+=self.arr[1]*self.arr[2]/self.arr[3]
                if temp[1]=='/' and temp[2]=='*':
                    ans+=self.arr[1]/self.arr[2]*self.arr[3]
                if temp[1]=='*' and temp[2]=='*':
                    ans+=self.arr[1]*self.arr[2]*self.arr[3]
                if temp[1]=='/' and temp[2]=='/':
                    ans+=self.arr[1]*self.arr[2]/self.arr[3]
                if temp[0]=='+':
                    ans=self.arr[0]+ans
                else:
                    ans=self.arr[0]-ans
                if ans==24:
                    return True
                return False
        if temp[0] in ['*','/'] and temp[1] in ['+','-']:
            if temp[0]=='*':
                ans+=self.arr[0]*self.arr[1]
            else:
                ans+=self.arr[0]/self.arr[1]
            if temp[2] in ['+','-']:
                if temp[1] == '+':
                    if temp[2]=='-':
                        ans+=self.arr[2]-self.arr[3]
                    else:
                        ans+=self.arr[2]+self.arr[3]
                if temp[1] == '-':
                    if temp[2]=='-':
                        ans=ans-self.arr[2]-self.arr[3]
                    else:
                        ans=ans-self.arr[2]+self.arr[3]
                if ans==24:
                    return True
            if temp[2] in ['*','/']:
                if temp[1]=='+':
                    if temp[2]=='*':
                        ans+=self.arr[2]*self.arr[3]
                    else:
                        ans+=self.arr[2]/self.arr[3]
                if temp[1]=='-':
                    if temp[2]=='*':
                        ans-=self.arr[2]*self.arr[3]
                    else:
                        ans-=self.arr[2]/self.arr[3]
        if temp[0] in ['*','/'] and temp[1] in ['*','/']:
            if temp[0]=='*' and temp


        
