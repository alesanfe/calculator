import math
import os
from dataclasses import dataclass
import webbrowser


def mcd(num1, num2):
    A = max(num1, num2)
    B = min(num1, num2)
    while B:
        mcd = B
        B = A % B
        A = mcd
    return mcd

def mcm(num1, num2):
    
    return (num1*num2)/mcd(num1, num2)

def Decimal_Binario(decimal, bits=20):
    inverso, resultado = [], ""
    decimal_int = int(decimal)
    if decimal_int == 1:
        binario = "1"
        while True:
            if len(binario) < bits:
                binario = "0" + binario
            elif len(binario) == bits:
                break
    if decimal_int == 0:
        binario = "0"
        while True:
            if len(binario) < bits:
                binario = "0" + binario
            elif len(binario) == bits:
                break
    if decimal_int != 1 and decimal_int != 0:
        while True:
            Resto = decimal_int % 2
            Cociente = decimal_int//2
            if Cociente != 1:
                inverso.append(int(Resto))
                decimal_int = Cociente
            elif Cociente == 1:
                inverso.append(int(Resto))
                inverso.append(int(Cociente))
                break
        Máximo = len(inverso)
        binario = ""
        for i in range(Máximo-1, -1, -1):
            binario = binario+str(inverso[i])
    decimales, d = decimal- int(decimal), 0
    if decimales != 0:
        decimal = decimal - decimales
        while d<=4:
            estudiar = decimales*2
            if estudiar >= 1:
                cifra = 1
                decimales = estudiar - 1
                d+=1
            elif estudiar == 0:
                cifra = 0
                resultado += str(cifra)
                break
            elif estudiar < 1:
                cifra = 0
                decimales = estudiar
                d+=1
            resultado += str(cifra)
        return f"{binario}.{resultado}"
    return binario

def test_Miller_Rabin(número):
    primos = Criba_Erastotenes(número)
    for i in range(0, len(primos)):
        test1 = (Potencias_Rapidas(primos[i],número))%número
        if test1 != primos[i]:
            return "No es primo."
        test2 = (Potencias_Rapidas(primos[i], ((número-1)/2)))%número
        if test2 == 1 or test2 == (número-1):
            continue
        else:
            return "No es primo."
    return "Es primo."

def Potencias_Rapidas(base, exponente):
    resultado1 = 1
    inverso = []
    lista_binario = []
    definitiva = []
    while True:
        Resto = exponente % 2
        Cociente = exponente//2
        if Cociente != 1:
            inverso.append(Resto)
            exponente = Cociente
        elif Cociente == 1:
            inverso.append(Resto)
            inverso.append(Cociente)
            break
    Máximo = len(inverso)
    binario = ""
    for i in range(Máximo-1, -1, -1):
        binario = str(inverso[i])
        lista_binario.append(binario)
    for i in range(0, len(lista_binario)):
        if len(lista_binario)-1 == i and lista_binario[i] == "1":
            definitiva.append("M")
            continue
        elif lista_binario[i] == "1":
            definitiva.append("M")
            definitiva.append("C")
        elif len(lista_binario)-1 != i and lista_binario[i] == "0":
            definitiva.append("C")
    for i in range(0, len(definitiva)):
        if definitiva[i] == "M":
            resultado2 = resultado1*base
            resultado1 = resultado2
        elif definitiva[i] == "C":
            resultado2 = resultado1**2
            resultado1 = resultado2
    return resultado1

def Criba_Erastotenes(número):
    n = int(math.sqrt(número))
    lista = list(range(2, n+1))
    i = 0
    while(lista[i]*lista[i] <= n):
        for num in lista:
            if num <= lista[i]:
                continue
            elif num % lista[i] == 0:
                lista.remove(num)
            else:
                pass
        i += 1
    return lista

def Fermat(número):
    C = 2**2**número+1
    return C

def Marsenne(número):
    C = 2**número-1
    return C

def Fibonacci(número):
    x = 1/math.sqrt(5)
    y1 = (1+math.sqrt(5))
    y2 = (1-math.sqrt(5))
    z1 = (y1/2)**número
    z2 = (y2/2)**número
    w1 = x*z1
    w2 = x*z2
    F1 = w1
    F2 = w2
    C = F1-F2
    return C

Letras_L = (",", ".", "A", "B", "C", "D", "E", "F", "G", "H",
            "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q",
            "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "¿",
            "?", "!", "¡", "-", ":", "a", "á", "b", "c", "d",
            "e", "é", "f", "g", "h", "i", "í", "j", "k", "l",
            "m", "n", "ñ", "o", "ó", "p", "q", "r", "s", "t",
            "u", "ú", "v", "w", "x", "y", "z", "*", ";", "=",
            "|", '"', "'", "·", "$", "%", "&", "/", "(", ")",
            "[", "]", "{", "}", "_", "+")

Decimal_D, Letras_D = {}, {}
for i in range(0, len(Letras_L)):
    Letras_D[i] = Letras_L[i]
    Decimal_D[Letras_L[i]] = i


@dataclass(frozen=False, order=True)
class Text:

    mensaje: str
    canal: int
    módulo: int = len(Letras_L)+1
    conteo: int = 0

    @property
    def Code(self):

        if self.conteo == 0:
            criptación = ""
            for i in self.mensaje:
                if i == " ":
                    criptación = " " + criptación
                    continue
                elif i == "\n":
                    criptación = "\n" + criptación
                    continue
                decimal1 = Decimal_D[i]
                decimal2 = (decimal1*self.canal) % self.módulo
                criptación = Letras_D[decimal2] + criptación
                self.mensaje = criptación
            self.conteo = 1
            return self.mensaje
        elif self.conteo == 1:
            return Text("El mensaje ya está encriptado.")

    @property
    def Decode(self):
        """
    Nos permite desencriptar el mensaje.

    ENTRADA:
        Hace falta un objeto tipo Text.
    SALIDA:
        Devuelve el mensaje descodificado.
        """
        if self.conteo == 1:
            descriptación = ""
            for valor in range(0, self.módulo):
                condición = (self.canal*valor) % self.módulo
                if condición != 1:
                    continue
                elif condición == 1:
                    inverso = valor
                    break
            for i in self.mensaje:
                if i == " ":
                    descriptación = " " + descriptación
                    continue
                elif i == "\n":
                    descriptación = "\n" + descriptación
                    continue
                decimal1 = Decimal_D[i]
                decimal2 = (decimal1*inverso) % self.módulo
                descriptación = Letras_D[decimal2] + descriptación
                self.mensaje = descriptación
            self.conteo = 0
            return self.mensaje
        elif self.conteo == 0:
            return Text("El mensaje aún no ha sido encriptado.")

    @property
    def Create_Text(self):
        """
    Permite crear, fácilmente, un archivo de texto.

    ENTRADA:
        Hace falta un objeto tipo Text.
    SALIDA:
        Devuelve un arvhivo de texto que será llamado como: 
        self.canal en binario, más la extensión.
        """
        Info = open(f"{self}.txt", "w")
        Info.write(str(self.mensaje))
        Info.close()

    @property
    def Borrow_Text(self):
        """
    Permite borrar un archivo creado en un cierto canal 
    (en el caso de tener dos objetos distintos, uno puede
    crear y el otro eliminar, si tienen el mismo canal).
        """
        os.remove(f"{self}.txt")

    def Append_Text(self, mensaje):
        """
    Permite añadir texto (si tiene el mismo canal otro
    objeto también puede añadir texto).
        """
        Info = open(f"{self}.txt", "a")
        Info.write(mensaje)
        Info.close()

    @property
    def Return_Text(self):
        """
    Permite recuperar la información de una archivo de texto,
    es decir, realizar un guardado permanente
        """
        cadena = ""
        with open(f"{self}.txt", encoding="latin-1") as f:
            for linea in f:
                cadena = cadena + linea
        return cadena

    def ReWrite_Text(self, mensaje):
        """
    Permite cambiar el contenido de un archivo de texto.
        """
        self.mensaje = mensaje
        Info = open(f"{self}.txt", "w")
        Info.write(str(self.mensaje))
        Info.close()

    def Read_Text(self, inicio: int, final: int):
        """
    Permite leer un texto que se haya realizado con la clase Text.
        """
        conteo = 0
        with open(f"{self}.txt", encoding="latin-1") as f:
            for linea in f:
                conteo += 1
                if inicio <= conteo <= final:
                    print(linea, end='')
                elif inicio > conteo:
                    continue
                elif final < conteo:
                    break

    def __str__(self):
        return f"{Decimal_Binario(self.canal, int(math.sqrt(self.canal))+1)}"

def e(n_iteraciones=9999):
    variable, número2, iteración, resultado = 0, 0, 0, 0
    unidad = 1
    while iteración<=n_iteraciones:
        if variable == 0:
            número = unidad
        elif variable != 0:
            número = unidad/variable
        resultado += número
        número2 += unidad
        if variable == 0:
            variable = unidad
        elif variable != 0:
            variable *= número2
        iteración += unidad
    return resultado

def Metodo_Heron(raíz, n_iteraciones):
    Valores = 1
    for _ in range(n_iteraciones):
        Valores = 0.5*(Valores+raíz/Valores)
    return Valores


def pi(d=15):
    """Regresa una lista con los primeros d dígitos
       de pi utilizando el algoritmo de espita
       diseñado por Jeremy Gibbons. Implementación
       de John Zelle con ligeras alteraciones por
       Ariel Ortiz.
    """
    x, inicio = [], True
    q,r,t,k,n,l = 1,0,1,1,3,3
    while len(x) < d:
        if 4*q+r-t < n*t:
            x.append(n)
            q,r,t,k,n,l = (
                10*q,10*(r-n*t),t,k,
                (10*(3*q+r))//t-10*n,l)
        else:
            q,r,t,k,n,l = (
                q*k,(2*q+r)*l,t*l,k+1,
                (q*(7*k+2)+r*l)//(t*l),l+2)
    for número in x:
        if inicio:
            pi = f"{número}."
            inicio = False
        else:
            pi += str(número)
    return float(pi)

def FACT(número):
    resultado = 1
    for valores in range(1, número +1):
        resultado *= valores
    return resultado

def sol_ecuacion_primer_grado(A, B):
    print("Ax+B=0\n")
    print()
    while True:
        try:
            x = -B/A
            break
        except ZeroDivisionError:
            return "No tiene solución."
    return f"La solución es:{x}"

def sol_ecuacion_segundo_grado(A, B, C):
    while True:
        try:
            1/A
            break
        except ZeroDivisionError:
            return "No tiene solución."
    D = B**2-4*A*C
    E = math.sqrt(abs(B**2-4*A*C))
    if D >= 0:
        a = (-B+E)/(2*A)
        b = (-B-E)/(2*A)
        return f"Las soluciones son {a} y {b}."
    elif D < 0:
        a = complex(-B, E)/(2*A)
        b = complex(-B, -E)/(2*A)
        return f"Las soluciones son {a} y {b}."

def buscar_archivo(extensión, archivo):
    dirección, inicio_dirección = "", "C:/"
    programa = archivo + "." + extensión
    for resto_dirección, _, archivos in os.walk(inicio_dirección):
        if programa in archivos:
            dirección = os.path.join(resto_dirección, programa)
            break
    webbrowser.open_new(dirección)
    return dirección
