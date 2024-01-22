def viajar():

    paises = []

    pregunta = '¿Que paises quieres visitar?'

    pais = input (pregunta)

    while pais != '':
        
        paises.append(pais)
        pais = input (pregunta)

    if pais == '':
        
        return (paises)


paises= ['portugal', 'suiza', 'japon']

def borrar():

    pais = input ('q quieres borrar')

    if pais in paises:
        paises.remove(pais)
        print ('hecho')

    else:
        print ('no esta en la lista')

    

    
    
