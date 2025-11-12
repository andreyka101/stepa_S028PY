from tkinter import *


window = Tk()
window.title("lesson")
window.geometry("700x500")




lab_text1 = Label(text="555444" , bg="#569dcb") 
lab_text1.place(x=300, y=400 , width= 100 , height=50)

lab_text2 = Label(text="text2" , bg="#310505", fg="#f6ff47" , font=("Algerian" , 18)) 
lab_text2.place(x=300, y=200)






def fun_1():
    print("click")
    window.title("text")
    lab_text2.place(x=400, y=300)
    # window.geometry("500x300")
    but1.config(bg="#53ff44",font=("Algerian" , 23))
    lab_text2.configure(text="click button" ,font=("Algerian" , 23) , bg="#5bfaff")


    # global window2
    # window2 = Tk()

but1 = Button(text="button1", command=fun_1)
but1.place(x=100, y=400)







window.mainloop()
print("end")
