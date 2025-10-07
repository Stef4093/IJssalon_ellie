def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = round(bedrag / personen,2)
    except:
        bedrag_pp = "??"
    return(f"De gezamenlijke fooienpot komt neer op {bedrag_pp} euro per persoon.")

def onderstreept(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(lijst):
    telop = sum(lijst.values())
    return telop