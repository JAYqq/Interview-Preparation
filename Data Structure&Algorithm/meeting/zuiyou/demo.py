# dic = {'a': 36, 'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54, 't': 55,
#        'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61}
dic = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29,
       'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35}

def main():
    str_num = input()
    index = 0
    ans = 0
    flag=1
    if str_num and str_num[0]=='-':
        flag=-1
        str_num=str_num.replace("-","")
    for item in str_num[::-1]:
        if item <= '9' and item >= '0':
            ans += pow(36, index)*int(item)
        elif item <= 'z' and item >= 'a':
            ans += pow(36, index)*dic[item]
        else:
            ans = 0
            break
        index+=1
    if ans*flag>9223372036854775807:
        print(9223372036854775807)
    else:
        print(ans*flag)
main()
