alder = 31
aldersgrense = 18
navn = "Michael"
antall_studenter = 30

# Jeg tror svaret blir: 31
print(alder > aldersgrense)

# Jeg tror svaret blir: true (siden alder = 31)
print(alder == 31)

# Jeg tror svaret blir: vet ikke
print(alder != aldersgrense)

# Jeg tror svaret blir: false (siden alder er høyere enn aldersgrense, og "<" vil at aldersgrense skal være høyest? Sånn som i matte?)
print(alder <= aldersgrense)

# Jeg tror svaret blir: true (siden variabel navn = "Michael")
print(navn == "Michael")

# Jeg tror svaret blir: false (siden variabel navn = "Michael", med stor M, ikke liten, og programmeringspråk er sensitiv på sånt!)
print(navn == "michael")

# Jeg tror svaret blir: false (siden antall studenter er ikke høyere enn 30, men det samme)
print(antall_studenter >= 30)

# Jeg tror svaret blir: true (siden alder+5=36, og det er større tall en 30 (som antall_studenter er definert som))
print(alder + 5 > antall_studenter)

# --- Refleksjon ---
# 1. Gir ulikt svar fordi det er forskjell i stor og liten bokstav. Navn er definert som Michael med stor bokstav, da skjønner ikke språket når den bruker liten m, og blir da false
# 2. Forskjellen på = og == tror jeg er at = vil ha likt svar på begge sider, mens == sjekker om det er true eller false
# 3. Jeg tror python gjør dem i den rekkefølgen de er satt opp i, alder + 5 = 36, så >
# 4. True eller false er nyttig i et program for å sjekke om det er riktig eller galt