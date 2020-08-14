def main():
    all_str=input().split(" ")
    all_pairs=all_str[-1].split(all_str[0])
    rows=len(all_pairs)
    print(rows)
    for pairs in all_pairs:
        k,v=pairs.split(all_str[1])
        if not k or not v:
            continue
        print(k,v)
main()
