def solution(dartResult):
    result = []
    SDT = {'S': 1, 'D':2, 'T':3}
    dartResult = dartResult.replace('10', 'k')
    dartResult = list(dartResult)

    while dartResult:
            n = dartResult.pop(0)
            n = 10 if n=='k' else int(n)
            bonus = dartResult.pop(0)

            if dartResult:
                if dartResult[0] in ['*', '#']:
                    option = dartResult.pop(0)
            
                    if option == '*':
                        if not result:
                            result.append(pow(n,SDT[bonus])*2)
                        else:
                            prior = result.pop()
                            result.extend([prior*2, pow(n,SDT[bonus])*2])

                    elif option == '#':
                        result.append(-pow(n,SDT[bonus]))
        
                else:
                    result.append(pow(n, SDT[bonus]))
            
            else:
                result.append(pow(n, SDT[bonus]))
                break
        
    return sum(result)

#---other solution(using re)---

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer