import string
import numpy as np
import re
import random
import os


os.system('cls')
print('#'*100)
print("WordleSolver V 1.0")
print("Escrito por Bautista Ulecia para aprender Python")
print('#'*100)
print("")
idioma=""

buf_idioma=input("Ingrese 'i' para ingles, 'e' para español\n")
while True: #Loop para escoger idioma
    if buf_idioma=="i" or buf_idioma=="e":
        idioma=buf_idioma
        break
    else:
       buf_idioma=input("Error en ingreso. Por favor ingrese i para ingles, e para español\n") 

    
#Carga de la lista de palabras en ingles
if idioma=='i': 
    def load_words():
        with open('valid_wordle_en.txt') as word_file:
            valid_words = set(word_file.read().split())

        return valid_words

    palabras = load_words()
    palabras_5=[str for str in palabras if len(str)==5] #Posibilidad de usar otras listas de palabras mas largas. Cambiar el 5 por el numero de letras permitidas por palabra

#Carga de la lista de palabras en español
if idioma=='e':
    def load_words():
        with open('valid_wordle_es.txt') as word_file:
            valid_words = set(word_file.read().split())

        return valid_words

    palabras = load_words()
    palabras_5=[str for str in palabras if len(str)==5]



#Variables para el programa
posibles=[]
letrasSi=[" "," "," "," "," "]
letrasLugar=[]
letrasNo=[]
palabras_final=[]
buf=""
letrasMostrar=["#","#","#","#","#"]

class letras_mal:
    def __init__(self, letra, lugar):
            self.letra=letra
            self.lugar=lugar
letrasLugar.append(letras_mal('',0))

#######################################################################
#FUNCIONES
#######################################################################

def indicador(x): #Indicador para LetrasSi, muestra en que letra esta parado el usuario para ingresar
    espacio=" "
    print(letrasMostrar)
    print(2*espacio+5*x*espacio+ "↑")

def no_contiene(str,letrasNo): #Retorna True si la palabra NO tiene las letras enviadas (Son las letras que no aparecen en el wordle, es decir, las grises)
    for l in letrasNo:
        if l in str:
            return False
    return True


def inputSi(): #Muestra en pantalla el string vacio y permite el ingreso de letras validas (es decir, las verdes) por parte del usuario.
    print("\n\n")
    for x in range(0, 5):
        indicador(x)
        buf=input('\nINGRESE LETRA QUE VA EN ESTE LUGAR, ENTER SI NO LA SABE\n')
        os.system('cls')
        while len(buf)>1:
            print("ERROR DE INGRESO\n")
            indicador(x)
            buf=input('\nINGRESE LETRA QUE VA EN ESTE LUGAR, ENTER SI NO LA SABE\n')
            os.system('cls')
        else:
            letrasSi[x]=buf #Si el usuario toco enter, se guarda "" en el lugar de letrassi[x]. TODAS LAS PALABRAS TIENEN "", entonces la busqueda funciona.



def inputNo(): #Input para valores NO encontrados (es decir, las grises) por parte del usuario.
    while True:
        n=input("\nIngrese valores no encontrados de a uno. Para finalizar, ingrese un 0.\n")
        while len(n)>1:
            os.system('cls')
            print("ERROR DE INGRESO\n")
            n=input("\nIngrese valores no encontrados de a uno. Para finaliza, ingrese un 0.\n")

        if n=="0":
            os.system('cls')
            break
        else:
            letrasNo.append(n)
    
def inputLugar(): #Input para letras que van, pero en otro lugar(es decir, las naranjas), por parte del usuario. Las manejo en forma de objetos obj(letra,lugar).
        while True:
            n=input("\nIngrese letra encontrada en otro lugar, para finalizar ingrese un 0.\n")
            if n=="0":
                os.system('cls')
                break
            m=input("\nIngrese lugar donde esta esa letra en el ingreso. Es decir, en que casilla de la palabra hay naranja. (1-2-3-4-5).\n")
            letrasLugar.append(letras_mal(n, m))




def compararSi(letrasSi,str): #Compara todos los strings de la lista con el string de letras encontradas (verdes). Retornara true en caso de que el string tenga todas las letras
    #en dicho lugar, incluyendo los "", es decir que el flag se levante 5 veces.
    flag=0
    for x in range (0,5):
        if re.search (letrasSi[x], str[x]):
            flag+=1
        if flag==5:
            return True



def compararLugar(letrasLugar,str): #Retorna true si la letra encontrada en LetrasLugar (las naranjas) se encuentran en el string, pero no en el lugar que se probaron.
    flag=0
    for l in letrasLugar:
        if l.letra=='':
            flag+=1

        elif l.letra in str and l.letra!=str[int(l.lugar)-1]:
            flag+=1

        if flag==len(letrasLugar):
            return True


def listaposibles(): #Recorta la lista de palabras posibles utilizando varias de las funciones anteriores.
    posibles=[]
    palabras_final=[str for str in palabras_5 if no_contiene(str,letrasNo)]
    for str in palabras_final:
        if compararSi(letrasSi,str) and compararLugar(letrasLugar,str):
            posibles.append(str)
    return posibles

    

#Funcion integradora
def operar():
    inputSi()
    print(letrasSi)
    inputNo()
    inputLugar()


#Main
os.system('cls')
if idioma=="i":
    print("\n begin by trying any word on the webpage... maybe 'salet' ?")
if idioma=="e":
    print("Abra el wordle")
    print("\nPara comenzar, pruebe en la pagina web cualquier palabra... quizas 'nacer' ?")
for x in range(6): #6 vueltas por los 6 intentos que nos da el wordle
    operar()
    if(len(listaposibles())!=1):
        print("\nProba la palabra:\n\n"+random.choice(listaposibles())) #Si no hay una sola solucion, muestra una para probar. (Probe mostrando la lista entera, era molesto)
        
    else:
        print("\nLA PALABRA ES\n") #Solucion final
        print(listaposibles())
    



#PROBLEMAS A SOLUCIONAR

#MEDIO ASCO DE USAR

#INTERFAZ QUE PERMITA ELEGIR IDIOMA Y SEGUN ESO CARGUE LA LISTA DE ESAS PALABRAS (QUIZAS EN UN FUTURO ESCRIBIR TODO EN AMBOS IDIOMAS Y QUE SE TRADUZCA)