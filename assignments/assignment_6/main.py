from sys import stdin

def sorter(A):
    # Merk: den sorterte lista ma returneres
    # SKRIV DIN KODE HER

def finn(A, nedre, ovre):
    # Merk: resultatet ma returneres
    # SKRIV DIN KODE HER

liste = []
for x in stdin.readline().split():
    liste.append(int(x))

sortert = sorter(liste)

for linje in stdin:
    ord = linje.split()
    minst = int(ord[0])
    maks = int(ord[1])
    resultat = finn(sortert, minst, maks)
    print str(resultat[0]) + " " + str(resultat[1])