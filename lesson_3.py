# импортируем библиотеку tkinter
from tkinter import *


# создаём окно 
window = Tk()
# меняем название окна
window.title("lesson 2")
# меняем ширину и высоту окна 
window.geometry("600x500")



lab_text2 = Label(text="text2" , bg="#310505", fg="#f6ff47" , font=("Algerian" , 18)) 
lab_text2.place(x=300, y=200)



# пример дополнительного окна
window_mini = Toplevel()
window_mini.geometry("400x200")
lab_text_mini = Label(window_mini, text="i mini" , bg="#FFFF50", fg="#6f15af" , font=("Algerian" , 18)) 
lab_text_mini.place(x=200, y=100)




def fun_1():
    global window_mini
    window_mini = Toplevel()
    window_mini.geometry("400x200")
    lab_text_mini = Label(window_mini, text="i mini" , bg="#FFFF50", fg="#6f15af" , font=("Algerian" , 18)) 
    lab_text_mini.place(x=200, y=100)
    




but1 = Button(text="button1", command=fun_1)
but1.place(x=100, y=400)







window.mainloop()
print("end")