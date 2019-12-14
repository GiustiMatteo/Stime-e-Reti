"""
documento il programma
"""
def somma(a,b):
    return a + b
lista = [1,"ciao",3,somma(3,4)]
print(somma(10,8))
for i in lista:
    print(i)
print(lista)
posizione = 1
print(lista[posizione]) 
print(lista[3:5])#indico il range dlla posizione escluso i valori inseriti(3,5)
j = len(lista)
print(j)


