"""
VARIABLES LOCALES:
                    Son aquellas que defino dentro de la función y solo sirven 
                    dentro de esta.

VARIABLES GLOBALES: 
                    Son variables que se definen por fuera de una funcion y sirven
                    para todas las funciones. 

"""


#Declaramos una variable global

frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

def hola_mundo(frase):
    print(f"Sin declarar variable local me imprime esto:\n {frase}" )

    frase = "A palabras necias, oidos sordos"

    print(f"Sin declarar variable local me imprime esto:\n {frase}" )


def otra_funcion():
    print(f"Estando en otra funcion me imprime = \n {frase}")


hola_mundo(frase)
otra_funcion()