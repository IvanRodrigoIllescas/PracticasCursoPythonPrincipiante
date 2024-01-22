def cont_vocales():

    vocales = 'aeiou'

    num_vocales = 0

    na = 0
    ne = 0
    ni = 0
    no = 0
    nu = 0

    s = input ('Introducir texto para contar' + '\n' + '\n')

    for caracter in s:

        if caracter in 'Aa':
            na = na +1
            num_vocales = num_vocales + 1
        if caracter in 'Ee':
            ne = ne +1
            num_vocales = num_vocales + 1
        if caracter in 'Ii':
            ni = ni +1
            num_vocales = num_vocales + 1
        if caracter in 'Oo':
            no = no +1
            num_vocales = num_vocales + 1
        if caracter in 'Uu':
            nu = nu +1
            num_vocales = num_vocales + 1

    print ('A =', na, 'E =', ne, 'I =', ni, 'O =', no, 'U =', nu, 'Totales', num_vocales)
            
