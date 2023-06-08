from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    return(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro.")

def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for i in inkomsten:
        totaal += i
    bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

def hoog_en_laag(mijn_lijst):
    return(max(mijn_lijst),min(mijn_lijst))

def gemiddelde(mijn_lijst):
    totaal = 0
    for i in mijn_lijst:
        totaal += i
    aantal = len(mijn_lijst)
    gemiddelde = totaal / aantal   
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."

def meervoudig(invoer_lijst):
    return hoog_en_laag(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0],korte_lijst[1])

print(combinatie([10,5,3,2,1,2,9]))