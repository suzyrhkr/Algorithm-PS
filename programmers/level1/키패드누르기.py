import math
def num_index(phone, number):
    for row in range(len(phone)):
        for col in range(len(phone[row])):
            if number == phone[row][col]:
                return row, col

def solution(numbers, hand):
    answer = ''
    phone = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
    left_num, right_num = '*', '#'

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_num = num

        elif num in [3, 6, 9]:
            answer += 'R'
            right_num = num

        elif num in [2, 5, 8, 0]:
            left_row, left_col = num_index(phone, left_num)
            right_row, right_col = num_index(phone, right_num)
            num_row, num_col = num_index(phone, num)

            left_distance = abs(left_row - num_row) + abs(left_col - num_col)
            right_distance = abs(right_row - num_row) + abs(right_col - num_col)

            if left_distance < right_distance:
                answer += 'L'
                left_num = num

            elif right_distance < left_distance:
                answer += 'R'
                right_num = num

            else:
                if hand=='right':
                    answer += 'R'
                    right_num = num
                else:
                    answer += 'L'
                    left_num = num
            
    return answer