dim = input("inserisci la dimensione della lista : ")
lista = [] #crea una lista vuota

for i in range (int(dim)):
    x = input("inserisci un numero: ")
    lista.append(x)
print(lista)

ancora = True
lista2 = []
dim = input("inserisci la dimensione della lista : ")
while(ancora == True):
    lista2.append(input("inserisci un numero"))
    if(input("vuoi inserisci ancora? ") == True):
        ancora = True
    else:
        ancora = False    