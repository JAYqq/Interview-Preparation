# class Solution:
#     res=0
#     def CalulateMethodCount(self , num_money ):
#         # write code here
#         self.dfs(0,num_money)
#         return self.res
#     def dfs(self,ans,num_money):
#         if ans==num_money:
#             self.res+=1
#             return
#         for i in range(1,num_money+1):
#             if ans+i>num_money:
#                 break
#             self.dfs(ans+i,num_money)
# money=int(input())
# so=Solution()
# print(so.CalulateMethodCount(money))

class Solution:
    res=0
    def CalulateMethodCount(self , num_money ):
        # write code here
        def dfs(ans,num_money):
            if ans==num_money:
                self.res+=1
                return
            for i in range(1,num_money+1):
                if ans+i>num_money:
                    break
                dfs(ans+i,num_money)
        num_money=int(input())
        dfs(0,num_money)
        return self.res
so=Solution()
print(so.CalulateMethodCount(2))