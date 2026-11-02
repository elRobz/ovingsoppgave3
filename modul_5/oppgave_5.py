## DEL 1

# Snutt 1:
#def lag_hilsen():
    #melding = "Hei!"
    #print(melding)

#lag_hilsen()
#print(melding)

# lag_hilsen er en funksjon med en variabel melding som sier "Hei!", dette er en lokal scope siden den er låst i en funksjon, den printes i funksjonen. Under så blir funksjonen kallet på med lag_hilsen(), og da vil variabelen printes. den printer som er under vil ikke bli kjørt siden den ikke har tilgang til noen variabel som heter melding.
# da kjørte jeg den å jeg hadde litt feil - fikk feilmelding faktisk, jeg trodde den ville kjøre å bare ignorere

# Snutt 2:
#by = "Oslo"

#def skriv_by():
    #print(f"Jeg bor i {by}.")

#skriv_by()

# by variabelen er en global scope, i funksjonen blir den hentet i en f string. her vil alt gå smooth og det blir printet "jeg bor i oslo" siden funksjonen blir kalt på under

# Snutt 3:
#def doble(tall):
    #tall = tall * 2
    #print(f"Inne: {tall}") 

#tall = 5
#doble(tall)
#print(f"Ute: {tall}")



## DEL 2

poeng = 0

def legg_til_poeng(poeng: int) -> int:
    return poeng + 10

poeng = legg_til_poeng(poeng)
print(f"Du har nå {poeng}poeng mere en 2 sek siden!")

def legg_til_poeng_2(poeng: int) -> int:
    return poeng + 25

poeng = legg_til_poeng_2(poeng)
print(f"Du har nå {poeng}poeng mere en 2 sek siden!")

def trekk_fra_poeng(poeng: int) -> int:
    return poeng - 5

poeng = trekk_fra_poeng(poeng)
print(f"Du har nå {poeng}poeng, det er 5 stk mindre en 2 sek siden!")



# REFLEKTER
# 1. Snutt 1: lag_hilsen er en funksjon med en variabel melding som sier "Hei!", dette er en lokal scope siden den er låst i en funksjon, den printes i funksjonen. Under så blir funksjonen kallet på med lag_hilsen(), og da vil variabelen printes. den printen som er under vil ikke bli kjørt siden den ikke har tilgang til noen variabel som heter melding. siden den er låst i en variabel. det vil komme feilmelding eller så blir den bare ikke kjørt.
# 1. Snutt 3: her er også tall = 5 en global scope, utenfor funksjonen, men siden den er over der funksjonen blir kalt på så blir den medregnet i funksjonen, selvom pythonkode går fra topp til bunn. Siden det er global scope så har begge printstatemens tilgang til den så da blir begge kjørt. men hadde funksjonen blitt kalt på før den globale scopen var "tilgjenglig" så ville den ikke kjørt.

# 2. fordi man ikke har gitt funksjonen noe parameter? også blir jo ikke regnestykket "poeng += 10" brukt til noe siden den ikke blir returnert?

# 3. ville valgt b. lettere å lese å vedlikeholde. hva som skjer når poengsummen blir feil er at det det stopper å funke