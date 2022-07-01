def solution(numbers):
    answer = []
    
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
        else:
            binary = '0' + bin(n)[2:]
            idx = binary.rfind('0')
            binary = list(binary)
            binary[idx] = '1'
            binary[idx+1] = '0'
            
            n = int("".join(binary), 2)
            answer.append(n)
    
    return answer