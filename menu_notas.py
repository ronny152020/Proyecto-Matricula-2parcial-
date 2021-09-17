from funciones_archivos import Archivo
from funciones_pantalla import gotoxy,borrarPantalla,valida
from menu_mantenimiento import Periodo,Estudiante,Carrera,Materia,Profesor
import time
MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
class Notas: 
    def __init__(self,id,periodo,estudiante,materia,profesor,nota1,nota2):
        self.__id = id
        self.periodo = periodo
        self.estudiante = estudiante
        self.materia = materia
        self.profesor= profesor
        self.nota1 = nota1
        self.nota2 = nota2

    @property
    def id(self):
        return self.__id

    def getNotasEstudiante(self):
        return  [str(self.id),str(self.estudiante),str(self.materia),str(self.profesor),str(self.nota1),str(self.nota2)]
    
def ingresonotas():
   borrarPantalla()
   validar = valida()     
   gotoxy(20,2);print("INGRESO DE NOTAS ")
   gotoxy(15,4);print("Periodo ID[ AAAAMM ] : ")
   gotoxy(15,5);print("Estudiante ID [   ] : ")
   gotoxy(15,6);print("Materia ID[   ]: ")
   gotoxy(15,7);print("Profesor ID [    ] :")
   gotoxy(15,8);print("Primera nota: ")
   gotoxy(15,9);print("Segunda nota: ")
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
   lismateria,entmateria=[],None
   while not lismateria:
       gotoxy(27,6);idmat = input().upper()
       archimateria = Archivo("./materias.txt")
       lismateria = archimateria.buscar(idmat)
       if lismateria:
          entmateria = Materia(lismateria[0],lismateria[1]) 
          gotoxy(34,6);print(entmateria.descripcion)
       else:
           gotoxy(34,6);print("No existe una materia con ese codigo[{}]:".format(idmat))
           time.sleep(1);gotoxy(34,6);print(" "*60)
   lisprofe,entprofe=[],None
   while not lisprofe:
       gotoxy(29,7);idprof = input().upper()
       archiprofe = Archivo("./profesor.txt")
       lisprofe = archiprofe.buscar(idprof)
       if lisprofe:
          entprofe = Profesor(lisprofe[0],lisprofe[1],lisprofe[2],lisprofe[3],lisprofe[4],lisprofe[5]) 
          gotoxy(36,7);print(entprofe.nombre)
       else:
           gotoxy(36,7);print("No existe una materia con ese codigo[{}]:".format(idprof))
           time.sleep(1);gotoxy(36,7);print(" "*40)
   nota1=validar.solo_numeros("Error: Solo numeros",30,8)
   nota2=validar.solo_numeros("Error: Solo numeros",30,9)
   gotoxy(15,11);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(55,11);grabar = input().lower()
   if grabar == "s":
        archinotas = Archivo("./notas.txt")
        lisnotas = archinotas.leer()
        if lisnotas : 
            idSig = int(lisnotas[-1][0])+1
        else: 
            idSig=1
        entnotas = Notas(idSig,idpe,idest,idmat,idprof,nota1,nota2)
        datos = entnotas.getNotasEstudiante()
        datos = ';'.join(datos)
        archinotas.escribir([datos],"a")                 
        gotoxy(15,12);print(YELLOW+"Registro Grabado Satisfactoriamente")
        gotoxy(15,13);input("Presione una tecla para continuar....")
   else:
       gotoxy(15,12);print(YELLOW+"El registro no fue grabado")
       gotoxy(15,13);input("Presione una tecla para continuar....")