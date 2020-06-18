import os
#Variables Glovales----------------------------------------------------------------------------
ControlNumero = 0
NumeroCollatz = 13
ListaCollatz = []
ListaNumeros = []
#Abrimo un archivo collatz.txt, y si no esta esto lo cre, w es para escritura------------------
file = open("collatz.txt","w") 
#Primer Ciclo Global---------------------------------------------------------------------------
Contador = 2
while Contador <= NumeroCollatz:
    ControlNumero = Contador
    ListaCollatz.append(ControlNumero)
    #Ciclo que determina si el numero es par o impar, si es par lo divide dentro de 2, si es----
    #impar, el numero sera multimlicado por 3 y se le sumara 1, el resultado de ambas ----------
    #operaciones se guardara en una lista llamada ListaCollatz----------------------------------
    while ControlNumero != 1:
        if ControlNumero % 2 == 0:
            #print('El número', ControlNumero, 'es par.')
            ControlNumero = ControlNumero//2
            ListaCollatz.append(ControlNumero)
        else:
            #print('El número', ControlNumero, 'es impar.')
            ControlNumero = ControlNumero*3+1
            ListaCollatz.append(ControlNumero)
    #Agregamos cada ListaCollatz generada por cada numero como un elemento a la lista ListaNumeros
    ListaNumeros.append(str(ListaCollatz))
    #Borramos los elementos de la lista ListaCollatz, primero tomamos el tamaño de la lista------
    #luego borramos el ultimo elemento de dicha lista, el numero de veces igual al tamaño--------
    ContadorBorrar = len(ListaCollatz)
    u = 1
    while u <= ContadorBorrar:
        ListaCollatz.pop()
        u = u + 1 
    #contador del ciclo global-------------------------------------------------------------------
    Contador = Contador + 1
#Escribimos ListaNumeros como string en un archivo .txt
file.write(str(ListaNumeros))
#Imprimimos el resultado en pantalla y cerramos el archivo .txt----------------------------------
print(ListaNumeros)
file.close()
#print(ListaCollatz)