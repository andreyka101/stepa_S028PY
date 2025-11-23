def fun_1(a):
    return 5*a

# num = fun_1(3)
# print(num)




lam_1 = lambda x: x * 7
# print(lam_1(2))



num = 4
lam_2 = lambda: num * 7
# print(lam_2())




lam_3 = lambda: "text"
# print(lam_3())




lam_4 = lambda x,y: x * y
# print(lam_4(2,5))




answer = ""
if(num%2 == 0):
    answer = "yes"
else:
    answer = "not"
# print(answer)




answer2 = "yes" if(num%2 == 0) else "not"
print(answer2)

print("yes" if(num%2 == 0) else "not")




lam_5 = lambda x,y = 5: y if(y >= x) else 0
# print(lam_5(4))




print((lambda x: x * 7)(3))




arr = [5,98,3,6,7,93,4]
# for i in range(len(arr)):
#     print("i =" , i)
#     print("arr[i] =" , arr[i])

# for i in arr:
#     print("i =" , i)





# def fun_map(x):
#     print(x*2)
#     return x*2
# arr = [1,2,3,4,5,6]
# arr_map = list(map(fun_map , arr))
# print(arr_map)




def fun_map(x , y):
    return x*y

arr = [1,2,3,4,5,6]
arr_2 = [1,2,3,4,5,6]
arr_map = list(map(fun_map , arr , arr_2))
# print(arr_map)






arr = [1,2,3,4,5,6]
arr_map = list(map(lambda x: x+10 , arr))
# print(arr_map)






arr = [1,2,3,4,5,6]
arr_filter = list(filter(lambda y: y<4,arr))
print(arr_filter)



arr = [1,2,3,4,5,6]
arr_map = list(map(lambda x: x*2 , filter(lambda y: y%2 == 0,arr)))
print(arr_map)








