
# 1.feladat: Hozzunk létre egy olyan dictionary-t, amelyben a régiók a kulcsok, a bolgyók pedig az értékek!


fh = open("C://Users/vend/Desktop/sw_planets.csv","r")  #fájl megnyitás ("r") megadott últvonalról
planets = {}                                            #planets nevű dictionary létrehozása
for line in fh:                                         #fájl beolvasás soronként
    planet, regio = line.strip().split(",")             #bolgyó-régió szeparáltság (vesszővel) meadása split-el, enterek figyelmen kívül hagyása strip()
    if regio in planets: planets[regio].append(planet)  #amennyiben a régió már szerepel a dict-ben, akkor ezen régióhoz, mint kulcshoz rendelje az következő bolgyót, mind értéket
    else: planets[regio]=[planet]                       #különben (nem tartalmazza), hozzon létre egy új kulcsot értékkel együtt

print("1. feladat megoldása:")
print(planets)

# 2.feladat: Határozzuk meg, melyik régió tartalmazza a legtöbb bolygót (melyik kulcs tartalmaz legtöbb értéket)!

max=0                                                   #"legtöbb érték" változó deklarálása
reg=""                                                  #a "legtöbb értékhez" tartozó kulcs deklarálása
for regio in planets:                                   #planets dict bejárása
    if len(planets[regio])>max:                         #amennyiben a vizsgálandó kulcshoz tartozó értékek száma nagyobb, mint az eddigi "legtöbb érték"
        max=len(planets[regio])                         #adja át a darabszámot a max változónak
        reg=regio                                       #a "legtöbb értéket" tartalmazó kulcs átadása a reg változónak

print("2. feladat megoldása:")
print("The biggest regio is {regio} with {len} planets.".format(regio=reg, len=max))

# 3.feladat: Határozzuk meg az 5 leggyakrabban használt szót a Háború és béke c. könyvből!
"""
könyvtár importálása: a Counter dict-ként tárolja a kulcsokat és az értékeket, és lehetőséget biztosít három különböző
metódust meghívni:
elements(): olyan értékkel tér vissza, amelyben annyiszor listázza ki az adott kulcsot, ahány értékkel rendelkezik, feltéve, 
hogy az érték nagyobb, mint 1.
most_common(): a kulcshoz tartozó értéket gyakoriságként tárolja és az érték szerint csökkenő sorrendben tárolja a kulcsokat.
Lehetőségünk van a zárójelbe írt db számnak megfelelő mennyiségű kulcsot kilistázni. 
substract(): kivonó metódus - 2 dict azonos kulcsainak értékeit kivonja egymásból. Szintaktika: c.substract(d) - c-ből
vonja ki d-t
"""
from collections import Counter

fh = open("C://Users/vend/Desktop/war_and_peace.txt","r")   #fájl megnyitás ("r") megadott últvonalról
words = Counter()                                           #words Counter objektum deklarálása

for line in fh:                                             #fájl beolvasás soronként
    words.update([word.strip(".,;\n") for word in line.lower().split()])
                                #a words kulcsokat ".,;" és entereket figyelmen kívül hagyva a csupa kisbetűs szövegben
                                #a Counter objektum a szavak előfordulásainak megfelelő értékkel látja el
print("3. feladat megoldása:")
print(words.most_common(5))     #az értékek szerinti csökkenő sorrendben tárolt kulcsok közül az első 5-öt kilistázza