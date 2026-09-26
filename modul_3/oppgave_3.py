brus = 24.90
smørbrød = 45
banan = 8.50

# Totalsum for alle tre varene: (Bruker 'f-string' for å blande ord og matte!), tok også med kr!
print(f"Totalsum for alle tre varene = {brus+smørbrød+banan}" + "kr")
#print (type(brus+smørbrød+banan))

# Totalsum med 25% mva: tar med kr her også
print(f"Totalsum med 25% mva = {brus+smørbrød+banan*1.25}" + "kr")

# Pris per person hvis fire personer deler regningen likt.
print(f"Hvis regningen deles på fire personer, må hver enkelt betale = {brus+smørbrød+banan*1.25/4}" + "kr")
#print(type(brus+smørbrød+banan*1.25/4))

# Prisforskjellen mellom den dyreste og den billigste varen.
print(f"Prisforskjellen på den billigste og dyreste varen = {smørbrød-banan}" + "kr")

# --- Refleksjon ---
# Datatypen brus, smørbrød og banan ble til var float.
# Datatypen brus, smørbrød og banan med 25% mva delt på 4 ble også float
# Fordelen med å brukte variabler i stedet for å skrive tallene på nytt hver gang er jo akkurat det .. koden blir lettere å vedlikeholde hvis det skulle skje endringer. F.eks. i en butikk hvor priser endrer seg ofte, da trenger man kun å endre prisen et sted, så vil variablene følge den automatisk.