import tkinter as tk
from tkinter import *
from tkinter import messagebox

def calc_exit():
    window.destroy()

def calculate_bmi():
   kg = int(weight_tf.get())
   m = int(height_tf.get())/100
   bmi = kg/(m*m)
   bmi = round(bmi, 1)
 
   if bmi < 18.5:
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
   elif (bmi > 18.5) and (bmi < 24.9):
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
   elif (bmi > 24.9) and (bmi < 29.9):
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
   else:
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')  

window = Tk()
window.title ("Калькулятор индекса массы тела (ИМТ)")
window.geometry('400x300')

frame = Frame(
   window, #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10 #Задаём отступ по вертикали.
)
frame.pack(expand=True) #Не забываем позиционировать виджет в окне. Здесь используется метод pack. С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, созданный для него.
height_lb = Label(
   frame,
   text="Введите свой рост (в см)  "
)
weight_lb = Label(
   frame,
   text="Введите свой вес (в кг)  ",
)
age_lb = Label(
   frame,
   text="Введите свой возраст  "
)
weight_lb.grid(row=4, column=1)
height_lb.grid(row=3, column=1)
age_lb.grid(row=2, column=1)
age_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
age_tf.grid(row=2, column=2)
height_tf = Entry(
   frame, #Используем нашу заготовку с настроенными отступами.
)
height_tf.grid(row=3, column=2)
weight_tf = Entry(
   frame,
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
   frame, #Заготовка с настроенными отступами.
   text='Рассчитать ИМТ', #Надпись на кнопке.
    command=calculate_bmi
)
cal_btn.grid(row=5, column=2) #Размещаем кнопку в ячейке, расположенной ниже, чем наши надписи, но во втором столбце, то есть под ячейками для ввода информации.

cal_btnn = Button(
   frame, #Заготовка с настроенными отступами.
   text='Закрыть программу', #Надпись на кнопке.
    command=calc_exit
)
cal_btnn.grid(row=6, column=2)

window.mainloop()
