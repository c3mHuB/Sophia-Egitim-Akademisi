import sqlite3
import sys

from PyQt5.QtWidgets import *

from sinif import *


class sinif_islemleri:

    def __init__(self, db_adi):

        # gerekli sabitler
        self.__TABLOADI = "tbl_sinifislemleri"  # veritabanında oluşturlacak tablonun adı
        self.__baglanti = sqlite3.connect(db_adi)

        # veritabanında tablo oluştur , self.__TABLOADI oluşturlacak tablonun adı
        self.__islem = self.__baglanti.cursor()
        self.__islem.execute(
            f"create table if not exists {self.__TABLOADI} (sinif text)")
        self.__baglanti.commit()

        # arayüzü göster
        self.uygulama = QApplication(sys.argv)
        self.__pencere = QMainWindow()
        self.__ui = Ui_SinifIslemleri()
        self.__ui.setupUi(self.__pencere)
        self.__pencere.show()

        # program açıldığında tabloda mevcut kayıtları görüntüle
        self.SiniflariGoster()

        self.Sinif_cmb()

        # button tıkladığında olayları
        self.__ui.btn_snfEkle.clicked.connect(self.SinifEkle)
        self.__ui.btn_snfSil.clicked.connect(self.sinifSil)
        self.__ui.btn_ogrenciAra.clicked.connect(self.sinifAra)
        self.__ui.Widget_snf.clicked.connect(self.kayitGetir)
        self.__ui.btn_snfgunc.clicked.connect(self.SinifGuncelle)


    def sınıfui(self):
        return self.__ui

    def snfpencere(self):
        return self.__pencere

    def SinifEkle(self):
        try:
            sinif_adi = self.__ui.lne_snfAd.text().lower()

            if not self.kayitMevcutMu(sinif_adi):
                sorgu = f"insert into {self.__TABLOADI}(sinif) values(?)"
                self.__islem.execute(sorgu, (sinif_adi,))
                self.__baglanti.commit()
                self.SiniflariGoster()
                print("program eklendi")
                QMessageBox.information(self.__pencere, "Bilgi", "başarılı", QMessageBox.Ok)
            else:
                QMessageBox.information(self.__pencere, "Bilgi", "kayıt mevcut işlem iptal edildi", QMessageBox.Ok)

        except Exception as error:
            print("HATA! hata mesajı = " + str(error))
            QMessageBox.information(self.__pencere, "HATA", "HATA", QMessageBox.Ok)

    def kayitMevcutMu(self, sinif):
        try:
            tum_kayitlar = []

            sorgu = f"select * from {self.__TABLOADI} where sinif='{sinif}'"
            self.__islem.execute(sorgu)
            tum_kayitlar.extend(self.__islem.fetchall())

            if len(tum_kayitlar) != 0:
                return True
            else:
                return False
        except Exception as ex:
            QMessageBox.information(self.__pencere, "HATA", "HATA", QMessageBox.Ok)

    def SiniflariGoster(self):

        self.__ui.Widget_snf.clear()
        self.__ui.Widget_snf.setHorizontalHeaderLabels(
            ("Sınıf",))
        self.__ui.Widget_snf.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tum_kayitlar = []

        sorgu = f"select * from {self.__TABLOADI} order by sinif asc"
        self.__islem.execute(sorgu)
        tum_kayitlar.extend(self.__islem.fetchall())

        # döngüler sorgudan dönen kayıtları gride yazdırmaya yarıyor
        for indexSatir, kayitNumarasi in enumerate(tum_kayitlar):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.__ui.Widget_snf.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def Sinif_cmb(self):
        try:
            self.__islem = self.__baglanti.cursor()
            self.__islem.execute(f"SELECT sinif FROM {self.__TABLOADI}")
            siniflar = self.__islem.fetchall()
            for satir in siniflar:
                self.__ui.cmb_snfara.addItems(satir)

        except Exception as ex:
            QMessageBox.information(self.__pencere, "HATA", "HATA", QMessageBox.Ok)

    def sinifAra(self):

        self.__ui.Widget_snf.clear()
        self.__ui.Widget_snf.setHorizontalHeaderLabels(
            ("Sınıf",))
        self.__ui.Widget_snf.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tum_kayitlar = []
        aranan = self.__ui.cmb_snfara.currentText()
        sorgu = f"select * from {self.__TABLOADI} WHERE sinif='{aranan}' order by sinif asc"
        self.__islem.execute(sorgu)
        tum_kayitlar.extend(self.__islem.fetchall())
        arananSinif = str.lower(self.__ui.cmb_snfara.currentText())

        if arananSinif!="tümü":
                
                sorgu = f"SELECT * FROM {self.__TABLOADI} WHERE sinif = '{arananSinif}' ORDER BY sinif ASC"
                self.__islem.execute(sorgu)
                tum_kayitlar.extend(self.__islem.fetchall())
        else:
            
            sorgu = f"SELECT * FROM {self.__TABLOADI} ORDER BY sinif ASC"
            self.__islem.execute(sorgu)
            tum_kayitlar.extend(self.__islem.fetchall())

        # döngüler sorgudan dönen kayıtları gride yazdırmaya yarıyor
        for indexSatir, kayitNumarasi in enumerate(tum_kayitlar):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.__ui.Widget_snf.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def sinifSil(self):
        try:
            selected_row = self.__ui.Widget_snf.currentRow()
            mesaj = QMessageBox.question(self.__pencere, "Silme onayı", "bu kaydı silmek istediğinizden emin misiniz?", QMessageBox.Yes | QMessageBox.No)
            if (mesaj == QMessageBox.Yes):
                sinif = self.__ui.Widget_snf.item(selected_row, 0).text()
            # veritabanından seçilen satırı sil
            sorgu = f"delete from {self.__TABLOADI} where sinif=?"
            self.__islem.execute(sorgu, (sinif,))
            self.__baglanti.commit()
            # tablodan seçilen satırı kaldır
            self.__ui.Widget_snf.removeRow(selected_row)
            self.Sinif_cmb()
        except Exception as ex:
            pass





        

    def kayitGetir(self):
        selected_row = self.__ui.Widget_snf.currentRow()
        if selected_row >= 0 and selected_row is not None:
            self.__ui.lne_snfAd.setText(self.__ui.Widget_snf.item(selected_row, 0).text())

    def SinifGuncelle(self):
            selected_row = self.__ui.Widget_snf.currentRow()
            if selected_row >= 0:  
                mevcut_sinif = self.__ui.Widget_snf.item(selected_row, 0).text()
                yeni_sinif, ok = QtWidgets.QInputDialog.getText(self.__pencere,"Sınıf Güncelle","Yeni sınıf adını girin:",QtWidgets.QLineEdit.Normal,mevcut_sinif)
                if ok and yeni_sinif.strip():
                    if not self.kayitMevcutMu(yeni_sinif):
                        sorgu = f"UPDATE {self.__TABLOADI} SET sinif=? WHERE sinif=?"
                        self.__islem.execute(sorgu, (yeni_sinif, mevcut_sinif))
                        self.__baglanti.commit()
                        self.__ui.Widget_snf.setItem(selected_row, 0, QTableWidgetItem(yeni_sinif))
                        self.Sinif_cmb()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    sinif_penceresi = sinif_islemleri("db.db")
    sinif_penceresi.show()
    sys.exit(app.exec_())
