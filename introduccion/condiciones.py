# Condiciones y Ciclos
# las condiciones o sentencias condicionales son instrucciones que se ejecutan o no
# a cumplirse una condicion  

# igual ==
# diferencia !=

# Comparar variables numericas
# Menor <
# Mayor >
# Menos o igual que <=
# Mayor o igual que >=

# Expresiones condicionales
# is
# and
# or
# not

# Condicion = No se cumple => Bloque else
#          = Se cumple => Bloque if
# Ejemplo codigo en Python:
#    if <condicion logica>:
#        print("if block")
#    elif<condicion logica>:
#        print("Elif block")
#    else:
#        print("Else block")
        
# Los ciclos
# son instrucciones que se repiten hasta que se cumple una condicion
# Tipos de Ciclos:
# for
# while

# Ciclo For
# for <element> in <object>:
#    print("Elemento:" <element>)
    
# Ciclo While
# while<Condicion>:
#    print("Ciclo while")

a = 10
b = 5
c = 1

if a < b:
    print("A es menor que B")
elif a == b:
    print("A es igual a B")
else:
    print("A es mayor que B")
    
if a>b and b>c:
    print("las dos condiciones son verdaderas")