# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sertan\Desktop\sss\birleştirme\DersIslem.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DersIslemleri(object):
    def setupUi(self, DersIslemleri):
        DersIslemleri.setObjectName("DersIslemleri")
        DersIslemleri.resize(1211, 731)
        DersIslemleri.setMinimumSize(QtCore.QSize(1211, 731))
        DersIslemleri.setMaximumSize(QtCore.QSize(1211, 731))
        self.widget_4 = QtWidgets.QWidget(DersIslemleri)
        self.widget_4.setGeometry(QtCore.QRect(170, 140, 311, 571))
        self.widget_4.setAutoFillBackground(False)
        self.widget_4.setStyleSheet("border-radius: 15px;\n"
"border: 3px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_4.setObjectName("widget_4")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 15px;\n"
"border: 0px solid black;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius: 15px;\n"
"border: 0px solid black;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lne_ogrtmen = QtWidgets.QLineEdit(self.widget_4)
        self.lne_ogrtmen.setGeometry(QtCore.QRect(130, 80, 161, 31))
        self.lne_ogrtmen.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lne_ogrtmen.setObjectName("lne_ogrtmen")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius: 15px;\n"
"border: 0px solid black;\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-radius: 15px;\n"
"border: 0px solid black;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setGeometry(QtCore.QRect(20, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 15px;\n"
"border: 0px solid black;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.widget_4)
        self.comboBox.setGeometry(QtCore.QRect(130, 30, 161, 31))
        self.comboBox.setStyleSheet("border-radius: 0px;\n"
"border: 1px solid black;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.lne_dersAdi = QtWidgets.QLineEdit(self.widget_4)
        self.lne_dersAdi.setGeometry(QtCore.QRect(130, 130, 161, 31))
        self.lne_dersAdi.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lne_dersAdi.setObjectName("lne_dersAdi")
        self.lne_dersGunu = QtWidgets.QLineEdit(self.widget_4)
        self.lne_dersGunu.setGeometry(QtCore.QRect(130, 180, 161, 31))
        self.lne_dersGunu.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lne_dersGunu.setObjectName("lne_dersGunu")
        self.lne_dersSaati = QtWidgets.QLineEdit(self.widget_4)
        self.lne_dersSaati.setGeometry(QtCore.QRect(130, 230, 161, 31))
        self.lne_dersSaati.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.lne_dersSaati.setObjectName("lne_dersSaati")
        self.btn_gunc = QtWidgets.QPushButton(self.widget_4)
        self.btn_gunc.setGeometry(QtCore.QRect(20, 460, 271, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_gunc.setFont(font)
        self.btn_gunc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_gunc.setObjectName("btn_gunc")
        self.bnt_Sil = QtWidgets.QPushButton(self.widget_4)
        self.bnt_Sil.setEnabled(True)
        self.bnt_Sil.setGeometry(QtCore.QRect(20, 400, 271, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bnt_Sil.setFont(font)
        self.bnt_Sil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bnt_Sil.setObjectName("bnt_Sil")
        self.btn_Ekle = QtWidgets.QPushButton(self.widget_4)
        self.btn_Ekle.setGeometry(QtCore.QRect(20, 340, 271, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Ekle.setFont(font)
        self.btn_Ekle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Ekle.setObjectName("btn_Ekle")
        self.widget = QtWidgets.QWidget(DersIslemleri)
        self.widget.setGeometry(QtCore.QRect(10, 10, 141, 701))
        self.widget.setStyleSheet("QWidget{\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    border-radius: 15px;\n"
"    border: 3px solid;\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 101, 101))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/Sophia(1).png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 120, 121, 561))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_home_ders = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_home_ders.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_home_ders.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/anasayfa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home_ders.setIcon(icon)
        self.btn_home_ders.setIconSize(QtCore.QSize(35, 35))
        self.btn_home_ders.setObjectName("btn_home_ders")
        self.verticalLayout.addWidget(self.btn_home_ders)
        self.btn_ogr_ders = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_ogr_ders.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogr_ders.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/ogrenci.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ogr_ders.setIcon(icon1)
        self.btn_ogr_ders.setIconSize(QtCore.QSize(35, 35))
        self.btn_ogr_ders.setObjectName("btn_ogr_ders")
        self.verticalLayout.addWidget(self.btn_ogr_ders)
        self.btn_ders_ders = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_ders_ders.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ders_ders.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/dersW.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ders_ders.setIcon(icon2)
        self.btn_ders_ders.setIconSize(QtCore.QSize(35, 35))
        self.btn_ders_ders.setObjectName("btn_ders_ders")
        self.verticalLayout.addWidget(self.btn_ders_ders)
        self.btn_snf_ders = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_snf_ders.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_snf_ders.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/sınıf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_snf_ders.setIcon(icon3)
        self.btn_snf_ders.setIconSize(QtCore.QSize(35, 35))
        self.btn_snf_ders.setObjectName("btn_snf_ders")
        self.verticalLayout.addWidget(self.btn_snf_ders)
        self.btn_net_ders = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_net_ders.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_net_ders.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_net_ders.setIcon(icon4)
        self.btn_net_ders.setIconSize(QtCore.QSize(35, 35))
        self.btn_net_ders.setObjectName("btn_net_ders")
        self.verticalLayout.addWidget(self.btn_net_ders)
        self.widget_2 = QtWidgets.QWidget(DersIslemleri)
        self.widget_2.setGeometry(QtCore.QRect(500, 140, 701, 571))
        self.widget_2.setStyleSheet("\n"
"background-color: rgb(100, 100, 254);\n"
"\n"
"border-radius: 15px;\n"
"border: 3px solid black;\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.Widget_dersislem = QtWidgets.QTableWidget(self.widget_2)
        self.Widget_dersislem.setGeometry(QtCore.QRect(10, 10, 681, 551))
        self.Widget_dersislem.setStyleSheet("border-radius: 0px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.Widget_dersislem.setRowCount(30)
        self.Widget_dersislem.setColumnCount(5)
        self.Widget_dersislem.setObjectName("Widget_dersislem")
        self.Widget_dersislem.horizontalHeader().setDefaultSectionSize(128)
        self.widget_3 = QtWidgets.QWidget(DersIslemleri)
        self.widget_3.setGeometry(QtCore.QRect(170, 10, 1031, 111))
        self.widget_3.setStyleSheet("border-radius: 15px;\n"
"border: 3px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_3.setObjectName("widget_3")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 211, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_10.setStyleSheet("border-radius: 0px;\n"
"border: 0px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.comboBox_Ara = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_Ara.setGeometry(QtCore.QRect(570, 40, 288, 30))
        self.comboBox_Ara.setStyleSheet("border-radius: 0px;\n"
"border: 1px solid black;\n"
"")
        self.comboBox_Ara.setObjectName("comboBox_Ara")
        self.comboBox_Ara.addItem("")
        self.btn_Ara = QtWidgets.QPushButton(self.widget_3)
        self.btn_Ara.setGeometry(QtCore.QRect(870, 40, 141, 30))
        self.btn_Ara.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Ara.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid black;\n"
"")
        self.btn_Ara.setIconSize(QtCore.QSize(20, 20))
        self.btn_Ara.setObjectName("btn_Ara")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(260, 40, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-radius: 15px;\n"
"border: 0px solid black;\n"
"")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(DersIslemleri)
        QtCore.QMetaObject.connectSlotsByName(DersIslemleri)

    def retranslateUi(self, DersIslemleri):
        _translate = QtCore.QCoreApplication.translate
        DersIslemleri.setWindowTitle(_translate("DersIslemleri", "Ders İşlemleri"))
        self.label_3.setText(_translate("DersIslemleri", "Ders Adı"))
        self.label_2.setText(_translate("DersIslemleri", "Öğretmen Adı"))
        self.label_5.setText(_translate("DersIslemleri", "Ders Saati"))
        self.label_4.setText(_translate("DersIslemleri", "Ders Günü"))
        self.label.setText(_translate("DersIslemleri", "Sıınıf"))
        self.btn_gunc.setText(_translate("DersIslemleri", "Güncelle"))
        self.bnt_Sil.setText(_translate("DersIslemleri", "Sil"))
        self.btn_Ekle.setText(_translate("DersIslemleri", "Ekle"))
        self.label_10.setText(_translate("DersIslemleri", "Ders İşlemleri"))
        self.comboBox_Ara.setItemText(0, _translate("DersIslemleri", "tümü"))
        self.btn_Ara.setText(_translate("DersIslemleri", "Filtrele"))
        self.label_7.setText(_translate("DersIslemleri", "Listelemek İstediğiniz Sınıfı Seçin"))
import resource_rc
