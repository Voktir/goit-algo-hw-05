def b_search(arr: list, trgt: float):

    frst = 0
    lst = len(arr) - 1

    itrt = 0
    up_trgt = None
    
    while frst <= lst:
        itrt += 1
        mddl = (frst + lst) // 2
        if arr[mddl] == trgt:
            return (itrt, arr[mddl])
        elif trgt > arr[mddl]:
            frst = mddl + 1
        else:
            up_trgt = arr[mddl]
            lst = mddl - 1

    return (itrt, up_trgt)

r = b_search([2.3, 3.9, 4.5, 10.1, 12.9], 7.1)      
print(r)