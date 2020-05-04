def longestPalindrome(s):
    start,end=0,0
    length=len(s)
    if length<1:
        return ""
    for i in range(length):
        len1=getLength(s,i,i)
        len2=getLength(s,i,i+1)
        max_len=max(len1,len2)
        if max_len>end-start:
            start=i-((max_len-1)>>1)
            end=i+((max_len)>>1)
            # print(start,end)
    return s[start:end+1]

def getLength(s,i,j):
    l,r=i,j
    while l>=0 and r<len(s) and s[i]==s[j]:
        l-=1
        r+=1
    return r-l-1

dd=longestPalindrome("babad")