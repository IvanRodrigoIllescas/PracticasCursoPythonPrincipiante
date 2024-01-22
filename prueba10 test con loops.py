def preguntar(pregunta):

    pregunta = '¿' + pregunta + '?' + '\n' + '\n'
    
    respuesta = input (pregunta)

    respuesta = respuesta.strip()
    
    while not (respuesta == 'si' or respuesta == 'no'):
        print ('respuesta no valida' + '\n')
        respuesta = input (pregunta)
        respuesta = respuesta.strip()

    return respuesta 
