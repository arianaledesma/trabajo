#ejercicio 1.

def area_rectangulo(b, a):

    area = b * a

    return area

valor = area_rectangulo(15, 2)

print ("el area es de : ", valor )


#Ejercicio 2.

PI = 3.14159

def area_circulo(radio):

    area = PI * (radio**2)

    return area 

valor = (area_circulo(2))

print ("el circulo es de : ", valor )

# ejercicio 3.

def relacion( num1, num2):

     if num1 > num2 : 

         return 1

     else :

         if num1 < num2:

             return -1

         else: 

             return 0

valor = (relacion(228, 183))

print("la relacion es de : ", valor)

#ejercicio 4

def intermedio (num1,num2):

        promedio = (num1 + num2)/2

        return promedio

valor = (intermedio(62,24))

print ("el intermedio es de : ", valor)

#ejercicio 5.

def recortar(nro,limInf,limsup):

 if nro < limInf :

    return limInf
    
    if nro > limSup :

     return limSup

    else:

        return nro

        valor = ("", valor)

print(recortar(63, 22, 34))


#ejercicio 6.

def separar(listanum):

    listpares = [ ]

    listimpares = [ ]

    numfin = len(listanum)

    for numini in range (0,numfin):

        if (listanum[numini] % 2) == 0:

            listpares.append(listanum[numini])
            
        else:

            listimpares.append(listanum[numini])
            

    print(listanum)
    print(listpares)
    print(listimpares)
    print(numfin)
print(separar([2,3,5,7,8,14,11,15,39,18,25,28,35,49]))