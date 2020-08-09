def dfs(target, key):
    if target == key:
        return True
    for item in dic[target]:
        return dfs(item, key)
dic = {}

def main():
    n, m = list(map(int, input().split(" ")))
    global dic
    ans = 0
    while m:
        a, b = list(map(int, input().split(" ")))
        if a == b:
            continue
        if a not in dic:
            dic[a] = [b]
        else:
            dic[a].append(b)
        m -= 1
    print(dic)
    for key in dic:
        for item in dic[key]:
            if dfs(item, key):
                ans += 1
main()
