from collections import deque

class Node:
    def __init__(self):
        self.prev = -1 
        self.is_delete = False # 삭제 여부
        
def solution(n, k, cmd):
    # 1. 링크드리스트 초기화
    node_list = [Node() for _ in range(n)] # 노드 리스트 생성
    for i in range(n - 1):
        node_list[i].next = i + 1 # i 번째 노드의 next는 i+1
        node_list[i + 1].prev = i # i+1 번째 노드의 prev는 i
 
    del_stack = deque()
 
    cur = k # 현재 가리키고 있는 노드의 인덱스
    for c in cmd:
 
        if len(c) > 1:
            c, move_size = c.split(' ')
            move_size = int(move_size)
 
        if c == "U":
            for i in range(move_size):
                cur = node_list[cur].prev 
        elif c == "D":
            for i in range(move_size):
                cur = node_list[cur].next 
        elif c == "C":
            node_list[cur].is_delete = True 
            del_stack.append(cur) 
 
            prev_node = node_list[cur].prev
            next_node = node_list[cur].next
 
            if prev_node != -1: 
                node_list[prev_node].next = next_node 
            if next_node != -1: 
                node_list[next_node].prev = prev_node 
                cur = next_node 
            else: 
                cur = prev_node 

        elif c == "Z":
            del_node = del_stack.pop() 
            node_list[del_node].is_delete = False 
 
            prev_node = node_list[del_node].prev 
            next_node = node_list[del_node].next 
 
            if prev_node != -1: 
                node_list[prev_node].next = del_node 
            if next_node != -1:
                node_list[next_node].prev = del_node 
 
    answer = []
    for i in range(n):
        if node_list[i].is_delete: answer.append("X")
        else: answer.append("O")
    return "".join(answer)