from funciones_archivos import Archivo
from funciones_pantalla import gotoxy,borrarPantalla,valida
import time
MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
class Carrera:
    def __init__(self,id,descripcion):
        self.__id = id
        self.descripcion = descripcion
       
    @property
    def id(self):
        return self.__id

    def getCarrera(self):
        return  [str(self.id),self.descripcion]


def carreras():
    borrarPantalla()  
    validar=valida()   
    gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Carrera: ")
    descarrera = validar.solo_letras("Error solo letras",37,5)
    archiCarrera = Archivo("./carreras.txt",";")
    carreras = archiCarrera.leer()
    if carreras : 
        idSig = int(carreras[-1][0])+1
    else: 
        idSig=1
    idstr=str(idSig)
    gotoxy(23,4);print(MAGENTA+idstr)
    time.sleep(2)
    carrera = Carrera(idSig,descarrera)
    datos = carrera.getCarrera()
    datos = ';'.join(datos)
    archiCarrera.escribir([datos],"a")

class Materia:
    def __init__(self,id, descripcion):
        self.__id = id
        self.descripcion = descripcion
       
    @property
    def id(self):
        return self.__id

    def getMateria(self):
        return  [str(self.id),self.descripcion]
    
def materias():
    borrarPantalla()
    validar=valida()     
    gotoxy(20,2);print("MANTENIMIENTO DE MATERIAS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion de la materia: ")
    desmateria = validar.solo_letras("Error solo letras",43,5)
    archimateria= Archivo("./materias.txt",";")
    materias= archimateria.leer()
    if materias : 
        idSig = int(materias[-1][0])+1
    else: 
        idSig=1
    idstr=str(idSig)
    gotoxy(23,4);print(MAGENTA+idstr)
    time.sleep(2)
    materia= Materia(idSig,desmateria)
    datos = materia.getMateria()
    datos = ';'.join(datos)
    archimateria.escribir([datos],"a")
    
class Periodo:
    def __init__(self,periodo,descripcion):
        self.periodo =periodo     # 202111
        self.descripcion = descripcion # Segundo semestre 2021
       
   
    def getPeriodo(self):
        return  [str(self.periodo),self.descripcion]
    
def periodos():
    validar=valida()
    borrarPantalla()     
    gotoxy(20,2);print("MANTENIMIENTO DE PERIODO")
    gotoxy(15,4);print("Periodo: AAAAMM")
    gotoxy(15,5);print("Descripcion del periodo: ")
    perio = validar.solo_numeros("Error solo numeros",24,4)
    gotoxy(41,5);desperiodo=input()
    archiperiodo= Archivo("./periodos.txt",";")
    periodo= Periodo(perio,desperiodo)
    datos = periodo.getPeriodo()
    datos = ';'.join(datos)
    archiperiodo.escribir([datos],"a")
    
class Profesor: 
    def __init__(self,id,nombre,cedula,carrera,titulo,telefono):
        self.__id = id
        self.nombre = nombre
        self.cedula = cedula
        self.titulo = titulo
        self.telefono = telefono
        self.carrera=carrera
       
    @property
    def id(self):
        return self.__id

    def getProfesor(self):
        return  [str(self.id),self.nombre,self.cedula,self.titulo,self.telefono,self.carrera.id]
    
def profesores():
   borrarPantalla()
   validar = valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula : ")
   gotoxy(15,6);print("Titulo : ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   nom = validar.solo_letras("Error: solo ingrese letras",25,4)
   ced=validar.solo_cedynum("Error: ingrese solo numeros","Error: ingrese solo 10 digitos",25,5)
   tit = validar.solo_letras("Error: solo ingrese letras",25,6)
   tel=validar.solo_cedynum("Error: Solo numeros","Error: ingrese solo 10 digitos",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("./carreras.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n): ")
   gotoxy(56,10);grabar = input().lower()
   if grabar == "s":
        archiProfesor = Archivo("./profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : 
            idSig = int(lisProfesores[-1][0])+1
        else: 
            idSig=1
        entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,tel)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")                 
        gotoxy(15,11);print(YELLOW+"Registro Grabado Satisfactoriamente")
        gotoxy(15,12);input("Presione una tecla para continuar...")
   else:
       gotoxy(15,11);print(YELLOW+"Su Registro No fue Grabado") 
       gotoxy(15,12);input("Presione una tecla para continuar...")
       
class Estudiante: 
    def __init__(self,id,nombre,cedula,direccion,telefono):
        self.__id = id
        self.nombre = nombre
        self.cedula = cedula
        self.direccion=direccion
        self.telefono = telefono
       
    @property
    def id(self):
        return self.__id

    def getEstudiante(self):
        return  [str(self.id),self.nombre,self.cedula,self.direccion,self.telefono]
    
def estudiantes():
   borrarPantalla()
   validar = valida()     
   gotoxy(20,2);print("INGRESO DE ESTUDIANTES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula  : ")
   gotoxy(15,6);print("Direccion : ")
   gotoxy(15,7);print("Telefono: ")
   nom = validar.solo_letras("Error: solo ingrese letras",25,4)
   ced=validar.solo_cedynum("Error: solo ingrese solo numeros","Error: ingrese solo 10 digitos",25,5)
   gotoxy(28,6);direccion = input()
   tel=validar.solo_cedynum("Error: Solo numeros","Error: ingrese solo 10 digitos",26,7)
   archiestudiante=Archivo("./estudiantes.txt",";")
   lisestudiante= archiestudiante.leer()
   if lisestudiante : 
        idSig = int(lisestudiante[-1][0])+1
   else: 
        idSig=1
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(55,10);grabar = input().lower()
   if grabar == "s":
        entestudiante = Estudiante(idSig,nom,ced,direccion,tel)
        datos = entestudiante.getEstudiante()
        datos = ';'.join(datos)
        archiestudiante.escribir([datos],"a")                 
        gotoxy(15,11);print(YELLOW+"Registro Grabado Satisfactoriamente")
        gotoxy(15,12);input("Presione una tecla para continuar...")
   else:
       gotoxy(15,11);print(YELLOW+"Su Registro No fue Grabado") 
       gotoxy(15,12);input("Presione una tecla para continuar...")