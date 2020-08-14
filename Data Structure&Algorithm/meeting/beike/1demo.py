def main():
    length=int(input())
    str1=input()
    ans=0
    if length%2==1:
        left,right=length//2,length//2
    else:
        left,right=length//2-1,length//2
    while left>=0 and right<length:
        if str1[left]!=str1[right]:
            ans+=1
        left-=1
        right+=1
    print(ans)
main()