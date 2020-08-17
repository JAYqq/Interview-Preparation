def main():
    raw=input()
    raw.replace(""," ")
    words=raw.strip('"').split(" ")
    undo_stack=[]
    words_stack=[]
    for item in words:
        if item!="undo" and item!="redo":
            words_stack.append(item)
        elif item=="undo" and words_stack:
            temp=words_stack.pop()
            undo_stack.append(temp)
        elif item=="redo" and undo_stack:
            temp=undo_stack.pop()
            words_stack.append(temp)
    print(" ".join(words_stack))
main()
