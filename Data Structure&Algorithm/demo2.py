import sys
def judge(dic):
    for item in dic:
        if len(dic[item])>1:
            return True
    return False
def main():
    dic={}
    n=int(input())
    arr=list(map(int,input().strip().split(" ")))
    length=len(arr)
    for i in range(length):
        if not dic.get(arr[i]):
            dic[arr[i]]=[i]
        else:
            dic[arr[i]].append(i)
    while judge(dic):
        for item in arr:
            if(len(dic[item])>1):
                arr[(dic[item][0])]=-1
                dic[item].pop(0)
                arr[dic[item][0]]*=2
                temp=arr[dic[item][0]]
                if not dic.get(temp):
                    dic[temp]=[dic[item][0]]
                else:
                    dic[temp].append(dic[item][0])
                dic[item].pop(0)
    brr=[]
    for item in arr:
        if item!=-1:
            brr.append(item)
    return brr
res=main()
for item in res:
    print(item,end=" ")

# def main():
#     arr=list(map(int,input().strip().split(" ")))
#     dic={}
#     for item in arr:
#         if not dic.get(item):
#             dic[item]=1
#         else:
#             dic[item]+=1
#     for item in dic:
#         if dic[item]>1:
#             while dic[item]>1:
#                 if not dic.get(dic[item]*2):
#                     dic[item*2]=1
#                 else:
#                     dic[item*2]+=1
#                 dic[item]-=2

                