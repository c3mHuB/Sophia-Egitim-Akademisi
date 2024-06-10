import sqlite3
import sys
from PyQt5.QtWidgets import *
from ders import Ui_DersIslemleri


class DersProgramlari(QMainWindow):
    gunler = ["pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"]

    # constructor
    def __init__(self, db_adi):
        super().__init__()  # QMainWindow'ın __init__() metodunu çağırın
        # gerekli sabitler
        self.__TABLOADI = "tbl_dersprogramlari"  # veritabanında oluşturlacak tablonun adı
        self.__snftablosu = "tbl_sinifislemleri"
        self.__baglanti = sqlite3.connect(db_adi)

        # veritabanında tablo oluştur , self.__TABLOADI oluşturlacak tablonun adı
        self.__islem = self.__baglanti.cursor()
        self.__islem.execute(
            f"create table if not exists {self.__TABLOADI} (sinif text,ogretmen_adi text,ders_adi text, ders_gunu text, ders_saati text)")
        self.__baglanti.commit()

        # arayüzü göster
        self.__pencere = QMainWindow() 
        self.__ui = Ui_DersIslemleri()
        self.__ui.setupUi(self.__pencere)
        self.__pencere.show()
        #sınıf combo
        self.Sinif_cmb()
         

        #filtre combobox
        self.filtre_sinif_cmb()
        # program açıldığında tabloda mevcut kayıtları görüntüle

        self.kayitYenile()

        # button tıkladığında olayları..
        self.__ui.btn_Ekle.clicked.connect(self.kayitEkle)
        self.__ui.btn_Ara.clicked.connect(self.sinifagore_filtrele)
        self.__ui.bnt_Sil.clicked.connect(self.kayitSil)
        self.__ui.Widget_dersislem.clicked.connect(
            self.textleriGetir)  # tıklandığında satırdaki bilgileri textboxlara almak için
        self.__ui.btn_gunc.clicked.connect(self.programGuncelle)

        
       
        #Bağlantı
     # Arayüzü ayarla

    def dersui(self):
        return self.__ui
    
    def derspencere(self):
        return self.__pencere


    def kayitEkle(self):
        try:
            sinif = self.__ui.comboBox.currentText()
            ogretmen_adi = str.lower(self.__ui.lne_ogrtmen.text())
            ders_adi = self.__ui.lne_dersAdi.text()
            ders_gunu = self.__ui.lne_dersGunu.text()
            ders_saati = self.__ui.lne_dersSaati.text()
            sorgu = f"insert into {self.__TABLOADI}(sinif,ogretmen_adi,ders_adi,ders_gunu,ders_saati) values(?,?,?,?,?)"
            self.__islem.execute(sorgu, (sinif, ogretmen_adi, ders_adi, ders_gunu, ders_saati))
            self.__baglanti.commit()
            print("program eklendi")
            self.kayitYenile()
            mesaj = QMessageBox.question(self.__pencere, "Eklendi", "Ders programa eklendi", QMessageBox.Ok)

            self.__ui.lne_ogrtmen.clear()
            self.__ui.lne_dersAdi.clear()
            self.__ui.lne_dersGunu.clear()
            self.__ui.lne_dersSaati.clear()

        except Exception as error:
            print("HATA! hata mesajı = " + str(error))

    def sinifagore_filtrele(self):
        try:
            self.__ui.Widget_dersislem.clear()
            self.__ui.Widget_dersislem.setHorizontalHeaderLabels(("Sınıf", "Öğretmen Adı", "Ders Adı", "Ders Günü", "Ders Saati"))
            self.__ui.Widget_dersislem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            tum_kayitlar = []
            arananSinif = str.lower(self.__ui.comboBox_Ara.currentText())
            if arananSinif!="tümü":
                for gun in self.gunler:
                    sorgu = f"SELECT * FROM {self.__TABLOADI} WHERE ders_gunu = '{gun}' AND sinif='{arananSinif}' ORDER BY ders_saati ASC"
                    self.__islem.execute(sorgu)
                    tum_kayitlar.extend(self.__islem.fetchall())
            else:
                for gun in self.gunler:
                    sorgu = f"SELECT * FROM {self.__TABLOADI} WHERE ders_gunu = '{gun}'ORDER BY ders_saati ASC"
                    self.__islem.execute(sorgu)
                    tum_kayitlar.extend(self.__islem.fetchall())
            
            for indexSatir, kayitNumarasi in enumerate(tum_kayitlar):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    self.__ui.Widget_dersislem.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))
        except Exception as ex:
            mesaj = QMessageBox.question(self.__pencere, "Hata!", "HATA! hata mesajı== ." + str(ex), QMessageBox.Ok)
            
        
        

    def kayitYenile(self):
        self.__ui.Widget_dersislem.clear()
        self.__ui.Widget_dersislem.setHorizontalHeaderLabels(
            ("Sınıf", "Öğretmen Adı", "Ders Adı", "Ders Günü", "Ders Saati"))
        self.__ui.Widget_dersislem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tum_kayitlar = []
        for gun in self.gunler:
            sorgu = f"select * from {self.__TABLOADI} where ders_gunu = '{gun}' order by ders_saati asc"
            self.__islem.execute(sorgu)
            tum_kayitlar.extend(self.__islem.fetchall())

            # döngüler sorgudan dönen kayıtları gride yazdırmaya yarıyor
            for indexSatir, kayitNumarasi in enumerate(tum_kayitlar):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    self.__ui.Widget_dersislem.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))
            
    def kayitSil(self):
        selected_row = self.__ui.Widget_dersislem.currentRow()
        guncelleMesaj = QMessageBox.question(self.__pencere, "güncelleme onayı", "bu kaydı güncellemek istediğinizden emin misiniz?",
         QMessageBox.Yes | QMessageBox.No)
        if (guncelleMesaj == QMessageBox.Yes):
            sinif = self.__ui.Widget_dersislem.item(selected_row, 0).text()
            ogretmen_adi = self.__ui.Widget_dersislem.item(selected_row, 1).text()
            ders_adi = self.__ui.Widget_dersislem.item(selected_row, 2).text()
            ders_gunu = self.__ui.Widget_dersislem.item(selected_row, 3).text()
            ders_saati = self.__ui.Widget_dersislem.item(selected_row, 4).text()
            # veritabanından seçilen satırı sil
            sorgu = f"delete from {self.__TABLOADI} where sinif=? AND ogretmen_adi=? AND ders_adi=? AND ders_gunu=? AND ders_saati=?"
            self.__islem.execute(sorgu, (sinif, ogretmen_adi, ders_adi, ders_gunu, ders_saati))
            self.__baglanti.commit()
        
            # tablodan seçilen satırı kaldır
            self.__ui.Widget_dersislem.removeRow(selected_row)
            mesaj = QMessageBox.question(self.__pencere, "Sil", "Kayıt Silindi", QMessageBox.Ok)
            self.__ui.lne_ogrtmen.clear()
            self.__ui.lne_dersAdi.clear()
            self.__ui.lne_dersGunu.clear()
            self.__ui.lne_dersSaati.clear()
        
           

    def textleriGetir(self):
        try:
            selected_row = self.__ui.Widget_dersislem.currentRow()
            if selected_row >= 0:  # eğer bir satır seçildiyse
                self.__ui.comboBox.setCurrentText(self.__ui.Widget_dersislem.item(selected_row, 0).text())
                self.__ui.lne_ogrtmen.setText(self.__ui.Widget_dersislem.item(selected_row, 1).text())
                self.__ui.lne_dersAdi.setText(self.__ui.Widget_dersislem.item(selected_row, 2).text())
                self.__ui.lne_dersGunu.setText(self.__ui.Widget_dersislem.item(selected_row, 3).text())
                self.__ui.lne_dersSaati.setText(self.__ui.Widget_dersislem.item(selected_row, 4).text())
                
        except:
            pass

    def programGuncelle(self):
        try:
            guncelleMesaj = QMessageBox.question(self.__pencere, "güncelleme onayı",
                                                 "bu kaydı güncellemek istediğinizden emin misiniz?",
                                                 QMessageBox.Yes | QMessageBox.No)
            selected_row = self.__ui.Widget_dersislem.currentRow()
            if (guncelleMesaj == QMessageBox.Yes):
                sinif = self.__ui.comboBox.currentText()
                ogretmen_adi = self.__ui.lne_ogrtmen.text()
                ders_adi = self.__ui.lne_dersAdi.text()
                ders_gunu = self.__ui.lne_dersGunu.text()
                ders_saati = self.__ui.lne_dersSaati.text()

                sorgu = f"update {self.__TABLOADI} set sinif = ?, ogretmen_adi = ?,ders_adi = ?, ders_gunu = ?, ders_saati = ? WHERE sinif=? AND ogretmen_adi=? AND ders_adi=? AND ders_gunu=? AND ders_saati=?"
                self.__islem.execute(sorgu, (
                    sinif, ogretmen_adi, ders_adi, ders_gunu, ders_saati,
                    self.__ui.Widget_dersislem.item(selected_row, 0).text(),
                    self.__ui.Widget_dersislem.item(selected_row, 1).text(),
                    self.__ui.Widget_dersislem.item(selected_row, 2).text(),
                    self.__ui.Widget_dersislem.item(selected_row, 3).text(),
                    self.__ui.Widget_dersislem.item(selected_row, 4).text()))
                self.__baglanti.commit()
                self.kayitYenile()
                mesaj = QMessageBox.question(self.__pencere, "Günceleme", "güncelleme başarılı", QMessageBox.Ok)
                self.__ui.lne_ogrtmen.clear()
                self.__ui.lne_dersAdi.clear()
                self.__ui.lne_dersGunu.clear()
                self.__ui.lne_dersSaati.clear()
            else:
                mesaj = QMessageBox.question(self.__pencere, "İptal", "güncelleme iptal edildi", QMessageBox.Ok)
        except Exception as ex:
            mesaj = QMessageBox.question(self.__pencere, "Hata","lütfen doğru seçim yaptığınızdan emin olup tekrar deneyin", QMessageBox.Ok)
            


    def Sinif_cmb(self):
        try:
            self.__islem = self.__baglanti.cursor()
            self.__islem.execute(f"SELECT sinif FROM {self.__snftablosu}")
            siniflar = self.__islem.fetchall()
            for satir in siniflar:
                self.__ui.comboBox.addItems(satir)

        except Exception as ex:
            mesaj = QMessageBox.question(self.__pencere, "Hata","HATA! hata mesajı== ." + str(ex), QMessageBox.Ok)

    def filtre_sinif_cmb(self):
        try:
            self.__islem = self.__baglanti.cursor()
            self.__islem.execute(f"SELECT sinif FROM {self.__snftablosu} ORDER BY sinif ASC")
            siniflar = self.__islem.fetchall()
            for satir in siniflar:
                self.__ui.comboBox_Ara.addItems(satir)

        except Exception as ex:
            mesaj = QMessageBox.question(self.__pencere, "Hata","HATA! hata mesajı== ." + str(ex), QMessageBox.Ok)
          

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ders_penceresi = DersProgramlari("db.db")
    ders_penceresi.show()
    sys.exit(app.exec_())
