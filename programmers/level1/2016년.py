def solution(a, b):
    daya = 0
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = sum(month[:a-1]) + b

    return week[days%7]