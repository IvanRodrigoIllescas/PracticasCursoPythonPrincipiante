def calc_media(lista_examenes):

    media = 0

    n = 0
   
    for i in lista_examenes:
        
        media = media + i[1]
        
    media = media / len(lista_examenes)

    print (media)
    






'''s = [['E1', 3],['E2', 8],['E3', 6],['E4', 5],['E5', 2]]

 media = media + lista_examenes[0][1]

    print (media)

'''
