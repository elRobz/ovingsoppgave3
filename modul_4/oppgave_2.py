aldersgrense = 18 

alder = input("Hvor gammel er du? ")
alder = int(alder)

if alder >= aldersgrense:
    print(f"Du er {alder}år, og gammel nok.")
else:
    print(f"Du er {alder}år, og dessverre ikke gammel nok! Pell deg vekk!")
print("Takk for at du sjekket")





# --- Refleksjon ---
# 1.
# Intrykket forteller at det koden under tilhører blokken med if-statementet.
# Kolonet forteller python at det er det under som tilhører koden og skal kjøres etterpå

# 2.
# Fordi den har ikke innrykk, å tilhører ikke if eller else blokk-koden. Den er uavhengig av de og vil bli kjørt uansett!

# 3. 
# Den sjekker om variabel alder har større verdi enn variabel aldersgrense. Hvis den har større verdi kjører den if - hvis den har lavere verdi kjører den else.

# 4.
# Fordi da sjekker den kun om variabel alder er større enn variabel aldersgrense, den bruker det ikke som fasit? Lett feil å gjøre fordi man tenker kanskje matte og glemmer hvordan man gjøre det i programmering?