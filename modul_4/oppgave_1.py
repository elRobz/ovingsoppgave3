navn = input("Hva heter du? ") # lagrer svaret i variabelen navn
alder = input("Hvor gammel er du? ") # lagrer svaret i variabelen alder
høyde = input("Hva er høyden din? Svar i meter! ")
alder = int(alder) # gjør variabelen alder om fra string til en integer (tall)
alder1 = (alder + 1) # lager en ny variabel som kalkulerer ut alder + 1år.
høyde = float(høyde) # gjør høyden om til float (desimaltall)

# Fra oppgaven:
#print("Hei,", navn)
#print(type(alder))
#print(f"Hei, {navn}!")
#print(alder + 1)
#print(type(høyde))

print(f"Hei, {navn}! Du er nå {alder}år gammel! Neste år blir du faktisk {alder1}år gammel! Og du er faktisk {høyde}m lav!")

# --- Refleksjon ---
# 1. 
# Den gir meg type string. Det er fordi alt man skriver i input blir automatisk til string. Det vil si at man må da endre type hvis man vil bruke det til noe annet en string. F.eks til float (desilamtall) eller integer (tall) hvis man vil bruke det..
# Og siden man spør med en string, så blir svaret også lagret som en string? ("Hva er navnet ditt? ") - da er det vel kanskje naturlig at det blir også lagret som en string?

# 2.
# Den klagde på at man kan ikke kan slå sammen to forskjellige typer. Variablene Alder var på daværende tidspunkt en string, og man kan ikke plusse en string med integer.
# Så når man da gjorde variabelen alder om til en integer kunne man gjøre matten. Da ble det integer + integer, og ikke string + integer!

# 3.
# F-string er åpenbart lettere å skrive (som kode), men også lettere å lese for den som skal lese over koden. Det er lettere å forstå med å bruke {} med variabler, og ikke så knotete.

# 4. 
# Det kommer en feilmelding. Inputen forventer å få tall(integer), ikke string.