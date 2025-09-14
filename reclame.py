from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    return(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-(prijs * korting)} euro.")

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    btwtotaal = 0
    for i in inkomsten:
        totaal = totaal + i
    for j in btw:
        btwtotaal = btwtotaal + j
    return(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btwtotaal} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    return([max(mijn_lijst),min(mijn_lijst)])

def gemiddelde(mijn_lijst):
    tellen = 0
    for i in mijn_lijst:
        tellen += 1 
    return(f"De gemiddelde inkomsten deze week zijn {sum(mijn_lijst) / tellen} euro.")

def meervoudig(invoer_lijst):
    return(laag_en_hoog(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return(mijn_functie_2(korte_lijst[0],korte_lijst[1]))