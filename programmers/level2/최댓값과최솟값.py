def solution(s):
    answer = ''
    nums = s.split(' ')
    integer_nums = [eval(n) for n in nums]
    answer = str(min(integer_nums)) + " " + str(max(integer_nums))
    
    return answer