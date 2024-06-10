import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_Anasayfa
from ogrenci import Ui_OgrenciIslemleri
from sinif import Ui_SinifIslemleri
from PyQt5.QtWidgets import QDialog
import ders_islemleri
from ogrenciislemlerikod import Ogrencikayit
from Sınıfislemleri import sinif_islemleri
from ders_islemleri import DersProgramlari
from nethesapla import Nethesapla


class Anasayfa(QMainWindow, Ui_Anasayfa):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_ders.clicked.connect(self.show_ders)
        self.btn_snf.clicked.connect(self.show_sinif)
        self.btn_ogr.clicked.connect(self.show_ogrenci)
        self.btn_mhsb.clicked.connect(self.show_net)
       
        self.sinif_window = sinif_islemleri("db.db")
        self.ogrenci_window = Ogrencikayit("db.db")
        self.ders_window = DersProgramlari("db.db")
        self.net_window = Nethesapla()
        self.derspc = self.ders_window.derspencere()
        self.ogrpencere = self.ogrenci_window.ogrpencere()
        self.sinifpc = self.sinif_window.snfpencere()
        self.netpencere = self.net_window.netpencere()
        
        
        self.show_anasayfa()
        

    def show_sinif(self):
        self.close()
        self.derspc.close()
        self.ogrpencere.close()
        self.netpencere.close()
        self.sinifpc.show()
        self.snf = self.sinif_window.sınıfui()
        self.snf.btn_ders.clicked.connect(self.show_ders)
        self.snf.btn_ogr.clicked.connect(self.show_ogrenci)
        self.snf.btn_home.clicked.connect(self.show_anasayfa)
        self.snf.btn_net.clicked.connect(self.show_net)
        
        
    def show_anasayfa(self):
        self.close()
        self.derspc.close()
        self.ogrpencere.close()
        self.sinifpc.close()
        self.netpencere.close()
        self.show()

    def show_ogrenci(self):
        self.close()
        self.derspc.close()
        self.sinifpc.close()
        self.netpencere.close()
        self.ogrpencere.show()
        self.ogrenci = self.ogrenci_window.ogrenciui()
        self.ogrenci.btn_ders.clicked.connect(self.show_ders) 
        self.ogrenci.btn_snf.clicked.connect(self.show_sinif)
        self.ogrenci.btn_home.clicked.connect(self.show_anasayfa)
        self.ogrenci.btn_net.clicked.connect(self.show_net)
    
    def show_ders(self):
        self.close()
        self.ogrpencere.close()
        self.sinifpc.close()
        self.netpencere.close()
        self.derspc.show()
        self.ders_window.dersui().btn_home_ders.clicked.connect(self.show_anasayfa)
        self.ders_window.dersui().btn_ogr_ders.clicked.connect(self.show_ogrenci)
        self.ders_window.dersui().btn_snf_ders.clicked.connect(self.show_sinif)
        self.ders_window.dersui().btn_net_ders.clicked.connect(self.show_net)

    def show_net(self):
        self.close()
        self.derspc.close()
        self.ogrpencere.close()
        self.sinifpc.close()
        self.netpencere.show()
        self.net_window.netui().btn_ders_ders.clicked.connect(self.show_ders)
        self.net_window.netui().btn_home_ders.clicked.connect(self.show_anasayfa)
        self.net_window.netui().btn_ogr_ders.clicked.connect(self.show_ogrenci)
        self.net_window.netui().btn_snf_ders.clicked.connect(self.show_sinif)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Anasayfa()
    window.show()
    sys.exit(app.exec_())
