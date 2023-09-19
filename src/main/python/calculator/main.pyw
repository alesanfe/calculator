from math import *
from tkinter import *

from Tool import math


def create_button(text, command, row, column, width=3):
    print(width)
    button = Button(my_frame, text=text, width=width, command=command)
    button.grid(row=row, column=column, sticky="NSEW")


def change_chain(number):
    return float(number) if "." in number else int(number)


def check_float(number):
    if type(number) == float:
        entero_y_decimal = str(number).split(".")
        return entero_y_decimal[0] if entero_y_decimal[1] == "0" else number
    return number


root_tk = Tk()
root_tk.resizable(False, False)  # Poder o no redimensionar.
root_tk.title("∞")
root_tk.iconbitmap('../data/calcu.ico')
my_frame = Frame(root_tk)
my_frame.pack()

# Iniciar variables.
start = True
operation1, operation2 = "", ""
pi, e, result = Math.pi(), Math.e(), 0
stock = Math.Text("", canal=7)
stock.Create_Text

# ---Pantalla--- #
numberScreen = StringVar()
screen = Entry(my_frame, textvariable=numberScreen, font=("Calculator", 24), relief=RAISED, justify=RIGHT,
               borderwidth=0)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=8, sticky="nsew")
screen.config(background="black", fg="#03f943", justify="right")


# ---Pulsaciones teclado--- #
def number_pressed(num):
    global operation1
    if operation1 != "":
        numberScreen.set(num)
        operation1 = ""
    else:
        numberScreen.set(numberScreen.get() + num)


# ---función calculadora--- #
def add(num):
    global operation1
    global operation2
    global result
    result = change_chain(num)
    numberScreen.set(f"{num}+x")
    operation1 = "suma"
    operation2 = "suma"


def subtract(num):
    global operation1
    global operation2
    global result
    result = change_chain(num)
    numberScreen.set(f"{num}-x")
    operation1 = "resta"
    operation2 = "resta"


def multiply(num):
    global operation1
    global operation2
    global result
    result = change_chain(num)
    numberScreen.set(f"{num}*x")
    operation1 = "multiplicación"
    operation2 = "multiplicación"


def division(num):
    global operation1
    global operation2
    global result
    result = change_chain(num)
    numberScreen.set(f"{num}/x")
    operation1 = "división"
    operation2 = "división"


def root():
    global operation1
    global operation2
    numberScreen.set(f"√x")
    operation1 = "raíz"
    operation2 = "raíz"


def raised(num):
    global operation1
    global operation2
    global result
    result = change_chain(num)
    numberScreen.set(f"{num}^x")
    operation1 = "elevado"
    operation2 = "elevado"


def miller_rabin():
    global operation1
    global operation2
    numberScreen.set(f"Número a introducir: ")
    operation1 = "Miller-Rabin"
    operation2 = "Miller-Rabin"


def fermat():
    global operation1
    global operation2
    numberScreen.set(f"Introduzca la iteración: ")
    operation1 = "Fermat"
    operation2 = "Fermat"


def marsenne():
    global operation1
    global operation2
    numberScreen.set(f"Introduzca la iteración: ")
    operation1 = "Marsenne"
    operation2 = "Marsenne"


def fibonacci():
    global operation1
    global operation2
    numberScreen.set(f"Introduzca la iteración: ")
    operation1 = "Fibonacci"
    operation2 = "Fibonacci"


def mod(num):
    global operation1
    global operation2
    global result
    result = change_chain(num)
    if type(result) == int:
        numberScreen.set(f"{num} (mod x)")
        operation1 = "Mod"
        operation2 = "Mod"
    elif type(result) == float:
        numberScreen.set("Tiene que ser un entero.")


def decimal_to_binary():
    global operation1
    global operation2
    numberScreen.set(f"Introduzca la cifra: ")
    operation1 = "Decimal a binario"
    operation2 = "Decimal a binario"


def greatest_common_divisor(num):
    global operation1
    global operation2
    global result
    result = change_chain(num)
    if type(result) == int:
        operation1 = "Mínimo común divisor"
        operation2 = "Mínimo común divisor"
    elif type(result) == float:
        numberScreen.set("Tiene que ser un entero.")


def least_common_multiple(num):
    global operation1
    global operation2
    global result
    result = change_chain(num)
    if type(result) == int:
        operation1 = "Máximo común múltiplo"
        operation2 = "Máximo común múltiplo"
    elif type(result) == float:
        numberScreen.set("Tiene que ser un entero.")


def keep(num):
    global stock
    stock.ReWrite_Text(num)


def return_value():
    global stock
    numberScreen.set(stock.Return_Text)


def radians_to_degrees():
    global operation1
    global operation2
    numberScreen.set("x*(180/π)")
    operation1 = "Radianes a grados"
    operation2 = "Radianes a grados"


def degrees_to_radians():
    global operation1
    global operation2
    numberScreen.set("x*(π/180)")
    operation1 = "Grados a radianes"
    operation2 = "Grados a radianes"


def logarithm(num):
    global operation1
    global operation2
    global result
    result = change_chain(num)
    numberScreen.set(f"log{num}(x)")
    operation1 = "Logaritmo"
    operation2 = "Logaritmo"


def sine():
    global operation1
    global operation2
    numberScreen.set("sen(x)")
    operation1 = "Seno"
    operation2 = "Seno"


def cosine():
    global operation1
    global operation2
    numberScreen.set("cos(x)")
    operation1 = "Coseno"
    operation2 = "Coseno"


def tangent():
    global operation1
    global operation2
    numberScreen.set("tan(x)")
    operation1 = "Tangente"
    operation2 = "Tangente"


def factorial():
    global operation1
    global operation2
    numberScreen.set("x!")
    operation1 = "Factorial"
    operation2 = "Factorial"


def solution(number):
    global operation1
    global operation2
    global result
    result = change_chain(number)
    if type(result) == int:
        if result == 1:
            numberScreen.set("Introduzca A y B: ")
        elif result == 2:
            numberScreen.set("Introduzca A, B y C: ")
        operation1 = "Solucionar"
        operation2 = "Solucionar"
    elif type(result) == float:
        numberScreen.set("Tiene que ser un entero.")


def find(extensión):
    global operation1
    global operation2
    global result
    result = extensión
    numberScreen.set(f"Buscar archivo '{extensión}': ")
    operation1 = "Buscar"
    operation2 = "Buscar"


# ---función el_resultado---#
def the_result():
    global start
    global result
    global operation2
    if operation2 == "suma":
        numberScreen.set(check_float(result + change_chain(numberScreen.get())))
        operation2 = ""
    elif operation2 == "resta":
        numberScreen.set(check_float(result - change_chain(numberScreen.get())))
        operation2 = ""
    elif operation2 == "multiplicación":
        numberScreen.set(check_float(result * change_chain(numberScreen.get())))
        operation2 = ""
    elif operation2 == "división":
        numberScreen.set(check_float(result / change_chain(numberScreen.get())))
        operation2 = ""
    elif operation2 == "raíz":
        numberScreen.set(check_float(sqrt(change_chain(numberScreen.get()))))
        operation2 = ""
    elif operation2 == "elevado":
        if type(change_chain(numberScreen.get())) == int:
            numberScreen.set(check_float(Math.Potencias_Rapidas(result, change_chain(numberScreen.get()))))
        elif type(change_chain(numberScreen.get())) == float:
            numberScreen.set(check_float(result ** change_chain(numberScreen.get())))
    elif operation2 == "Miller-Rabin":
        if type(change_chain(numberScreen.get())) == int:
            numberScreen.set(Math.test_Miller_Rabin(change_chain(numberScreen.get())))
        elif type(change_chain(numberScreen.get())) == float:
            numberScreen.set("Tiene que ser un entero.")
    elif operation2 == "Fermat":
        if type(change_chain(numberScreen.get())) == int:
            numberScreen.set(check_float(Math.Fermat(change_chain(numberScreen.get()))))
        elif type(change_chain(numberScreen.get())) == float:
            numberScreen.set("Tiene que ser un entero.")
    elif operation2 == "Marsenne":
        if type(change_chain(numberScreen.get())) == int:
            numberScreen.set(check_float(Math.Marsenne(change_chain(numberScreen.get()))))
        elif type(change_chain(numberScreen.get())) == float:
            numberScreen.set("Tiene que ser un entero.")
    elif operation2 == "Fibonacci":
        if type(change_chain(numberScreen.get())) == int:
            numberScreen.set(check_float(Math.Fibonacci(change_chain(numberScreen.get()))))
        elif type(change_chain(numberScreen.get())) == float:
            numberScreen.set("Tiene que ser un entero.")
    elif operation2 == "Mod":
        if type(change_chain(numberScreen.get())) == int:
            numberScreen.set(check_float(result % change_chain(numberScreen.get())))
        elif type(change_chain(numberScreen.get())) == float:
            numberScreen.set("Tiene que ser un entero.")
    elif operation2 == "Decimal a binario":
        numberScreen.set(Math.Decimal_Binario(change_chain(numberScreen.get())))
    elif operation2 == "Mínimo común divisor":
        if type(change_chain(numberScreen.get())) == int:
            numberScreen.set(check_float(Math.mcd(result, change_chain(numberScreen.get()))))
        elif type(change_chain(numberScreen.get())) == float:
            numberScreen.set("Tiene que ser un entero.")
    elif operation2 == "Máximo común múltiplo":
        if type(change_chain(numberScreen.get())) == int:
            numberScreen.set(check_float(Math.mcm(result, change_chain(numberScreen.get()))))
        elif type(change_chain(numberScreen.get())) == float:
            numberScreen.set("Tiene que ser un entero.")
    elif operation2 == "Grados a radianes":
        numberScreen.set(check_float(change_chain(numberScreen.get()) * (pi / 180)))
        print(numberScreen.get())
    elif operation2 == "Radianes a grados":
        numberScreen.set(check_float(change_chain(numberScreen.get()) * (180 / pi)))
    elif operation2 == "Logaritmo":
        numberScreen.set(check_float(log(change_chain(numberScreen.get()), result)))
    elif operation2 == "Seno":
        numberScreen.set(check_float(sin(change_chain(numberScreen.get()))))
    elif operation2 == "Coseno":
        numberScreen.set(check_float(cos(change_chain(numberScreen.get()))))
    elif operation2 == "Tangente":
        numberScreen.set(check_float(tan(change_chain(numberScreen.get()))))
    elif operation2 == "Factorial":
        if type(change_chain(numberScreen.get())) == int:
            numberScreen.set(check_float(Math.FACT(change_chain(numberScreen.get()))))
        elif type(change_chain(numberScreen.get())) == float:
            numberScreen.set("Tiene que ser un entero.")
    elif operation2 == "Solucionar":
        lista = numberScreen.get().split(",")
        if result == 1:
            numberScreen.set(Math.sol_ecuacion_primer_grado(change_chain(lista[0]), change_chain(lista[1])))
        elif result == 2:
            numberScreen.set(Math.sol_ecuacion_segundo_grado(change_chain(lista[0]), change_chain(lista[1]),
                                                             change_chain(lista[2])))
    elif operation2 == "Buscar":
        numberScreen.set(Math.buscar_archivo(result, numberScreen.get()))
    elif operation2 == "":
        numberScreen.set("ERROR")


def borrar():
    global result
    global operation2
    result = ""
    operation2 = ""
    numberScreen.set(result)


actions = {
    "R->G": lambda: radians_to_degrees(),"π": lambda: numberScreen.set(Math.pi()), "^": lambda: raised(numberScreen.get()),

}

# ---Fila 2:
create_button("R->G", lambda: radians_to_degrees(), 2, 1, 4)
create_button("π", lambda: numberScreen.set(Math.pi()), 2, 2, 4)
create_button("^", lambda: raised(numberScreen.get()), 2, 3, 4)
create_button("√", lambda: root(), 2, 4, 4)
create_button("/", lambda: division(numberScreen.get()), 2, 5, 4)
create_button("<-", lambda: borrar(), 2, 6, 4)
create_button("P?", lambda: miller_rabin(), 2, 7, 4)
create_button("D_B", lambda: decimal_to_binary(), 2, 8, 4)

# ---Fila 3:
create_button("G->R", lambda: degrees_to_radians(), 3, 1, 4)
create_button("e", lambda: numberScreen.set(Math.e()), 3, 2, 4)
create_button("7", lambda: number_pressed("7"), 3, 3)
create_button("8", lambda: number_pressed("8"), 3, 4)
create_button("9", lambda: number_pressed("9"), 3, 5)
create_button("x", lambda: multiply(numberScreen.get()), 3, 6, 4)
create_button("Fer", lambda: fermat(), 3, 7, 4)
create_button("Mcd", lambda: greatest_common_divisor(numberScreen.get()), 3, 8, 4)

# ---Fila 4:
create_button("log", logarithm(numberScreen.get()), 4, 1, 4)
create_button("sen", lambda: sine(), 4, 2, 4)
create_button("4", lambda: number_pressed("4"), 4, 3)
create_button("5", lambda: number_pressed("5"), 4, 4)
create_button("6", lambda: number_pressed("6"), 4, 5)
create_button("-", lambda: subtract(numberScreen.get()), 4, 6, 4)
create_button("Mar", lambda: marsenne(), 4, 7, 4)
create_button("Mcm", lambda: least_common_multiple(numberScreen.get()), 4, 8, 4)

# ---Fila 5:
create_button("√f(x)", lambda: solution(numberScreen.get()), 5, 1, 4)
create_button("cos", lambda: cosine(), 5, 2, 4)
create_button("1", lambda: number_pressed("1"), 5, 3)
create_button("2", lambda: number_pressed("2"), 5, 4)
create_button("3", lambda: number_pressed("3"), 5, 5)
create_button("+", lambda: add(numberScreen.get()), 5, 6, 4)
create_button("Fib", lambda: fibonacci(), 5, 7, 4)
create_button("Keep", lambda: keep(numberScreen.get()), 5, 8)

# ---Fila 6:
create_button("Find", lambda: find(numberScreen.get()), 6, 1, 4)
create_button("tan", lambda: tangent(), 6, 2, 4)
create_button("Mod", lambda: mod(numberScreen.get()), 6, 3, 4)
create_button("0", lambda: number_pressed("0"), 6, 4)
create_button(".", lambda: number_pressed("."), 6, 5, 4)
create_button("=", lambda: the_result(), 6, 6, 4)
create_button("n!", lambda: factorial(), 6, 7, 4)
create_button("ANS", lambda: return_value(), 6, 8, 4)

root_tk.mainloop()
