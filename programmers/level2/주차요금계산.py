from collections import defaultdict
import math

def calculate_time(start, end):
    s_h, s_m = map(int, start.split(":"))
    e_h, e_m = map(int, end.split(":"))
    s = s_h*60 + s_m
    e = e_h*60 + e_m
    return e-s

def solution(fees, records):
    answer = {}
    infos = defaultdict(list)

    for record in records:
        time, number, r_type = record.split(" ")
        infos[number].append([r_type, time])
        
    for car in infos:
        if len(infos[car]) % 2 != 0:
            infos[car].append(["OUT", "23:59"])
            
        # 누적 주차 시간 계산
        interval_time = 0
        for i in range(0, len(infos[car]), 2):
            interval_time += calculate_time(infos[car][i][1], infos[car][i+1][1])
        cost = 0
        if interval_time <= fees[0]:
            cost = fees[1]
        else:
            cost = fees[1] + math.ceil((interval_time - fees[0])/fees[2]) * fees[-1]
        
        answer[car] = cost
        
    answer = sorted(answer.items())
    
    return [cost[1] for cost in answer]