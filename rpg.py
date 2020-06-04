import random, os, sys, time, json

def br(): print("=============================================================================================")
def retry(): 
    print("Invalid answer please try again")
    time.sleep(2)
    os.execl(sys.executable, sys.executable, *sys.argv)
def createName():
    rng = random.randint(1, 2)
    if rng == 1:
        prerng = random.randint(0, len(pre) - 1)
        sufrng = random.randint(0, len(suf) - 1)
        name = pre[prerng] + suf[sufrng]
    elif rng == 2:
        adjrng = random.randint(0, len(adj) - 1)
        objrng = random.randint(0, len(obj) - 1)
        name = adj[adjrng] + " " + obj[objrng]
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

# Prefixes
with open("names/pre.txt") as f:
    pre = f.read().splitlines()
# Suffixes
with open("names/suf.txt") as f:
    suf = f.read().splitlines()
# Adjectives
with open("names/adj.txt") as f:
    adj = f.read().splitlines()
# Objects
with open("names/obj.txt") as f:
    obj = f.read().splitlines()
tiers = ["Unique", "Rare", "Legendary", "Mythical"]
types = ["Staff", "Wand", "Foci", "Longsword", "Sword", "Greatbow", "Shortbow", "Mace", "Dagger", "Axe", "Pistol", "Rifle", "Spear", "Relic", "Rifle"]
damagetypes = ["Dark", "Light", "Physical", "Arcane", "Air", "Lightning", "Fire", "Water", "Air"]

br()
print("What would you like to do? (Enter \"help\" for list of commands")
br()
input = input().lower()
br()
if input == "help":
    print(
        "List of commands:\n\n"
        "help| What you're seeing right now\n"
        "chance| Calculates the chance of a single name to be generated\n"
        "pre| Lists all the prefixes\n"
        "suf| Lists all the suffixes\n"
        "adj| Lists all the adjectives\n"
        "obj| lists all the objects/nouns\n"
        "f| Create a new JSON file with randomly generated weapon specifications\n"
        "r| Read the JSON file created beforehand\n"
        "ni| Creates multiple randomly generated names i times (Ex. n10, n9, n45). If it's only n, then 10 randomly generated names are created 10 times"
    )
    br()
elif input == "pre": print(pre)
elif input == "suf": print(suf)
elif input == "adj": print(adj)
elif input == "obj": print(obj)
elif input == "chance":
    chance = 1 / (len(pre)) * (len(suf))
    print("Each name has a " + str(round(chance, 2)) + "% of being created! (1 in " + str(len(pre)) + ")")
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
elif input.startswith("n"):
    times = input.split("n", 1)[1]
    names = ""
    if times == "":
        for n in range(10):
            names += createName() + ", "
        print(names[:-2])
    elif int(times) > 0:
        if int(times) < 101:
            for n in range(int(times)):
                names += createName() + ", "
            print(names[:-2])
        else: print(times + " times is too many times!")
else: retry()