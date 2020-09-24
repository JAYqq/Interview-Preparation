def main():
    arr=list(map(int,input().split()))
    se=set(arr)
    if len(se)!=len(arr):
        print("true")
    else:
        print("false")
main()