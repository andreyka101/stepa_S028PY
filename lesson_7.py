# arr = [5,3,6,85,8,-9,10]
arr = [1,2,3]

# def my_max(local_arr):
#     num_max = local_arr[0]
#     for el in local_arr:
#         # print(el)
#         if(el > num_max):
#             print(el , num_max)
#             num_max = el
#     return num_max


# print(my_max(arr))





# def my_sum(local_arr):
#     num_sum = 0
#     for i in range(len(local_arr)):
#         num_sum += local_arr[i]
#     return num_sum

# print(my_sum(arr))




import random


# создание двухмерного списка
arr2 = []
num = 0
for x in range(3):
    # через цикл в списке arr2 добавляем пустые списки
    arr2.append([])
    for y in range(3):
        num += 1
        # через цикл в цикле добавляем числа в пустые списки
        arr2[x].append(num)

        # через цикл в цикле добавляем рандомные числа в пустые списки
        # arr2[x].append(random.randint(1,9))
print(arr2)
# print(arr2[0])
# print(arr2[0][5])




def my_sum_X(local_arr):
    arr_sum = []
    # for x - перебираем списки 
    for x in range(len(local_arr)):
        num_sum = 0
        # for y - перебираем числа в списках 
        for y in range(len(local_arr[x])):
            # local_arr[индекс списка][индекс числа в списке]
            num_sum += local_arr[x][y]
        arr_sum.append(num_sum)
            
    return arr_sum

print(my_sum_X(arr2))




def my_sum_Y(local_arr):
    arr_sum = []
    # for x - перебираем списки 
    for x in range(len(local_arr)):
        num_sum = 0
        # for y - перебираем числа в списках 
        for y in range(len(local_arr[x])):
            # local_arr[индекс списка][индекс числа в списке]
            num_sum += local_arr[y][x]
        arr_sum.append(num_sum)

        
            
    return arr_sum

print(my_sum_Y(arr2))















