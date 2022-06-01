info = input()

str_list = []
sum_n = 0

for x in info:
    if '0' <= x <= '9':
        sum_n += int(x)
    else:
        str_list.append(x)

if sum_n != 0:
    answer = "".join(sorted(str_list)) + str(sum_n)
else:
    answer = "".join(sorted(str_list)) 
    
print(answer)