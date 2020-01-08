
lst = [1,1,1,3,3,3,2,4,4,5,6,7]

def calc_list(list):
    res = {}
    for obj in lst:
        if obj not in res:
            res[obj] = 0
        res[obj] += 1
    return res

print(calc_list(lst))
