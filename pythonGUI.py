'''
                                        -----EdPiy-----

Autores:
    Axel Mercado Gasque
    Armando Montaño González
'''
#Librerias/Paquetes requeridos
from tkinter import *
import random
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO

# Funciones
def n_pregunta():
    global l_value1
    global l_operator
    global l_value2
    global e_ans
    global l_opcion
    global b_pregunta
    global l_check

    def check_ans():
        ans = e_ans.get()
        print(ans)
        if oper == "+":
            if val + val1 == int(ans):
                l_check.config(text = "Correcto!", fg = "green")
            else:
                l_check.config(text = "Incorrecto!", fg = "red")

        elif oper == "x":
            if val * val1 == int(ans):
                l_check.config(text = "Correcto!", fg = "green")
            else:
                l_check.config(text = "Incorrecto!", fg = "red")

        elif oper == "-":
            if val - val1 == int(ans):
                l_check.config(text = "Correcto!", fg = "green")
            else:
                l_check.config(text = "Incorrecto!", fg = "red")

        else:
            if val // val1 == int(ans):
                l_check.config(text = "Correcto!", fg = "green")
            else:
                l_check.config(text = "Incorrecto!", fg = "red")

    arr_signs = ['+', '-', 'x', '/']
    global val
    val = str(random.randint(5, 20))
    l_value1 = Label(frame3, text=val)
    global val1
    val1 = str(random.randint(1, 5))
    global oper
    oper = arr_signs[random.randint(0, 3)]
    l_operator = Label(frame3, text=oper)
    l_value2 = Label(frame3, text=val1)
    e_ans = Entry(frame3, text="Respuesta")
    b_respuesta = Button(frame3, text="Ok", command=check_ans)
    l_check = Label(frame3, text="Correcto o Incorrecto")
    l_opcion = Label(frame3, text="Desea otra pregunta")
    b_pregunta = Button(frame3, text="Si", command=destroy_pregunta)
    button_back1 = Button(frame3, text="Anterior", padx=50, pady=20, command=from_arit_showstart)
    val = int(val)
    val1 = int(val1)

    frame3.grid(row=0, column=0)
    l_value1.grid(row=0, column=0)
    l_operator.grid(row=0, column=1)
    l_value2.grid(row=0, column=2)
    e_ans.grid(row=0, column=3)
    b_respuesta.grid(row=1, column=3)
    l_check.grid(row=2, column=3)
    l_opcion.grid(row=1, column=0)
    b_pregunta.grid(row=2, column=0)


def destroy_pregunta():
    l_value1.destroy()
    l_operator.destroy()
    l_value2.destroy()
    e_ans.destroy()
    l_opcion.destroy()
    b_pregunta.destroy()

    n_pregunta()

def from_geo_showstart():
    frame4.grid_forget()
    start()


def from_arit_showstart():
    frame3.grid_forget()
    start()

def geo_again():
    frame4.grid_forget()
    geometria()

def geometria():
    frame2.grid_forget()
    global frame4
    frame4 = Frame(main)

    figuras = ['Triángulo Equilátero', 'Cuadrado', 'Rectangulo', 'Trapecio']
    i = random.randint(0, 3)

    if i == 0:
        def check_area():
            if int(e_area.get()) == (h * b / 2):
                t_check_area.config(text = 'Correcto!', fg = 'green')
            else:
                t_check_area.config(text='Incorrecto!', fg = 'red')
        def check_per():
            if int(e_per.get()) == (b * 3):
                t_check_per.config(text = 'Correcto!', fg = 'green')
            else:
                t_check_per.config(text='Incorrecto!', fg = 'red')
        global b
        b = random.randint(1, 20)
        global h
        h = random.randint(1, 20)
        label_t_b = Label(frame4, text= 'Base: ' + str(b))
        label_preg = Label(frame4, text = '¿Desea otra pregunta?')
        b_si = Button(frame4, text = 'Si', command = geo_again)
        label_t_h = Label(frame4, text = 'Altura: ' + str(h))
        label_area = Label(frame4, text = 'Area: ')
        label_per = Label(frame4, text = 'Perímetro: ')
        e_area = Entry(frame4)
        e_per = Entry(frame4)
        global t_check_area
        global t_check_per
        t_check_area = Label(frame4, text = 'Area: Correcto o Incorrecto')
        t_check_per = Label(frame4, text='Perímetro: Correcto o Incorrecto')
        button_check_area = Button(frame4, text = 'Ok', command = check_area)
        button_check_per = Button(frame4, text='Ok', command = check_per)
        col = ['red', 'blue', 'yellow', 'black', 'green', 'pink']
        canvas_r = Canvas(frame4, width=190, height=190, bg='white')
        canvas_r.grid(row=8, column=3)
        canvas_r.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        b_si.grid(row = 4, column = 0)
        label_preg.grid(row = 3, column = 0)
        t_check_area.grid(row = 3, column = 1, columnspan = 3)
        t_check_per.grid(row = 3, column = 5)
        button_check_area.grid(row=4, column=1, columnspan = 3)
        button_check_per.grid(row=4, column=5 )
        label_t_b.grid(row = 1, column = 0)
        label_t_h.grid(row = 1, column = 1)
        label_area.grid(row = 1, column = 2)
        label_per.grid(row=1, column=4)
        e_area.grid(row = 1, column = 3)
        e_per.grid(row=1, column=5)

    elif i == 1:
        def check_area():
            if int(e_area.get()) == (l * l):
                c_check_area.config(text = 'Correcto!', fg = 'green')
            else:
                c_check_area.config(text='Incorrecto!', fg = 'red')
        def check_per():
            if int(e_per.get()) == (l * 4):
                c_check_per.config(text = 'Correcto!', fg = 'green')
            else:
                c_check_per.config(text='Incorrecto!', fg = 'red')
        global l
        l = random.randint(1, 20)
        label_lado = Label(frame4, text='Lado: ' + str(l))
        label_area = Label(frame4, text='Area: ')
        label_per = Label(frame4, text='Perímetro: ')
        e_area = Entry(frame4)
        e_per = Entry(frame4)
        label_preg = Label(frame4, text='¿Desea otra pregunta?')
        b_si = Button(frame4, text='Si', command = geo_again)
        global c_check_area
        global c_check_per
        c_check_area = Label(frame4, text='Area: Correcto o Incorrecto')
        c_check_per = Label(frame4, text='Perímetro: Correcto o Incorrecto')
        button_check_area = Button(frame4, text='Ok', command = check_area)
        button_check_per = Button(frame4, text='Ok', command = check_per)
        col = ['red','blue','yellow','black','green','pink']
        canvas_r = Canvas(frame4, width = 150, height = 150, bg = col[random.randint(0,5)])
        canvas_r.grid(row = 8, column = 3)

        c_check_area.grid(row = 3, column = 2)
        c_check_per.grid(row = 3, column = 4)
        button_check_area.grid(row = 4, column = 2)
        button_check_per.grid(row = 4, column = 4)
        b_si.grid(row=4, column=0)
        label_preg.grid(row=3, column=0)
        label_lado.grid(row=1, column=0)
        label_area.grid(row=1, column=1)
        label_per.grid(row=1, column=3)
        e_area.grid(row=1, column=2)
        e_per.grid(row=1, column=4)

    elif i == 2:
        def check_area():
            if int(e_area.get()) == (largo * altura):
                r_check_area.config(text = 'Correcto!', fg = 'green')
            else:
                r_check_area.config(text='Incorrecto!', fg = 'red')
        def check_per():
            if int(e_per.get()) == (largo + largo + altura + altura):
                r_check_per.config(text = 'Correcto!', fg = 'green')
            else:
                r_check_per.config(text='Incorrecto!', fg = 'red')

        global largo
        global altura
        largo = random.randint(1, 20)
        altura = random.randint(1, 20)
        label_lado = Label(frame4, text='Lado: ' + str(largo))
        label_altura1 = Label(frame4, text='Altura: ' + str(altura))
        label_area = Label(frame4, text='Area: ')
        label_per = Label(frame4, text='Perímetro: ')
        e_area = Entry(frame4)
        e_per = Entry(frame4)
        label_preg = Label(frame4, text='¿Desea otra pregunta?')
        b_si = Button(frame4, text='Si', command = geo_again)
        global r_check_area
        global r_check_per
        r_check_area = Label(frame4, text='Area: Correcto o Incorrecto')
        r_check_per = Label(frame4, text='Perímetro: Correcto o Incorrecto')
        button_check_area = Button(frame4, text='Ok', command = check_area)
        button_check_per = Button(frame4, text='Ok', command = check_per)
        col = ['red', 'blue', 'yellow', 'black', 'green', 'pink']
        canvas_r = Canvas(frame4, width=170, height=160, bg= 'white')
        canvas_r.grid(row=8, column=3)
        canvas_r.create_rectangle(10,10,160,120, fill = col[random.randint(0,5)])

        r_check_area.grid(row=3, column=3)
        r_check_per.grid(row=3, column=5)
        button_check_area.grid(row=4, column=3)
        button_check_per.grid(row=4, column=5)
        b_si.grid(row=4, column=0)
        label_preg.grid(row=3, column=0)
        label_lado.grid(row=1, column=0)
        label_altura1.grid(row = 1, column = 1)
        label_area.grid(row=1, column=2)
        label_per.grid(row=1, column=4)
        e_area.grid(row=1, column=3)
        e_per.grid(row=1, column=5)

    else:
        def check_area():
            if int(e_area.get()) == ((B + base) * altura_t)/2:
                tr_check_area.config(text='Correcto!', fg='green')
            else:
                tr_check_area.config(text='Incorrecto!', fg='red')

        def check_per():
            if int(e_per.get()) == (B + base + lado1 + lado2):
                tr_check_per.config(text='Correcto!', fg='green')
            else:
                tr_check_per.config(text='Incorrecto!', fg='red')
        global B,base,altura_t,lado1,lado2
        B = random.randint(1, 20)
        base = random.randint(1, 20)
        altura_t = random.randint(1, 20)
        lado1 = random.randint(1, 20)
        lado2 = random.randint(1, 20)

        label_Base = Label(frame4, text='Base mayor: ' + str(B))
        label_base = Label(frame4, text='Base menor: ' + str(base))
        label_altura = Label(frame4, text='Altura: ' + str(altura_t))
        label_lado1 = Label(frame4, text='Lado 1: ' + str(lado1))
        label_lado2 = Label(frame4, text='Lado 2: ' + str(lado2))
        label_area = Label(frame4, text='Area: ')
        label_per = Label(frame4, text='Perímetro: ')
        e_area = Entry(frame4)
        e_per = Entry(frame4)
        label_preg = Label(frame4, text='¿Desea otra pregunta?')
        b_si = Button(frame4, text='Si', command = geo_again)
        global tr_check_area, tr_check_per
        tr_check_area = Label(frame4, text='Area: Correcto o Incorrecto')
        tr_check_per = Label(frame4, text='Perímetro: Correcto o Incorrecto')
        button_check_area = Button(frame4, text='Ok', command = check_area )
        button_check_per = Button(frame4, text='Ok', command = check_per)

        tr_check_area.grid(row=3, column=2)
        tr_check_per.grid(row=3, column=4)
        button_check_area.grid(row=4, column=2)
        button_check_per.grid(row=4, column=4)
        label_preg.grid(row = 3, column = 0)
        b_si.grid(row = 4, column = 0)
        label_Base.grid(row = 1, column = 0)
        label_base.grid(row=1, column=1)
        label_altura.grid(row=1, column=2)
        label_lado1.grid(row=1, column=3)
        label_lado2.grid(row=1, column=4)
        label_area.grid(row = 2, column = 1)
        e_area.grid(row = 2, column = 2)
        label_per.grid(row = 2, column = 3)
        e_per.grid(row = 2, column = 4)

    label_figura = Label(frame4, text = figuras[i])
    button_back1 = Button(frame4, text="Anterior", padx=50, pady=20, command=from_geo_showstart)

    label_figura.grid(row = 0, column = 0)
    button_back1.grid(row = 5, column = 0)

    frame4.grid(row = 0, column = 0)

def aritmetica():
    frame2.grid_forget()
    global frame3
    frame3 = Frame(main)

    global l_value1
    global l_operator
    global l_value2
    global e_ans
    global l_opcion
    global b_pregunta
    global b_respuesta
    global l_check

    def check_ans():
        ans = e_ans.get()
        print(ans)
        if oper == "+":
            if val + val1 == int(ans):
                l_check.config(text = "Correcto!", fg = "black")
            else:
                l_check.config(text = "Incorrecto!", fg = "red")

        elif oper == "x":
            if val * val1 == int(ans):
                l_check.config(text = "Correcto!", fg = "black")
            else:
                l_check.config(text = "Incorrecto!", fg = "red")

        elif oper == "-":
            if val - val1 == int(ans):
                l_check.config(text = "Correcto!", fg = "black")
            else:
                l_check.config(text = "Incorrecto!", fg = "red")

        else:
            if val // val1 == int(ans):
                l_check.config(text = "Correcto!", fg = "black")
            else:
                l_check.config(text = "Incorrecto!", fg = "red")


    arr_signs = ['+', '-', 'x', '/']
    global val
    val = str(random.randint(5, 20))
    l_value1 = Label(frame3, text=val)
    global val1
    val1 = str(random.randint(1, 5))
    global oper
    oper = arr_signs[random.randint(0, 3)]
    l_operator = Label(frame3, text=oper)
    l_value2 = Label(frame3, text=val1)
    e_ans = Entry(frame3, text="Respuesta")
    b_respuesta = Button(frame3, text = "Ok", command = check_ans)
    l_check = Label(frame3, text = "Correcto o Incorrecto")
    l_opcion = Label(frame3, text="Desea otra pregunta")
    b_pregunta = Button(frame3, text="Si", command=destroy_pregunta)
    button_back1 = Button(frame3, text="Anterior", padx=50, pady=20, command=from_arit_showstart)
    val = int(val)
    val1 = int(val1)

    frame3.config(bg='deep sky blue')
    frame3.grid(row = 0, column = 0)
    l_value1.grid(row=0, column=0)
    l_operator.grid(row=0, column=1)
    l_value2.grid(row=0, column=2)
    e_ans.grid(row=0, column=3)
    b_respuesta.grid(row = 1, column = 3)
    l_check.grid(row = 2, column = 3)
    l_opcion.grid(row=1, column=0)
    b_pregunta.grid(row=2, column=0)
    button_back1.grid(row=3, column=1)

def show_frame1():
    frame2.grid_forget()
    frame1.grid(row = 0, column = 0)

def show_frame2():
    frame2.pack()

def start():  # Oculta frame1 y crea otra frame con las secciones
    frame1.grid_forget()
    global frame2
    frame2 = Frame(main)

    img_url2 = "http://pluspng.com/img-png/math-symbols-png-math-symbols-600.png"
    response2 = requests.get(img_url2)
    img_data2 = response2.content
    img2 = ImageTk.PhotoImage(Image.open(BytesIO(img_data2)))
    panel2 = Label(frame2, image=img2, bg="deep sky blue")
    panel2.image = img2

    button_back = Button(frame2, text="Anterior", padx=50, pady=20, command=show_frame1)
    button_geo = Button(frame2, text="Geometría", padx=50, pady=20, command=geometria)
    button_arit = Button(frame2, text="Aritmetica", padx=50, pady=20, command=aritmetica)

    frame2.config(bg='deep sky blue')
    frame2.grid(row=0, column=0)
    button_geo.grid(row=1, column=0)
    button_back.grid(row=2, column=0)
    button_arit.grid(row=1, column=1)
    panel2.grid(row = 3, column = 2)

main = Tk()
main.geometry("950x650")  # define tamaño de ventana
main.title("Proyecto Integrador")  # define título de ventana
global frame1
frame1 = Frame(main)  # se agrega un frame para almacenar contenido de primera ventana

img_url = "http://atlanticschools.net/wp-content/uploads/2017/05/PISA_LOGO-04.png"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel = Label(frame1, image=img, bg="RoyalBlue2")
panel.image = img
#panel.pack(side="bottom", fill="both", expand="yes")

label_title = Label(frame1, text="Proyecto Integrador.", fg="blue")
label_app = Label(frame1, text="Mejora tu rendimiento en la prueba PISA.", fg="blue")
label_names = Label(frame1,
                    text="Desarrollado por: Armando Montaño, Axel Mercado, Fabrizzio Ramírez, Fernando Cuellar y Fernando Fernández.",
                    fg="blue")
button_start = Button(frame1, text="Comienza a practicar", padx=50, pady=60, command=start)

frame1.config(bg='brown2')
main.config(bg='#abd7e5')
panel.grid(row = 1, column = 0) #se agrega el label de la imágen y su ubicación en la ventana
label_title.grid(row=2, column=0)
label_app.grid(row=3, column=0)
label_names.grid(row=4, column=0)
button_start.grid(row=5, column=0)
frame1.grid(row=0, column=0)

main.mainloop()
