import sqlite3
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from net import Ui_NetHesaplatma




class Nethesapla(QMainWindow):

    def __init__(self):
        super().__init__()

        self.__pencere = QMainWindow()
        self.__ui = Ui_NetHesaplatma()
        self.__ui.setupUi(self.__pencere)
        self.__pencere.show()

        
        self.__ui.btn_hesapla.clicked.connect(self.sonuc)


    def netpencere(self):
        return self.__pencere
    
    def netui(self):
        return self.__ui




    def hesapla(self,dogru,yanlis):

        fazlayanlis=yanlis%3
        net=dogru-(yanlis+fazlayanlis)

        return net
    
    def sonuc(self):
        try:
            biod=int(self.__ui.lne_bio_d.text())
            bioy=int(self.__ui.lne_bio_y.text())
            bionet=self.hesapla(biod,bioy)
            self.__ui.lbl_bio.setText(str(bionet))

            edbd=int(self.__ui.lne_edb_d.text())
            edby=int(self.__ui.lne_edb_y.text())
            edbnet=self.hesapla(edbd,edby)
            self.__ui.lbl_edb.setText(str(edbnet))

            matd=int(self.__ui.lne_mat_d.text())
            maty=int(self.__ui.lne_mat_y.text())
            matnet=self.hesapla(matd,maty)
            self.__ui.lbl_mat.setText(str(matnet))

            fizd=int(self.__ui.lne_fiz_d.text())
            fizy=int(self.__ui.lne_fiz_y.text())
            fiznet=self.hesapla(fizd,fizy)
            self.__ui.lbl_fiz.setText(str(fiznet))

            kimd=int(self.__ui.lne_kim_d.text())
            kimy=int(self.__ui.lne_kim_y.text())
            kimnet=self.hesapla(kimd,kimy)
            self.__ui.lbl_kim.setText(str(kimnet))

            trhd=int(self.__ui.lne_trh_d.text())
            trhy=int(self.__ui.lne_trh_y.text())
            trhnet=self.hesapla(trhd,trhy)
            self.__ui.lbl_trh.setText(str(trhnet))

            cogd=int(self.__ui.lne_cog_d.text())
            cogy=int(self.__ui.lne_cog_y.text())
            cognet=self.hesapla(cogd,cogy)
            self.__ui.lbl_cog.setText(str(cognet))

            dind=int(self.__ui.lne_din_d.text())
            diny=int(self.__ui.lne_din_y.text())
            dinnet=self.hesapla(dind,diny)
            self.__ui.lbl_din.setText(str(dinnet))

            feld=int(self.__ui.lne_fel_d.text())
            fely=int(self.__ui.lne_fel_y.text())
            felnet=self.hesapla(feld,fely)
            self.__ui.lbl_fel.setText(str(felnet))

            top=bionet+edbnet+matnet+fiznet+kimnet+trhnet+cognet+dinnet+felnet
            self.__ui.lbl_top.setText(str(top))

        except:
            QMessageBox.information(self, "!!!HATA!!!", "Hatalı Giriş", QMessageBox.Ok)
