def skriv_skillelinje():
    print("-" * 20)

def skriv_meny():
    skriv_skillelinje()
    print("--- Meny ---")
    print("1. Pizza")
    print("2. Burger")
    print("3. Salat")
    skriv_skillelinje()

def skriv_velkomst():
    print("Velkommen til oss")
    print("Gratis brus på deg!")

skriv_velkomst() 
skriv_meny()

# --- Refleksjon ---
# 1. Ingenting skjedde - fordi en funksjon funker bare hvis den blir kallet på.
# 2. Når du definerer en funksjon så lager du den, og lager selve koden. Du er som en kokk som lager maten.
# Mens når du kaller på en prosedyre, så henter du/serverer den koden som en servitør. Altså koden blir brukt der den trengs.
# 3. "NameError: name 'skrive_meny' is not defined" - det sier at python leser filen fra topp til bunn. Når skriv_meny() er øverst så vet enda ikke python at den er definert, før den går et hakk ned, og da er det feil i logikk/rekkefølge.
# 4. Hvis noe er repetivt, som det ofte er i objektorientert programmering, - noe du skal bruke opp igjen mye så kan du lage en funksjon å kalle på prosedyren istedet for å copy paste koden gang på gang - også er det mere oversiktlig i koden, og du trenger færre linjekoder som gjør at også koden kan gå fortere (siden den leser fra topp til bunn)
# 5. Det som skjer med skriv_meny() med skriv_skillelinje() er at det blir en automatisk å fin formatering i terminalen.