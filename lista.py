lista = [ ]

cant = int(input( "cantidad de productos" ))
totaltotal=0

for  i in range(cant):

    nro_suc = int (input(" nro de sucursal: "))

    nombre = input( "nombre de sucursal" )

    ventas = int(input( "cantidad de ventas" ))

    total = int (input( "inporte total de ventas"))

    promedio = total / ventas

    print (f"nro sucursal: {nro_suc}")

    print (f"nombre sucursal: {nombre}")

    print (f"cantidad de ventas: {ventas}")

    print (f"inporte total de ventas: {total}")
    print (f"promedio: {promedio}")
    totaltotal = totaltotal + total

print (f"nombre sucursal: {totaltotal}")