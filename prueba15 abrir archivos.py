
def leer(documento):
    e = 0
    doc = open(documento)

    while e != '':
        e = doc.readline()
        print(e, end = '')
    doc.close()





'''

'D:\\python\\doc_prueba\\doc.txt'

'''
