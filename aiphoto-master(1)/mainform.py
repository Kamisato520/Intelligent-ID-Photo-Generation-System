from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextOption
from PyQt5.QtWidgets import *
import pymysql
import re
import csv
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
from main import deal
from PIL import Image
from MakupGUI import Ui_MainWindow

class user_mainWindow(QWidget):
    def __init__(self):
        super(user_mainWindow, self).__init__()
        self.setWindowTitle("C++程序设计实验课-智能证件照生成系统-吴迪-张启淞-陈则宇")
        self.resize(1920,1080)  # 设置窗体大小1920, 1080
        self.setStyleSheet("background-color:#F6F6F6")
        self.sourcefile_path = ""
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.color = "white"
        self.size_width = 1920
        self.size_height = 1080
        self.size3 = 10

        pic3 = QLabel(self)
        pic3.setGeometry(213, -123, 1500, 350)
        pic3.setStyleSheet("border-image:url(pic3.PNG)")

        pic2 = QLabel(self)
        pic2.setGeometry(200, 230, 900, 550)
        pic2.setStyleSheet("border-image:url(pic2.png)")

        pic4 = QLabel(self)
        pic4.setGeometry(1080, 230, 610, 550)
        pic4.setStyleSheet("border-image:url(pic4.jpg)")

        line2 = QLabel(self)
        line2.setGeometry(227, 780, 1450, 300)
        line2.setStyleSheet("border-image:url(pic1.png)")

        self.last_label = QLabel(self)

        self.white_select = QPushButton(self)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.white_select.setFont(font)
        self.white_select.setGeometry(1200, 290, 70, 70)
        self.white_select.setStyleSheet("border:1px solid black;background-color:white")
        self.white_select.clicked.connect(self.click_white)

        self.red_select = QPushButton(self)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.red_select.setFont(font)
        self.red_select.setGeometry(1375, 290, 70, 70)
        self.red_select.setStyleSheet("background-color:red")
        self.red_select.clicked.connect(self.click_red)

        self.blue_select = QPushButton(self)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.blue_select.setFont(font)
        self.blue_select.setGeometry(1550, 290, 70, 70)
        self.blue_select.setStyleSheet("background-color:blue")
        self.blue_select.clicked.connect(self.click_blue)

        self.size_select1 = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.size_select1.setFont(font)
        self.size_select1.setGeometry(1200, 380, 450, 50)
        self.size_select1.setStyleSheet("background-color:white")
        self.size_select1.setText("一寸    25*35mm  295*413px")
        self.size_select1.setChecked(True)
        self.size_select1.clicked.connect(self.click1)

        self.size_select2 = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.size_select2.setFont(font)
        self.size_select2.setGeometry(1200, 435, 450, 50)
        self.size_select2.setStyleSheet("background-color:white")
        self.size_select2.setText("大一寸  33*48mm  390*566px")
        self.size_select2.clicked.connect(self.click2)

        self.size_select3 = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.size_select3.setFont(font)
        self.size_select3.setGeometry(1200, 490, 450, 50)
        self.size_select3.setStyleSheet("background-color:white")
        self.size_select3.setText("小二寸  35*45mm  413*531px")
        self.size_select3.clicked.connect(self.click3)

        self.size_select4 = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.size_select4.setFont(font)
        self.size_select4.setGeometry(1200, 545, 450, 50)
        self.size_select4.setStyleSheet("background-color:white")
        self.size_select4.setText("二寸    35*49mm  413*579px")
        self.size_select4.clicked.connect(self.click4)

        self.size_select5 = QRadioButton(self)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.size_select5.setFont(font)
        self.size_select5.setGeometry(1200, 600, 450, 50)
        self.size_select5.setStyleSheet("background-color:white")
        self.size_select5.setText("大二寸  35*53mm  413*626px")
        self.size_select5.clicked.connect(self.click5)

        self.upload_pic = QPushButton(self)
        self.upload_pic.setGeometry(QtCore.QRect(1275, 10, 280, 110))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.upload_pic.setFont(font)
        self.upload_pic.setStyleSheet("border-image:url(upload.png)")
        self.upload_pic.clicked.connect(self.deal_pic)

        self.download_pic = QPushButton(self)
        self.download_pic.setGeometry(QtCore.QRect(1150, 670, 240, 75))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.download_pic.setFont(font)
        self.download_pic.setStyleSheet("border-image:url(download.png)")
        self.download_pic.clicked.connect(self.saveImage)
        
        self.beautiful = QPushButton(self)
        self.beautiful.setGeometry(QtCore.QRect(1460, 670, 240, 80))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        self.beautiful.setFont(font)
        self.beautiful.setStyleSheet("border-image:url(beautiful.png)")
        self.beautiful.clicked.connect(self.openMakeupGUI)
 



    def openMakeupGUI(self):
        self.makeup_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.makeup_window)
        self.makeup_window.show()

    def saveImage(self):
        img = Image.open("last.jpg")
        fdir, ftype = QFileDialog.getSaveFileName(self, "Save Image",
                                                  "./", "Image Files (*.jpg)")
        if fdir:
            img.save(fdir)
            QMessageBox.information(self, "提示", "保存成功", QMessageBox.Yes)
    def click_white(self):
        if self.sourcefile_path == "":
            QMessageBox.warning(self, "警告", "请先上传图片", QMessageBox.Yes)
        else:
            self.color = "white"
            deal(self.sourcefile_path, self.color, self.size_width, self.size_height, self.size3)
            self.last_label.setGeometry(589, 340, int(self.size_width / 2), int(self.size_height / 2))
            self.last_label.setStyleSheet("border-image:url(last.jpg)")

    def click_red(self):
        if self.sourcefile_path == "":
            QMessageBox.warning(self, "警告", "请先上传图片", QMessageBox.Yes)
        else:
            self.color = "red"
            deal(self.sourcefile_path, self.color, self.size_width, self.size_height, self.size3)
            self.last_label.setGeometry(589, 340, int(self.size_width / 2), int(self.size_height / 2))
            self.last_label.setStyleSheet("border-image:url(last.jpg)")

    def click_blue(self):
        if self.sourcefile_path == "":
            QMessageBox.warning(self, "警告", "请先上传图片", QMessageBox.Yes)
        else:
            self.color = "blue"
            deal(self.sourcefile_path, self.color, self.size_width, self.size_height, self.size3)
            self.last_label.setGeometry(589, 340, int(self.size_width / 2), int(self.size_height / 2))
            self.last_label.setStyleSheet("border-image:url(last.jpg)")

    def click1(self):
        if self.sourcefile_path == "":
            QMessageBox.warning(self, "警告", "请先上传图片", QMessageBox.Yes)
        else:
            self.size_width = 295
            self.size_height = 413
            self.size3 = 10
            deal(self.sourcefile_path, self.color, self.size_width, self.size_height, self.size3)
            self.last_label.setGeometry(600, 350, int(self.size_width / 2), int(self.size_height / 2))
            self.last_label.setStyleSheet("border-image:url(last.jpg)")

    def click2(self):
        if self.sourcefile_path == "":
            QMessageBox.warning(self, "警告", "请先上传图片", QMessageBox.Yes)
        else:
            self.size_width = 389
            self.size_height = 566
            self.size3 = 100
            deal(self.sourcefile_path, self.color, self.size_width, self.size_height, self.size3)
            self.last_label.setGeometry(589, 340, int(self.size_width / 2), int(self.size_height / 2))
            self.last_label.setStyleSheet("border-image:url(last.jpg)")

    def click3(self):
        if self.sourcefile_path == "":
            QMessageBox.warning(self, "警告", "请先上传图片", QMessageBox.Yes)
        else:
            self.size_width = 413
            self.size_height = 531
            self.size3 = 80
            deal(self.sourcefile_path, self.color, self.size_width, self.size_height, self.size3)
            self.last_label.setGeometry(587, 340, int(self.size_width / 2), int(self.size_height / 2))
            self.last_label.setStyleSheet("border-image:url(last.jpg)")

    def click4(self):
        if self.sourcefile_path == "":
            QMessageBox.warning(self, "警告", "请先上传图片", QMessageBox.Yes)
        else:
            self.size_width = 413
            self.size_height = 579
            self.size3 = 110
            deal(self.sourcefile_path, self.color, self.size_width, self.size_height, self.size3)
            self.last_label.setGeometry(587, 330, int(self.size_width / 2), int(self.size_height / 2))
            self.last_label.setStyleSheet("border-image:url(last.jpg)")

    def click5(self):
        if self.sourcefile_path == "":
            QMessageBox.warning(self, "警告", "请先上传图片", QMessageBox.Yes)
        else:
            self.size_width = 413
            self.size_height = 626
            self.size3 = 140
            deal(self.sourcefile_path, self.color, self.size_width, self.size_height, self.size3)
            self.last_label.setGeometry(600, 310, int(self.size_width / 2), int(self.size_height / 2))
            self.last_label.setStyleSheet("border-image:url(last.jpg)")

    def slot_btn_chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                self.cwd,  # 起始路径
                                                                "All Files (*)")  # 设置文件扩展名过滤,用双分号间隔  All Files (*);;

        if fileName_choose == "":
            return

        print("\n你选择的文件为:")
        print(fileName_choose)
        self.sourcefile_path = fileName_choose
        return fileName_choose

    def deal_pic(self):
        path = self.slot_btn_chooseFile()
        deal(path, self.color, self.size_width, self.size_height, self.size3)

        self.last_label.setGeometry(600, 350, int(295 / 2), int(413 / 2))
        self.last_label.setStyleSheet("border-image:url(last.jpg)")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainForm = user_mainWindow()
    mainForm.show()
    sys.exit(app.exec_())




