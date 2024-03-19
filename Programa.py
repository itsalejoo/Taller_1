#programa para genrar un numero aleatorio en python 


import random
#la función input() captura un dato desde el telcado
#como si fuera una cadena de texto (string)
a=input("limite inferior:")
b=input("limite superior:")

#convertir a y b a enteros 
a=int(a)
b=int(b)
respuesta=random.randint(a,b)
print(respuesta)








