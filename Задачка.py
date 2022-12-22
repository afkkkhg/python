def isSublist(small,larger):
    for i in small:
        if not i in larger:
            return False
    return True


sm = [1,2,3]
lg = [-1,0,1,2,3,4,5]
print(isSublist(sm,lg))