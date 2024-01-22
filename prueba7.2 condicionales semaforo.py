def estado_agua():

    temperatura = input ('A que temperatura está el agua' + '\n' + '\n')
    
    try:
        temperatura = int (temperatura)

        if temperatura <= 0:
                    print ('Hielo')

        elif temperatura > 0 and temperatura < 100:
                    print ('Liquido')

        elif temperatura >= 100:
                    print ('Gaseoso')
    except ValueError:
            print ('Formato no valido' + '\n')
            estado_agua()
        
