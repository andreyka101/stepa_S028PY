from tkinter import *


# создаём окно 
window = Tk()
# меняем название окна
window.title("lesson 11")
# меняем ширину и высоту окна 
window.config(bg="#353535")


window.geometry("600x500+300+200")

# создаём текст через Label
# bg= цвет фона 
# fg= цвет текстам
# font = шрифт и размер текста 
lab_text1 = Label(text="555444" , bg="#569dcb" , font=("",20)) 
lab_text1.place(x=200,y=200)



def fun():
    # получаем положение Checkbutton
    print(num_check.get())
    check_but_1.config(text=num_check.get())
    if(num_check.get()):
        window.config(bg="#D2D2D2")
        # if(window2 != None):
        #     window2.config(bg="#D2D2D2")
    else:
        window.config(bg="#353535")


def fun2():
    print(num_check.get())



# в num_check хранится положения Checkbutton
num_check = IntVar()
# num_check = BooleanVar()
# Checkbutton это кнопка с двумя положениями
check_but_1 = Checkbutton(variable=num_check , text= "check 1" , command= fun)
check_but_1.place(x= 200 , y=300)


num_check2 = IntVar()
check_but_2 = Checkbutton(variable=num_check2 , text= "check 1" , command= fun2)
check_but_2.place(x= 200 , y=400)









window.mainloop()