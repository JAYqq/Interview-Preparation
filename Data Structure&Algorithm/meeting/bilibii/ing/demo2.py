def main(num1):
    num=1024-num1
    ans=0
    ans+=(num//64)
    num=num%64
    ans+=(num//16)
    num=num%16
    ans+=(num//4)
    num=num%4
    ans+=num
    return ans
print(main(200))

