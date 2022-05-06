from itertools import combinations

def minimum_check(minimum_key_index, curr_idx):
    flag = False 
    for key in minimum_key_index:
        if not (set(key) - set(list(curr_idx))):
            flag = True
            break
    return flag

def solution(relation):
    answer = 0
    row_length = len(relation[0])
    len_tuples = len(relation)
    
    minimum_key_idx = []

    for num in range(1, row_length+1):
        idx = list(combinations(range(row_length), num))

        for comb in idx:
            flag = minimum_check(minimum_key_idx, comb)
            if flag:
                continue
            subset = []
            for info in relation: 
                tmp = []
                for j, elem in enumerate(info): 
                    if j in comb:
                        tmp.append(elem)
                tmp = tuple(tmp)
                subset.append(tmp)  
 
            subset = set(subset)
            if len_tuples == len(subset):
                minimum_key_idx.append(list(comb))

    return len(minimum_key_idx)