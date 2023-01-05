from tkinter import *
import random, time
#пропишем функцию рандомного выбора броска
def bros():
    x = random.choice(['b.png', 'b2.png', 'b3.png',
                       'b4.png', 'b5.png', 'b6.png'])
    return x
#пропишем функцию запуска с кнопки цикла броска с отображением картинки кубика
def img(event):
    global b1, b2
    for i in range(18):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.12)
        
root = Tk()
root.geometry('400x200')
root.title('Игра в кости. Сделай бросок!')
root.resizable(height = False, width=False)#зафиксировали окно
#добавляем иконку в проводник
root.iconphoto(True, PhotoImage(file=('iconka.png')))
#добавляем холст игрового стола
font = PhotoImage(file=('holst.png'))
Label(root, image=font).pack()
#добавляем метки для размещения кубика
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
#сделаем на клик мышки бросок+уберем метки
root.bind('<1>', img)
img('event')
root.mainloop()
