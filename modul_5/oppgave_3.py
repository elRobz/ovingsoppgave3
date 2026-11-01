#def doble_print(tall):
    #print(tall * 2)

#def doble_return(tall):
    #return tall * 2
    #print("Ferdig!")

#doble_print(5)
#doble_return(5)

#a = doble_print(5)
#b = doble_return(5)
#print(a)
#print(b)

#print(doble_return(5) + 1)
#print(doble_print(5) + 1)

#print(doble_return(doble_return(3)))

# utvidelse

lengde = input("Hvor lang er lengden i cm? ")
lengde = int(lengde)
bredde = input("Hvor brei er bredden i cm? ")
bredde = int(bredde)

def regn_areal(lengde, bredde):
    return lengde * bredde
    
def skriv_areal(lengde, bredde):
    print(f"Arealet på rektangelet er: {regn_areal(lengde, bredde)}cm ")

skriv_areal(lengde, bredde)



# Refleksjon
# 1. fordi man kan ikke regne ut matte utenfor parantes
# 2. Det var none - tror det betyr at verdien ikke har noen verdi?
# 3. at den skal returnere tallet tilbake i funksjonen
# 4. En prosedyre er en funksjon som ikke blir brukt. Mens funksjon er en prosedyre som blir brukt. Prosedyre ville jeg brukt hvis jeg skal ha en funksjon som ikke skal brukes av en person men bare kjøre i programmet. mens en funksjon er noe man kan interacte med ?