
zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},

]

zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]

objekty_zvirat = []
objekty_zamestnanci = []

def vytvoreni_zvirat_z_dict():
    for animal in zvirata_dict:
        objekty_zvirat.append(Zvire(animal["jmeno"], animal["druh"], animal["vaha"]))

def vytvoreni_zamestnancu_z_dict():
    for zamestnanec in zamestnanci_dict:
        objekty_zamestnanci.append(Zamestnanec(zamestnanec["cele_jmeno"], zamestnanec["rocni_plat"], zamestnanec["pozice"]))


class Zvire:
    def __init__(self, jmeno: str, druh: str, vaha: int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha
    
    def __str__(self) -> str:
        return f"{self.jmeno}, což je {self.druh} a jeho/jeji vaha je {self.vaha}. "
    
    def export_to_dict(self):
        export_d = {}
        export_d["jmeno"] = self.jmeno
        export_d["druh"] = self.druh
        export_d["vaha"] = self.vaha
        return export_d

class Zamestnanec:
    def __init__(self, cele_jmeno: str, rocni_plat: int, pozice: str):
        self.cele_jmeno = cele_jmeno
        self.rocni_plat= rocni_plat
        self.pozice = pozice
    
    def __str__(self) -> str:
        return f"Zaměstnanec se jmenuje {self.cele_jmeno}, pracuje na pozici: {self.pozice} a ročně vydělá {self.rocni_plat}Kč. "

    def ziskej_inicialy(self):
        list_jmena = (self.cele_jmeno.split())
        pracovni_inicialy = (list_jmena[0][0], list_jmena[1][0], "")

        inicialy = ".".join(pracovni_inicialy)
        return inicialy

class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno: str, rocni_plat: int, oblibene_zvire: Zvire, pozice: str = "Reditel"):
        super().__init__(cele_jmeno, rocni_plat, pozice)
        self.oblibene_zvire = oblibene_zvire
    def __str__(self) -> str:
        return super().__str__() + f"Oblíbencem je {self.oblibene_zvire}"

class Zoo:
    def __init__(self, jmeno: str, adresa: str, reditel: Reditel, zamestnanci: list[Zamestnanec], zvirata: list[Zvire]):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata

    # def __str__(self) -> str:
    #     return f"Zoo se jmenuje: {self.jmeno}, sídli na adrese: {self.adresa}, jejím ředitelem je: {self.reditel} a zamestnanci jsou: {self.zamestnanci} a sídli zde tato zvířata: {self.zvirata}" 

    def vaha_vsech_zvirat_v_zoo(self):
        vysledna_vaha = 0
        for zvire in self.zvirata:
            vysledna_vaha += getattr(zvire, "vaha", 0)
        return vysledna_vaha

    def mesicni_naklady_na_zamestnance(self):
        vysledne_naklady = (getattr(self.reditel, "rocni_plat", 0))/12
        for zamestnanec in self.zamestnanci:
            rocni_naklady = 0
            rocni_naklady += getattr(zamestnanec, "rocni_plat", 0)
            mesicni_naklady = rocni_naklady/12
            vysledne_naklady += mesicni_naklady
        return int(round(vysledne_naklady, 0))

# croco = Zvire("Croco", "krokodyl nilsky", "1 tuna")
# lala = Zvire("Lála", "Irbis", "5kg")

# print(croco)
# print(lala)

# croco_export = croco.export_to_dict()
# lala_export = lala.export_to_dict()

# assert croco_export["jmeno"] == "Croco"
# assert croco_export["druh"] == "krokodyl nilsky"
# assert croco_export["vaha"] == "1 tuna"

# print(lala_export)
# print(croco_export)

vytvoreni_zvirat_z_dict()
vytvoreni_zamestnancu_z_dict()

# print(objekty_zvirat[1])

# Růženka_export = objekty_zvirat[0].export_to_dict()

# print(Růženka_export)

# Adolf = Zamestnanec("Adolf Mánička", 100000, "uklízeč")
# print(Adolf)


# print(Adolf.ziskej_inicialy())
# print(objekty_zamestnanci[1])

reditel = Reditel(cele_jmeno='Karel Louse', rocni_plat=800_000, oblibene_zvire=objekty_zvirat[0])

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, objekty_zamestnanci, objekty_zvirat)

# print(zoo.zvirata[0])

print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo(), 'Kg.' )
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance(), "Kč.")

# Zvire class
zvire = Zvire('Láďa', 'Koala', 15)
assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}

# Zamestnanec class
zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programator')
assert hasattr(zamestnanec, 'cele_jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.cele_jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
assert zamestnanec.ziskej_inicialy() == 'P.N.'

# Reditel class
zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel('Jan Novotny', 80000, zvire)
assert isinstance(reditel.oblibene_zvire, Zvire)

# Zoo class
zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'jmeno')
assert hasattr(zoo, 'adresa')
assert hasattr(zoo, 'reditel')
assert hasattr(zoo, 'zamestnanci')
assert hasattr(zoo, 'zvirata')
assert isinstance(zoo.jmeno, str)
assert isinstance(zoo.adresa, str)
assert isinstance(zoo.reditel, Reditel)
assert isinstance(zoo.zamestnanci, list)
assert isinstance(zoo.zvirata, list)
assert zoo.vaha_vsech_zvirat_v_zoo() == 150
# assert zoo.mesicni_naklady_na_zamestnance() == (zamestnanec.rocni_plat + reditel.rocni_plat) / 12 # protoze mam roundnuto
