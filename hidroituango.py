#la entrada o entradas del problema

nivelAgua=int(input("Digita el nivel de agua de la represa"))

#Proceso del problema 
if(nivelAgua>=0 and nivelAgua<20):
    print(f'el nivel de agua {nivelAgua} es muy bajo')
elif(nivelAgua>=20 and nivelAgua<400):
    print(f'el nivel de agua{nivelAgua} es óptimo')
elif(nivelAgua>=400):
    print(f'el nivel de agua {nivelAgua} es muy alto')
else: print("Digite una opción válida")