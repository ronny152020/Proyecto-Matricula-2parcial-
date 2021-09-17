from funciones_archivos import Archivo
from funciones_pantalla import gotoxy,borrarPantalla,valida
from menu_mantenimiento import Periodo,Estudiante,Carrera
import time
MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
class Matricula: 
    def __init__(self,id,estudiante,carrera,periodo,valor):
        self.__id = id
        self.periodo= periodo
        self.estudiante = estudiante
        self.carrera = carrera
        self.valor = valor
       
    @property
    def id(self):
        return self.__id

    def getMatestudiante(self):
        return  [str(self.id),self.periodo,str(self.estudiante),str(self.carrera),str(self.valor)]
    
def matriculacion():
   borrarPantalla()
   validar = valida()     
   gotoxy(20,2);print("INGRESO DEL ESTUDIANTE A MATRICULAR")
   gotoxy(15,4);print("Periodo ID[ AAAAMM ] : ")
   gotoxy(15,5);print("Estudiante ID [   ] : ")
   gotoxy(15,6);print("Carrera ID[   ]: ")
   gotoxy(15,7);print("Valor matricula: ")
   lisperiodo,entperiodo = [],None
   while not lisperiodo:
       gotoxy(27,4);idpe = input().upper()
       archiperiodo = Archivo("./periodos.txt")
       lisperiodo = archiperiodo.buscar(idpe)
       if lisperiodo:
          entperiodo = Periodo(lisperiodo[0],lisperiodo[1]) 
          gotoxy(38,4);print(entperiodo.descripcion)
       else:
           gotoxy(38,4);print("No existe Periodo con ese codigo[{}]:".format(idpe))
           time.sleep(1);gotoxy(38,4);print(" "*60)
   lisestu,entestu=[],None
   while not lisestu:
       gotoxy(31,5);idest = input().upper()
       archiestudiantes = Archivo("./estudiantes.txt")
       lisestu = archiestudiantes.buscar(idest)
       if lisestu:
          entestu = Estudiante(lisestu[0],lisestu[1],lisestu[2],lisestu[3],lisestu[4]) 
          gotoxy(37,5);print(entestu.nombre)
       else:
           gotoxy(37,5);print("No existe un estudiante con ese codigo[{}]:".format(idest))
           time.sleep(1);gotoxy(37,5);print(" "*60)
   liscarrera,entcarrera=[],None
   while not liscarrera:
       gotoxy(27,6);idcar = input().upper()
       archicarrer = Archivo("./carreras.txt")
       liscarrera = archicarrer.buscar(idcar)
       if liscarrera:
          entcarrera = Carrera(liscarrera[0],liscarrera[1]) 
          gotoxy(32,6);print(entcarrera.descripcion)
       else:
           gotoxy(32,6);print("No existe una carrera con ese codigo[{}]:".format(idcar))
           time.sleep(1);gotoxy(32,6);print(" "*60)
   valor=validar.solo_numeros("Error: Solo numeros",32,7)
   gotoxy(15,8);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(55,8);grabar = input().lower()
   if grabar == "s":
        archimatricula = Archivo("./matriculas.txt")
        lismatricula = archimatricula.leer()
        if lismatricula : 
            idSig = int(lismatricula[-1][0])+1
        else: 
            idSig=1
        entmatricula = Matricula(idSig,idest,idcar,idpe,valor)
        datos = entmatricula.getMatestudiante()
        datos = ';'.join(datos)
        archimatricula.escribir([datos],"a")                 
        gotoxy(15,9);print(YELLOW+"Registro Grabado Satisfactoriamente")
        gotoxy(15,10);input("Presione una tecla para continuar....")
        
   else:
       gotoxy(15,9);print(YELLOW+"El registro no fue grabado")
       gotoxy(15,10);input("Presione una tecla para continuar....")
       

       
   