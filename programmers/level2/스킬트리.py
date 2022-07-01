def solution(skill, skill_trees):
    answer = 0
    
    for sk in skill_trees:
        skill_list = ""
        for i in sk:
            if i in skill:
                skill_list += i
        
        if skill_list == skill[:len(skill_list)]:
            answer += 1
    return answer