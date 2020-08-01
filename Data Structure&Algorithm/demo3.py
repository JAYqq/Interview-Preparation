def main():
    dic={}
    input1=list(map(int,input().strip().split(" ")))
    input2=list(map(int,input().strip().split(" ")))
    length=len(input2)
    #先将可以以m为底的所有积木放到list中，m与list的对应关系放到map
    for i in range(length-1):
        for j in range(i+1,length):
            if input1[i]&input1[j]==input1[j]:
                if not dic.get(input1[i]):
                    dic[input1[i]]=[input1[j]]
                else:
                    dic[input1[i]].append(input1[j])
    #写不完了，然后就是跟邻接表一样的操作
    for item in dic:

