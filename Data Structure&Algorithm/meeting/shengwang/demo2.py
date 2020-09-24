def main():
    n=int(input())
    sr=1
    while sr%n!=0:
        sr=sr*10+1
    print(len(str(sr)))
main()