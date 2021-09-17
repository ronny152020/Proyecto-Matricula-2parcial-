
from funciones_pantalla import gotoxy,borrarPantalla
from menu_mantenimiento import carreras,materias,periodos,profesores,estudiantes
from menu_matriculacion import matriculacion
from menu_notas import ingresonotas
import time
MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
class menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
            self.titulo=titulo
            self.opciones=opciones
            self.col=col
            self.fil=fil
            
    def menuprincipal(self):
        gotoxy(self.col,self.fil);print(MAGENTA+self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(RESET+opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc

opc=""
while opc!="4":
    borrarPantalla()
    principal=menu("Menu Principal",["1) Mantenimiento","2) Matriculacion","3) Notas","4) Salir"],20,10)
    opc=principal.menuprincipal()
    if opc=="1":
        opc1=""
        while opc1!="6":
            borrarPantalla()
            menu1=menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
            opc1=menu1.menuprincipal()
            if opc1=="1":
                carreras()
            elif opc1=="2":
                materias()
            elif opc1=="3":
                periodos()
            elif opc1=="4":
                profesores()
            elif opc1=="5":
                estudiantes()
            elif opc1=="6":
                gotoxy(20,19);print(YELLOW+"Presione para volver a MENU PRINCIPAL")
                gotoxy(20,20);input()
            else:
                gotoxy(20,19);print(YELLOW+"la opcion {} no existe".format(opc1))
                time.sleep(2)
    elif opc=="2":
        opc2=""
        while opc2!="2":
            borrarPantalla()
            menu2=menu("Menu Matriculacion",["1) Matricula","2) Salir"],20,10)
            opc2=menu2.menuprincipal()
            if opc2=="1":
                matriculacion()
            elif opc2=="2":
                gotoxy(20,15);print(YELLOW+"Presione para volver a MENU PRINCIPAL")
                gotoxy(20,16);input()
            else:
                gotoxy(20,15);print(YELLOW+"la opcion {} no existe".format(opc2))
                time.sleep(2)
    elif opc=="3":
        opc3=""
        while opc3!="2":
            borrarPantalla()
            menu3=menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3=menu3.menuprincipal()
            if opc3=="1":
                ingresonotas()
            elif opc3=="2":
                gotoxy(20,15);print(YELLOW+"Presione para volver a MENU PRINCIPAL")
                gotoxy(20,16);input()
            else:
                gotoxy(20,15);print(YELLOW+"la opcion {} no existe".format(opc3))
                time.sleep(2)
    elif opc>"4":
        gotoxy(20,17);print(YELLOW+"La opcion {} no es valida".format(opc))
        time.sleep(1)

gotoxy(20,17);print(YELLOW+"Gracias por visitarnos")
            
            



