#navn = input("Hva er navnet ditt? ").capitalize()
#poeng = input("Hvor mye poeng fikk du på prøven? ")
#poeng = int(poeng)


#def finn_karakter(poeng: int) -> str:
    #if poeng >= 90:
        #return("A!")
    #elif poeng >= 80:
        #return("B!")
    #elif poeng >= 70:
        #return("C!")
    #elif poeng >= 60:
        #return("D!")
    #elif poeng >= 50:
        #return("E!")
    #elif poeng >= 40:
        #return("F!")
    #else:
        #return("ERROR!")


#def skriv_resultat(navn: str, karakter: str) -> None:
    #print(f"Gratulerer {navn}, du fikk karakteren: {finn_karakter(poeng)} ")

#skriv_resultat(navn, poeng)

# ----- del 2

#tall = input("Skriv et tall ")

#def doble(tall: int) -> str:
    #return tall * 2
    #print(doble("5"))

#doble(tall)

# Utvidelse
brus = 24.90
smørbrød = 45
banan = 8.50

def regn_total(brus: float, smørbrød: float, banan: float) -> float:
    return brus + smørdbrød + banan

def legg_til_mva(totalsum: float) -> float:
    return totalsum * 1.25

def del_regning(totalsum: float) -> float:
    return totalsum / 4


# Refleksjon
# 1. Denne, fordi det er mindre kode å lese - mere oversiktlig. 
# 2. Fordi - vet ærlig talt ikke
# 3. vet ikke, kom ingenting i terminalen - men tror poenget med typehint ligger i navnet, man kan forhåndsbestemme hvilken type som er akseptabelt i svaret
# 4. nå må man kun endre et sted hvis mva satsen endres, og det er legg til mva funksjonen