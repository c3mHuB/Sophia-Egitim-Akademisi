# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sertan\Desktop\düzenle2\birleştirme\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Anasayfa(object):
    def setupUi(self, Anasayfa):
        Anasayfa.setObjectName("Anasayfa")
        Anasayfa.resize(970, 600)
        Anasayfa.setMinimumSize(QtCore.QSize(970, 600))
        Anasayfa.setMaximumSize(QtCore.QSize(970, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/anasayfa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Anasayfa.setWindowIcon(icon)
        Anasayfa.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Anasayfa)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_ogr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ogr.setGeometry(QtCore.QRect(740, 120, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_ogr.setFont(font)
        self.btn_ogr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ogr.setStyleSheet("border-radius: 15px;\n"
"border: 3px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"background-image: url(:/icons/white.png);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/ogrenci.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ogr.setIcon(icon1)
        self.btn_ogr.setIconSize(QtCore.QSize(50, 50))
        self.btn_ogr.setObjectName("btn_ogr")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 60, 571, 551))
        self.label_2.setMinimumSize(QtCore.QSize(571, 551))
        self.label_2.setMaximumSize(QtCore.QSize(571, 551))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/Sophia(1).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 941, 80))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 15px;\n"
"border: 3px solid white;\n"
"background-image: url(:/icons/black.png);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(150, 10, 641, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 0x;\n"
"border: 0px solid white;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_snf = QtWidgets.QPushButton(self.centralwidget)
        self.btn_snf.setGeometry(QtCore.QRect(30, 370, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_snf.setFont(font)
        self.btn_snf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_snf.setStyleSheet("border-radius: 15px;\n"
"border: 3px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"background-image: url(:/icons/white.png);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/sınıf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_snf.setIcon(icon2)
        self.btn_snf.setIconSize(QtCore.QSize(50, 50))
        self.btn_snf.setObjectName("btn_snf")
        self.btn_ders = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ders.setGeometry(QtCore.QRect(30, 110, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_ders.setFont(font)
        self.btn_ders.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ders.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_ders.setStyleSheet("border-radius: 15px;\n"
"border: 3px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"background-image: url(:/icons/white.png);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/ders.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ders.setIcon(icon3)
        self.btn_ders.setIconSize(QtCore.QSize(50, 50))
        self.btn_ders.setObjectName("btn_ders")
        self.btn_mhsb = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mhsb.setGeometry(QtCore.QRect(740, 370, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_mhsb.setFont(font)
        self.btn_mhsb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_mhsb.setStyleSheet("border-radius: 15px;\n"
"border: 3px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"background-image: url(:/icons/white.png);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_mhsb.setIcon(icon4)
        self.btn_mhsb.setIconSize(QtCore.QSize(50, 50))
        self.btn_mhsb.setObjectName("btn_mhsb")
        Anasayfa.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Anasayfa)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 21))
        self.menubar.setObjectName("menubar")
        Anasayfa.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Anasayfa)
        self.statusbar.setObjectName("statusbar")
        Anasayfa.setStatusBar(self.statusbar)

        self.retranslateUi(Anasayfa)
        QtCore.QMetaObject.connectSlotsByName(Anasayfa)

    def retranslateUi(self, Anasayfa):
        _translate = QtCore.QCoreApplication.translate
        Anasayfa.setWindowTitle(_translate("Anasayfa", "Anasayfa"))
        self.btn_ogr.setText(_translate("Anasayfa", "Öğrenci İşlemleri"))
        self.label.setText(_translate("Anasayfa", "Sophia - Eğitim Akademisi"))
        self.btn_snf.setText(_translate("Anasayfa", "Sınıf İşlemleri"))
        self.btn_ders.setText(_translate("Anasayfa", "Ders İşlemleri"))
        self.btn_mhsb.setText(_translate("Anasayfa", "Net Hesaplama"))
import resource_rc
