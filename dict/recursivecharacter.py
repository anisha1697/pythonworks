pattern="ABCAABD"
recursive_word={}
for p in pattern:
    if p in recursive_word:
        print("first recursive",{p})
        break
    else:
        recursive_word[p]=1
pattern="ABCAABD"
secondrecursive={}
recursive=[]
for p in pattern:
    if p in secondrecursive:
        recursive.append(p)
        print("second recursive",{p})
    else:
        secondrecursive[p]=1

