from arabaprojesi import *

print("""--------------------------------
Araba İşleri PRogramına hoşgeldiniz....

İşlemler ;

1 - Arabaları Göster

2 - Arabaları Sorgula

3 - Araba Ekle

4 - Araba Sil

5 - Fiyat Yükselt

Çıkmak için 'q' ya basınız..... 

--------------------------------""")

arabaprojesi = Galeri()

while True:
    cevap = input("Yapmak istediğiniz işlemi giriniz: ")

    if (cevap=="q") :
        print("Programdan çıkılıyor....")
        print("Yine bekleriz.....")
        break

    elif (cevap == "1"):
        arabaprojesi.arabaları_göster()


    elif (cevap == "2"):
        plaque = input("İstediğiniz arabanın plakasını giriniz: ")
        print("Araba sorgulanıyor....")

        arabaprojesi.araba_sorgula(plaque)

    elif (cevap == "3"):
        plaka = input("Arabanın plakasını giriniz: ")
        marka = input("Arabanın markasını giriniz: ")
        renk  = input("Arabanın rengini giriniz: ")
        motor = float(input("Arabanın motorunu giriniz: "))
        fiyat = float(input("Arabanın fiyatınız giriniz: "))
        model = int(input("Arabanın modelini giriniz: "))

        car = Arabalar(plaka,marka,renk,motor,fiyat,model)

        print("Araba ekleniyor.....")
        time.sleep(2)

        arabaprojesi.araba_ekle(car)

        print("Araba eklendi....")

    elif (cevap == "4"):
        plaka = input("Silmek istediğiniz arabanın plakasını giriniz: ")

        istek = input("Emin misiniz, (E/H): ")
        if istek == "E":
            print("Araba siliniyor.....")
            time.sleep(2)

            arabaprojesi.araba_sil(plaka)
            print("Araba silindi....")

    elif (cevap == "5"):
        plaka = input("Fiyat yükseltmek istediğiniz arabanın plakasını giriniz: ")

        arabaprojesi.fiyat_yükselt(plaka)













