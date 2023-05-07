import json
def MainMenu():
    while True:
        try:
            print("\n----------Menü---------\n1....Yeni Kayıt Ekle\n2....Kayıt Ara\n3....Kayıt Listele\n4....Çıkış\n---------------------------\n")
            tercih=int(input("Lütfen tercihinizi giriniz : "))
            if tercih in [1,2,3,4]:return tercih
            else:print("Lütfen 1 ile 4 arasında bir tercihte bulununuz...")
        except ValueError:print("!!!Lütfen sadece sayı giriniz!!!")
        except:print("Hata oluştu. Lütfen başka bir tercihte bulununuz...")

def DosyaOku():
    with open(r"e:\veriler.json") as dosya:jsonDosya=json.load(dosya)
    return jsonDosya

def ListeleMenu():
    global veriler
    print("\n       ID       İsim Soyisim                 İş     ")
    print("------------------------------------------------------")
    for i in range(1,len(veriler)+1):print(f"        {i}       {veriler[str(i)]['isim']}       {veriler[str(i)]['is']}")
    print("\n")
    
def JsonKayit():
    global veriler
    with open(r"e:\veriler.json","w") as dosya:dosya.writelines(json.dumps(veriler))

def KayitMenu():
    global veriler
    isim=input("Lütfen isim giriniz : ")
    isler=input("Lütfen mesleği giriniz : ")
    egitim=input("Lütfen eğitim durmunuzu giriniz : ")
    maas=input("Lütfen maaşını giriniz : ")
    veriler[str(len(veriler)+1)]={"isim":isim,"is":isler,"egitim":egitim,"maas":maas}
    JsonKayit()
    
def KayitAra():
    ara=input("Lütfen aranan kaydın ID'sini giriniz : ")
    try:print(f"""\n{veriler[ara]["isim"]} {veriler[ara]["is"]} {veriler[ara]["egitim"]} {veriler[ara]["maas"]}""")
    except:print("\n!!!Böyle bir ID bulunmamaktadır!!!")

while True:
    secim=MainMenu()
    veriler=DosyaOku()
    if secim==4:
        print("Program sonlandırıldı...")
        break
    elif secim==3:ListeleMenu()
    elif secim==1:KayitMenu()
    elif secim==2:KayitAra()