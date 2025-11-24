from enum import Enum
import requests

STALA =3.13
"""
class tryb(Enum):
    wylaczony = 0
    wejscie = 1
    wyjscie = 2
    iolink =3

print(tryb.iolink.name)
print(tryb.iolink.value)
mode=tryb.iolink.value
print(mode)
#if tryb.iolink.name ==

data1={"code":"request","cid":1,"adr":"/connections/mqttConnection/mqttCmdChannel/status/start"}
data2={"code":"request","cid":1,"adr":"/connections/mqttConnection2/mqttCmdChannel/status/start"}
data3={"code":"request","cid":1,"adr":"/connections/mqttConnection3/mqttCmdChannel/status/start"}
auth={"user":"YWRtaW4=","passwd":"cGFzc3dvcmQ="}
lista=[data1,data2,data3]

for item in lista:
    item['auth']=auth
    print(item)
"""
dict1={'a': [1,3,4,5,6],'b':  [1,3,4,5,6],'c':  [1,3,4,5,6],'d':  [1,3,4,5,6],'e':  [1,3,4,5,6],}

for x,y in dict1.items():       # iteracja po kluczu i wartosc mozliwosc wyswietlania obu argumentow slownika
    print(f"klucz :{x} ,wartosc :{y}")
    for item in y:
        print(item)
for x in dict1:
    print(f"klucz :{x}")

for x in dict1.values():
    print(f"wartosc :{x}")
    print("XXXX", dict1)
    print("Ilosceelemntow",len(dict1))

    class Czlowiek:  # ZACZYNAMY Z DUZEJ LITERY
        def __init__(self, imie, wiek):
            self.imie = imie
            self.wiek = wiek

        def przedstawSie(self, powitanie="Czesc"):
            return powitanie + " mam na imie " + self.imie + "i mam " + str(self.wiek) + " lat"

class Port:
    def __init__(self, number):
        self.number = number
    def mode(self, mode):
        print(mode)


"""

class dataline_mqtt(Enum):
    mqttcmdchannel_status = ['/connections/mqttConnection/mqttCmdChannel/status', ['']]
    mqttcmdchannel_status_datachanged = ['/connections/mqttConnection/mqttCmdChannel/status/datachanged',
                                                 ['/subscribe', '/unsubscribe', '/getsubscriptioninfo']]
    mqttcmdchannel_status_preset = ['/connections/mqttConnection/mqttCmdChannel/status/preset',
                                            ['/getdata', '/setdata']]
    mqttcmdchannel_status_preset_datachanged = [
                '/connections/mqttConnection/mqttCmdChannel/status/preset/datachanged',
                ['/subscribe', '/unsubscribe', '/getsubscriptioninfo']]
    mqttcmdchannel_status_reset = ['/connections/mqttConnection/mqttCmdChannel/status/reset', ['']]
    mqttcmdchannel_status_start = ['/connections/mqttConnection/mqttCmdChannel/status/start', ['']]
    mqttcmdchannel_status_stop = ['/connections/mqttConnection/mqttCmdChannel/status/stop', ['']]
    mqttcmdchannel_type = ['/connections/mqttConnection/mqttCmdChannel/type', ['/getdata', '/setdata']]
    mqttcmdchannelsetup_brokerip = ['/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/brokerIP',
                                            ['/getdata', '/setdata']]
    mqttcmdchannelsetup_brokerip_datachanged = [
                '/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/brokerIP/datachanged',
                ['/subscribe', '/unsubscribe', '/getsubscriptioninfo']]
    mqttcmdchannelsetup_brokerport = [
                '/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/brokerPort', ['/getdata', '/setdata']]
    mqttcmdchannelsetup_brokerport_datachanged = [
                '/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/brokerPort/datachanged',
                ['/subscribe', '/unsubscribe', '/getsubscriptioninfo']]
    mqttcmdchannelsetup_cmdtopic = ['/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/cmdTopic',
                                            ['/getdata', '/setdata']]
    mqttcmdchannelsetup_cmdtopic_datachanged = [
                '/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/cmdTopic/datachanged',
                ['/subscribe', '/unsubscribe', '/getsubscriptioninfo']]
    mqttcmdchannelsetup_defaultreplytopic = [
                '/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/defaultReplyTopic',
                ['/getdata', '/setdata']]
    mqttcmdchannelsetup_defaultreplytopic_datachanged = [
                '/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/defaultReplyTopic/datachanged',
                ['/subscribe', '/unsubscribe', '/getsubscriptioninfo']]
    mqttconnection_status = ['/connections/mqttConnection/status', ['']]
    mqttconnection_status_datachanged = ['/connections/mqttConnection/status/datachanged',
                                                 ['/subscribe', '/unsubscribe', '/getsubscriptioninfo']]
    mqttconnection_status_preset = ['/connections/mqttConnection/status/preset', ['/getdata', '/setdata']]
    mqttconnection_status_preset_datachanged = ['/connections/mqttConnection/status/preset/datachanged',
                                                        ['/subscribe', '/unsubscribe', '/getsubscriptioninfo']]
    mqttconnection_status_reset = ['/connections/mqttConnection/status/reset', ['']]
    mqttconnection_status_start = ['/connections/mqttConnection/status/start', ['']]
    mqttconnection_status_stop = ['/connections/mqttConnection/status/stop', ['']]
    mqttconnection_type = ['/connections/mqttConnection/type', ['/getdata', '/setdata']]
    mqttsetup_keepalive = ['/connections/mqttConnection/MQTTSetup/KeepAlive', ['/getdata', '/setdata']]
    mqttsetup_keepalive_datachanged = ['/connections/mqttConnection/MQTTSetup/KeepAlive/datachanged',
                                               ['/subscribe', '/unsubscribe', '/getsubscriptioninfo']]
    mqttsetup_qos = ['/connections/mqttConnection/MQTTSetup/QoS', ['/getdata', '/setdata']]
    mqttsetup_qos_datachanged = ['/connections/mqttConnection/MQTTSetup/QoS/datachanged',
                                         ['/subscribe', '/unsubscribe', '/getsubscriptioninfo']]
    mqttsetup_version = ['/connections/mqttConnection/MQTTSetup/version', ['/getdata', '/setdata']]


dl_mqtt = dataline_mqtt
for item in dl_mqtt:
    #print("ITEM NAME: "+ str(item.name))
    #print("ITEM VALUE: " + str(item.value[1]))
    #atr=getattr(dl_mqtt, item.name)
    #print(atr.value[1])
    #if 'getdata' in str(atr.value[1]):
        #print("GETDATA")
    #print(str(getattr(dl_mqtt, item.name).value[1]))

    if 'getdata' in str(getattr(dl_mqtt, item.name).value[1]):
        adr = getattr(dl_mqtt, item.name).value[0] + "/getdata"
        json = {'code': 'request', 'cid': 4711, 'adr': adr}
        resp = requests.post(url='http://192.168.5.131', json=json)
        try:
            print("\n", adr, "\n\t>>>\t", str(resp.json()['data']['value']))
        except KeyError:
            print("\n", adr, "\n\t>>>\t", resp.json())






dziedzina=np.linspace(0, 99, 100,dtype=int)
fy=[0]*(len(dziedzina))
fy2=[0]*(len(dziedzina))
fy3=[0]*(len(dziedzina))
#print("Dziedzina",len(dziedzina))
-----------------------------------------------------------------IF---------------------------------------------
if (x<30) and x> 20:
    print(x)
elif x>50:
    print("X >50)")
else:
    print("fałsz")

while x<30:
    x+=1
    print(x)
    if x >25:
        break

print("koniec")
---------------------------------------------------------------------LISTA----------------------------------------
listaX=[0]*10 # - twoprzenie listy z zadanym rozmiarem

los = randint(1,10)
odp =-1
i=0
lista = [1,2,3,4,1,"a","b","c","d",]
print(lista[2])
tekst="XYZXYXZ"
print(tekst[2])
print("Zagadnij liczbe z przedzialu 1-10")
print(lista + [8,8])
lista.append(7)
lista.append(["c","y","c"])
print("iloscelemntwo=",len(lista))
print(lista)
lista.insert(3,99)
print(lista[3])
print(lista)
print("Ilość",lista.count(1))
print("indeks:", lista.index("a"))
lista.remove("d")
print(lista)
lista2=[13,2,3,4,5,6,7,8,9]
print("Minimum z listy2 =", min(lista2))
lista2.sort()
print(lista2)
print("maksymalna wartosc z listy =", max(lista2))
lista2.clear()
print("Pusta lista", lista2)
i=0
-----------------------------------------------------------------WHILE i FOR----------------------------------------
while i<len(lista):
    print(lista[i])
    i+=1

for x in lista:
    print("Petla for dla listy",x)

for y in range (0,10,1) :
    print("Pętla FOR Y=",y)

while odp!=los and los==-100:
    i+=1
    odp = int(input("Podaj liczbę"))
    if odp>los:
        print("Liczba jest mniejsza od twojej")
    elif odp<los:
        print("Liczba jest wieksza od twoje")
    if "q"==input("Zakoncz gre nacisnij 'q' aby grac dalej nacisnij dowolny klawisz"):
        break;
print("brawo odgadles liczbe za" , i ,"razem")

-----------------------------------------------------------------FUNKCJE---------------------------------------
def funkcja(x,y=1):
    print(x+y)

funkcja(2,5)
funkcja(2)
def funkcja2(x,y=1):
    return x+y

print("Funkcja 2 =",funkcja2(44,49))

def funkcja3(f1,x,y):
    return f1(x,y)*x

print("FUnkcja z argumentem jako funkcja",funkcja3(funkcja2,pi,8))
xc=10
print("Pierwiastek z ",xc,"=",round(pierwiastek(xc),1))

x1=9
x2=1
lista4=[]
--------------------------------------------------------------------WYJATKI---------------------------------------
try:
    print(lista4[0])
    print(x1/x2)
except ZeroDivisionError:
    print("Niedziel przez zero")
except TypeError:
    print("Podano znak inny niz cyfra")
except IndexError:
    print("Indeks listy nie istnieje")

------------------------------------------------------------------------PLIKI---------------------------------
while True:
    plik = open("test.txt", "a")
    if plik.writable():
         plik.write(input("Wprowadz tekst:")+"\n")
    plik.close()
    plik=open("test.txt","r")
    listaTekst=plik.readlines()
    if plik.readable():
        tekst=plik.read()
        print(tekst)
        for l in listaTekst:
            print("Lista:",l)

-------------------------------------------------------------------WYKRESY-----------------------------------
for d in dziedzina:

    fy[d]=(d*d)
    fy2[d]=15*d
    fy3[d]=fy[d]+fy2[d]
    #print("FC1", fy[d])

plt.subplot(3,1,1)
plt.plot(dziedzina,fy3)
plt.title("Funkcja f(x)=X^2")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.tight_layout()


plt.subplot(3,1,2)
plt.plot(dziedzina,fy2)
plt.title("Funkcja f(x)=x*2")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.subplot(3,1,3)
plt.plot(dziedzina,fy3)
plt.title("Funkcja f(x)=fy+fy2")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

---------------------------------------------------------------SLOWNIKI --------------------------------------
slownik={1:"Poniedzialek", 2:"Wtorek", 7: "Niedziela"}
slownik[3]="sroda"
slownik[4]=False
slownik["a"]=1
print(slownik)
print(slownik.get(8,"Niema"))
print("\nPętla po kluczach:")
for s in slownik:
    print(s)
slownik.pop(3) # usuwa wartosc ze slownika po kluczu
print("\nPętla po wartosciach:")
for s in slownik.values():
    print(s)
-----------------------------------------------------------#KROTKA ---------------------------------------------
krotka=(2,4,8,16,32,64,128)# rozni sie od listy ze nie mozna modyfikowac jej elementow
print(krotka[0])
print(krotka[6])
print("Liczba elemntow: ",krotka.count(2))
print("Pozycja wartości 64: ",krotka.index(64)) # zwraca pozycje na ktorej znajduje sie wpisana wartosc
print(krotka[0:3]) #zwraca klilka indeksow

#--------------------------------------------------------Wyrazenia listowe-----------------------------------------

listaW=list(range(10))   # generator listy !!!!!!!!!
litaX=[0]*10 #- tworzenie listy o zadanym rozmiarze
listaY=[0]*len(listaX) - tworzenie listy o rozmiarze innej listy
print("\nWyrazenie listowe:",listaW)
nowa =[i*2 for i in listaW] # Tworzenie nowej listy z wartosciami obliczonymi na podstawie istniejacej listy
print("\n Lista nowa:",nowa)
nowa2=[i+2 for i in nowa if i%2==0]
print("Lista parzystych:",nowa2)
#Formatowanie string
arg=["Sebastian",24]
tekst="Czescmam na imie {0} i mam {1} lat.".format(arg[0],arg[1])
print(tekst)
print(" join ,".join(tekst))

------------------------------------------------------------------Generatory------------------------------------

def gen():
    i=0
    while i<5:
        yield i
        i+=1

for i in gen():

    print("Generator:",i)

print("Generator lista:",list(gen()))
def parzyste(x):
     i=0
     while i<=x:
         if  i % 2 == 0: # reszta z dzielenia rowna sie 0 ( sprawdzamy liczby parzyste)
             yield i
         i+=1

for i in parzyste(12):
    print("Funkcja parzyste:",i)

--------------------------------------------------------------WRAPPER - otoczka-------------------------------
def decorator(func):
    def wrapper():
        print("------")
        func()
        print("------")
    return wrapper

def hello():
    print("HELLO")

hello = decorator(hello)

hello()
-------------------------------------------------------------------KLASY-------------------------------------
class Czlowiek:     # ZACZYNAMY Z DUZEJ LITERY
    def __init__(self, imie, wiek):
        self.imie=imie
        self.wiek=wiek

    def przedstawSie(self,powitanie="Czesc"):

        return powitanie+" mam na imie "+self.imie + "i mam "+ str(self.wiek) +" lat"

obiekt =Czlowiek("Ola",33)
obiekt2=Czlowiek("Wiesiek",79)
print(obiekt.przedstawSie("Witaj"))
print(obiekt2.przedstawSie())

class Animal:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Dog(Animal):      # dziedziczenie z klasy animal
    def voice(self):
        print("WOF")
dog = Dog("Rex",32)
class Cat(Animal):
    def Getvoice(self):
        print("MIAU")

cat=Cat("Kira",5)
class Wolf(Dog):
    def getVoice(self):
        print("WOOOUU")
        super().voice()     # szuka w dziedziczeniu w klasach bazowych danej funkcji

print(dog.name)
print(dog.age)
dog.voice()
print(cat.name, "  ", cat.age)
cat.Getvoice()
wolf=Wolf("Wilkolak", 2134)
print(wolf.name,wolf.age)
wolf.getVoice()

class Punkt2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.odleglosc = math.sqrt(x**2 + y**2)
    def __add__(self, drugi):
        return Punkt2D(self.x + drugi.x, self.y + drugi.y)
    def __lt__(self, drugi):
        return self.odleglosc < drugi.odleglosc
    def __eq__(self, drugi):
        return self.x == drugi.x and self.y == drugi.y


p1=Punkt2D(2,5)
p2=Punkt2D(4,5)
p3 = p1 + p2
print(p1.odleglosc)
print(p2.odleglosc)

print(p3.x)
print(p3.y)
print(p1==p2)
print(p1<p2)

#KLASY

class Test:
    #def __new__(cls):
    def __del__(self):  # destruktor usuwa klase na samym koncu kodu !!!
        print("By by class")


-------------------------------------------------KLASY-destruktor------------------------------
obj= Test()
obj2 = obj # objekt jest kasowany gdy juz niema do niego zadnych referencji, lecz kiedy zostanie gdzies przypisany funkcja DEL go nie usunie
del obj
print("Destruktor wywolywany jest przed koncem progrmau")
class Test2:
    _lista=[]   # dodanie "_" powoduje zmiane zmiennej na prywatną!!
    def dodaj(self,arg):
        self._lista.append(arg)

    def zdejmij(self):
        if len(self._lista)>0:
            return self._lista.pop(len(self._lista)-1)
        else:
            return

obj3 = Test2()

obj3.dodaj("A")
obj3.dodaj("B")
obj3.dodaj("C")
obj3.dodaj("D")
#obj3._lista.append("X")
print(obj3.zdejmij())
print(obj3._lista)
print(obj3.zdejmij())
print(obj3._lista)

#------------------------------------------------KLASY- metody klas---------------------------------

class Czlowiek:
    def __init__(self, imie):
        self.imie=imie

    def przedstaw(self):
        print("Nazywam sie "+self.imie) # metody objektow

    @classmethod
    def nowy_czlwoiek(cls,imie): # metoda klasy
        return cls(imie)  # zwraca nowy obiekt klasy

    @staticmethod   # dziala podobnie jak metoda klasy ale przyjmuje tylko nasz argument
    def przywitaj(arg):
        print("Czesc "+arg)

cz1=Czlowiek.nowy_czlwoiek("wiesiek")   # metoda wywolywana z poziomu klasy bezposrednio
cz1.przedstaw()
cz2=cz1.nowy_czlwoiek("Adrian")
cz2.przedstaw()
Czlowiek.przywitaj("ziomek")
#------------------------------------------------KLASY- walasnosci-setter-getter------------------------
class KontoBankowe:
    __stan = 0
    @property   # wlasnosc - stan tylko do odczytu !!
    def stan_konta(self):
        return self.__stan
    @stan_konta.getter
    def stan_konta(self):
        return "Stan konta  "+ str(self.__stan)+"zl" # pobranie i odczytania wartosci

    @stan_konta.setter
    def stan_konta(self, value):
        self.__stan+=value

konto = KontoBankowe()
print(konto.stan_konta) # funkcje zmienia sie na wlasciowosc - bez nawaisow (), mozna tylko odczytac nie mozna zapisywac
#konto.stan_konta =3 - nie dziala nie mozna zapisac do tylko do odczytu GETTER
konto.stan_konta =30
print(konto.stan_konta)









"""
