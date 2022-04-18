def solution(s):
    answer, length = len(s), len(s)
    s = list(s)
    
    for i in range(1, (length//2)+1):
        str_s = s.copy()
        curr = str_s[:i]
        repeat = []
        cnt = 0

        while str_s:
            if curr == str_s[:i]:
                cnt += 1
                del str_s[:i]
                if not str_s:
                    repeat.append([cnt, curr])      
            else:
                repeat.append([cnt, curr])
                curr = str_s[:i]
                cnt = 0
                
        result = ""
        for num, word in repeat:
            if num != 1:
                result += str(num)
            result += "".join(word)
        answer = min(answer, len(result))
    return answer