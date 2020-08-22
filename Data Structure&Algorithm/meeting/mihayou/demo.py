def main():
    arr=input().split()
    nums=[]
    temp1=arr[0].split('/')
    temp2=arr[2].split('/')
    nums.append(temp1)
    nums.append(temp2)
    if arr[1]=='+' or arr[1]=='-':
        fenmu=int(nums[0][1])*int(nums[1][1])
        nums[0][0],nums[1][0]=int(int(nums[0][0])*int(nums[1][1])),int(int(nums[1][0])*int(nums[0][1]))
        nums[0][1],nums[1][1]=fenmu,fenmu
        if arr[1]=='+':
            fenzi=nums[0][0]+nums[1][0]
        else:
            fenzi=nums[0][0]-nums[1][0]
        if fenzi==0:
            ans="0"
        else:
            g=get_big(abs(fenzi),abs(fenmu))
            fenmu/=g
            fenzi/=g
            ans=str(int(fenzi))+'/'+str(int(fenmu))
    else:
        if arr[1]=='*':
            fenzi=int(nums[0][0])*int(nums[1][0])
            fenmu=int(nums[0][1])*int(nums[1][1])
        else:
            fenzi=int(nums[0][0])*int(nums[1][1])
            fenmu=int(nums[0][1])*int(nums[1][0])
        g=get_big(abs(fenzi),abs(fenmu))
        fenzi/=g
        fenmu/=g
        ans=str(int(fenzi))+'/'+str(int(fenmu))
    if fenzi%fenmu==0:
        ans=str(int(fenzi/fenmu))
    if ans.count('-')==2:
        ans=ans.replace('-','')
    print(ans)        
def get_big(a,b):
    m=min(a,b)
    for i in range(m,0,-1):
        if a%i==0 and b%i==0:
            return i
main()