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




# ввод данных
entry_input = Entry(font=("",18))
entry_input.place(x=200,y=270)





def fun_1():
    # получаем текст Entry
    print(entry_input.get())
    lab_text1.config(text=entry_input.get())
    window.geometry(entry_input.get())


but1 = Button(text="button1", command=fun_1)
but1.place(x=100, y=400)





def fun_1():
    # очищаем Entry
    # entry_input.delete(0,4)
    entry_input.delete(0,END)

but2 = Button(text="button del text", command=fun_1)
but2.place(x=180, y=400)







window.mainloop()