def main(s):
    simble=[]
    for i in range(len(s)):
        if s[i]=='[' or s[i]=='(' or s[i]=='{':
            simble.append(s[i])
        else:
            if not simble:
                return False
            if s[i]==')':
                if simble[-1]!='(':
                    return False
                else:
                    simble.pop()
            if s[i]==']':
                if simble[-1]!='[':
                    return False
                else:
                    simble.pop()
            if s[i]=='}':
                if simble[-1]!='{':
                    return False
                else:
                    simble.pop()
    if simble:
        return False
    return True
s=input()
print(main(s))