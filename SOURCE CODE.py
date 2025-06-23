import requests
import time
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QTextEdit, QVBoxLayout, QLineEdit, QMessageBox
import os
import pytesseract
import pyautogui
from PySide2.QtCore import QTimer, Qt  # QtCore yerine doğrudan Qt import edildi
from PySide2.QtGui import QFont
import requests
from pathlib import Path

# Belgeler klasörünün yolunu almak (Windows için)
documents_folder = Path(os.path.expanduser("~")) / "Documents"

# 'profilesi' adında bir klasör oluşturmak
profilesi_folder = documents_folder / "Screen Translator Profiles"

# Klasörün var olup olmadığını kontrol et ve yoksa oluştur
if not profilesi_folder.exists():
    profilesi_folder.mkdir(parents=True, exist_ok=True)
    print(f"'profilesi' klasörü {profilesi_folder} dizininde başarıyla oluşturuldu.")
else:
    print(f"'profilesi' klasörü zaten {profilesi_folder} dizininde mevcut.")

testwindowacikmi = False

topwindowacikmi = False

eskimetin = ""

buton_font = QFont("MS Shell Dlg 2")
buton_font.setPixelSize(13)

# 🔥 Burada dosyanın bulunduğu klasörü alıyoruz
dosya_dizini = os.path.dirname(os.path.abspath(sys.argv[0]))

dosyalar = os.listdir(profilesi_folder)

# Tesseract'ın tam yolunu oluştur
tesseract_path = os.path.join(dosya_dizini, "Tesseract", "tesseract.exe")

# pytesseract'a yolu tanımla
pytesseract.pytesseract.tesseract_cmd = tesseract_path

app = QApplication(sys.argv)

# 1.) Pencere
pencere = QWidget()
pencere.setWindowTitle("Screen Translator")
pencere.setGeometry(560, 390, 800, 400)

# 2.) Ana Menü

# 2.1.) Ana Menü Label

anamenuprofilelabel = QLabel("Profile : ", pencere)
anamenuprofilelabel.move(250, 100)
anamenuprofilelabel.setFont(buton_font)
anamenuprofilelabel.adjustSize()

anamenudevelopedbyrasnetlabel = QLabel("Screen-Translator v4.2 | Developed by Rasnet", pencere)
anamenudevelopedbyrasnetlabel.move(10, 380)
anamenudevelopedbyrasnetlabel.setFont(buton_font)
anamenudevelopedbyrasnetlabel.adjustSize()

# 2.2.) Ana Menü Combo Box

anamenuprofilsecimicombobox = QComboBox(pencere)
anamenuprofilsecimicombobox.setGeometry(350, 100, 94, 22)
anamenuprofilsecimicombobox.addItems(dosyalar)
anamenuprofilsecimicombobox.setFont(buton_font)

# 2.3.) Ana Menü Buton

anamenustartbutton = QPushButton("Start", pencere)
anamenustartbutton.setGeometry(250, 150, 93, 28)
anamenustartbutton.setFont(buton_font)

anamenustopbutton = QPushButton("Stop", pencere)
anamenustopbutton.setGeometry(350,150, 93, 28)
anamenustopbutton.setFont(buton_font)

anamenunewprofilebutton = QPushButton("New Profile", pencere)
anamenunewprofilebutton.setGeometry(300, 200, 93, 28)
anamenunewprofilebutton.setFont(buton_font)

anamenueditprofilebutton = QPushButton("Edit Profile", pencere)
anamenueditprofilebutton.setGeometry(300, 250, 93, 28)
anamenueditprofilebutton.setFont(buton_font)

# 3.1. ) Profile Settings Profile Name Menu Label

profilsettingsprofilenamemenuprofilenamelabel = QLabel("Profile Name : ", pencere)
profilsettingsprofilenamemenuprofilenamelabel.move(300, 150)
profilsettingsprofilenamemenuprofilenamelabel.setFont(buton_font)
profilsettingsprofilenamemenuprofilenamelabel.adjustSize()

# 3.2. ) Profile Settings Profile Name Menu Text Box

profilsettingsprofilenamemenuprofilnametextbox = QLineEdit(pencere)
profilsettingsprofilenamemenuprofilnametextbox.setGeometry(400, 150, 137, 24)
profilsettingsprofilenamemenuprofilnametextbox.setFont(buton_font)

# 3.3. ) Profile Settings Profile Name Menu Button

profilsettingsprofilenamemenunextbutton = QPushButton("Next", pencere)
profilsettingsprofilenamemenunextbutton.setGeometry(650, 350, 93, 28)
profilsettingsprofilenamemenunextbutton.setFont(buton_font)

profilsettingsprofilenamemenubackbutton = QPushButton("Back", pencere)
profilsettingsprofilenamemenubackbutton.setGeometry(550, 350, 93, 28)
profilsettingsprofilenamemenubackbutton.setFont(buton_font)

# 4.1. ) Profile Settings Scan Menu Label

profilsettingsscanxlabel = QLabel("x : ", pencere)
profilsettingsscanxlabel.move(200, 50)
profilsettingsscanxlabel.setFont(buton_font)
profilsettingsscanxlabel.adjustSize()
profilsettingsscanylabel = QLabel("y : ", pencere)
profilsettingsscanylabel.move(200, 100)
profilsettingsscanylabel.setFont(buton_font)
profilsettingsscanylabel.adjustSize()
profilsettingsscanwidthlabel = QLabel("Width : ", pencere)
profilsettingsscanwidthlabel.move(200, 150)
profilsettingsscanwidthlabel.setFont(buton_font)
profilsettingsscanwidthlabel.adjustSize()
profilsettingsscanheightlabel = QLabel("Heigth : ", pencere)
profilsettingsscanheightlabel.move(200, 200)
profilsettingsscanheightlabel.setFont(buton_font)
profilsettingsscanheightlabel.adjustSize()
profilsettingsscanbilgilabel = QLabel("Scan", pencere)
profilsettingsscanbilgilabel.move(350, 20)
profilsettingsscanbilgilabel.setFont(buton_font)
profilsettingsscanbilgilabel.adjustSize()

# 4.2. ) Profile Settings Scan Menu Text Box

profilsettingsscanxtextbox = QLineEdit(pencere)
profilsettingsscanxtextbox.setGeometry(300, 50, 137, 24)
profilsettingsscanxtextbox.setFont(buton_font)
profilsettingsscanytextbox = QLineEdit(pencere)
profilsettingsscanytextbox.setGeometry(300, 100, 137, 24)
profilsettingsscanytextbox.setFont(buton_font)
profilsettingsscanwidthtextbox = QLineEdit(pencere)
profilsettingsscanwidthtextbox.setGeometry(300, 150, 137, 24)
profilsettingsscanwidthtextbox.setFont(buton_font)
profilsettingsscanheighttextbox = QLineEdit(pencere)
profilsettingsscanheighttextbox.setGeometry(300, 200, 137, 24)
profilsettingsscanheighttextbox.setFont(buton_font)

# 4.3. ) Profile Settings Scan Menu Button

profilsettingsscansetbutton = QPushButton("Set", pencere)
profilsettingsscansetbutton.setGeometry(320, 250, 93, 28)
profilsettingsscansetbutton.setFont(buton_font)

profilsettingsscannextbutton = QPushButton("Next", pencere)
profilsettingsscannextbutton.setGeometry(650, 350, 93, 28)
profilsettingsscannextbutton.setFont(buton_font)

profilsettingsscanbackbutton = QPushButton("Back", pencere)
profilsettingsscanbackbutton.setGeometry(550, 350, 93, 28)
profilsettingsscanbackbutton.setFont(buton_font)

# 5.1. ) Profile Settings Write Menu Label

profilsettingswritexlabel = QLabel("x : ", pencere)
profilsettingswritexlabel.move(200, 50)
profilsettingswritexlabel.setFont(buton_font)
profilsettingswritexlabel.adjustSize()
profilsettingswriteylabel = QLabel("y : ", pencere)
profilsettingswriteylabel.move(200, 100)
profilsettingswriteylabel.setFont(buton_font)
profilsettingswriteylabel.adjustSize()
profilsettingswritewidthlabel = QLabel("Width : ", pencere)
profilsettingswritewidthlabel.move(200, 150)
profilsettingswritewidthlabel.setFont(buton_font)
profilsettingswritewidthlabel.adjustSize()
profilsettingswriteheightlabel = QLabel("Heigth : ", pencere)
profilsettingswriteheightlabel.move(200, 200)
profilsettingswriteheightlabel.setFont(buton_font)
profilsettingswriteheightlabel.adjustSize()
profilsettingswritebilgilabel = QLabel("Write", pencere)
profilsettingswritebilgilabel.move(350, 20)
profilsettingswritebilgilabel.setFont(buton_font)
profilsettingswritebilgilabel.adjustSize()

# 5.2. ) Profile Settings Write Menu Text Box

profilsettingswritextextbox = QLineEdit(pencere)
profilsettingswritextextbox.setGeometry(300, 50, 137, 24)
profilsettingswritextextbox.setFont(buton_font)
profilsettingswriteytextbox = QLineEdit(pencere)
profilsettingswriteytextbox.setGeometry(300, 100, 137, 24)
profilsettingswriteytextbox.setFont(buton_font)
profilsettingswritewidthtextbox = QLineEdit(pencere)
profilsettingswritewidthtextbox.setGeometry(300, 150, 137, 24)
profilsettingswritewidthtextbox.setFont(buton_font)
profilsettingswriteheighttextbox = QLineEdit(pencere)
profilsettingswriteheighttextbox.setGeometry(300, 200, 137, 24)
profilsettingswriteheighttextbox.setFont(buton_font)

# 5.3. ) Profile Settings Write Menu Button

profilsettingswritesetbutton = QPushButton("Set", pencere)
profilsettingswritesetbutton.setGeometry(320, 250, 93, 28)
profilsettingswritesetbutton.setFont(buton_font)

profilsettingswritenextbutton = QPushButton("Next", pencere)
profilsettingswritenextbutton.setGeometry(650, 350, 93, 28)
profilsettingswritenextbutton.setFont(buton_font)

profilsettingswritebackbutton = QPushButton("Back", pencere)
profilsettingswritebackbutton.setGeometry(550, 350, 93, 28)
profilsettingswritebackbutton.setFont(buton_font)

# 6.1. ) Profile Settings Text Edit Menu Label

profilsettingstexteditbackgroundopacitylabel = QLabel("Background Opacity : ", pencere)
profilsettingstexteditbackgroundopacitylabel.move(50, 50)
profilsettingstexteditbackgroundopacitylabel.setFont(buton_font)
profilsettingstexteditbackgroundopacitylabel.adjustSize()
profilsettingstexteditbackgroundcolorlabel = QLabel("Background Color : ", pencere)
profilsettingstexteditbackgroundcolorlabel.move(50, 90)
profilsettingstexteditbackgroundcolorlabel.setFont(buton_font)
profilsettingstexteditbackgroundcolorlabel.adjustSize()
profilsettingstexteditlabelcolorlabel = QLabel("Label Color : ", pencere)
profilsettingstexteditlabelcolorlabel.move(50, 130)
profilsettingstexteditlabelcolorlabel.setFont(buton_font)
profilsettingstexteditlabelcolorlabel.adjustSize()
profilsettingstextedittextcolorlabel = QLabel("Text Color : ", pencere)
profilsettingstextedittextcolorlabel.move(50, 170)
profilsettingstextedittextcolorlabel.setFont(buton_font)
profilsettingstextedittextcolorlabel.adjustSize()
profilsettingstextedittranslatelabel = QLabel("Translate : ", pencere)
profilsettingstextedittranslatelabel.move(50, 210)
profilsettingstextedittranslatelabel.setFont(buton_font)
profilsettingstextedittranslatelabel.adjustSize()
profilsettingstexteditfontlabel = QLabel("Font : ", pencere)
profilsettingstexteditfontlabel.move(400, 50)
profilsettingstexteditfontlabel.setFont(buton_font)
profilsettingstexteditfontlabel.adjustSize()
profilsettingstexteditfontsizelabel = QLabel("Font Size : ", pencere)
profilsettingstexteditfontsizelabel.move(400, 90)
profilsettingstexteditfontsizelabel.setFont(buton_font)
profilsettingstexteditfontsizelabel.adjustSize()
profilsettingstextedittranslatorkimlabel = QLabel("Translator : ", pencere)
profilsettingstextedittranslatorkimlabel.move(400, 130)
profilsettingstextedittranslatorkimlabel.setFont(buton_font)
profilsettingstextedittranslatorkimlabel.adjustSize()
profilsettingstexteditapilabel = QLabel("API : ", pencere)
profilsettingstexteditapilabel.move(400, 170)
profilsettingstexteditapilabel.setFont(buton_font)
profilsettingstexteditapilabel.adjustSize()
profilsettingstextedittolabel = QLabel("to", pencere)
profilsettingstextedittolabel.move(400, 210)
profilsettingstextedittolabel.setFont(buton_font)
profilsettingstextedittolabel.adjustSize()

# 6.2. ) Profile Settings Text Edit Menu Text Box

profilsettingstexteditbackgroundcolortextbox = QLineEdit(pencere)
profilsettingstexteditbackgroundcolortextbox.setGeometry(200, 85, 137, 24)
profilsettingstexteditbackgroundcolortextbox.setFont(buton_font)
profilsettingstexteditlabelcolortextbox = QLineEdit(pencere)
profilsettingstexteditlabelcolortextbox.setGeometry(200, 125, 137, 24)
profilsettingstexteditlabelcolortextbox.setFont(buton_font)
profilsettingstextedittextcolortextbox = QLineEdit(pencere)
profilsettingstextedittextcolortextbox.setGeometry(200, 165, 137, 24)
profilsettingstextedittextcolortextbox.setFont(buton_font)
profilsettingstexteditfontsizetextbox = QLineEdit(pencere)
profilsettingstexteditfontsizetextbox.setGeometry(550, 85, 137, 24)
profilsettingstexteditfontsizetextbox.setFont(buton_font)
profilsettingstexteditapitextbox = QLineEdit(pencere)
profilsettingstexteditapitextbox.setGeometry(550, 165, 137, 24)
profilsettingstexteditapitextbox.setFont(buton_font)


# 6.3. ) Profile Settings Text Edit Menu Combo Box

profilsettingstexteditbackgroundopacitycombobox = QComboBox(pencere)
profilsettingstexteditbackgroundopacitycombobox.setGeometry(200, 45, 94, 22)
profilsettingstexteditbackgroundopacitycombobox.setFont(buton_font)
profilsettingstexteditbackgroundopacitycombobox.addItem("Translucent")
profilsettingstexteditbackgroundopacitycombobox.addItem("Opaque")

profilsettingstextedittranslatetaranacakdilcombobox = QComboBox(pencere)
profilsettingstextedittranslatetaranacakdilcombobox.setGeometry(200, 205, 94, 22)
profilsettingstextedittranslatetaranacakdilcombobox.setFont(buton_font)
profilsettingstextedittranslatetaranacakdilcombobox.addItem("German")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Arabic")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Bulgarian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Czech")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Chinese")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Danish")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Indonesian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Estonian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Dutch")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Finnish")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("French")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("English")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Spanish")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Swedish")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Italian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Japanese")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Korean")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Polish")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Latvian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Lithuanian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Hungarian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Norwegian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Portuguese")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Romanian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Russian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Slovak")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Slovenian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Turkish")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Ukrainian")
profilsettingstextedittranslatetaranacakdilcombobox.addItem("Greek")

profilsettingstexteditfontcombobox = QComboBox(pencere)
profilsettingstexteditfontcombobox.setGeometry(550, 45, 94, 22)
profilsettingstexteditfontcombobox.setFont(buton_font)
profilsettingstexteditfontcombobox.addItem("Arial")
profilsettingstexteditfontcombobox.addItem("Times New Roman")
profilsettingstexteditfontcombobox.addItem("Courier New")
profilsettingstexteditfontcombobox.addItem("Verdana")
profilsettingstexteditfontcombobox.addItem("Tahoma")
profilsettingstexteditfontcombobox.addItem("Trebuchet MS")
profilsettingstexteditfontcombobox.addItem("Georgia")
profilsettingstexteditfontcombobox.addItem("Comic Sans MS")
profilsettingstexteditfontcombobox.addItem("Lucida Console")
profilsettingstexteditfontcombobox.addItem("Segoe UI")
profilsettingstexteditfontcombobox.addItem("Calibri")
profilsettingstexteditfontcombobox.addItem("Cambria")
profilsettingstexteditfontcombobox.addItem("Impact")
profilsettingstexteditfontcombobox.addItem("Century Gothic")
profilsettingstexteditfontcombobox.addItem("Palatino Linotype")
profilsettingstexteditfontcombobox.addItem("Book Antiqua")
profilsettingstexteditfontcombobox.addItem("Garamond")
profilsettingstexteditfontcombobox.addItem("Franklin Gothic Medium")

profilsettingstextedittranslatehedefdilcombobox = QComboBox(pencere)
profilsettingstextedittranslatehedefdilcombobox.setGeometry(550, 205, 94, 22)
profilsettingstextedittranslatehedefdilcombobox.setFont(buton_font)
profilsettingstextedittranslatehedefdilcombobox.addItem("German")
profilsettingstextedittranslatehedefdilcombobox.addItem("Arabic")
profilsettingstextedittranslatehedefdilcombobox.addItem("Bulgarian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Czech")
profilsettingstextedittranslatehedefdilcombobox.addItem("Chinese")
profilsettingstextedittranslatehedefdilcombobox.addItem("Danish")
profilsettingstextedittranslatehedefdilcombobox.addItem("Indonesian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Estonian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Dutch")
profilsettingstextedittranslatehedefdilcombobox.addItem("Finnish")
profilsettingstextedittranslatehedefdilcombobox.addItem("French")
profilsettingstextedittranslatehedefdilcombobox.addItem("English")
profilsettingstextedittranslatehedefdilcombobox.addItem("Spanish")
profilsettingstextedittranslatehedefdilcombobox.addItem("Swedish")
profilsettingstextedittranslatehedefdilcombobox.addItem("Italian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Japanese")
profilsettingstextedittranslatehedefdilcombobox.addItem("Korean")
profilsettingstextedittranslatehedefdilcombobox.addItem("Polish")
profilsettingstextedittranslatehedefdilcombobox.addItem("Latvian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Lithuanian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Hungarian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Norwegian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Portuguese")
profilsettingstextedittranslatehedefdilcombobox.addItem("Romanian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Russian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Slovak")
profilsettingstextedittranslatehedefdilcombobox.addItem("Slovenian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Turkish")
profilsettingstextedittranslatehedefdilcombobox.addItem("Ukrainian")
profilsettingstextedittranslatehedefdilcombobox.addItem("Greek")

profilsettingstextedittranslatorkimcombobox = QComboBox(pencere)
profilsettingstextedittranslatorkimcombobox.setGeometry(550, 125, 94, 22)
profilsettingstextedittranslatorkimcombobox.setFont(buton_font)
profilsettingstextedittranslatorkimcombobox.addItem("Libre Translate")
profilsettingstextedittranslatorkimcombobox.addItem("DeepL Free")
profilsettingstextedittranslatorkimcombobox.addItem("DeepL Pro")

# 6.4. ) Profile Settings Text Edit Menu Button

profilsettingstextedittestbutton = QPushButton("Test", pencere)
profilsettingstextedittestbutton.setGeometry(450, 350, 93, 28)
profilsettingstextedittestbutton.setFont(buton_font)

profilsettingstexteditsavebutton = QPushButton("Save", pencere)
profilsettingstexteditsavebutton.setGeometry(650, 350, 93, 28)
profilsettingstexteditsavebutton.setFont(buton_font)

profilsettingstexteditbackbutton = QPushButton("Back", pencere)
profilsettingstexteditbackbutton.setGeometry(550, 350, 93, 28)
profilsettingstexteditbackbutton.setFont(buton_font)




# Fonksiyonlar

def anamenuduzeni():
    anamenuprofilelabel.show()
    anamenudevelopedbyrasnetlabel.show()
    anamenuprofilsecimicombobox.show()
    anamenustartbutton.show()
    anamenunewprofilebutton.show()
    anamenueditprofilebutton.show()
    profilsettingsprofilenamemenuprofilenamelabel.hide()
    profilsettingsprofilenamemenuprofilnametextbox.hide()
    profilsettingsprofilenamemenunextbutton.hide()
    profilsettingsprofilenamemenubackbutton.hide()
    profilsettingsscanxlabel.hide()
    profilsettingsscanylabel.hide()
    profilsettingsscanwidthlabel.hide()
    profilsettingsscanheightlabel.hide()
    profilsettingsscanxtextbox.hide()
    profilsettingsscanytextbox.hide()
    profilsettingsscanwidthtextbox.hide()
    profilsettingsscanheighttextbox.hide()
    profilsettingsscansetbutton.hide()
    profilsettingsscannextbutton.hide()
    profilsettingsscanbackbutton.hide()
    profilsettingswritexlabel.hide()
    profilsettingswriteylabel.hide()
    profilsettingswritewidthlabel.hide()
    profilsettingswriteheightlabel.hide()
    profilsettingswritextextbox.hide()
    profilsettingswriteytextbox.hide()
    profilsettingswritewidthtextbox.hide()
    profilsettingswriteheighttextbox.hide()
    profilsettingswritesetbutton.hide()
    profilsettingswritenextbutton.hide()
    profilsettingswritebackbutton.hide()
    profilsettingsscanbilgilabel.hide()
    profilsettingswritebilgilabel.hide()
    profilsettingstexteditbackgroundopacitylabel.hide()
    profilsettingstexteditbackgroundcolorlabel.hide()
    profilsettingstexteditlabelcolorlabel.hide()
    profilsettingstextedittextcolorlabel.hide()
    profilsettingstextedittranslatelabel.hide()
    profilsettingstexteditfontlabel.hide()
    profilsettingstexteditfontsizelabel.hide()
    profilsettingstextedittolabel.hide()
    profilsettingstexteditbackgroundcolortextbox.hide()
    profilsettingstexteditlabelcolortextbox.hide()
    profilsettingstextedittextcolortextbox.hide()
    profilsettingstexteditfontsizetextbox.hide()
    profilsettingstexteditbackgroundopacitycombobox.hide()
    profilsettingstextedittranslatetaranacakdilcombobox.hide()
    profilsettingstexteditfontcombobox.hide()
    profilsettingstextedittranslatehedefdilcombobox.hide()
    profilsettingstextedittestbutton.hide()
    profilsettingstexteditsavebutton.hide()
    profilsettingstexteditbackbutton.hide()
    anamenustopbutton.show()
    profilsettingstexteditapilabel.hide()
    profilsettingstextedittranslatorkimlabel.hide()
    profilsettingstextedittranslatorkimcombobox.hide()
    profilsettingstexteditapitextbox.hide()

def profilesettingsprofilenamemenuduzeni():
    anamenuprofilelabel.hide()
    anamenudevelopedbyrasnetlabel.hide()
    anamenuprofilsecimicombobox.hide()
    anamenustartbutton.hide()
    anamenunewprofilebutton.hide()
    anamenueditprofilebutton.hide()
    profilsettingsprofilenamemenuprofilenamelabel.show()
    profilsettingsprofilenamemenuprofilnametextbox.show()
    profilsettingsprofilenamemenunextbutton.show()
    profilsettingsprofilenamemenubackbutton.show()
    profilsettingsscanxlabel.hide()
    profilsettingsscanylabel.hide()
    profilsettingsscanwidthlabel.hide()
    profilsettingsscanheightlabel.hide()
    profilsettingsscanxtextbox.hide()
    profilsettingsscanytextbox.hide()
    profilsettingsscanwidthtextbox.hide()
    profilsettingsscanheighttextbox.hide()
    profilsettingsscansetbutton.hide()
    profilsettingsscannextbutton.hide()
    profilsettingsscanbackbutton.hide()
    profilsettingswritexlabel.hide()
    profilsettingswriteylabel.hide()
    profilsettingswritewidthlabel.hide()
    profilsettingswriteheightlabel.hide()
    profilsettingswritextextbox.hide()
    profilsettingswriteytextbox.hide()
    profilsettingswritewidthtextbox.hide()
    profilsettingswriteheighttextbox.hide()
    profilsettingswritesetbutton.hide()
    profilsettingswritenextbutton.hide()
    profilsettingswritebackbutton.hide()
    profilsettingsscanbilgilabel.hide()
    profilsettingswritebilgilabel.hide()
    profilsettingstexteditbackgroundopacitylabel.hide()
    profilsettingstexteditbackgroundcolorlabel.hide()
    profilsettingstexteditlabelcolorlabel.hide()
    profilsettingstextedittextcolorlabel.hide()
    profilsettingstextedittranslatelabel.hide()
    profilsettingstexteditfontlabel.hide()
    profilsettingstexteditfontsizelabel.hide()
    profilsettingstextedittolabel.hide()
    profilsettingstexteditbackgroundcolortextbox.hide()
    profilsettingstexteditlabelcolortextbox.hide()
    profilsettingstextedittextcolortextbox.hide()
    profilsettingstexteditfontsizetextbox.hide()
    profilsettingstexteditbackgroundopacitycombobox.hide()
    profilsettingstextedittranslatetaranacakdilcombobox.hide()
    profilsettingstexteditfontcombobox.hide()
    profilsettingstextedittranslatehedefdilcombobox.hide()
    profilsettingstextedittestbutton.hide()
    profilsettingstexteditsavebutton.hide()
    profilsettingstexteditbackbutton.hide()
    anamenustopbutton.hide()
    profilsettingstexteditapilabel.hide()
    profilsettingstextedittranslatorkimlabel.hide()
    profilsettingstextedittranslatorkimcombobox.hide()
    profilsettingstexteditapitextbox.hide()


def profilesettingsscanmenuduzeni():
    anamenuprofilelabel.hide()
    anamenudevelopedbyrasnetlabel.hide()
    anamenuprofilsecimicombobox.hide()
    anamenustartbutton.hide()
    anamenunewprofilebutton.hide()
    anamenueditprofilebutton.hide()
    profilsettingsprofilenamemenuprofilenamelabel.hide()
    profilsettingsprofilenamemenuprofilnametextbox.hide()
    profilsettingsprofilenamemenunextbutton.hide()
    profilsettingsprofilenamemenubackbutton.hide()
    profilsettingsscanxlabel.show()
    profilsettingsscanylabel.show()
    profilsettingsscanwidthlabel.show()
    profilsettingsscanheightlabel.show()
    profilsettingsscanxtextbox.show()
    profilsettingsscanytextbox.show()
    profilsettingsscanwidthtextbox.show()
    profilsettingsscanheighttextbox.show()
    profilsettingsscansetbutton.show()
    profilsettingsscannextbutton.show()
    profilsettingsscanbackbutton.show()
    profilsettingswritexlabel.hide()
    profilsettingswriteylabel.hide()
    profilsettingswritewidthlabel.hide()
    profilsettingswriteheightlabel.hide()
    profilsettingswritextextbox.hide()
    profilsettingswriteytextbox.hide()
    profilsettingswritewidthtextbox.hide()
    profilsettingswriteheighttextbox.hide()
    profilsettingswritesetbutton.hide()
    profilsettingswritenextbutton.hide()
    profilsettingswritebackbutton.hide()
    profilsettingsscanbilgilabel.show()
    profilsettingswritebilgilabel.hide()
    profilsettingstexteditbackgroundopacitylabel.hide()
    profilsettingstexteditbackgroundcolorlabel.hide()
    profilsettingstexteditlabelcolorlabel.hide()
    profilsettingstextedittextcolorlabel.hide()
    profilsettingstextedittranslatelabel.hide()
    profilsettingstexteditfontlabel.hide()
    profilsettingstexteditfontsizelabel.hide()
    profilsettingstextedittolabel.hide()
    profilsettingstexteditbackgroundcolortextbox.hide()
    profilsettingstexteditlabelcolortextbox.hide()
    profilsettingstextedittextcolortextbox.hide()
    profilsettingstexteditfontsizetextbox.hide()
    profilsettingstexteditbackgroundopacitycombobox.hide()
    profilsettingstextedittranslatetaranacakdilcombobox.hide()
    profilsettingstexteditfontcombobox.hide()
    profilsettingstextedittranslatehedefdilcombobox.hide()
    profilsettingstextedittestbutton.hide()
    profilsettingstexteditsavebutton.hide()
    profilsettingstexteditbackbutton.hide()
    anamenustopbutton.hide()
    profilsettingstexteditapilabel.hide()
    profilsettingstextedittranslatorkimlabel.hide()
    profilsettingstextedittranslatorkimcombobox.hide()
    profilsettingstexteditapitextbox.hide()


def profilesettingswritemenuduzeni():
    anamenuprofilelabel.hide()
    anamenudevelopedbyrasnetlabel.hide()
    anamenuprofilsecimicombobox.hide()
    anamenustartbutton.hide()
    anamenunewprofilebutton.hide()
    anamenueditprofilebutton.hide()
    profilsettingsprofilenamemenuprofilenamelabel.hide()
    profilsettingsprofilenamemenuprofilnametextbox.hide()
    profilsettingsprofilenamemenunextbutton.hide()
    profilsettingsprofilenamemenubackbutton.hide()
    profilsettingsscanxlabel.hide()
    profilsettingsscanylabel.hide()
    profilsettingsscanwidthlabel.hide()
    profilsettingsscanheightlabel.hide()
    profilsettingsscanxtextbox.hide()
    profilsettingsscanytextbox.hide()
    profilsettingsscanwidthtextbox.hide()
    profilsettingsscanheighttextbox.hide()
    profilsettingsscansetbutton.hide()
    profilsettingsscannextbutton.hide()
    profilsettingsscanbackbutton.hide()
    profilsettingswritexlabel.show()
    profilsettingswriteylabel.show()
    profilsettingswritewidthlabel.show()
    profilsettingswriteheightlabel.show()
    profilsettingswritextextbox.show()
    profilsettingswriteytextbox.show()
    profilsettingswritewidthtextbox.show()
    profilsettingswriteheighttextbox.show()
    profilsettingswritesetbutton.show()
    profilsettingswritenextbutton.show()
    profilsettingswritebackbutton.show()
    profilsettingsscanbilgilabel.hide()
    profilsettingswritebilgilabel.show()
    profilsettingstexteditbackgroundopacitylabel.hide()
    profilsettingstexteditbackgroundcolorlabel.hide()
    profilsettingstexteditlabelcolorlabel.hide()
    profilsettingstextedittextcolorlabel.hide()
    profilsettingstextedittranslatelabel.hide()
    profilsettingstexteditfontlabel.hide()
    profilsettingstexteditfontsizelabel.hide()
    profilsettingstextedittolabel.hide()
    profilsettingstexteditbackgroundcolortextbox.hide()
    profilsettingstexteditlabelcolortextbox.hide()
    profilsettingstextedittextcolortextbox.hide()
    profilsettingstexteditfontsizetextbox.hide()
    profilsettingstexteditbackgroundopacitycombobox.hide()
    profilsettingstextedittranslatetaranacakdilcombobox.hide()
    profilsettingstexteditfontcombobox.hide()
    profilsettingstextedittranslatehedefdilcombobox.hide()
    profilsettingstextedittestbutton.hide()
    profilsettingstexteditsavebutton.hide()
    profilsettingstexteditbackbutton.hide()
    anamenustopbutton.hide()
    profilsettingstexteditapilabel.hide()
    profilsettingstextedittranslatorkimlabel.hide()
    profilsettingstextedittranslatorkimcombobox.hide()
    profilsettingstexteditapitextbox.hide()


def profilesettingstexteditmenuduzen():
    anamenuprofilelabel.hide()
    anamenudevelopedbyrasnetlabel.hide()
    anamenuprofilsecimicombobox.hide()
    anamenustartbutton.hide()
    anamenunewprofilebutton.hide()
    anamenueditprofilebutton.hide()
    profilsettingsprofilenamemenuprofilenamelabel.hide()
    profilsettingsprofilenamemenuprofilnametextbox.hide()
    profilsettingsprofilenamemenunextbutton.hide()
    profilsettingsprofilenamemenubackbutton.hide()
    profilsettingsscanxlabel.hide()
    profilsettingsscanylabel.hide()
    profilsettingsscanwidthlabel.hide()
    profilsettingsscanheightlabel.hide()
    profilsettingsscanxtextbox.hide()
    profilsettingsscanytextbox.hide()
    profilsettingsscanwidthtextbox.hide()
    profilsettingsscanheighttextbox.hide()
    profilsettingsscansetbutton.hide()
    profilsettingsscannextbutton.hide()
    profilsettingsscanbackbutton.hide()
    profilsettingswritexlabel.hide()
    profilsettingswriteylabel.hide()
    profilsettingswritewidthlabel.hide()
    profilsettingswriteheightlabel.hide()
    profilsettingswritextextbox.hide()
    profilsettingswriteytextbox.hide()
    profilsettingswritewidthtextbox.hide()
    profilsettingswriteheighttextbox.hide()
    profilsettingswritesetbutton.hide()
    profilsettingswritenextbutton.hide()
    profilsettingswritebackbutton.hide()
    profilsettingsscanbilgilabel.hide()
    profilsettingswritebilgilabel.hide()
    profilsettingstexteditbackgroundopacitylabel.show()
    profilsettingstexteditbackgroundcolorlabel.show()
    profilsettingstexteditlabelcolorlabel.show()
    profilsettingstextedittextcolorlabel.show()
    profilsettingstextedittranslatelabel.show()
    profilsettingstexteditfontlabel.show()
    profilsettingstexteditfontsizelabel.show()
    profilsettingstextedittolabel.show()
    profilsettingstexteditbackgroundcolortextbox.show()
    profilsettingstexteditlabelcolortextbox.show()
    profilsettingstextedittextcolortextbox.show()
    profilsettingstexteditfontsizetextbox.show()
    profilsettingstexteditbackgroundopacitycombobox.show()
    profilsettingstextedittranslatetaranacakdilcombobox.show()
    profilsettingstexteditfontcombobox.show()
    profilsettingstextedittranslatehedefdilcombobox.show()
    profilsettingstextedittestbutton.show()
    profilsettingstexteditsavebutton.show()
    profilsettingstexteditbackbutton.show()
    anamenustopbutton.hide()
    profilsettingstexteditapilabel.show()
    profilsettingstextedittranslatorkimlabel.show()
    profilsettingstextedittranslatorkimcombobox.show()
    profilsettingstexteditapitextbox.show()


def profilsettingsscansetbuttontiklandi():
    # 1.) Pencere
    scanwindow = QWidget()
    scanwindow.setWindowTitle("Screen Translator")
    scanwindow.setGeometry(200, 700, 800, 200)
    scanwindow.setWindowOpacity(0.5)  # %50 saydamlık

    # 2.) Button
    scanwindowsetbutton = QPushButton("Set", scanwindow)
    scanwindowsetbutton.setGeometry(50, 50, 93, 28)

    def scanwindowsetbuttontiklandi():
        scanwindowscantiklandiscangeometry = scanwindow.geometry()
        scanwindowscantiklandiscanx = scanwindowscantiklandiscangeometry.x()
        scanwindowscantiklandiscany = scanwindowscantiklandiscangeometry.y()
        scanwindowscantiklandiscanwidth = scanwindowscantiklandiscangeometry.width()
        scanwindowscantiklandiscanheight = scanwindowscantiklandiscangeometry.height()

        profilsettingsscanxtextbox.setText(str(scanwindowscantiklandiscanx))
        profilsettingsscanytextbox.setText(str(scanwindowscantiklandiscany))
        profilsettingsscanwidthtextbox.setText(str(scanwindowscantiklandiscanwidth))
        profilsettingsscanheighttextbox.setText(str(scanwindowscantiklandiscanheight))

        # 3 saniye sonra sadece bu pencere kapanacak
        QTimer.singleShot(100, scanwindow.close)

    scanwindowsetbutton.clicked.connect(scanwindowsetbuttontiklandi)
    scanwindow.show()

def profilsettingswritesetbuttontiklandi():
    # 1.) Pencere
    writewindow = QWidget()
    writewindow.setWindowTitle("Screen Translator")
    writewindow.setGeometry(200, 700, 800, 200)
    writewindow.setWindowOpacity(0.5)  # %50 saydamlık

    # 2.) Button
    writewindowsetbutton = QPushButton("Set", writewindow)
    writewindowsetbutton.setGeometry(50, 50, 93, 28)

    def writewindowsetbuttontiklandi():
        writewindowsettiklandiwritegeometry = writewindow.geometry()
        writewindowsettiklandiwritex = writewindowsettiklandiwritegeometry.x()
        writewindowsettiklandiwritey = writewindowsettiklandiwritegeometry.y()
        writewindowsettiklandiwritewidth = writewindowsettiklandiwritegeometry.width()
        writewindowsettiklandiwriteheight = writewindowsettiklandiwritegeometry.height()

        profilsettingswritextextbox.setText(str(writewindowsettiklandiwritex))
        profilsettingswriteytextbox.setText(str(writewindowsettiklandiwritey))
        profilsettingswritewidthtextbox.setText(str(writewindowsettiklandiwritewidth))
        profilsettingswriteheighttextbox.setText(str(writewindowsettiklandiwriteheight))

        # 3 saniye sonra sadece bu pencere kapanacak
        QTimer.singleShot(100, writewindow.close)

    writewindowsetbutton.clicked.connect(writewindowsetbuttontiklandi)
    writewindow.show()

def profilsettingstextedittesttiklandi():
    global testwindowacikmi
    if testwindowacikmi == False:
        
        testwindowacikmi = True
        testwindow = QWidget()
        testwindow.setWindowTitle("Test")
        testwindow.setGeometry(560, 390, 800, 200)
        testwindow.setWindowFlags(Qt.FramelessWindowHint)
        testwindow.setFixedSize(800, 200)
        testwindow.move(560, 390)

        testwindowbackgroundopacitydegisken = profilsettingstexteditbackgroundopacitycombobox.currentText()
        testwindowbackgroundcolordegisken = profilsettingstexteditbackgroundcolortextbox.text()
        testwindowlabelcolordegisken = profilsettingstexteditlabelcolortextbox.text()
        testwindowtextcolordegisken = profilsettingstextedittextcolortextbox.text()
        testwindowfontdegisken = profilsettingstexteditfontcombobox.currentText()
        testwindowfontsizedegisken = profilsettingstexteditfontsizetextbox.text()

        # Yazı içeren küçük label (arka planı sarı, köşeleri yuvarlak)
        testwindowtext_label = QLabel("Hello World", testwindow)
        try:
            testwindowtext_label.setFont(QFont(testwindowfontdegisken, int(testwindowfontsizedegisken)))
        except:
            testwindowtext_label.setFont(QFont("Arial", int(15)))
        
        try:
            testwindowtext_label.setStyleSheet(
                f"""
                background-color: {testwindowlabelcolordegisken};
                color: {testwindowtextcolordegisken};
                border-radius: 15px;
                padding: 10px;
                """
            )
        except:
            testwindowtext_label.setStyleSheet(
                f"""
                background-color: black;
                color: white;
                border-radius: 15px;
                padding: 10px;
                """
            )

        testwindowtext_label.adjustSize()
        testwindowclosebuton = QPushButton("Close", testwindow)
        testwindowclosebuton.move(20, 20)
        try:
            testwindow.setStyleSheet("background-color: " + testwindowbackgroundcolordegisken + ";")
        except:
            testwindow.setStyleSheet("background-color: white;")

        if testwindowbackgroundopacitydegisken == "Translucent":
            testwindow.setAttribute(Qt.WA_TranslucentBackground)  # Arka planı şeffaf yap
        else:
            testwindow.setAttribute(Qt.WA_TranslucentBackground, False)

        # Ortalamak için pozisyon ayarı
        label_x = (800 - testwindowtext_label.width()) // 2
        label_y = (200 - testwindowtext_label.height()) // 2
        testwindowtext_label.move(label_x, label_y)

        def testwindowclosetiklandi():
            global testwindowacikmi
            testwindow.close()
            testwindowacikmi = False


        testwindowclosebuton.clicked.connect(testwindowclosetiklandi)
        testwindow.show()

    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("Please close the currently open “Test” window first.")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

def anamenunewprofilebuttontiklandi():
    profilsettingsprofilenamemenuprofilnametextbox.setText("")
    profilsettingsscanxtextbox.setText("")
    profilsettingsscanytextbox.setText("")
    profilsettingsscanwidthtextbox.setText("")
    profilsettingsscanheighttextbox.setText("")
    profilsettingswritextextbox.setText("")
    profilsettingswriteytextbox.setText("")
    profilsettingswritewidthtextbox.setText("")
    profilsettingswriteheighttextbox.setText("")
    profilsettingstexteditbackgroundcolortextbox.setText("")
    profilsettingstexteditlabelcolortextbox.setText("")
    profilsettingstextedittextcolortextbox.setText("")
    profilsettingstexteditfontsizetextbox.setText("")
    profilsettingstexteditbackgroundopacitycombobox.setCurrentIndex(0)
    profilsettingstextedittranslatetaranacakdilcombobox.setCurrentIndex(0)
    profilsettingstexteditfontcombobox.setCurrentIndex(0)
    profilsettingstextedittranslatehedefdilcombobox.setCurrentIndex(0)
    profilesettingsprofilenamemenuduzeni()

def profilsettingsprofilenamemenunextbuttontiklandi():
    randomdeger1 = profilsettingsprofilenamemenuprofilnametextbox.text()
    if randomdeger1 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("Please give your profile a name")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster
    else:
        profilesettingsscanmenuduzeni()

def profilsettingsscannextbuttontiklandi():
    randomdegisken2 = profilsettingsscanxtextbox.text()
    randomdegisken3 = profilsettingsscanytextbox.text()
    randomdegisken4 = profilsettingsscanwidthtextbox.text()
    randomdegisken5 = profilsettingsscanheighttextbox.text()

    if randomdegisken2 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("please define an x value")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    elif randomdegisken3 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("please define an y value")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    elif randomdegisken4 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("please define an width value")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    elif randomdegisken5 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("please define an height value")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    else:
        profilesettingswritemenuduzeni()

def profilsettingswritenextbuttontiklandi():
    randomdegisken6 = profilsettingsscanxtextbox.text()
    randomdegisken7 = profilsettingsscanytextbox.text()
    randomdegisken8 = profilsettingsscanwidthtextbox.text()
    randomdegisken9 = profilsettingsscanheighttextbox.text()

    if randomdegisken6 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("please define an x value")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    elif randomdegisken7 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("please define an y value")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    elif randomdegisken8 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("please define an width value")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    elif randomdegisken9 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("please define an height value")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    else:
        profilesettingstexteditmenuduzen()

def profilsettingstexteditsavebuttontiklandi():
    global anamenuprofilsecimicombobox
    randomdeger10 = profilsettingstexteditbackgroundcolortextbox.text()
    randomdeger11 = profilsettingstexteditlabelcolortextbox.text()
    randomdeger12 = profilsettingstextedittextcolortextbox.text()
    randomdeger13 = profilsettingstexteditfontsizetextbox.text()
    randomdeger71 = profilsettingstextedittranslatorkimcombobox.currentText()
    randomdeger72 = profilsettingstexteditapitextbox.text()

    if randomdeger10 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("Please type the color you want into the Background Color box")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    elif randomdeger11 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("Please type the color you want into the Label Color box")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    elif randomdeger12 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("Please type the color you want into the Text Color box")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    elif randomdeger13 == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("Please type the desired number into the font size box")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    elif randomdeger71 == "DeepL Free":
        if randomdeger72 == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
            msg.setWindowTitle("Warning")  # Pencere başlığı
            msg.setText("If you want to use DeepL you have to enter the API")  # Ana mesaj
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
            msg.exec()  # Mesaj kutusunu göster

        else:
            kaydedilecekprofilname = profilsettingsprofilenamemenuprofilnametextbox.text()
            kaydedilecekscanx = profilsettingsscanxtextbox.text()
            kaydedilecekscany = profilsettingsscanytextbox.text()
            kaydedilecekscanwidth = profilsettingsscanwidthtextbox.text()
            kaydedilecekscanheight = profilsettingsscanheighttextbox.text()
            kaydedilecekwritex = profilsettingswritextextbox.text()
            kaydedilecekwritey = profilsettingswriteytextbox.text()
            kaydedilecekwritewidth = profilsettingswritewidthtextbox.text()
            kaydedilecekwriteheight = profilsettingswriteheighttextbox.text()
            kaydedilecektexteditbackgroundcolor = profilsettingstexteditbackgroundcolortextbox.text()
            kaydedilecektexteditlabelcolor = profilsettingstexteditlabelcolortextbox.text()
            kaydedilecektextedittextcolor = profilsettingstextedittextcolortextbox.text()
            kaydedilecektexteditfontsize = profilsettingstexteditfontsizetextbox.text()
            kaydedilecektexteditapi = profilsettingstexteditapitextbox.text()
            kaydedilecektexteditbackgroundopacity = profilsettingstexteditbackgroundopacitycombobox.currentText()
            kaydedilecektexteditaranacakdil = profilsettingstextedittranslatetaranacakdilcombobox.currentText()
            kaydedilecektexteditfont = profilsettingstexteditfontcombobox.currentText()
            kaydedilecektextedittranslator = profilsettingstextedittranslatorkimcombobox.currentText()
            kaydedilecektextedithedefdil = profilsettingstextedittranslatehedefdilcombobox.currentText()

            # Dosya yolunu oluştur
            dosya_yolu = os.path.join(profilesi_folder, kaydedilecekprofilname + ".txt")

            dosya = open(dosya_yolu, "w", encoding="utf-8")
            dosya.write(kaydedilecekprofilname + "\n")
            dosya.write(kaydedilecekscanx + "\n")
            dosya.write(kaydedilecekscany + "\n")
            dosya.write(kaydedilecekscanwidth + "\n")
            dosya.write(kaydedilecekscanheight + "\n")
            dosya.write(kaydedilecekwritex + "\n")
            dosya.write(kaydedilecekwritey + "\n")
            dosya.write(kaydedilecekwritewidth + "\n")
            dosya.write(kaydedilecekwriteheight + "\n")
            dosya.write(kaydedilecektexteditbackgroundcolor + "\n")
            dosya.write(kaydedilecektexteditlabelcolor + "\n")
            dosya.write(kaydedilecektextedittextcolor + "\n")
            dosya.write(kaydedilecektexteditfontsize + "\n")
            dosya.write(kaydedilecektexteditapi + "\n")
            dosya.write(kaydedilecektexteditbackgroundopacity + "\n")
            dosya.write(kaydedilecektexteditaranacakdil + "\n")
            dosya.write(kaydedilecektexteditfont + "\n")
            dosya.write(kaydedilecektextedittranslator + "\n")
            dosya.write(kaydedilecektextedithedefdil + "\n")
            dosya.close()

            dosyalar1 = os.listdir(profilesi_folder)
            anamenuprofilsecimicombobox.clear()
            anamenuprofilsecimicombobox.addItems(dosyalar1)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
            msg.setWindowTitle("Warning")  # Pencere başlığı
            msg.setText("Succesfuly saved.")  # Ana mesaj
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
            msg.exec()  # Mesaj kutusunu göster

            anamenuduzeni()

    elif randomdeger71 == "DeepL Pro":
        if randomdeger72 == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
            msg.setWindowTitle("Warning")  # Pencere başlığı
            msg.setText("If you want to use DeepL you have to enter the API")  # Ana mesaj
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
            msg.exec()  # Mesaj kutusunu göster

        else:
            kaydedilecekprofilname = profilsettingsprofilenamemenuprofilnametextbox.text()
            kaydedilecekscanx = profilsettingsscanxtextbox.text()
            kaydedilecekscany = profilsettingsscanytextbox.text()
            kaydedilecekscanwidth = profilsettingsscanwidthtextbox.text()
            kaydedilecekscanheight = profilsettingsscanheighttextbox.text()
            kaydedilecekwritex = profilsettingswritextextbox.text()
            kaydedilecekwritey = profilsettingswriteytextbox.text()
            kaydedilecekwritewidth = profilsettingswritewidthtextbox.text()
            kaydedilecekwriteheight = profilsettingswriteheighttextbox.text()
            kaydedilecektexteditbackgroundcolor = profilsettingstexteditbackgroundcolortextbox.text()
            kaydedilecektexteditlabelcolor = profilsettingstexteditlabelcolortextbox.text()
            kaydedilecektextedittextcolor = profilsettingstextedittextcolortextbox.text()
            kaydedilecektexteditfontsize = profilsettingstexteditfontsizetextbox.text()
            kaydedilecektexteditapi = profilsettingstexteditapitextbox.text()
            kaydedilecektexteditbackgroundopacity = profilsettingstexteditbackgroundopacitycombobox.currentText()
            kaydedilecektexteditaranacakdil = profilsettingstextedittranslatetaranacakdilcombobox.currentText()
            kaydedilecektexteditfont = profilsettingstexteditfontcombobox.currentText()
            kaydedilecektextedittranslator = profilsettingstextedittranslatorkimcombobox.currentText()
            kaydedilecektextedithedefdil = profilsettingstextedittranslatehedefdilcombobox.currentText()

            # Dosya yolunu oluştur
            dosya_yolu = os.path.join(profilesi_folder, kaydedilecekprofilname + ".txt")

            dosya = open(dosya_yolu, "w", encoding="utf-8")
            dosya.write(kaydedilecekprofilname + "\n")
            dosya.write(kaydedilecekscanx + "\n")
            dosya.write(kaydedilecekscany + "\n")
            dosya.write(kaydedilecekscanwidth + "\n")
            dosya.write(kaydedilecekscanheight + "\n")
            dosya.write(kaydedilecekwritex + "\n")
            dosya.write(kaydedilecekwritey + "\n")
            dosya.write(kaydedilecekwritewidth + "\n")
            dosya.write(kaydedilecekwriteheight + "\n")
            dosya.write(kaydedilecektexteditbackgroundcolor + "\n")
            dosya.write(kaydedilecektexteditlabelcolor + "\n")
            dosya.write(kaydedilecektextedittextcolor + "\n")
            dosya.write(kaydedilecektexteditfontsize + "\n")
            dosya.write(kaydedilecektexteditapi + "\n")
            dosya.write(kaydedilecektexteditbackgroundopacity + "\n")
            dosya.write(kaydedilecektexteditaranacakdil + "\n")
            dosya.write(kaydedilecektexteditfont + "\n")
            dosya.write(kaydedilecektextedittranslator + "\n")
            dosya.write(kaydedilecektextedithedefdil + "\n")
            dosya.close()

            dosyalar1 = os.listdir(profilesi_folder)
            anamenuprofilsecimicombobox.clear()
            anamenuprofilsecimicombobox.addItems(dosyalar1)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
            msg.setWindowTitle("Warning")  # Pencere başlığı
            msg.setText("Succesfuly saved.")  # Ana mesaj
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
            msg.exec()  # Mesaj kutusunu göster

            anamenuduzeni()
    
    else:
        kaydedilecekprofilname = profilsettingsprofilenamemenuprofilnametextbox.text()
        kaydedilecekscanx = profilsettingsscanxtextbox.text()
        kaydedilecekscany = profilsettingsscanytextbox.text()
        kaydedilecekscanwidth = profilsettingsscanwidthtextbox.text()
        kaydedilecekscanheight = profilsettingsscanheighttextbox.text()
        kaydedilecekwritex = profilsettingswritextextbox.text()
        kaydedilecekwritey = profilsettingswriteytextbox.text()
        kaydedilecekwritewidth = profilsettingswritewidthtextbox.text()
        kaydedilecekwriteheight = profilsettingswriteheighttextbox.text()
        kaydedilecektexteditbackgroundcolor = profilsettingstexteditbackgroundcolortextbox.text()
        kaydedilecektexteditlabelcolor = profilsettingstexteditlabelcolortextbox.text()
        kaydedilecektextedittextcolor = profilsettingstextedittextcolortextbox.text()
        kaydedilecektexteditfontsize = profilsettingstexteditfontsizetextbox.text()
        kaydedilecektexteditapi = ""
        kaydedilecektexteditbackgroundopacity = profilsettingstexteditbackgroundopacitycombobox.currentText()
        kaydedilecektexteditaranacakdil = profilsettingstextedittranslatetaranacakdilcombobox.currentText()
        kaydedilecektexteditfont = profilsettingstexteditfontcombobox.currentText()
        kaydedilecektextedittranslator = ""
        kaydedilecektextedithedefdil = profilsettingstextedittranslatehedefdilcombobox.currentText()

        # Dosya yolunu oluştur
        dosya_yolu = os.path.join(profilesi_folder, kaydedilecekprofilname + ".txt")

        dosya = open(dosya_yolu, "w", encoding="utf-8")
        dosya.write(kaydedilecekprofilname + "\n")
        dosya.write(kaydedilecekscanx + "\n")
        dosya.write(kaydedilecekscany + "\n")
        dosya.write(kaydedilecekscanwidth + "\n")
        dosya.write(kaydedilecekscanheight + "\n")
        dosya.write(kaydedilecekwritex + "\n")
        dosya.write(kaydedilecekwritey + "\n")
        dosya.write(kaydedilecekwritewidth + "\n")
        dosya.write(kaydedilecekwriteheight + "\n")
        dosya.write(kaydedilecektexteditbackgroundcolor + "\n")
        dosya.write(kaydedilecektexteditlabelcolor + "\n")
        dosya.write(kaydedilecektextedittextcolor + "\n")
        dosya.write(kaydedilecektexteditfontsize + "\n")
        dosya.write(kaydedilecektexteditapi + "\n")
        dosya.write(kaydedilecektexteditbackgroundopacity + "\n")
        dosya.write(kaydedilecektexteditaranacakdil + "\n")
        dosya.write(kaydedilecektexteditfont + "\n")
        dosya.write(kaydedilecektextedittranslator + "\n")
        dosya.write(kaydedilecektextedithedefdil + "\n")
        dosya.close()

        dosyalar1 = os.listdir(profilesi_folder)
        anamenuprofilsecimicombobox.clear()
        anamenuprofilsecimicombobox.addItems(dosyalar1)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("Succesfuly saved.")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

        anamenuduzeni()

def anamenueditprofilebuttontiklandi():
    mevcut_profile = anamenuprofilsecimicombobox.currentText()

    # Okunacak dosyanın yolunu oluştur (örnek olarak "kullanici1.txt")
    profile_file_path = os.path.join(profilesi_folder, mevcut_profile)

    # Dosyayı oku ve satırları liste olarak al
    with open(profile_file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]

    alinacakprofilname = lines[0]
    alinacakscanx = lines[1]
    alinacakscany = lines[2]
    alinacakscanwidth = lines[3]
    alinacakscanheight = lines[4]
    alinacakwritex = lines[5]
    alinacakwritey = lines[6]
    alinacakwritewidth = lines[7]
    alinacakwriteheight = lines[8]
    alinacaktexteditbackgroundcolor = lines[9]
    alinacaktexteditlabelcolor = lines[10]
    alinacaktextedittextcolor = lines[11]
    alinacaktexteditfontsize = lines[12]
    alinacaktexteditapi = lines[13]
    alinacaktexteditbackgroundopacity = lines[14]
    alinacaktexteditaranacakdil = lines[15]
    alinacaktexteditfont = lines[16]
    alinacaktextedittranslator = lines[17]
    alinacaktextedithedefdil = lines[18]

    profilsettingsprofilenamemenuprofilnametextbox.setText(alinacakprofilname)
    profilsettingsscanxtextbox.setText(alinacakscanx)
    profilsettingsscanytextbox.setText(alinacakscany)
    profilsettingsscanwidthtextbox.setText(alinacakscanwidth)
    profilsettingsscanheighttextbox.setText(alinacakscanheight)
    profilsettingswritextextbox.setText(alinacakwritex)
    profilsettingswriteytextbox.setText(alinacakwritey)
    profilsettingswritewidthtextbox.setText(alinacakwritewidth)
    profilsettingswriteheighttextbox.setText(alinacakwriteheight)
    profilsettingstexteditbackgroundcolortextbox.setText(alinacaktexteditbackgroundcolor)
    profilsettingstexteditlabelcolortextbox.setText(alinacaktexteditlabelcolor)
    profilsettingstextedittextcolortextbox.setText(alinacaktextedittextcolor)
    profilsettingstexteditfontsizetextbox.setText(alinacaktexteditfontsize)
    profilsettingstexteditapitextbox.setText(alinacaktexteditapi)

    randomdeger16 = profilsettingstexteditbackgroundopacitycombobox.findText(alinacaktexteditbackgroundopacity)
    profilsettingstexteditbackgroundopacitycombobox.setCurrentIndex(randomdeger16)

    randomdeger17 = profilsettingstextedittranslatetaranacakdilcombobox.findText(alinacaktexteditaranacakdil)
    profilsettingstextedittranslatetaranacakdilcombobox.setCurrentIndex(randomdeger17)

    randomdeger18 = profilsettingstexteditfontcombobox.findText(alinacaktexteditfont)
    profilsettingstexteditfontcombobox.setCurrentIndex(randomdeger18)

    randomdeger20 = profilsettingstextedittranslatehedefdilcombobox.findText(alinacaktextedithedefdil)
    profilsettingstextedittranslatehedefdilcombobox.setCurrentIndex(randomdeger20)

    randomdeger75 = profilsettingstextedittranslatorkimcombobox.findText(alinacaktextedittranslator)
    profilsettingstextedittranslatorkimcombobox.setCurrentIndex(randomdeger75)

    profilesettingsprofilenamemenuduzeni()

def starttiklandi():
    global topwindow, topwindowscanx, topwindowscany, topwindowscanwidth, topwindowscanheight, topwindowaranacakdil, topwindowhedefdil, cevirilenmetinlabel, okunandil, ocrdili, targetdil, timer, topwindowwritewidth, topwindowwriteheight, topwindowtranslator, topwindowapi
    
    mevcut_profile = anamenuprofilsecimicombobox.currentText()

    if mevcut_profile == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("Please select a profile")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    else:
        # Okunacak dosyanın yolunu oluştur (örnek olarak "kullanici1.txt")
        profile_file_path = os.path.join(profilesi_folder, mevcut_profile)

        # Dosyayı oku ve satırları liste olarak al
        with open(profile_file_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        topwindowprofilname = lines[0]
        topwindowscanx = lines[1]
        topwindowscany = lines[2]
        topwindowscanwidth = lines[3]
        topwindowscanheight = lines[4]
        topwindowwritex = lines[5]
        topwindowwritey = lines[6]
        topwindowwritewidth = lines[7]
        topwindowwriteheight = lines[8]
        topwindowbackgroundcolor = lines[9]
        topwindowlabelcolor = lines[10]
        topwindowtextcolor = lines[11]
        topwindowfontsize = lines[12]
        topwindowapi = lines[13]
        topwindowbackgroundopacity = lines[14]
        topwindowaranacakdil = lines[15]
        topwindowtextfont = lines[16]
        topwindowtranslator = lines[17]
        topwindowhedefdil = lines[18]

        topwindow = QWidget()
        topwindow.setWindowTitle("Translator")
        topwindow.setGeometry(int(topwindowwritex), int(topwindowwritey), int(topwindowwritewidth), int(topwindowwriteheight))
        # Mevcut bayrakları al ve yeni bayrakları ekle
        topwindow.setWindowFlags(topwindow.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        if topwindowbackgroundopacity == "Translucent":
            # Pencereyi saydam yapma (arka plan saydam)
            topwindow.setAttribute(Qt.WA_TranslucentBackground)
        else:
            # Tamamen opak yapma
            topwindow.setWindowOpacity(1)  # 1 => tamamen opak
        try:
            topwindow.setStyleSheet("background-color: " + topwindowbackgroundcolor + ";")
        except:
            topwindow.setStyleSheet("background-color: white;")
            print("Ayarlanan Background Color da bir sıkıntı var Background Color White olarak ayarlandı")
    

        cevirilenmetinlabel = QLabel("Hello", topwindow)
        cevirilenmetinlabel.adjustSize()
        # QLabel'ı ortalamak için konum hesaplama
        x_pos = (int(topwindowwritewidth) - cevirilenmetinlabel.width()) // 2
        y_pos = (int(topwindowwriteheight) - cevirilenmetinlabel.height()) // 2

        # QLabel'ı yeni konumda hareket ettir
        cevirilenmetinlabel.move(x_pos, y_pos)

        try:
            cevirilenmetinlabel.setStyleSheet("""
            QLabel {
                background-color: """ + topwindowlabelcolor + """;
                color: """ + topwindowtextcolor + """;
                font-size: """ + topwindowfontsize + """px;
                font-family: """ + topwindowtextfont + """;
                padding: 10px;
                border-radius: 15px;
            }
            """)
        except:
            cevirilenmetinlabel.setStyleSheet("""
            QLabel {
                background-color: black;  # Arka plan rengi (mavi)
                color: white;               # Yazı rengi (beyaz)
                font-size: 18px;            # Yazı boyutu
                font-family: 'Arial'; # Yazı tipi
                padding: 10px;              # Kenar boşlukları (label'ın içinde)
                border-radius: 15px;        # Köşe yuvarlama (15px)
            }
            """)

        topwindow.show()

        if topwindowaranacakdil == "German":
            ocrdili = "deu"
        elif topwindowaranacakdil == "Arabic":
            ocrdili = "ara"
        elif topwindowaranacakdil == "Bulgarian":
            ocrdili = "bul"
        elif topwindowaranacakdil == "Czech":
            ocrdili = "ces"
        elif topwindowaranacakdil == "Chinese":
            ocrdili = "chi_sim"  # Chinese Simplified
        elif topwindowaranacakdil == "Danish":
            ocrdili = "dan"
        elif topwindowaranacakdil == "Indonesian":
            ocrdili = "ind"
        elif topwindowaranacakdil == "Estonian":
            ocrdili = "est"
        elif topwindowaranacakdil == "Dutch":
            ocrdili = "nld"
        elif topwindowaranacakdil == "Finnish":
            ocrdili = "fin"
        elif topwindowaranacakdil == "French":
            ocrdili = "fra"
        elif topwindowaranacakdil == "English":
            ocrdili = "eng"
        elif topwindowaranacakdil == "Spanish":
            ocrdili = "spa"
        elif topwindowaranacakdil == "Swedish":
            ocrdili = "swe"
        elif topwindowaranacakdil == "Italian":
            ocrdili = "ita"
        elif topwindowaranacakdil == "Japanese":
            ocrdili = "jpn"
        elif topwindowaranacakdil == "Korean":
            ocrdili = "kor"
        elif topwindowaranacakdil == "Polish":
            ocrdili = "pol"
        elif topwindowaranacakdil == "Latvian":
            ocrdili = "lav"
        elif topwindowaranacakdil == "Lithuanian":
            ocrdili = "lit"
        elif topwindowaranacakdil == "Hungarian":
            ocrdili = "hun"
        elif topwindowaranacakdil == "Norwegian":
            ocrdili = "nor"
        elif topwindowaranacakdil == "Portuguese":
            ocrdili = "por"
        elif topwindowaranacakdil == "Romanian":
            ocrdili = "ron"
        elif topwindowaranacakdil == "Russian":
            ocrdili = "rus"
        elif topwindowaranacakdil == "Slovak":
            ocrdili = "slk"
        elif topwindowaranacakdil == "Slovenian":
            ocrdili = "slv"
        elif topwindowaranacakdil == "Turkish":
            ocrdili = "tur"
        elif topwindowaranacakdil == "Ukrainian":
            ocrdili = "ukr"
        elif topwindowaranacakdil == "Greek":
            ocrdili = "ell"
        else:
            ocrdili = "eng"

        if topwindowaranacakdil == "German":
            okunandil = "de"
        elif topwindowaranacakdil == "Arabic":
            okunandil = "ar"
        elif topwindowaranacakdil == "Bulgarian":
            okunandil = "bg"
        elif topwindowaranacakdil == "Czech":
            okunandil = "cs"
        elif topwindowaranacakdil == "Chinese":
            okunandil = "zh-cn"
        elif topwindowaranacakdil == "Danish":
            okunandil = "da"
        elif topwindowaranacakdil == "Indonesian":
            okunandil = "id"
        elif topwindowaranacakdil == "Estonian":
            okunandil = "et"
        elif topwindowaranacakdil == "Dutch":
            okunandil = "nl"
        elif topwindowaranacakdil == "Finnish":
            okunandil = "fi"
        elif topwindowaranacakdil == "French":
            okunandil = "fr"
        elif topwindowaranacakdil == "English":
            okunandil = "en"
        elif topwindowaranacakdil == "Spanish":
            okunandil = "es"
        elif topwindowaranacakdil == "Swedish":
            okunandil = "sv"
        elif topwindowaranacakdil == "Italian":
            okunandil = "it"
        elif topwindowaranacakdil == "Japanese":
            okunandil = "ja"
        elif topwindowaranacakdil == "Korean":
            okunandil = "ko"
        elif topwindowaranacakdil == "Polish":
            okunandil = "pl"
        elif topwindowaranacakdil == "Latvian":
            okunandil = "lv"
        elif topwindowaranacakdil == "Lithuanian":
            okunandil = "lt"
        elif topwindowaranacakdil == "Hungarian":
            okunandil = "hu"
        elif topwindowaranacakdil == "Norwegian":
            okunandil = "no"
        elif topwindowaranacakdil == "Portuguese":
            okunandil = "pt"
        elif topwindowaranacakdil == "Romanian":
            okunandil = "ro"
        elif topwindowaranacakdil == "Russian":
            okunandil = "ru"
        elif topwindowaranacakdil == "Slovak":
            okunandil = "sk"
        elif topwindowaranacakdil == "Slovenian":
            okunandil = "sl"
        elif topwindowaranacakdil == "Turkish":
            okunandil = "tr"
        elif topwindowaranacakdil == "Ukrainian":
            okunandil = "uk"
        elif topwindowaranacakdil == "Greek":
            okunandil = "el"
        else:
            okunandil = "en"

        if topwindowhedefdil == "German":
            targetdil = "de"
        elif topwindowhedefdil == "Arabic":
            targetdil = "ar"
        elif topwindowhedefdil == "Bulgarian":
            targetdil = "bg"
        elif topwindowhedefdil == "Czech":
            targetdil = "cs"
        elif topwindowhedefdil == "Chinese":
            targetdil = "zh"
        elif topwindowhedefdil == "Danish":
            targetdil = "da"
        elif topwindowhedefdil == "Indonesian":
            targetdil = "id"
        elif topwindowhedefdil == "Estonian":
            targetdil = "et"
        elif topwindowhedefdil == "Dutch":
            targetdil = "nl"
        elif topwindowhedefdil == "Finnish":
            targetdil = "fi"
        elif topwindowhedefdil == "French":
            targetdil = "fr"
        elif topwindowhedefdil == "English":
            targetdil = "en"
        elif topwindowhedefdil == "Spanish":
            targetdil = "es"
        elif topwindowhedefdil == "Swedish":
            targetdil = "sv"
        elif topwindowhedefdil == "Italian":
            targetdil = "it"
        elif topwindowhedefdil == "Japanese":
            targetdil = "ja"
        elif topwindowhedefdil == "Korean":
            targetdil = "ko"
        elif topwindowhedefdil == "Polish":
            targetdil = "pl"
        elif topwindowhedefdil == "Latvian":
            targetdil = "lv"
        elif topwindowhedefdil == "Lithuanian":
            targetdil = "lt"
        elif topwindowhedefdil == "Hungarian":
            targetdil = "hu"
        elif topwindowhedefdil == "Norwegian":
            targetdil = "no"
        elif topwindowhedefdil == "Portuguese":
            targetdil = "pt"
        elif topwindowhedefdil == "Romanian":
            targetdil = "ro"
        elif topwindowhedefdil == "Russian":
            targetdil = "ru"
        elif topwindowhedefdil == "Slovak":
            targetdil = "sk"
        elif topwindowhedefdil == "Slovenian":
            targetdil = "sl"
        elif topwindowhedefdil == "Turkish":
            targetdil = "tr"
        elif topwindowhedefdil == "Ukrainian":
            targetdil = "uk"
        elif topwindowhedefdil == "Greek":
            targetdil = "el"
        else:
            targetdil = "deu"

        # Timer oluştur
        timer = QTimer()

        # Her tetiklenmede yazdir fonksiyonunu çalıştır
        timer.timeout.connect(cevirifonksiyonu)

        # Timer’ı başlat (1000 ms = 1 saniye)
        timer.start(500)
    

def cevirifonksiyonu():
    global eskimetin, url, labeltemizlemesayaci
    # Ekran görüntüsünü al
    screenshot = pyautogui.screenshot(region=(int(topwindowscanx), int(topwindowscany), int(topwindowscanwidth), int(topwindowscanheight)))

    # Görseldeki yazıyı tanı
    text = pytesseract.image_to_string(screenshot, lang=ocrdili)  # "tur" yazarsan Türkçe OCR yapar
    text = text.replace("\n", " ")

    print(f"🧠 OCR ile alınan metin: {text}")
    if text:
        try:
            if text == eskimetin:
                print("Eski metin bu")
                cevirilenmetinlabel.show()
            else:
                if topwindowtranslator == "DeepL Free":
                    url = "https://api-free.deepl.com/v2/translate"  # Pro kullanıcıysan: "https://api.deepl.com/v2/translate"

                    data = {
                        "auth_key": topwindowapi,
                        "text": text,
                        "target_lang": targetdil
                    }

                    
                    response = requests.post(url, data=data)
                    response.raise_for_status()  # HTTP 4xx/5xx hataları için istisna fırlatır

                    result = response.json()
                    translated_text = result["translations"][0]["text"]
                    
                    yazdirilacakmetin = translated_text
                    cevirilenmetinlabel.setText(yazdirilacakmetin)
                    cevirilenmetinlabel.adjustSize()
                    cevirilenmetinlabel.show()
                    # QLabel'ı ortalamak için konum hesaplama
                    x_pos = (int(topwindowwritewidth) - cevirilenmetinlabel.width()) // 2
                    y_pos = (int(topwindowwriteheight) - cevirilenmetinlabel.height()) // 2

                    # QLabel'ı yeni konumda hareket ettir
                    cevirilenmetinlabel.move(x_pos, y_pos)
                    eskimetin = text
                    labeltemizlemesayaci = 0

                elif topwindowtranslator == "DeepL Pro":
                    url = "https://api.deepl.com/v2/translate"  # Pro kullanıcıysan: "https://api.deepl.com/v2/translate"

                    data = {
                        "auth_key": topwindowapi,
                        "text": text,
                        "target_lang": targetdil
                    }

                    
                    response = requests.post(url, data=data)
                    response.raise_for_status()  # HTTP 4xx/5xx hataları için istisna fırlatır

                    result = response.json()
                    translated_text = result["translations"][0]["text"]
                    
                    yazdirilacakmetin = translated_text
                    cevirilenmetinlabel.setText(yazdirilacakmetin)
                    cevirilenmetinlabel.adjustSize()
                    cevirilenmetinlabel.show()
                    # QLabel'ı ortalamak için konum hesaplama
                    x_pos = (int(topwindowwritewidth) - cevirilenmetinlabel.width()) // 2
                    y_pos = (int(topwindowwriteheight) - cevirilenmetinlabel.height()) // 2

                    # QLabel'ı yeni konumda hareket ettir
                    cevirilenmetinlabel.move(x_pos, y_pos)
                    eskimetin = text
                    labeltemizlemesayaci = 0


                else:
                    url = "http://libretranslate.screentranslator.online:5000/translate"
                    data = {
                        "q": text,
                        "source": okunandil,
                        "target": targetdil,
                        "format": "text"
                    }
            
                    response = requests.post(url, json=data)
            
                    if response.status_code == 200:
                        translated = response.json()['translatedText']
                    else:
                        print("Hata oluştu:", response.status_code, response.text)

                    yazdirilacakmetin = translated
                    cevirilenmetinlabel.setText(yazdirilacakmetin)
                    cevirilenmetinlabel.adjustSize()
                    cevirilenmetinlabel.show()
                    # QLabel'ı ortalamak için konum hesaplama
                    x_pos = (int(topwindowwritewidth) - cevirilenmetinlabel.width()) // 2
                    y_pos = (int(topwindowwriteheight) - cevirilenmetinlabel.height()) // 2

                    # QLabel'ı yeni konumda hareket ettir
                    cevirilenmetinlabel.move(x_pos, y_pos)
                    eskimetin = text
                    labeltemizlemesayaci = 0

        except Exception as e:
            print(f"🚨 Translate Eror: {e}")
            cevirilenmetinlabel.setText(f"Translate Eror: {e}")
            cevirilenmetinlabel.adjustSize()
            # QLabel'ı ortalamak için konum hesaplama
            x_pos = (int(topwindowwritewidth) - cevirilenmetinlabel.width()) // 2
            y_pos = (int(topwindowwriteheight) - cevirilenmetinlabel.height()) // 2

            # QLabel'ı yeni konumda hareket ettir
            cevirilenmetinlabel.move(x_pos, y_pos)

    else:
        labeltemizlemesayaci = labeltemizlemesayaci + 1
        if (labeltemizlemesayaci > 8):
            cevirilenmetinlabel.setText("")
            cevirilenmetinlabel.adjustSize()
            cevirilenmetinlabel.hide()

def anamenustopbuttontiklandi():
    global timer, topwindow, topwindowacikmi
    if topwindowacikmi == False:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("The application has already been stopped")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster
    else:
        topwindowacikmi = False
        timer.stop()
        topwindow.close()

def starttiklandikontrol():
    global topwindowacikmi
    if topwindowacikmi == True:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Uyarı ikonu
        msg.setWindowTitle("Warning")  # Pencere başlığı
        msg.setText("The application has already been launched")  # Ana mesaj
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Tamam butonu
        msg.exec()  # Mesaj kutusunu göster

    else:
        topwindowacikmi = True
        starttiklandi()

# 2
anamenunewprofilebutton.clicked.connect(anamenunewprofilebuttontiklandi)
anamenueditprofilebutton.clicked.connect(anamenueditprofilebuttontiklandi)
anamenustartbutton.clicked.connect(starttiklandikontrol)
anamenustopbutton.clicked.connect(anamenustopbuttontiklandi)

# 3 
profilsettingsprofilenamemenunextbutton.clicked.connect(profilsettingsprofilenamemenunextbuttontiklandi)
profilsettingsprofilenamemenubackbutton.clicked.connect(anamenuduzeni)

#4
profilsettingsscansetbutton.clicked.connect(profilsettingsscansetbuttontiklandi)
profilsettingsscannextbutton.clicked.connect(profilsettingsscannextbuttontiklandi)
profilsettingsscanbackbutton.clicked.connect(profilesettingsprofilenamemenuduzeni)

#5
profilsettingswritesetbutton.clicked.connect(profilsettingswritesetbuttontiklandi)
profilsettingswritenextbutton.clicked.connect(profilsettingswritenextbuttontiklandi)
profilsettingswritebackbutton.clicked.connect(profilesettingsscanmenuduzeni)

#6
profilsettingstextedittestbutton.clicked.connect(profilsettingstextedittesttiklandi)
profilsettingstexteditsavebutton.clicked.connect(profilsettingstexteditsavebuttontiklandi)
profilsettingstexteditbackbutton.clicked.connect(profilesettingswritemenuduzeni)

anamenuduzeni()

pencere.show()
sys.exit(app.exec_())