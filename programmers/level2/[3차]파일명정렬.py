def solution(files):
    answer = []
    sorted_files = []
    
    for f in files:
        head, number, tail = "", "", ""
        flag = False
        
        for i, ch in enumerate(f):
            if ch.isdigit():
                number += ch
                flag = True
            elif not flag:
                head += ch
            else:
                tail = f[i:]
                break
                   
        sorted_files.append([head, number, tail])
        
    sorted_files.sort(key=lambda x: (x[0].upper(), int(x[1])))
    
    return [''.join(t) for t in sorted_files]   