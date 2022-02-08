def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_list = []

    while truck_weights:
        truck = truck_weights.pop(0)
        if bridge_length == len(bridge_list):
            del bridge_list[-1]
      
        if sum(bridge_list)+truck <= weight:
            bridge_list.insert(0, truck)
        else:
            bridge_list.insert(0, 0)
            truck_weights.insert(0, truck)
  
        answer += 1

        if not bridge_list:
            break

    return answer + bridge_length