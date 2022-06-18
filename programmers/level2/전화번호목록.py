def solution(phone_book):
    answer = True
    hash_map = {}
    
    for number in phone_book:
        hash_map[number] = 1
        
    for number in phone_book:
        temp = ""
        for n in number:
            temp += n
            if temp in hash_map and temp != number:
                answer = False
    return answer