dic={}
def main():
    n=int(input())
    while n:
        num=int(input())
        if num==1:
            print(1)
            n-=1
            continue
        ans=helper(num)
        print(ans)
        # print(dic)
        n-=1
def get_count(a,b):
    ans=0
    base=a
    while a:
        if dic.get(a):
            ans+=dic[a]
            break
        ans+=a%10
        a=a//10
    dic[base]=ans
    # print(base,ans)
    ans2=0
    base=b
    while b:
        if dic.get(b):
            ans2+=dic[b]
            break
        ans2+=b%10
        b=b//10
    dic[base]=ans2
    return ans+ans2
def helper(num):
    count=0
    mid=num//2
    for i in range(mid+1):
        count=max(count,get_count(i,num-i))
    return count
main()