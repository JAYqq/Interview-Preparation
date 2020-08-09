def main():
    st=input()
    left,right=0,len(st)-1
    se=[]
    flag=0
    while left<right:
        if flag==1:
            se.append(st[right+1:left:-1])
            break
        if st[left]!=st[right]:
            se.append(st[left])
            left+=1
            continue
        else:
            flag=1
            left+=1
            right-=1
    length=len(se)-1
    for i in range(length+1):
        st+=se[length-i]
    print(st)
main()