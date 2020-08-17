class Solution:
    def CalulateMethodCount(self , num_money ):
        ans=1
        if num_money==0:
            return 1
        for i in range(1,num_money):
            ans*=2;
        return ans;
so=Solution()
print(so.CalulateMethodCount(2))
