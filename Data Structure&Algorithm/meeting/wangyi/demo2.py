def main():
    x=int(input())
    ans=0
    ans+=int(x/5)
    if x%5!=0:
        ans+=1
    print(ans,end=" ")
main()