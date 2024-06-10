import sqlite3
import sys

from PyQt5.QtWidgets import *

from ogrenci import *

    
class Ogrencikayit(QMainWindow):

    def __init__(self, db_adi):
        super().__init__()
       
        self.__TABLOADI = "tbl_Ogrencikayit"  
        self.__snfTablo = "tbl_sinifislemleri"
        self.__baglanti = sqlite3.connect(db_adi)
        self.__islem = self.__baglanti.cursor()
        self.__islem.execute(f"create table if not exists {self.__TABLOADI} (Ad text,Soyad text,Telefon text, Veli_Telefon text, Sinif text)")
        self.__baglanti.commit()

        
        self.__pencere = QMainWindow()
        self.__ui = Ui_OgrenciIslemleri()
        self.__ui.setupUi(self.__pencere)
        self.__pencere.show()
        
      
        self.Listele()

        self.Sinif_cmb()
        
        self.__ui.btn_ogrenciEkle.clicked.connect(self.ogrenciEkle)
        self.__ui.btn_ogrenciSil.clicked.connect(self.ogrenciSil)
        self.__ui.Widget_ogrenciIslem.clicked.connect(self.textleriGetir)  # tıklandığında satırdaki bilgileri textboxlara almak için
        self.__ui.btn_ogrenciGunc.clicked.connect(self.OgrenciGuncelle)
        self.__ui.btn_ogrenciAra.clicked.connect(self.OgrenciAra)
        
    
    


    def ogrenciui(self):
        return self.__ui
    
    def ogrpencere(self):
        return self.__pencere
    
    
    def ogrenciEkle(self):
        try:
            Ad = self.__ui.lne_ogrenciAd.text()
            Soyad = self.__ui.lne_ogrenciSoyad.text()
            Telefon = self.__ui.lne_ogrenciTel.text()
            Veli_Telefon = self.__ui.lne_veliTel.text()
            Sinif = self.__ui.comboBox_ogrenciSinif.currentText()

            if not self.kayitMevcutMu(Ad, Soyad, Telefon, Veli_Telefon, Sinif):
                sorgu = f"insert into {self.__TABLOADI}(Ad,Soyad,Telefon,Veli_Telefon,Sinif) values(?,?,?,?,?)"
                self.__islem.execute(sorgu, (Ad, Soyad,Telefon, Veli_Telefon, Sinif))
                self.__baglanti.commit()
                self.Listele()
                mesaj = QMessageBox.question(self.__pencere, "Eklendi", "bu kayıt Eklendi", QMessageBox.Ok)
                self.__ui.lne_ogrenciAd.clear()
                self.__ui.lne_ogrenciSoyad.clear()
                self.__ui.lne_ogrenciTel.clear()
                self.__ui.lne_veliTel.clear()
                
           
                
            else:
                mesaj = QMessageBox.question(self.__pencere, "Mevcut", "bu kayıt Zaten Mevcut", QMessageBox.Ok)
                

        except Exception as error:
            print("HATA! hata mesajı = " + str(error))
    


    def Listele(self):
        self.__ui.Widget_ogrenciIslem.clear()
        self.__ui.Widget_ogrenciIslem.setHorizontalHeaderLabels(
            ("Ad", "Soyad", "Telefon", "Veli_Telefon", "Sinif"))
        self.__ui.Widget_ogrenciIslem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sorgu = f"select * from {self.__TABLOADI}"
        self.__islem.execute(sorgu)

            # döngüler sorgudan dönen kayıtları gride yazdırmaya yarıyor
        for indexSatir, kayitNumarasi in enumerate(self.__islem):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.__ui.Widget_ogrenciIslem.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))




    def ogrenciSil(self):
        guncelleMesaj = QMessageBox.question(self.__pencere, "güncelleme onayı", "bu kaydı güncellemek istediğinizden emin misiniz?",
         QMessageBox.Yes | QMessageBox.No)
            
        if (guncelleMesaj == QMessageBox.Yes):
            selected_row = self.__ui.Widget_ogrenciIslem.currentRow()
            Ad = self.__ui.Widget_ogrenciIslem.item(selected_row, 0).text()
            Soyad = self.__ui.Widget_ogrenciIslem.item(selected_row, 1).text()
            Telefon = self.__ui.Widget_ogrenciIslem.item(selected_row, 2).text()
            Veli_Telefon = self.__ui.Widget_ogrenciIslem.item(selected_row, 3).text()
            Sinif = self.__ui.Widget_ogrenciIslem.item(selected_row, 4).text()
       
            sorgu = f"delete from {self.__TABLOADI} where Ad=? AND Soyad=? AND Telefon=? AND Veli_Telefon=? AND Sinif=?"
            self.__islem.execute(sorgu, (Ad,Soyad,Telefon,Veli_Telefon,Sinif))
            self.__baglanti.commit()
        # tablodan seçilen satırı kaldır
            self.__ui.Widget_ogrenciIslem.removeRow(selected_row)
            mesaj = QMessageBox.question(self.__pencere, "Sil", "Kayıt Silindi", QMessageBox.Ok)
            self.__ui.lne_ogrenciAd.clear()
            self.__ui.lne_ogrenciSoyad.clear()
            self.__ui.lne_ogrenciTel.clear()
            self.__ui.lne_veliTel.clear()
            
           
        else:
             mesaj = QMessageBox.question(self.__pencere, "İptal", "güncelleme iptal edildi", QMessageBox.Ok)
            


    def textleriGetir(self):
        try:
            selected_row = self.__ui.Widget_ogrenciIslem.currentRow()
            if selected_row >= 0:  # eğer bir satır seçildiyse
                self.__ui.lne_ogrenciAd.setText(self.__ui.Widget_ogrenciIslem.item(selected_row, 0).text())
                self.__ui.lne_ogrenciSoyad.setText(self.__ui.Widget_ogrenciIslem.item(selected_row, 1).text())
                self.__ui.lne_ogrenciTel.setText(self.__ui.Widget_ogrenciIslem.item(selected_row, 2).text())
                self.__ui.lne_veliTel.setText(self.__ui.Widget_ogrenciIslem.item(selected_row, 3).text())
                self.__ui.comboBox_ogrenciSinif.setCurrentText(self.__ui.Widget_ogrenciIslem.item(selected_row, 4).text())
        except:
            pass

    def OgrenciAra(self):
        try:
            self.__ui.Widget_ogrenciIslem.clear()
            self.__ui.Widget_ogrenciIslem.clear()
            self.__ui.Widget_ogrenciIslem.setHorizontalHeaderLabels(
                ("Ad", "Soyad", "Telefon", "Veli_Telefon", "Sinif"))
            self.__ui.Widget_ogrenciIslem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            tum_kayitlar = []
            arananKayit = str.lower(self.__ui.lne_ogrenciAra.text())
            sorgu = f"select * from {self.__TABLOADI} where Ad like '{arananKayit}%' "
            self.__islem.execute(sorgu)
            tum_kayitlar.extend(self.__islem.fetchall())
                # döngüler sorgudan dönen kayıtları gride yazdırmaya yarıyor
            for indexSatir, kayitNumarasi in enumerate(tum_kayitlar):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    self.__ui.Widget_ogrenciIslem.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))
        except Exception as ex:
            mesaj = QMessageBox.question(self.__pencere, "Hata","HATA! hata mesajı== ." + str(ex), QMessageBox.Ok)

    def OgrenciGuncelle(self):
        try:
            guncelleMesaj = QMessageBox.question(self.__pencere, "güncelleme onayı","bu kaydı güncellemek istediğinizden emin misiniz?",
            QMessageBox.Yes | QMessageBox.No)
            selected_row = self.__ui.Widget_ogrenciIslem.currentRow()
            if (guncelleMesaj == QMessageBox.Yes):
                Ad= self.__ui.lne_ogrenciAd.text()
                Soyad = self.__ui.lne_ogrenciSoyad.text()
                Telefon = self.__ui.lne_ogrenciTel.text()
                Veli_Telefon = self.__ui.lne_veliTel.text()
                Sinif = self.__ui.comboBox_ogrenciSinif.currentText()
                print(f"{Ad},{Soyad},{Telefon},{Veli_Telefon},{Sinif}")
                

                sorgu = f"update {self.__TABLOADI} set Ad = ?, Soyad = ?,Telefon = ?, Veli_Telefon = ?, Sinif = ? WHERE Ad=? AND Soyad=? AND Telefon=? AND Veli_Telefon=? AND Sinif=?"
                self.__islem.execute(sorgu, (
                    Ad, Soyad, Telefon, Veli_Telefon, Sinif,
                    self.__ui.Widget_ogrenciIslem.item(selected_row, 0).text(),
                    self.__ui.Widget_ogrenciIslem.item(selected_row, 1).text(),
                    self.__ui.Widget_ogrenciIslem.item(selected_row, 2).text(),
                    self.__ui.Widget_ogrenciIslem.item(selected_row, 3).text(),
                    self.__ui.Widget_ogrenciIslem.item(selected_row, 4).text()))
                self.__baglanti.commit()
                self.Listele()
                mesaj = QMessageBox.question(self.__pencere, "Güncellendi", "bu kayıt güncellendi", QMessageBox.Ok)
                self.__ui.lne_ogrenciAd.clear()
                self.__ui.lne_ogrenciSoyad.clear()
                self.__ui.lne_ogrenciTel.clear()
                self.__ui.lne_veliTel.clear()
               
           
                
           
            else:
                mesaj = QMessageBox.question(self.__pencere, "İptal", "güncelleme iptal edildi", QMessageBox.Ok)
        except Exception as ex:
            mesaj = QMessageBox.question(self.__pencere, "Hata","Lütfen Doğru Seçimi Yaptığınızdan Emin Olup Tekrar Deneyin" , QMessageBox.Ok)

    def kayitMevcutMu(self, Ad, Soyad, Telefon, Veli_Telefon, Sinif):
        try:
            tum_kayitlar = []

            sorgu = f"select * from {self.__TABLOADI} where Ad='{Ad}' and Soyad = '{Soyad}' and Telefon='{Telefon}' and Veli_Telefon='{Veli_Telefon}' and Sinif = '{Sinif}'"
            self.__islem.execute(sorgu)
            tum_kayitlar.extend(self.__islem.fetchall())

            if len(tum_kayitlar) != 0:
                return True
            else:
                return False
        except Exception as ex:
            mesaj = QMessageBox.question(self.__pencere, "Hata","HATA! hata mesajı== ." + str(ex), QMessageBox.Ok)



    def Sinif_cmb(self):
        try:
            self.__islem = self.__baglanti.cursor()
            self.__islem.execute(f"SELECT sinif FROM {self.__snfTablo}")
            siniflar = self.__islem.fetchall()
            for satir in siniflar:
                self.__ui.comboBox_ogrenciSinif.addItems(satir)

        except Exception as ex:
            mesaj = QMessageBox.question(self.__pencere, "Hata","HATA! hata mesajı== ." + str(ex), QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ders_penceresi = Ogrencikayit("db.db")
    ders_penceresi.show()
    sys.exit(app.exec_())
