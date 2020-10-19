from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys, os
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PIL import Image

import braille_TF as TF

form_class1 = uic.loadUiType("main_window.ui")[0]
form_class2 = uic.loadUiType("img_input.ui")[0]
form_class3 = uic.loadUiType("result_window.ui")[0]
form_class4 = uic.loadUiType("img_output.ui")[0]

class MainWindow(QMainWindow, form_class1):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)
        self.pushButton_2.clicked.connect(self.button_clicked_2)

    def button_clicked(self):
        self.imageInput = ImageInput(self)
        self.imageInput.show()
    # 지현파트
    def button_clicked_2(self):
        self.myWindow = MyWindow(self)
        self.myWindow.show()

class ResultWindow(QMainWindow, form_class3):
    def __init__(self, parent=None):
        super(ResultWindow, self).__init__(parent)
        self.setupUi(self)
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(file_path)
        self.label.setPixmap(self.qPixmapFileVar)
        self.label_2.clear()
        # 판별 함수 불러옴
        self.label_2.setText(TF.action(file_path)) # 결과값 출력 file_path는 임시
        
class ImageInput(QMainWindow, form_class2):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        global file_path
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.newWindow = ResultWindow(self)

            self.newWindow.show()
            event.accept()


        else:
            event.ignore()

def return_file_path():
    return file_path

class MyWindow(QMainWindow, form_class4):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.reset)
        self.pushButton_2.clicked.connect(self.confirm)

    def confirm(self):
        self.lbl.clear()
        spell = self.textEdit.toPlainText()

        merged = Image.new('L', (100*len(spell), 120), 255)

        for i in range(0, len(spell)):

            if spell[i] == " ":
                im = Image.open("Braille_img/null_output_img.png")
            else:
                im = Image.open("Braille_img/" + spell[i] + "_output_img.png")

            merged.paste(im, (100 * i + 5, 5))

        size = (int(merged.width * 1.2), merged.height)
        new_merged = merged.resize(size=size)
        print(new_merged.size)
        new_merged.save('Braille_img_change.png')

        path = "Braille_img_change.png"
        pixmap = QPixmap(path)
        self.lbl.setPixmap(QPixmap(pixmap))


    def reset(self):
        self.textEdit.clear()
        self.lbl.clear()

app = QApplication(sys.argv)
mywindow = MainWindow()
mywindow.show()
print("a")
app.exec_()

print("b")
