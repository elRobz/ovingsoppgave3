riktig_brukernavn = "michael"
riktig_passord = "python123"

brukernavn = input("Skriv inn ditt brukernavn: ") == riktig_brukernavn
if brukernavn == True:
    passord = input("Skriv inn ditt passord: ") == riktig_passord
    if passord and brukernavn == True:
        alder = input("Skriv inn alderen din: ")
        alder = int(alder)
        alder >= 13
        riktig_alder = alder >= 13
        if brukernavn and passord and riktig_alder == True:
            print(f"Velkommen, {riktig_brukernavn}!")
        elif riktig_alder == False:
            print("Du er for ung til å logge inn!")
    elif passord == False:
        print("Feil passord")
elif brukernavn == False:
    print("Ukjent bruker.")
else:
    print("Error 404")

# --- Refleksjon ---
# 1. jeg brukte and for å sjekke om alle variablene var true, hvis de ikke var true gikk koden til elif hvor man da fikk en annen beskjed

# 2. SJekkene måtte stå i riktig rekkefølge, først sjekke brukernavn med en elif, så riktig passord hvis riktig brukernavn og en elif, samme med alder, der å må man ha en elif
# Tok også med en else tilfelle noe annet skulle oppstå

# 3. Sånn så hackere skal få minst mulig informasjon om hva som faktisk er feil så de kan teste flere ting med informasjonen de eventuelt ville fått

# 4. fordi eller så kan man lure systemet mest sannsynlig