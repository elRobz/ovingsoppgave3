
def regn_pris(antall: int, pris_per_stk: float) -> float:
    total = antall * pris_per_stk
    print(f"Du betalte {total} kr.")
    return total

def skriv_kvittering(navn, total):
    print(f"Kvittering for {navn}")
    print(f"Totalt: {total} kr")

def avslutt():
    print("Takk for handelen!")

pris = regn_pris(3, 49.90)
skriv_kvittering("Michael", pris)
print(f"Du betalte {pris} kr.")
avslutt

## refleksjon

# 1. feilene var det manglet : bak ene funksjonen så den viste ikke at det under skulle leses av i funksjonen
# 1. andre feilen var at det ikke var innrykk på ene koden under funksjonen så den viste ikke at det var i samme kodeblokk

# 2. to feil som ikke ga feilmelding var logikkfeil, ikke syntaksfeil, det var bare littfeil tenking av variabler, brukt feil variabler i f strings

# 3. vet ærlig talt ikke xd