import sqlite3

import time


class Arabalar():
    def __init__(self,plaka,marka,renk,motor,fiyat,model):
        self.plaka = plaka
        self.marka = marka
        self.renk = renk
        self.motor = motor
        self.fiyat = fiyat
        self.model = model

    def __str__(self):
        return "Plaka : {}\nMarka : {}\nRenk : {}\nMotor : {}\nFiyat : {}\nModel : {}".format(self.plaka,self.marka,self.renk,self.motor,self.fiyat,self.model)


class Galeri():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.bağlantı = sqlite3.connect("Araba Verileri.db")

        self.cursor = self.bağlantı.cursor()

        sorgu = "Create Table if not exists Arabalar(plaka TEXT,marka TEXT,renk TEXT,motor INT,fiyat INT,model INT)"

        self.cursor.execute(sorgu)

        self.bağlantı.commit()

    def bağlantı_kes(self):

        self.bağlantı.close()

    def arabaları_göster(self):
        sorgu = "Select * From Arabalar"

        self.cursor.execute(sorgu)

        data = self.cursor.fetchall()

        if (len(data) == 0 ):
            print("Galeride araba bulunmamaktadır...")
        else:
            for i in data:
                araba = Arabalar(i[0],i[1],i[2],i[3],i[4],i[5])
                print("-------------------------------")
                print(araba)

    def araba_sorgula(self,plaka):
        sorgu = "Select * From Arabalar where plaka=?"

        self.cursor.execute(sorgu,(plaka,))

        data = self.cursor.fetchall()

        for i in data:
            araba = Arabalar(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5])
            print(araba)


    def araba_ekle(self,araba):

        sorgu = "Insert Into Arabalar Values(?,?,?,?,?,?)"

        self.cursor.execute(sorgu,(araba.plaka,araba.marka,araba.renk,araba.motor,araba.fiyat,araba.model))

        self.bağlantı.commit()

    def araba_sil(self,plaka):

        sorgu = "Delete From Arabalar where plaka =?"

        self.cursor.execute(sorgu,(plaka,))

        self.bağlantı.commit()

    def fiyat_yükselt(self,plaka):
        sorgu = "Select * From Arabalar where plaka = ?"

        self.cursor.execute(sorgu, (plaka,))

        data = self.cursor.fetchall()

        if (len(data) == 0) :
            print("Böyle bir araba bulunmamaktadır....")
        else:
            fiyat = data[0][4]

            eklenecek_fiyat = int(input("Kaç lira eklersiniz: "))

            fiyat += eklenecek_fiyat

            sorgu2 = "Update Arabalar set fiyat=? where plaka = ? "

            self.cursor.execute(sorgu2,(fiyat,plaka,))

            self.bağlantı.commit()
        print("Fiyat yükseltildi.....")































