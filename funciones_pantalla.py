import os
import time
MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def borrarPantalla():
    os.system("cls") 

def mensaje(msg,f,c):
    pass

class valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0 :
                    break
            except:
                gotoxy(col,fil);print(MAGENTA+mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(RESET+" "*40)
        return valor

    def solo_letras(self,mensajeError,col,fil): 
        while True:
            gotoxy(col,fil) 
            valor = str(input())
            if valor.isalpha():
                break
            else:
                gotoxy(col,fil);print(MAGENTA+"<<{}>>".format(mensajeError))
                time.sleep(1)
                gotoxy(col,fil);print(RESET+" "*40)
        return valor

    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    
    def solo_cedynum(self,mensajeError,errordigitos,col,fil):
        while True: 
            gotoxy(col,fil)     
            valnum=self.solo_numeros(mensajeError,col,fil)     
            cant=len(valnum)
            if cant==10:
                break
            else:
                gotoxy(col,fil);print(MAGENTA+errordigitos)
                time.sleep(1)
                gotoxy(col,fil);print(RESET+" "*40)
        return valnum