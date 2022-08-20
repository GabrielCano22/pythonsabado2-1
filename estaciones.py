estacion=input("Esciba el mes que desea saber la estación ")

if estacion == 'enero' or estacion =='febrero' or estacion == 'marzo':
    print(f'usted actualmente se encuuentra en el mes de {estacion} y está en invierno')
elif estacion == 'abril' or estacion =='mayo' or estacion == 'junio':
    print(f'usted actualmente se encuuentra en el mes de {estacion} y está en primavera')
elif estacion == 'julio' or estacion =='agosto' or estacion == 'septiembre':
    print(f'usted actualmente se encuuentra en el mes de {estacion} y está en verano')
elif estacion == 'octubre' or estacion =='noviembre' or estacion == 'diciembre':
    print(f'usted actualmente se encuuentra en el mes de {estacion} y está en otoño')
else: print("El nombre del mes que ingresaste, no es correcto")