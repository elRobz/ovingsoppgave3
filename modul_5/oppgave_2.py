navn = input("Hei, hva heter du? ")
alder = input(f"Hei {navn}, hvor gammel er du? ")

def hilsen(navn, alder, by="Oslo"):
    print(f"Hei, {navn}! Du er {alder}år gammel! Du bor i {by}! ")

hilsen(alder=31, navn="Robert")

# Refleksjoner
# 1. parameter er det man har i def hilsen - det definerer de ulike parameterne man vil gjøre noe med i selve funksjonen. argument er det man gir de ulike paramterne. navn er parameter mens "Robin" er argument. så da i starten av def hilsen(navn) beskriver man at man vil gjøre noe med parameteret navn, og den verdien man da gir parameteren navn, er da argumentet-
# 1. navn, alder og by er parameter, mens 31, robert og oslo er argument. også input over koden er jo da argument som man kan bruke i funksjonen. btw, så er inputene som er variabel navn og alder global scopes, altså globale variabler som kan brukes i hele koden mens by er en local scope som kun kan brukes i funksjonen
# 2. ga ikke feilmelding, men den ble omvendt plassert
# 3. fungerte likevel, sammenhengen sier at det man kan skrive hvilket som helst argument på en parameter så lenge den ikke er bestemt på forhånd i koden, som kan være lurt hvis det er spesifikt type man skal ha
# 4. navngitte argumenter er nyttige når det er en mulighet at brukeren glemmer å skrive inn et argument, eller når det er forhåndsbestemt hva det er

