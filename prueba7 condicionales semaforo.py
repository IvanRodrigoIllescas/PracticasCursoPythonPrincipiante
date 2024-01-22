color = 'verde'

def que_hago():
    
    if color == 'verde':
        print ('Pasa')

    elif color == 'amarillo':
        print ('Precaucion')

    elif color == 'rojo':
        print ('Para')

    else:
        print ('Error')




        

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




'''
2º Posible solucion para averiguar el estado del agua


def estado_agua():


    temperatura = ''
        
    while temperatura == '':
        try:
            temperatura = int (input ('a que temperatura está el agua' + '\n' + '\n'))

            if temperatura <= 0:
                    print ('Hielo')

            elif temperatura > 0 and temperatura < 100:
                    print ('Liquido')

            elif temperatura >= 100:
                    print ('Gaseoso')
        except ValueError:
            print ('Formato no valido')
        '''

    

   

