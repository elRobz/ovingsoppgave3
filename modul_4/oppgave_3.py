navn = input("Hva er navnet ditt? ")
poeng = input("Hvor mye poeng fikk du på prøven? ")
poeng = int(poeng)

if poeng >= 90:
    print(f"Du fikk karakteren: A! Gratulerer {navn}.")
elif poeng >= 80:
    print(f"Du fikk karakteren: B! Gratulerer {navn} - du er akkurat dårlig nok til å ikke være best!")
elif poeng >= 70:
    print(f"Du fikk karakteren: C! Gratulerer {navn} - du er helt gjennomsnittlig..")
elif poeng >= 60:
    print(f"Du fikk karakteren: D! Gratulerer {navn} - D for Drittdårlig!")
elif poeng >= 50:
    print(f"Du fikk karakteren: E! Gratulerer {navn} - E for Ekstra dårlig")
elif poeng >= 40:
    print(f"Du fikk karakteren: F! Gratulerer {navn} - du er helt fortapt!")
else:
    print(f"{navn}.. du er så dårlig at du ikke fikk en F engang!")

# Gjør nummer 4:
#if poeng >= 40:
    #print(f"Du fikk karakteren: F! Gratulerer {navn} - du er helt fortapt!")
#elif poeng >= 50:
    #print(f"Du fikk karakteren: E! Gratulerer {navn} - E for Ekstra dårlig")
#elif poeng >= 60:
    #print(f"Du fikk karakteren: D! Gratulerer {navn} - D for Drittdårlig!")
#elif poeng >= 70:
    #print(f"Du fikk karakteren: C! Gratulerer {navn} - du er helt gjennomsnittlig..")
#elif poeng >= 80:
    #print(f"Du fikk karakteren: B! Gratulerer {navn} - du er akkurat dårlig nok til å ikke være best!")
#elif poeng >= 90:
    #print(f"Du fikk karakteren: A! Gratulerer {navn}.")
#else:
    #print(f"{navn}.. du er så dårlig at du ikke fikk en F engang!")



# --- Refleksjon ---
# 1.
# 95 poeng fikk F, det skjedde fordi den var byttet om på rekkefølgen

# 2.
# IF sjekker om noe stemmer, og da printes det, mens elif har da logikken, hvis det over ikke stemmer sjekker den den neste, og så neste og så neste.. Så hvis du har alle på IF så vil den printe alle

# 3.
# Fordi vi har en elif under som sjekker de under der igjen, som da setter en grense 

# 4.
# Else-blokken kjører hvis ingen av de blokkene med if/ eller elif matcher. På 150poeng så printer den A, siden det ikke er satt noe max grense!
