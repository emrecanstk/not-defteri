with open("notlar.txt","a",encoding="utf-8") as notlar:
    pass

basliklar,aciklamalar,x = [],[],1

def Secim():
    global basliklar,aciklamalar,x
    with open("notlar.txt","r",encoding="utf-8") as notlar:
        bloklar = notlar.read().split("\n\n")
        for i in bloklar:
            if "►" in i:
                ayriklar = i.split("►")
                basliklar.append(ayriklar[0])
                aciklamalar.append(ayriklar[1])
    for i in basliklar:
        print(f"{x}. {i}",end="")
        x+=1
    secim = int(input("\nSeçim: "))
    return secim

def NotGoruntule():
    secim = Secim()
    if secim not in range(1,len(basliklar)+1):
        print("geçersiz seçim\n\n")
    else:
        print("\n\n" + basliklar[secim-1],aciklamalar[secim-1] + "\n\n")

def NotOlustur():
    baslik = input("Başlık: ")
    aciklama = input("Not: ")
    with open(f"notlar.txt","a",encoding="utf-8") as notlar:
        notlar.write(f"{baslik}")
    with open(f"notlar.txt","a",encoding="utf-8") as notlar:
        notlar.write(f"\n►{aciklama}\n\n")
    print("\n")
              
def NotSil():
    secim = Secim()
    if secim not in range(0,len(basliklar)+1):
        print("geçersiz seçim")
    else:
        with open("notlar.txt","w",encoding="utf-8") as notlar:
            basliklar.remove(basliklar[secim-1])
            aciklamalar.remove(aciklamalar[secim-1])  
            if len(basliklar)>0:
                a=0
                while a<len(basliklar):
                    notlar.write(f"{basliklar[a]}")
                    notlar.write(f"►{aciklamalar[a]}\n\n")
                    a+=1
            else:
                pass

def NotDuzenle():
    secim = Secim()
    if secim not in range(0,len(basliklar)+1):
        print("geçersiz seçim")
    else:
        print("INAKTIF")

print("--------------- Not Defteri ---------------")
islem=0
while islem!=5:
    islem = int(input("1. Not Görüntüle\n2. Not Oluştur\n3. Not Sil\n4. ÇIKIŞ\n\nİşlem: "))
    print("\n")
    if islem == 1:
        NotGoruntule()
    elif islem == 2:
        NotOlustur()
    elif islem == 3:
        NotSil()
    elif islem == 4:
        print("Çıkış Yapıldı.")
    else:
        print("geçersiz işlem")