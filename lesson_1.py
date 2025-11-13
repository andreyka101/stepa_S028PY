# импортируем библиотеку tkinter
from tkinter import *


# создаём окно 
window = Tk()
# меняем название окна
window.title("lesson 11")
# меняем ширину и высоту окна 


window.geometry("600x500+300+200")

# создаём текст через Label
# bg= цвет фона 
# fg= цвет текстам
# font = шрифт и размер текста 
lab_text1 = Label(text="555444" , bg="#569dcb") 
# placе - позиция и размер элемента
lab_text1.place(x=300, y=400 , width= 100 , height=50)

lab_text2 = Label(text="text2" , bg="#310505", fg="#f6ff47" , font=("Algerian" , 18)) 
lab_text2.place(x=300, y=200)






def fun_1():
    print("click")
    window.title("text")

    # изменяем позицию lab_text_1
    lab_text2.place(x=400, y=300)

    # # меняем ширину и высоту окна
    # window.geometry("500x300")
    print(window.geometry())

    # с помощью метода configure или config можно изменить параметры объекта 
    but1.config(bg="#53ff44",font=("Algerian" , 23) , )
    lab_text2.configure(text="click button" ,font=("Algerian" , 23) , bg="#5bfaff")


    # global window2
    # window2 = Tk()

but1 = Button(text="button1", command=fun_1)
but1.place(x=100, y=400)







window.mainloop()
print("end")



# задача 1
# Создайте игру clicker, при нажатии на кнопку должно число увеличиваться на один

# задача 2
# Сделать игру найди кнопку, при нажатии на кнопку она перемещается в случайное место по координатам ,но не выходит за границы окна