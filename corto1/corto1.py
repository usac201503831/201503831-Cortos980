
ControConteo = 2
ControlNumero = 0
Lista = []
i=0
while ControConteo <= 831:
    ControlNumero = ControConteo
    if ControlNumero % 2 == 0:
        ControlNumero = ControlNumero/2
        Lista.append(i)
        print('El número', ControlNumero, 'es par.')
    else:
        ControlNumero = ControlNumero*3 + 1
        Lista.append(i)
        print('El número', ControlNumero, 'es impar.')
    print(Lista)
    ControlNumero = ControlNumero +1