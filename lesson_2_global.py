# num = 8
# def fun():
#     print("num =" , num)
# fun()




# def fun():
#     numFun = 3

    # print("fun() =" , numFun)
# fun()
# print(numFun)



# num = 8
# def fun():
#     num = 5
#     print("fun() =" , num)
# fun()
# print(num)



num = 8
def fun():
    global num , numFun
    num = 5
    numFun= 20
    print("fun() =" , num)
fun()
print(num)
print("numFun =" , numFun)


