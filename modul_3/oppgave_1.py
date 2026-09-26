# Lag fem variabler som beskriver deg selv. Du skal bruke én av hver datatype:
Navn = "Robin"
Alder = 24
Høyde = 1.8
er_student = True
Hobby = ["lese", "trene", "gaming", "friluft"]

# Skriv ut hver variabel på sin egen linje, med en ledetekst foran:
print("Navn:", Navn)
print("Alder:", Alder)
print("Høyde:", Høyde)
print("er_student:", er_student)
print("Hobby:", Hobby)

# Skriv ut alle fem en gang til, i motsatt rekkefølge av den du brukte over.
print(f"Hobby: {Hobby}\ner_student: {er_student}\nHøyde: {Høyde}\nAlder: {Alder}\nNavn: {Navn}")

# Legg til print(type(navn)) for hver av de fem variablene:
print(type(Navn))
print(type(Alder))   
print(type(Høyde))
print(type(er_student))
print(type(Hobby))

# --- Refleksjon ---
# 1. Jeg måtte ikke flytte på variablene for å endre rekkefølgen. 
# Jeg skrev heller en egen linje for den med f string og formaterte i motsatt rekkefølge. 
# 2. Python skrev ut de riktige datatypene som var ment for hver enkelt.
# 3. Jeg tror python må vite hvilken datatype en variabel har fordi den behandler variablene ulikt utifra hvilken datatype det er.
# Ekstra: Jeg fant ut at ved å bruke "\n" så avsluttes linjen å begynner på ny, da den printes! Mens der man skrive koden er den på samme linje.
