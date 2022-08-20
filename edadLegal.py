edad=int(input("Por favor ingrese su edad "))

if(edad >=0 and edad <14):
    print(f'usted tiene {edad}años y es considerado un niño')
elif(edad >=14 and edad <28):
    print(f'usted tiene {edad}años y es considerado un joven')
elif(edad >=28 and edad <60):
    print(f'usted tiene {edad}años y es considerado un adulto')
elif(edad >=60 and edad <=100):
    print(f'usted tiene {edad}años y es considerado un adulto mayor')
else: 
    print("Por favor ingrese una edad válida")
