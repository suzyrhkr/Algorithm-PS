def j_similarity(a, b):
    if not a and not b:
        return 1*65536

    similarity = 0
    intersection_set, union_set = [], a+b
    b_copy = b.copy()
    
    for ch in a:
        if ch in b_copy:
            intersection_set.append(ch)
            b_copy.remove(ch)

    for i in intersection_set:
        if i in union_set:
            union_set.remove(i)

    similarity = len(intersection_set)/len(union_set)

    return int(similarity*65536)


def solution(str1, str2):
    str1, str2 = list(str1.lower()), list(str2.lower())
    set_str1, set_str2 = [], []
    
    for i, ch in enumerate(str1[:-1]):
        s = "".join([str1[i], str1[i+1]])
        if s.isalpha():
            set_str1.append(s)

    for i, ch in enumerate(str2[:-1]):
        s = "".join([str2[i], str2[i+1]])
        if s.isalpha():
            set_str2.append(s)

    return j_similarity(set_str1, set_str2)

#---other solution---

def solution(str1, str2):
    str1_arr = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].lower().isalpha()]
    str2_arr = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].lower().isalpha()]

    union, intersection = 0, 0
    for element in set(str1_arr + str2_arr):
        union += max(str1_arr.count(element), str2_arr.count(element))
        intersection += min(str1_arr.count(element), str2_arr.count(element))

    if union == 0:
        return 65536
    answer = (intersection / union) * 65536
    return int(answer)
