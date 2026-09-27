poeng = 0

# Jeg tror poeng blir: 10
poeng = poeng + 10
print(poeng)

# Jeg tror poeng blir: 25
poeng += 25
print(poeng)

# Jeg tror poeng blir: 30
poeng -= 5
print(poeng)

# Jeg tror poeng blir: 60
poeng *= 2
print(poeng)

# Jeg tror poeng blir: 15
poeng /= 4
print(poeng)

# --- Refleksjon ---
# 1. Alle forutsigelsene mine stemte utenom nr 2. Nr 1 skjønte jeg jo siden det legges til 10 poeng.
# 1. Og etter nr 2 skjønner jeg at den lagrer poengene fra forrrige print å bruker i regnestykket, så etter det forutser jeg hvert svar.
# 2. Svaret på siste steget ble til 15.0 - altså et desimaltall, og da datatypen float. Jeg vet ikke hvorfor, null peiling.
# 3. Ja svaret ble det samme med utvidelsen. Men poenget er jo at det er tungvindt å skrive det på hver enkelt ting. Kode skal være så enkelt som mulig og skalerbart og enkelt å vedlikeholde.

# Så sånn jeg forstår +=, -=, *=, /=, så husker den svaret fra forrige reknestykket, å bruker det å lagrer det til neste regnestykket?