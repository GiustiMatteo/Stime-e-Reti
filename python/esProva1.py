lista = [10,3,-4,6]
 #lista[2:4]
lista2 = lista[2:4:2] #slicing "2" indica il salto ogni due in questo caso
l = [5,2,3,6,3]
l.append(4)#aggiunge un elemnto alla fine della lista 
print(l)
l.pop(3)#elimina elemento alla cella 3
print(l)
print(l.count(3))#count conta quate volta si trova un elmento nella lista
l.sort()#ordina la lista se non gli passo parametri lui mette dei parametri di default
print(l)
l2 = l #l2 punta l ..se modifico l anche l2 viene modificato
l2 = l[:]#equivalente a copy copia la gli elementi della lista in l2
l.append(999) 
print(l2)
x = input("dammi un numero: ")#equivalente alla scanf
print(x)
for i in range(0,3):
    print(f,i + x)
    