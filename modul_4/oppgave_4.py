# DEL 1:

# Variabler
#alder = 25
#er_student = True
#har_medlemskort = False

# Hva jeg tror resultatene blir:
#alder < 12 or alder < 67 
# den vil være sann, eller true siden 25 er mindre enn 67

#er_student and alder < 30
# Den vil være sann, eller true siden er_student er true fra før og 25 er mindre enn 30

#not har_medlemskort
# Den blir sann, eller true

#er_student and har_medlemskort
# er true siden er_student er true

#er_student or har_medlemskort
# er sann, eller true siden er_student er true

#not er_student or alder < 30 
# blir false, siden er _student er true fra før, og alder(25) er mindre enn 30

#if True:
    #print("Sant")
#if False:
    #print("Usant")

# ---------------------------------------------

# DEL 2:
alder = input("Hvor gammel er du? ")
alder = int(alder)

ordinær_pris = 120
Barn_under_12 = pensjonister_over67 = 0
studenter_under_30 = 50

er_student = input("Er du student? (ja/nei) ").lower() == "ja"
if er_student == True and alder <= 30:
    print(f"Du er en student som er under 30år, prisen for deg blir 50kr!")
elif er_student == True and alder >= 30:
    print(f"Du er student men du er over 30år gammel, du må betale ordinær pris på 120kr!")
elif er_student == False and alder <= 12:
    print(f"Du er er under 12år gammel og regnes som et barn. For deg er det gratis inngang!")
elif er_student == False and alder >= 67:
    print(f"Du er over 67år og du går under kategorien pensjonist. For deg er inngangen gratis!")
else:
    print(f"Du er en glitch i systemet - error 404")

# Forventninger:
# 8 år, ikke student: forventer gratis
# 70, ikke student: forventer gratis
# 22 år, student: forventer 50kr
# 35år, student: forventer ordinær pris
# 25år, ikke student: forventer error

# --- Refleksjon ---
# 1.
# and / og: sjekker om begge stemmer, hvis begge stemmer blir det True, hvis en stemmer eller ingen stemmer blir det False
# or / eller: sjekker om en eller begge stemmer, her trenger kun 1 å stemme for at det skal bli true

# 2.
# 35åringen fikk ordinær pris: fordi jeg kodet det sånn at hvis man er over 30 men student så må man fortsatt betale ordinær pris (kodet fra eget hodet btw so i am proud :D)

# 3. 
# not gjør noe som er True til False, eller omvendt -> noe som er False til True - jeg brukte ikke Not i det hele tatt, så i guess i can

# 4.
# Den vil ikke gå siden jeg kodet det sånn jeg kodet

# Gjerne si fra om måten jeg kodet det på er "tungvindt" og om det er en lettere måte eller ryddigere måte, eller om det er bra!
