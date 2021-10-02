import os
from Tool import src as M
from tkinter import *

root = Tk()

direcciones = M.Text("", 13)

varOpción = StringVar()

nombreArchivo = StringVar()
pantalla = Entry(root, textvariable=nombreArchivo, font=("Calculator", 24), relief=RAISED, justify=RIGHT, borderwidth=0)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=3, sticky="nsew")
pantalla.config(background="black", fg="#03f943", justify="right")


def buscar_archivo(extensión, archivo):
    global direcciones
    posibilidades = direcciones.Return_Text.split(",")
    dirección, inicio_dirección = "", "C:/"
    programa = archivo + "." + extensión
    for direcciones_usadas in posibilidades:
        if programa in direcciones_usadas:
            Label(root, text=direcciones_usadas).grid(row=6, column=1, columnspan=3)
            return
        else:
            continue
    for resto_dirección, _, archivos in os.walk(inicio_dirección):
        if programa in archivos:
            dirección = os.path.join(resto_dirección, programa)
            break
    direcciones.Append_Text(f"{dirección},")
    Label(root, text=dirección).grid(row=6, column=1, columnspan=3)


def imprimir():
    if varOpción.get() == "exe":
        etiqueta.config(text=f"El archivo a buscar es '{nombreArchivo.get()}.exe.'")
    elif varOpción.get() == "png":
        etiqueta.config(text=f"El archivo a buscar es '{nombreArchivo.get()}.png.'")
    elif varOpción.get() == "pdf":
        etiqueta.config(text=f"El archivo a buscar es '{nombreArchivo.get()}.pdf'.")
    elif varOpción.get() == "mp4":
        etiqueta.config(text=f"El archivo a buscar es '{nombreArchivo.get()}.mp4'.")
    elif varOpción.get() == "py":
        etiqueta.config(text=f"El archivo a buscar es '{nombreArchivo.get()}.py'.")
    elif varOpción.get() == "docx":
        etiqueta.config(text=f"El archivo a buscar es '{nombreArchivo.get()}.docx'.")


texto = Label(root, text="Elija el formato:")
texto.grid(row=2, column=1, columnspan=3)
exe = Radiobutton(root, text="exe", variable=varOpción, value="exe", command=imprimir)
exe.grid(row=3, column=1)
png = Radiobutton(root, text="png", variable=varOpción, value="png", command=imprimir)
png.grid(row=3, column=2)
pdf = Radiobutton(root, text="pdf", variable=varOpción, value="pdf", command=imprimir)
pdf.grid(row=3, column=3)
mp4 = Radiobutton(root, text="mp4", variable=varOpción, value="mp4", command=imprimir)
mp4.grid(row=4, column=1)
py = Radiobutton(root, text="py", variable=varOpción, value="py", command=imprimir)
py.grid(row=4, column=2)
docx = Radiobutton(root, text="docx", variable=varOpción, value="docx", command=imprimir)
docx.grid(row=4, column=3)
botonFind = Button(root, text="Buscar", width=3, command=lambda: buscar_archivo(varOpción.get(), nombreArchivo.get()))
botonFind.grid(row=5, column=2, sticky="nsew")

etiqueta = Label(root)
etiqueta.grid(row=0, column=1)

root.mainloop()
