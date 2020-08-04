def main():
    str1=input()
    stack=[]
    res,num="",""
    ans=""
    for i in str1:
        if i<='9' and i>='0':
            num+=i
        if i>='A' and i<='Z':
            res+=i
        if i=='|':
            stack.append((res,num))
            res,num="",""
        if i==']':
            temp=stack.pop()
            res=temp[0]+int(temp[1])*res
    print(res)
main()
        
         