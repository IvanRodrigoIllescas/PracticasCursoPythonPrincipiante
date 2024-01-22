def convertir_c_f(centigrados):
    '''
    numero --> numero

    Convierte de grados Centigrados a grados Farenheit


    >>>convertir_c_f(20)
    68.0
    
    >>>convertir_c_f(20.56)
    69.008
    '''
    
    farenheit = centigrados * 1.8 + 32

    return farenheit
