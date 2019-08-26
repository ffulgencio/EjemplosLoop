# comentario de una linea

"""
Comentario de 
multiples lineas.
Esta forma de comentario
tambien se conoce como docstring (en python)
"""

cont = 1

while cont <= 100:
    cont = cont + 1
    if  cont % 2 > 0:
        continue
    print(cont)

print(" Contador: ",cont)
    