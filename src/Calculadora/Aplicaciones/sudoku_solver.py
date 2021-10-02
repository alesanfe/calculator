import numpy as np
from tkinter import *

cambiador = {"": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

def sudoku():

    sudoku = Tk()

    sudoku.resizable(False, False)

    sudoku.title("Resolver sudoku")

    sudoku.iconbitmap('../data/calcu.ico')

    miFrame = Frame(sudoku)

    miFrame.pack()

    # Ajustes:
    
    tipo_letra = "Calculator"
    tamaño = 30 
    tipo_bordes = RAISED
    tamaño_bordes=0
    distancia_x = 1
    distancia_y = 1
    anclamiento = "nsew"
    fondo = "black"
    color_letra = "white"
    posición = "center"
    ancho=2

    # Fila 1.

    numeroPantalla1_1 = StringVar()
    pantalla1_1 = Entry(miFrame, textvariable=numeroPantalla1_1, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla1_1.grid(row=1, column=1, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla1_1.config(background=fondo, fg=color_letra, justify=posición, width=ancho)

    numeroPantalla1_2 = StringVar()
    pantalla1_2 = Entry(miFrame, textvariable=numeroPantalla1_2, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla1_2.grid(row=1, column=2, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla1_2.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla1_3 = StringVar()
    pantalla1_3 = Entry(miFrame, textvariable=numeroPantalla1_3, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla1_3.grid(row=1, column=3, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla1_3.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea1=Label(miFrame, text="|")
    línea1.grid(row=1,column=4, sticky="e", padx=1, pady=1)
 
    numeroPantalla1_4 = StringVar()
    pantalla1_4 = Entry(miFrame, textvariable=numeroPantalla1_4, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla1_4.grid(row=1, column=5, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla1_4.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla1_5 = StringVar()
    pantalla1_5 = Entry(miFrame, textvariable=numeroPantalla1_5, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla1_5.grid(row=1, column=6, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla1_5.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla1_6 = StringVar()
    pantalla1_6 = Entry(miFrame, textvariable=numeroPantalla1_6, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla1_6.grid(row=1, column=7, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla1_6.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea2=Label(miFrame, text="|")
    línea2.grid(row=1,column=8, sticky="e", padx=1, pady=1)
 
    numeroPantalla1_7 = StringVar()
    pantalla1_7 = Entry(miFrame, textvariable=numeroPantalla1_7, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla1_7.grid(row=1, column=9, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla1_7.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla1_8 = StringVar()
    pantalla1_8 = Entry(miFrame, textvariable=numeroPantalla1_8, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla1_8.grid(row=1, column=10, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla1_8.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla1_9 = StringVar()
    pantalla1_9 = Entry(miFrame, textvariable=numeroPantalla1_9, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla1_9.grid(row=1, column=11, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla1_9.config(background=fondo, fg=color_letra, justify=posición, width=ancho)

    # Fila 2.
 
    numeroPantalla2_1 = StringVar()
    pantalla2_1 = Entry(miFrame, textvariable=numeroPantalla2_1, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla2_1.grid(row=2, column=1, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla2_1.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla2_2 = StringVar()
    pantalla2_2 = Entry(miFrame, textvariable=numeroPantalla2_2, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla2_2.grid(row=2, column=2, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla2_2.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla2_3 = StringVar()
    pantalla2_3 = Entry(miFrame, textvariable=numeroPantalla2_3, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla2_3.grid(row=2, column=3, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla2_3.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea3=Label(miFrame, text="|")
    línea3.grid(row=2,column=4, sticky="e", padx=1, pady=1)
 
    numeroPantalla2_4 = StringVar()
    pantalla2_4 = Entry(miFrame, textvariable=numeroPantalla2_4, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla2_4.grid(row=2, column=5, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla2_4.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla2_5 = StringVar()
    pantalla2_5 = Entry(miFrame, textvariable=numeroPantalla2_5, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla2_5.grid(row=2, column=6, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla2_5.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla2_6 = StringVar()
    pantalla2_6 = Entry(miFrame, textvariable=numeroPantalla2_6, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla2_6.grid(row=2, column=7, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla2_6.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea4=Label(miFrame, text="|")
    línea4.grid(row=2,column=8, sticky="e", padx=1, pady=1)
 
    numeroPantalla2_7 = StringVar()
    pantalla2_7 = Entry(miFrame, textvariable=numeroPantalla2_7, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla2_7.grid(row=2, column=9, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla2_7.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla2_8 = StringVar()
    pantalla2_8 = Entry(miFrame, textvariable=numeroPantalla2_8, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla2_8.grid(row=2, column=10, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla2_8.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla2_9 = StringVar()
    pantalla2_9 = Entry(miFrame, textvariable=numeroPantalla2_9, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla2_9.grid(row=2, column=11, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla2_9.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    # Fila 3.
 
    numeroPantalla3_1 = StringVar()
    pantalla3_1 = Entry(miFrame, textvariable=numeroPantalla3_1, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla3_1.grid(row=3, column=1, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla3_1.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla3_2 = StringVar()
    pantalla3_2 = Entry(miFrame, textvariable=numeroPantalla3_2, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla3_2.grid(row=3, column=2, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla3_2.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla3_3 = StringVar()
    pantalla3_3 = Entry(miFrame, textvariable=numeroPantalla3_3, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla3_3.grid(row=3, column=3, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla3_3.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea5=Label(miFrame, text="|")
    línea5.grid(row=3,column=4, sticky="e", padx=1, pady=1)
 
    numeroPantalla3_4 = StringVar()
    pantalla3_4 = Entry(miFrame, textvariable=numeroPantalla3_4, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla3_4.grid(row=3, column=5, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla3_4.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla3_5 = StringVar()
    pantalla3_5 = Entry(miFrame, textvariable=numeroPantalla3_5, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla3_5.grid(row=3, column=6, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla3_5.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla3_6 = StringVar()
    pantalla3_6 = Entry(miFrame, textvariable=numeroPantalla3_6, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla3_6.grid(row=3, column=7, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla3_6.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea6=Label(miFrame, text="|")
    línea6.grid(row=3,column=8, sticky="e", padx=1, pady=1)
 
    numeroPantalla3_7 = StringVar()
    pantalla3_7 = Entry(miFrame, textvariable=numeroPantalla3_7, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla3_7.grid(row=3, column=9, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla3_7.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla3_8 = StringVar()
    pantalla3_8 = Entry(miFrame, textvariable=numeroPantalla3_8, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla3_8.grid(row=3, column=10, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla3_8.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla3_9 = StringVar()
    pantalla3_9 = Entry(miFrame, textvariable=numeroPantalla3_9, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla3_9.grid(row=3, column=11, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla3_9.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    # Fila 4 (lineas).
 
    línea7=Label(miFrame, text="---------")
    línea7.grid(row=4,column=1, sticky="e", padx=1, pady=1)
 
    línea8=Label(miFrame, text="---------")
    línea8.grid(row=4,column=2, sticky="e", padx=1, pady=1)
 
    línea9=Label(miFrame, text="---------")
    línea9.grid(row=4,column=3, sticky="e", padx=1, pady=1)
 
    línea10=Label(miFrame, text="---------")
    línea10.grid(row=4,column=5, sticky="e", padx=1, pady=1)
 
    línea11=Label(miFrame, text="---------")
    línea11.grid(row=4,column=6, sticky="e", padx=1, pady=1)
 
    línea12=Label(miFrame, text="---------")
    línea12.grid(row=4,column=7, sticky="e", padx=1, pady=1)
 
    línea13=Label(miFrame, text="---------")
    línea13.grid(row=4,column=9, sticky="e", padx=1, pady=1)
    
    línea14=Label(miFrame, text="---------")
    línea14.grid(row=4,column=10, sticky="e", padx=1, pady=1)
 
    línea15=Label(miFrame, text="---------")
    línea15.grid(row=4,column=11, sticky="e", padx=1, pady=1)
    
    # Fila 5.

    numeroPantalla4_1 = StringVar()
    pantalla4_1 = Entry(miFrame, textvariable=numeroPantalla4_1, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla4_1.grid(row=5, column=1, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla4_1.config(background=fondo, fg=color_letra, justify=posición, width=ancho)

    numeroPantalla4_2 = StringVar()
    pantalla4_2 = Entry(miFrame, textvariable=numeroPantalla4_2, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla4_2.grid(row=5, column=2, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla4_2.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla4_3 = StringVar()
    pantalla4_3 = Entry(miFrame, textvariable=numeroPantalla4_3, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla4_3.grid(row=5, column=3, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla4_3.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea16=Label(miFrame, text="|")
    línea16.grid(row=5,column=4, sticky="e", padx=1, pady=1)
 
    numeroPantalla4_4 = StringVar()
    pantalla4_4 = Entry(miFrame, textvariable=numeroPantalla4_4, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla4_4.grid(row=5, column=5, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla4_4.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla4_5 = StringVar()
    pantalla4_5 = Entry(miFrame, textvariable=numeroPantalla4_5, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla4_5.grid(row=5, column=6, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla4_5.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla4_6 = StringVar()
    pantalla4_6 = Entry(miFrame, textvariable=numeroPantalla4_6, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla4_6.grid(row=5, column=7, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla4_6.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea17=Label(miFrame, text="|")
    línea17.grid(row=5,column=8, sticky="e", padx=1, pady=1)
 
    numeroPantalla4_7 = StringVar()
    pantalla4_7 = Entry(miFrame, textvariable=numeroPantalla4_7, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla4_7.grid(row=5, column=9, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla4_7.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla4_8 = StringVar()
    pantalla4_8 = Entry(miFrame, textvariable=numeroPantalla4_8, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla4_8.grid(row=5, column=10, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla4_8.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla4_9 = StringVar()
    pantalla4_9 = Entry(miFrame, textvariable=numeroPantalla4_9, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla4_9.grid(row=5, column=11, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla4_9.config(background=fondo, fg=color_letra, justify=posición, width=ancho)

    # Fila 6.
 
    numeroPantalla5_1 = StringVar()
    pantalla5_1 = Entry(miFrame, textvariable=numeroPantalla5_1, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla5_1.grid(row=6, column=1, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla5_1.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla5_2 = StringVar()
    pantalla5_2 = Entry(miFrame, textvariable=numeroPantalla5_2, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla5_2.grid(row=6, column=2, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla5_2.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla5_3 = StringVar()
    pantalla5_3 = Entry(miFrame, textvariable=numeroPantalla5_3, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla5_3.grid(row=6, column=3, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla5_3.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea18=Label(miFrame, text="|")
    línea18.grid(row=6,column=4, sticky="e", padx=1, pady=1)
 
    numeroPantalla5_4 = StringVar()
    pantalla5_4 = Entry(miFrame, textvariable=numeroPantalla5_4, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla5_4.grid(row=6, column=5, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla5_4.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla5_5 = StringVar()
    pantalla5_5 = Entry(miFrame, textvariable=numeroPantalla5_5, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla5_5.grid(row=6, column=6, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla5_5.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla5_6 = StringVar()
    pantalla5_6 = Entry(miFrame, textvariable=numeroPantalla5_6, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla5_6.grid(row=6, column=7, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla5_6.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea19=Label(miFrame, text="|")
    línea19.grid(row=6,column=8, sticky="e", padx=1, pady=1)
 
    numeroPantalla5_7 = StringVar()
    pantalla5_7 = Entry(miFrame, textvariable=numeroPantalla5_7, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla5_7.grid(row=6, column=9, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla5_7.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla5_8 = StringVar()
    pantalla5_8 = Entry(miFrame, textvariable=numeroPantalla5_8, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla5_8.grid(row=6, column=10, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla5_8.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla5_9 = StringVar()
    pantalla5_9 = Entry(miFrame, textvariable=numeroPantalla5_9, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla5_9.grid(row=6, column=11, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla5_9.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    # Fila 7.
 
    numeroPantalla6_1 = StringVar()
    pantalla6_1 = Entry(miFrame, textvariable=numeroPantalla6_1, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla6_1.grid(row=7, column=1, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla6_1.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla6_2 = StringVar()
    pantalla6_2 = Entry(miFrame, textvariable=numeroPantalla6_2, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla6_2.grid(row=7, column=2, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla6_2.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla6_3 = StringVar()
    pantalla6_3 = Entry(miFrame, textvariable=numeroPantalla6_3, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla6_3.grid(row=7, column=3, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla6_3.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea20=Label(miFrame, text="|")
    línea20.grid(row=7,column=4, sticky="e", padx=1, pady=1)
 
    numeroPantalla6_4 = StringVar()
    pantalla6_4 = Entry(miFrame, textvariable=numeroPantalla6_4, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla6_4.grid(row=7, column=5, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla6_4.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla6_5 = StringVar()
    pantalla6_5 = Entry(miFrame, textvariable=numeroPantalla6_5, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla6_5.grid(row=7, column=6, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla6_5.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla6_6 = StringVar()
    pantalla6_6 = Entry(miFrame, textvariable=numeroPantalla6_6, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla6_6.grid(row=7, column=7, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla6_6.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea21=Label(miFrame, text="|")
    línea21.grid(row=7,column=8, sticky="e", padx=1, pady=1)
 
    numeroPantalla6_7 = StringVar()
    pantalla6_7 = Entry(miFrame, textvariable=numeroPantalla6_7, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla6_7.grid(row=7, column=9, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla6_7.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla6_8 = StringVar()
    pantalla6_8 = Entry(miFrame, textvariable=numeroPantalla6_8, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla6_8.grid(row=7, column=10, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla6_8.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla6_9 = StringVar()
    pantalla6_9 = Entry(miFrame, textvariable=numeroPantalla6_9, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla6_9.grid(row=7, column=11, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla6_9.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
    
    # Fila 8 (lineas).
 
    línea22=Label(miFrame, text="---------")
    línea22.grid(row=8,column=1, sticky="e", padx=1, pady=1)
 
    línea23=Label(miFrame, text="---------")
    línea23.grid(row=8,column=2, sticky="e", padx=1, pady=1)
 
    línea24=Label(miFrame, text="---------")
    línea24.grid(row=8,column=3, sticky="e", padx=1, pady=1)
 
    línea25=Label(miFrame, text="---------")
    línea25.grid(row=8,column=5, sticky="e", padx=1, pady=1)
 
    línea26=Label(miFrame, text="---------")
    línea26.grid(row=8,column=6, sticky="e", padx=1, pady=1)
 
    línea27=Label(miFrame, text="---------")
    línea27.grid(row=8,column=7, sticky="e", padx=1, pady=1)
 
    línea28=Label(miFrame, text="---------")
    línea28.grid(row=8,column=9, sticky="e", padx=1, pady=1)
    
    línea29=Label(miFrame, text="---------")
    línea29.grid(row=8,column=10, sticky="e", padx=1, pady=1)
 
    línea30=Label(miFrame, text="---------")
    línea30.grid(row=8,column=11, sticky="e", padx=1, pady=1)
    
    # Fila 9.

    numeroPantalla7_1 = StringVar()
    pantalla7_1 = Entry(miFrame, textvariable=numeroPantalla7_1, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla7_1.grid(row=9, column=1, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla7_1.config(background=fondo, fg=color_letra, justify=posición, width=ancho)

    numeroPantalla7_2 = StringVar()
    pantalla7_2 = Entry(miFrame, textvariable=numeroPantalla7_2, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla7_2.grid(row=9, column=2, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla7_2.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla7_3 = StringVar()
    pantalla7_3 = Entry(miFrame, textvariable=numeroPantalla7_3, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla7_3.grid(row=9, column=3, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla7_3.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea31=Label(miFrame, text="|")
    línea31.grid(row=9,column=4, sticky="e", padx=1, pady=1)
 
    numeroPantalla7_4 = StringVar()
    pantalla7_4 = Entry(miFrame, textvariable=numeroPantalla7_4, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla7_4.grid(row=9, column=5, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla7_4.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla7_5 = StringVar()
    pantalla7_5 = Entry(miFrame, textvariable=numeroPantalla7_5, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla7_5.grid(row=9, column=6, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla7_5.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla7_6 = StringVar()
    pantalla7_6 = Entry(miFrame, textvariable=numeroPantalla7_6, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla7_6.grid(row=9, column=7, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla7_6.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea32=Label(miFrame, text="|")
    línea32.grid(row=9,column=8, sticky="e", padx=1, pady=1)
 
    numeroPantalla7_7 = StringVar()
    pantalla7_7 = Entry(miFrame, textvariable=numeroPantalla7_7, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla7_7.grid(row=9, column=9, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla7_7.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla7_8 = StringVar()
    pantalla7_8 = Entry(miFrame, textvariable=numeroPantalla7_8, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla7_8.grid(row=9, column=10, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla7_8.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla7_9 = StringVar()
    pantalla7_9 = Entry(miFrame, textvariable=numeroPantalla7_9, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla7_9.grid(row=9, column=11, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla7_9.config(background=fondo, fg=color_letra, justify=posición, width=ancho)

    # Fila 10.
 
    numeroPantalla8_1 = StringVar()
    pantalla8_1 = Entry(miFrame, textvariable=numeroPantalla8_1, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla8_1.grid(row=10, column=1, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla8_1.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla8_2 = StringVar()
    pantalla8_2 = Entry(miFrame, textvariable=numeroPantalla8_2, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla8_2.grid(row=10, column=2, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla8_2.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla8_3 = StringVar()
    pantalla8_3 = Entry(miFrame, textvariable=numeroPantalla8_3, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla8_3.grid(row=10, column=3, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla8_3.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea33=Label(miFrame, text="|")
    línea33.grid(row=10,column=4, sticky="e", padx=1, pady=1)
 
    numeroPantalla8_4 = StringVar()
    pantalla8_4 = Entry(miFrame, textvariable=numeroPantalla8_4, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla8_4.grid(row=10, column=5, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla8_4.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla8_5 = StringVar()
    pantalla8_5 = Entry(miFrame, textvariable=numeroPantalla8_5, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla8_5.grid(row=10, column=6, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla8_5.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla8_6 = StringVar()
    pantalla8_6 = Entry(miFrame, textvariable=numeroPantalla8_6, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla8_6.grid(row=10, column=7, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla8_6.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea34=Label(miFrame, text="|")
    línea34.grid(row=10,column=8, sticky="e", padx=1, pady=1)
 
    numeroPantalla8_7 = StringVar()
    pantalla8_7 = Entry(miFrame, textvariable=numeroPantalla8_7, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla8_7.grid(row=10, column=9, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla8_7.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla8_8 = StringVar()
    pantalla8_8 = Entry(miFrame, textvariable=numeroPantalla8_8, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla8_8.grid(row=10, column=10, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla8_8.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla8_9 = StringVar()
    pantalla8_9 = Entry(miFrame, textvariable=numeroPantalla8_9, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla8_9.grid(row=10, column=11, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla8_9.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    # Fila 11.
 
    numeroPantalla9_1 = StringVar()
    pantalla9_1 = Entry(miFrame, textvariable=numeroPantalla9_1, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla9_1.grid(row=11, column=1, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla9_1.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla9_2 = StringVar()
    pantalla9_2 = Entry(miFrame, textvariable=numeroPantalla9_2, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla9_2.grid(row=11, column=2, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla9_2.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla9_3 = StringVar()
    pantalla9_3 = Entry(miFrame, textvariable=numeroPantalla9_3, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla9_3.grid(row=11, column=3, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla9_3.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea35=Label(miFrame, text="|")
    línea35.grid(row=11,column=4, sticky="e", padx=1, pady=1)
 
    numeroPantalla9_4 = StringVar()
    pantalla9_4 = Entry(miFrame, textvariable=numeroPantalla9_4, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla9_4.grid(row=11, column=5, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla9_4.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla9_5 = StringVar()
    pantalla9_5 = Entry(miFrame, textvariable=numeroPantalla9_5, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla9_5.grid(row=11, column=6, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla9_5.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla9_6 = StringVar()
    pantalla9_6 = Entry(miFrame, textvariable=numeroPantalla9_6, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla9_6.grid(row=11, column=7, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla9_6.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    línea36=Label(miFrame, text="|")
    línea36.grid(row=11,column=8, sticky="e", padx=1, pady=1)
 
    numeroPantalla9_7 = StringVar()
    pantalla9_7 = Entry(miFrame, textvariable=numeroPantalla9_7, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla9_7.grid(row=11, column=9, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla9_7.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla9_8 = StringVar()
    pantalla9_8 = Entry(miFrame, textvariable=numeroPantalla9_8, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla9_8.grid(row=11, column=10, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla9_8.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
 
    numeroPantalla9_9 = StringVar()
    pantalla9_9 = Entry(miFrame, textvariable=numeroPantalla9_9, font=(tipo_letra, tamaño), relief=tipo_bordes, borderwidth=tamaño_bordes)
    pantalla9_9.grid(row=11, column=11, padx=distancia_x, pady=distancia_y, sticky=anclamiento)
    pantalla9_9.config(background=fondo, fg=color_letra, justify=posición, width=ancho)
    
    def hacer_lista():
        lista = [[cambiador[pantalla1_1.get()], cambiador[pantalla1_2.get()], cambiador[pantalla1_3.get()], cambiador[pantalla1_4.get()], cambiador[pantalla1_5.get()], cambiador[pantalla1_6.get()], cambiador[pantalla1_7.get()], cambiador[pantalla1_8.get()], cambiador[pantalla1_9.get()]],
                 [cambiador[pantalla2_1.get()], cambiador[pantalla2_2.get()], cambiador[pantalla2_3.get()],cambiador[pantalla2_4.get()], cambiador[pantalla2_5.get()], cambiador[pantalla2_6.get()], cambiador[pantalla2_7.get()], cambiador[pantalla2_8.get()], cambiador[pantalla2_9.get()]],
                 [cambiador[pantalla3_1.get()], cambiador[pantalla3_2.get()], cambiador[pantalla3_3.get()],cambiador[pantalla3_4.get()], cambiador[pantalla3_5.get()], cambiador[pantalla3_6.get()], cambiador[pantalla3_7.get()], cambiador[pantalla3_8.get()], cambiador[pantalla3_9.get()]],
                 [cambiador[pantalla4_1.get()], cambiador[pantalla4_2.get()], cambiador[pantalla4_3.get()],cambiador[pantalla4_4.get()], cambiador[pantalla4_5.get()], cambiador[pantalla4_6.get()], cambiador[pantalla4_7.get()], cambiador[pantalla4_8.get()], cambiador[pantalla4_9.get()]],
                 [cambiador[pantalla5_1.get()], cambiador[pantalla5_2.get()], cambiador[pantalla5_3.get()],cambiador[pantalla5_4.get()], cambiador[pantalla5_5.get()], cambiador[pantalla5_6.get()], cambiador[pantalla5_7.get()], cambiador[pantalla5_8.get()], cambiador[pantalla5_9.get()]],
                 [cambiador[pantalla6_1.get()], cambiador[pantalla6_2.get()], cambiador[pantalla6_3.get()],cambiador[pantalla6_4.get()], cambiador[pantalla6_5.get()], cambiador[pantalla6_6.get()], cambiador[pantalla6_7.get()], cambiador[pantalla6_8.get()], cambiador[pantalla6_9.get()]],
                 [cambiador[pantalla7_1.get()], cambiador[pantalla7_2.get()], cambiador[pantalla7_3.get()],cambiador[pantalla7_4.get()], cambiador[pantalla7_5.get()], cambiador[pantalla7_6.get()], cambiador[pantalla7_7.get()], cambiador[pantalla7_8.get()], cambiador[pantalla7_9.get()]],
                 [cambiador[pantalla8_1.get()], cambiador[pantalla8_2.get()], cambiador[pantalla8_3.get()],cambiador[pantalla8_4.get()], cambiador[pantalla8_5.get()], cambiador[pantalla8_6.get()], cambiador[pantalla8_7.get()], cambiador[pantalla8_8.get()], cambiador[pantalla8_9.get()]],
                 [cambiador[pantalla9_1.get()], cambiador[pantalla9_2.get()], cambiador[pantalla9_3.get()],cambiador[pantalla9_4.get()], cambiador[pantalla9_5.get()], cambiador[pantalla9_6.get()], cambiador[pantalla9_7.get()], cambiador[pantalla9_8.get()], cambiador[pantalla9_9.get()]]
                 ]
        return lista
    
    def devolver_lista(malla):
        numeroPantalla1_1.set(malla[0][0]); numeroPantalla1_2.set(malla[0][1]); numeroPantalla1_3.set(malla[0][2]); numeroPantalla1_4.set(malla[0][3]); numeroPantalla1_5.set(malla[0][4]); numeroPantalla1_6.set(malla[0][5]); numeroPantalla1_7.set(malla[0][6]); numeroPantalla1_8.set(malla[0][7]); numeroPantalla1_9.set(malla[0][8])
        numeroPantalla2_1.set(malla[1][0]); numeroPantalla2_2.set(malla[1][1]); numeroPantalla2_3.set(malla[1][2]); numeroPantalla2_4.set(malla[1][3]); numeroPantalla2_5.set(malla[1][4]); numeroPantalla2_6.set(malla[1][5]); numeroPantalla2_7.set(malla[1][6]); numeroPantalla2_8.set(malla[1][7]); numeroPantalla2_9.set(malla[1][8])
        numeroPantalla3_1.set(malla[2][0]); numeroPantalla3_2.set(malla[2][1]); numeroPantalla3_3.set(malla[2][2]); numeroPantalla3_4.set(malla[2][3]); numeroPantalla3_5.set(malla[2][4]); numeroPantalla3_6.set(malla[2][5]); numeroPantalla3_7.set(malla[2][6]); numeroPantalla3_8.set(malla[2][7]); numeroPantalla3_9.set(malla[2][8])
        numeroPantalla4_1.set(malla[3][0]); numeroPantalla4_2.set(malla[3][1]); numeroPantalla4_3.set(malla[3][2]); numeroPantalla4_4.set(malla[3][3]); numeroPantalla4_5.set(malla[3][4]); numeroPantalla4_6.set(malla[3][5]); numeroPantalla4_7.set(malla[3][6]); numeroPantalla4_8.set(malla[3][7]); numeroPantalla4_9.set(malla[3][8])
        numeroPantalla5_1.set(malla[4][0]); numeroPantalla5_2.set(malla[4][1]); numeroPantalla5_3.set(malla[4][2]); numeroPantalla5_4.set(malla[4][3]); numeroPantalla5_5.set(malla[4][4]); numeroPantalla5_6.set(malla[4][5]); numeroPantalla5_7.set(malla[4][6]); numeroPantalla5_8.set(malla[4][7]); numeroPantalla5_9.set(malla[4][8])
        numeroPantalla6_1.set(malla[5][0]); numeroPantalla6_2.set(malla[5][1]); numeroPantalla6_3.set(malla[5][2]); numeroPantalla6_4.set(malla[5][3]); numeroPantalla6_5.set(malla[5][4]); numeroPantalla6_6.set(malla[5][5]); numeroPantalla6_7.set(malla[5][6]); numeroPantalla6_8.set(malla[5][7]); numeroPantalla6_9.set(malla[5][8])
        numeroPantalla7_1.set(malla[6][0]); numeroPantalla7_2.set(malla[6][1]); numeroPantalla7_3.set(malla[6][2]); numeroPantalla7_4.set(malla[6][3]); numeroPantalla7_5.set(malla[6][4]); numeroPantalla7_6.set(malla[6][5]); numeroPantalla7_7.set(malla[6][6]); numeroPantalla7_8.set(malla[6][7]); numeroPantalla7_9.set(malla[6][8])
        numeroPantalla8_1.set(malla[7][0]); numeroPantalla8_2.set(malla[7][1]); numeroPantalla8_3.set(malla[7][2]); numeroPantalla8_4.set(malla[7][3]); numeroPantalla8_5.set(malla[7][4]); numeroPantalla8_6.set(malla[7][5]); numeroPantalla8_7.set(malla[7][6]); numeroPantalla8_8.set(malla[7][7]); numeroPantalla8_9.set(malla[7][8])
        numeroPantalla9_1.set(malla[8][0]); numeroPantalla9_2.set(malla[8][1]); numeroPantalla9_3.set(malla[8][2]); numeroPantalla9_4.set(malla[8][3]); numeroPantalla9_5.set(malla[8][4]); numeroPantalla9_6.set(malla[8][5]); numeroPantalla9_7.set(malla[8][6]); numeroPantalla9_8.set(malla[8][7]); numeroPantalla9_9.set(malla[8][8])
    
    def posible(x, y, número, malla):
        # Revisa fila.
        for pos_x in range(9):
            if malla[y][pos_x] == número:
                return False
        # Revisa columna.
        for pos_y in range(9):
            if malla[pos_y][x] == número:
                return False
        x0 = (x//3)*3
        y0= (y//3)*3
        # Revisa cuadrado.
        for y_pos in range(3):
            for x_pos in range(3):
                if malla[y0 + y_pos][x0 + x_pos] == número:
                    return False
        return True
    
    def solve(malla):
        for y in range(9):
            for x in range(9):
                if malla[y][x] == 0:
                    for número in range(1, 10):
                        if posible(x, y, número, malla):
                            malla[y][x] = número
                            solve(malla)
                            malla[y][x] = 0
                    return
        devolver_lista(malla)
    
    botonSolución = Button(miFrame, text="SOLVE", width=4, command = lambda: solve(hacer_lista()))
    botonSolución.grid(row=12, column=5, columnspan=3, sticky="nsew")
    
    sudoku.mainloop()

sudoku()



