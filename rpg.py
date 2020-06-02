import random, os, sys, time, json

def br(): print("===============================")
def retry(): 
    print("Invalid answer please try again")
    time.sleep(2)
    os.execl(sys.executable, sys.executable, *sys.argv)
def createName():
    rng = random.randint(1, 2)
    if rng == 1:
        prerng = random.randint(0, len(names1pre) - 1)
        sufrng = random.randint(0, len(names1suf) - 1)
        name = names1pre[prerng] + names1suf[sufrng]
    elif rng == 2:
        adjrng = random.randint(0, len(names2adj) - 1)
        objrng = random.randint(0, len(names2obj) - 1)
        name = names2adj[adjrng] + " " + names2obj[objrng]
    rng0 = random.randint(1, 2)
    if rng0 == 1: return name
    elif rng0 == 2: return "The " + name
def arrRand(foo): return(foo[random.randint(0, len(foo) - 1)])
def createDamage(tier):
    if tier == "Unique": return arrRand(list(range(1, 26)))
    elif tier == "Rare": return arrRand(list(range(26, 51)))
    elif tier == "Legendary": return arrRand(list(range(51, 76)))
    elif tier == "Mythical": return arrRand(list(range(76, 101)))
def getDamageType():
    rng = random.randint(1, 4)
    if rng == 1: return arrRand(damagetypes)
    elif rng == 2:
        dmg1, dmg2 = arrRand(damagetypes), arrRand(damagetypes)
        if dmg1 == dmg2: return getDamageType()
        else: return [dmg1, dmg2]
    elif rng == 3:
        dmg1, dmg2, dmg3 = arrRand(damagetypes), arrRand(damagetypes), arrRand(damagetypes)
        if dmg1 == dmg2 or dmg1 == dmg3 or dmg2 == dmg3: return getDamageType()
        else: return [dmg1, dmg2, dmg3]
    elif rng == 4:
        dmg1, dmg2, dmg3, dmg4 = arrRand(damagetypes), arrRand(damagetypes), arrRand(damagetypes), arrRand(damagetypes)
        if dmg1 == dmg2 or dmg1 == dmg3 or dmg1 == dmg4 or dmg2 == dmg3 or dmg2 == dmg4 or dmg3 == dmg4: return getDamageType()
        else: return [dmg1, dmg2, dmg3, dmg4]


with open("names/names1pre.txt") as f:
    names1pre = f.read().splitlines()
with open("names/names1suf.txt") as f:
    names1suf = f.read().splitlines()
with open("names/names2adj.txt") as f:
    names2adj = f.read().splitlines()
with open("names/names2obj.txt") as f:
    names2obj = f.read().splitlines()
tiers = ["Unique", "Rare", "Legendary", "Mythical"]
types = ["Staff", "Wand", "Foci", "Longsword", "Sword", "Greatbow", "Shortbow", "Mace", "Dagger", "Axe", "Pistol", "Rifle", "Spear", "Relic", "Rifle"]
damagetypes = ["Dark", "Light", "Physical", "Arcane", "Air", "Lightning", "Fire", "Water", "Air"]

print("What would you like to do?")
br()
input = input().lower()
br()
if input == "help": print("List of commands: help, chance, pre, suf")
elif input == "pre": print(names1pre)
elif input == "suf": print(names1suf)
elif input == "chance":
    chance = 1 / (len(names1pre)) * (len(names1suf))
    print("Each name has a " + str(round(chance, 2)) + "% of being created! (1 in " + str(len(names1pre)) + ")")
elif input == "f":
    print("Creating new item JSON...")
    f = open("w1.json", "w")
    name = createName()
    tier = arrRand(tiers)
    j = {
        "name": name,
        "tier": tier,
        "type": arrRand(types),
        "tradeable": arrRand([True, False]),
        "damage": {
            "value": createDamage(tier),
            "types": getDamageType()
        }
    }
    js = json.dumps(j, indent=4)
    f.write(js)
    print("Ding ding! New item created! (" + name + ")")
elif input == "r":
    f = open("w1.json", "r").read()
    jsload = json.loads(f)
    print(
        "Weapon Name: " + jsload["name"] + "\n"
        "Weapon Tier: " + jsload["tier"] + "\n"
        "Weapon Type: " + jsload["type"] + "\n"
        "Tradeable: " + str(jsload["tradeable"]) + "\n"
        # "Damage Value: " + jsload["damage[value]"] + "\n"
        # "Damage Type(s): " + jsload["damage[types]"] + "\n"

    )
    br()
else: retry()