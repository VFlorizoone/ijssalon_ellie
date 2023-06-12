def decoreer(tekst=""):
    tekst="header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag / personen
    return f"Het bedrag per persoon is {bedrag_pp}"

def onderstreep(tekst=""):
    uit=[]
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(dictionary):
    values = sum(dictionary.values())
    return values

def presenteer(mijn_dict, totaal):
    for k,v in mijn_dict.items():
        print(f"{k} : {v} euro")
    print("==========================")
    print(f"totaal : {totaal} euro")