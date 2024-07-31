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

# Тестуємо різні умови:
arrs = [    
    ([2.3, 3.9, 4.5, 10.1, 12.9], 17.1),   # Немає "верхньої межі"
    ([2.3, 3.9, 4.5, 10.1, 12.9], 7.1),    # У середині
    ([2.3, 3.9, 4.5, 10.1, 12.9], 10.1),   # Ціль дорівнює пошуковому елементу
    ([2.3, 3.9, 4.5, 10.1, 12.9], 1.1),    # Менше меншого елемента
    ([], 3.5)                              # Порожній масив
]

for arr, trgt in arrs:
    print(b_search(arr, trgt))