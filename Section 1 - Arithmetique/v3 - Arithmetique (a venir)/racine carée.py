from math import *

puissance = 2
nbMax = 2500
puiMax = 20
listeFinale = []
puiss = []
i = 2
while i <= nbMax :
    listeFinale.append(i)
    i = i + 1
nombre = listeFinale
listePuissance = []

a = 2

while (a <= puiMax) :
    puiA = pow(a,puissance)
    listePuissance.append(puiA)
    a = a + 1

a = 1
while (a <= nbMax) :
    b = 0
    while (b < puiMax - 2) :
        n = listePuissance[b]
        y = a * n
        if y in listeFinale :
            listeFinale.remove(y)
            puiss.append(y)
        b = b + 1
    a = a + 1

#print(listeFinale)
print(len(listeFinale))
print(listeFinale[len(listeFinale)-1])
print(listeFinale)
