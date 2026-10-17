riktig_svar = "Oslo"

svar = input("Hva er hovedstaden i Norge? ")

if svar == riktig_svar:
    print("Riktig!")
else:
    print("Feil, svaret var", riktig_svar)

alder = input("Hvor gammel er du? ")
alder = int(alder)

if alder == 18:
    print("Du er akkurat myndig!")
else:
    print("Du er ikke 18.")


# --- Refleksjon ---
# 1.
# Feil nr. 1: det er = og ikke ==, som vil si at den ikke sjekker om svaret er det riktig svaret
# Feil nr. 2: Det er ikke ":" der, som vil si at print("Riktig") ikke tilhører blokken over..
# Feil nr. 3: Det er ikke innrykk, som vil si at printen ikke tilhører else..

# 2.
# Jeg oppdaget den fordi jeg skjønte det var noe feil med koden rundt 18, så etter litt enking
# Så huska jeg at input blir lagret som string, og man må da gjøre inputen om til integer sånn så den sjekker integer mot integer 18

# 3.
# syntaksfeil er hvis du skriver feil, altså en stor bokstav der det ikke skal være, eller du glemmer er symbol eller tegn som " eller :
# mens logisk feil er kanskje rett satt opp men man tenker feil å da blir resultatet feil

# 4.
# skjønner ikke helt hva du mener hvilke verdier det er lurt å teste med
# men i if/else/elif er det jo lurt å teste ut verdier som akkurat ulik resultat, f.eks 18, og over 18, og under 18

