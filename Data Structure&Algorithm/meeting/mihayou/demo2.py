def main():
    m,n=list(map(int,input().split()))
    arr=[]
    for i in range(m):
        temp=list(map(int,input().split()))
        arr.append(temp)
    dic={}
    for item in arr:
        for i in range(n):

