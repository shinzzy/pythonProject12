import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import socket
import zipfile
import os
import sys
import pymysql
import webbrowser
import numpy as np
import shutil
import pyautogui as pg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import pandas as pd  # 데이터 프레임





conn = pymysql.connect(host='10.10.21.108', user='root', password='1234', db='clothes', charset='utf8')
cur = conn.cursor()

ui_form = uic.loadUiType("main.ui")[0]
ui_form2 = uic.loadUiType("graph.ui")[0]

class MainWindow(QMainWindow, ui_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.combobox()
        self.comboBox.activated.connect(self.combobox)
        self.pushButton.clicked.connect(self.goToStart)
        self.pushButton_graph.clicked.connect(self.goToGraph)
        self.search_btn.clicked.connect(self.search)
        self.next_btn.clicked.connect(self.Next)
        self.prev_btn.clicked.connect(self.Prev)
        self.doneSerach = False
        self.rank = 1

        self.Link_1 = ""
        self.Link_2 = ""
        self.Link_3 = ""
        self.Link_4 = ""

        self.mantoman = 0
        self.shirts = 5
        self.slacks = 15
        self.jeans = 10
        self.coats = 20
        self.paddings = 25

        # if self.doneSerach == False:
        #     pass
        # else:
        #     self.pushButton_link_1.clicked.connect(lambda: webbrowser.open(self.Link_1))
        #     self.pushButton_link_2.clicked.connect(lambda: webbrowser.open(self.Link_2))
        #     self.pushButton_link_3.clicked.connect(lambda: webbrowser.open(self.Link_3))

        self.pushButton_link_1.clicked.connect(lambda: webbrowser.open(self.Link_1))
        self.pushButton_link_2.clicked.connect(lambda: webbrowser.open(self.Link_2))
        self.pushButton_link_3.clicked.connect(lambda: webbrowser.open(self.Link_3))
        self.pushButton_link_4.clicked.connect(lambda: webbrowser.open(self.Link_4))

        g = QPixmap('./지마켓.png')
        st = QPixmap('./11번가.jpg')
        auc = QPixmap('./옥션.jpg')
        new = QPixmap('./신세계.png')

        self.labelFirst.setPixmap(st)
        self.labelSecond.setPixmap(g)
        self.labelThird.setPixmap(auc)
        self.labelFourth.setPixmap(new)




    ###############################################################
    ####################    압축파일 받아와서 풀기    ################
    ###############################################################
    def goToStart(self):
        HOST = '10.10.21.102'
        PORT = 5003
        ADDR = (HOST, PORT)
        BUFF_SIZE = 1024

        clientSocket = socket.socket()
        clientSocket.connect(ADDR)
        clientSocket.send('client message'.encode())
        with open('HI.zip', 'wb') as f:
            print('file opened')
            while True:
                print('receiving data...')
                data = clientSocket.recv(BUFF_SIZE)
                print('(data)', data)
                if not data:
                    break
                f.write(data)
        f.close()
        print('Successfully get the file')
        clientSocket.close()
        print('connection closed')
        zipfile.ZipFile('HI.zip').extractall('/home/aiot8/PycharmProjects/pythonProject12/HI')

        self.stackedWidget.setCurrentWidget(self.page)

    def combobox(self):
        first = self.comboBox.currentText()
        if first == "상의":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("맨투맨")
            self.comboBox_2.addItem("셔츠")
        elif first == "하의":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("청바지")
            self.comboBox_2.addItem("슬랙스")
        else:
            self.comboBox_2.clear()
            self.comboBox_2.addItem("코트")
            self.comboBox_2.addItem("패딩")

        self.shop_name_1.setText("11번가")
        self.shop_name_2.setText("G마켓")
        self.shop_name_3.setText("옥션")
        self.shop_name_4.setText("신세계TV쇼핑")

    def goToGraph(self):
        self.sh = GraphWindow()
        self.sh.show()
        self.hide()

    def search(self):
        self.Link_1 = ""
        self.Link_2 = ""
        self.Link_3 = ""
        self.Link_4 = ""

        self.doneSerach = True
        self.rank = 1
        self.label_top.setText(str(self.rank))
        keyWord = self.comboBox_2.currentText()
        kinds = ""
        if keyWord == "맨투맨" or keyWord == "셔츠":
            kinds = "shirts"
        elif keyWord == "청바지" or keyWord == "슬랙스":
            kinds = "pants"
        else :
            kinds = "outers"

        sql = 'select * from {} where top1to5 = 1 and category = "{}"'.format(kinds, keyWord)
        cur.execute(sql)
        result = cur.fetchall()

        self.name_1.setText(result[0][3])
        self.name_2.setText(result[1][3])
        self.name_3.setText(result[2][3])
        self.name_4.setText(result[3][3])


        self.price_1.setText(result[0][4])
        self.price_2.setText(result[1][4])
        self.price_3.setText(result[2][4])
        self.price_4.setText(result[3][4])

        self.review_1.setText(result[0][5])
        self.review_2.setText(result[1][5])
        self.review_3.setText(result[2][5])
        self.review_4.setText(result[3][5])

        self.Link_1 = result[0][6]
        self.Link_2 = result[1][6]
        self.Link_3 = result[2][6]
        self.Link_4 = result[3][6]

        ### 사진넣기 ###

        self.mantoman = 0
        self.shirts = 5
        self.slacks = 15
        self.jeans = 10
        self.coats = 20
        self.paddings = 25
        if keyWord == "맨투맨":
            pixmap1 = QPixmap('./HI/11번가_맨투맨{}.jpg'.format(self.mantoman))
            pixmap2 = QPixmap('./HI/G마켓_맨투맨{}.jpg'.format(self.mantoman))
            pixmap3 = QPixmap('./HI/옥션_맨투맨{}.jpg'.format(self.mantoman))
            pixmap4 = QPixmap('./HI/신세계_맨투맨{}.jpg'.format(self.mantoman))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)

        elif keyWord == "셔츠":


            pixmap1 = QPixmap('./HI/11번가_셔츠{}.jpg'.format(self.shirts))
            pixmap2 = QPixmap('./HI/G마켓_셔츠{}.jpg'.format(self.shirts))
            pixmap3 = QPixmap('./HI/옥션_셔츠{}.jpg'.format(self.shirts))
            pixmap4 = QPixmap('./HI/신세계_셔츠{}.jpg'.format(self.shirts))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)

        elif keyWord == "슬랙스":
            pixmap1 = QPixmap('./HI/11번가_슬랙스{}.jpg'.format(self.slacks))
            pixmap2 = QPixmap('./HI/G마켓_슬랙스{}.jpg'.format(self.slacks))
            pixmap3 = QPixmap('./HI/옥션_슬랙스{}.jpg'.format(self.slacks))
            pixmap4 = QPixmap('./HI/신세계_슬랙스{}.jpg'.format(self.slacks))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)

        elif keyWord == "청바지":
            pixmap1 = QPixmap('./HI/11번가_청바지{}.jpg'.format(self.jeans))
            pixmap2 = QPixmap('./HI/G마켓_청바지{}.jpg'.format(self.jeans))
            pixmap3 = QPixmap('./HI/옥션_청바지{}.jpg'.format(self.jeans))
            pixmap4 = QPixmap('./HI/신세계_청바지{}.jpg'.format(self.jeans))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)

        elif keyWord == "코트":
            pixmap1 = QPixmap('./HI/11번가_코트{}.jpg'.format(self.coats))
            pixmap2 = QPixmap('./HI/G마켓_코트{}.jpg'.format(self.coats))
            pixmap3 = QPixmap('./HI/옥션_코트{}.jpg'.format(self.coats))
            pixmap4 = QPixmap('./HI/신세계_코트{}.jpg'.format(self.coats))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)

        elif keyWord == "패딩":
            pixmap1 = QPixmap('./HI/11번가_패딩{}.jpg'.format(self.paddings))
            pixmap2 = QPixmap('./HI/G마켓_패딩{}.jpg'.format(self.paddings))
            pixmap3 = QPixmap('./HI/옥션_패딩{}.jpg'.format(self.paddings))
            pixmap4 = QPixmap('./HI/신세계_패딩{}.jpg'.format(self.paddings))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)



    def Next(self):
        if self.doneSerach == True:

            if self.rank <= 4:

                self.Link_1 = ""
                self.Link_2 = ""
                self.Link_3 = ""
                self.Link_4 = ""
                self.rank += 1
                self.label_top.setText(str(self.rank))

                keyWord = self.comboBox_2.currentText()
                kinds = ""
                if keyWord == "맨투맨" or keyWord == "셔츠":
                    kinds = "shirts"
                elif keyWord == "청바지" or keyWord == "슬랙스":
                    kinds = "pants"
                else :
                    kinds = "outers"
                sql = 'select * from {} where category = "{}" and top1to5 = {}'.format(kinds, keyWord, self.rank)
                cur.execute(sql)
                result = cur.fetchall()
                self.name_1.setText(result[0][3])
                self.name_2.setText(result[1][3])
                self.name_3.setText(result[2][3])
                self.name_4.setText(result[3][3])

                self.price_1.setText(result[0][4])
                self.price_2.setText(result[1][4])
                self.price_3.setText(result[2][4])
                self.price_4.setText(result[3][4])

                self.review_1.setText(result[0][5])
                self.review_2.setText(result[1][5])
                self.review_3.setText(result[2][5])
                self.review_4.setText(result[3][5])

                self.Link_1 = result[0][6]
                self.Link_2 = result[1][6]
                self.Link_3 = result[2][6]
                self.Link_4 = result[3][6]

                self.mantoman += 1
                self.shirts += 1
                self.jeans += 1
                self.slacks += 1
                self.coats += 1
                self.paddings += 1

                if keyWord == "맨투맨":
                    pixmap1 = QPixmap('./HI/11번가_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap2 = QPixmap('./HI/G마켓_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap3 = QPixmap('./HI/옥션_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap4 = QPixmap('./HI/신세계_맨투맨{}.jpg'.format(self.mantoman))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "셔츠":
                    pixmap1 = QPixmap('./HI/11번가_셔츠{}.jpg'.format(self.shirts))
                    pixmap2 = QPixmap('./HI/G마켓_셔츠{}.jpg'.format(self.shirts))
                    pixmap3 = QPixmap('./HI/옥션_셔츠{}.jpg'.format(self.shirts))
                    pixmap4 = QPixmap('./HI/신세계_셔츠{}.jpg'.format(self.shirts))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "청바지":
                    pixmap1 = QPixmap('./HI/11번가_청바지{}.jpg'.format(self.jeans))
                    pixmap2 = QPixmap('./HI/G마켓_청바지{}.jpg'.format(self.jeans))
                    pixmap3 = QPixmap('./HI/옥션_청바지{}.jpg'.format(self.jeans))
                    pixmap4 = QPixmap('./HI/신세계_청바지{}.jpg'.format(self.jeans))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)
                elif keyWord == "슬랙스":
                    pixmap1 = QPixmap('./HI/11번가_슬랙스{}.jpg'.format(self.slacks))
                    pixmap2 = QPixmap('./HI/G마켓_슬랙스{}.jpg'.format(self.slacks))
                    pixmap3 = QPixmap('./HI/옥션_슬랙스{}.jpg'.format(self.slacks))
                    pixmap4 = QPixmap('./HI/신세계_슬랙스{}.jpg'.format(self.slacks))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "코트":
                    pixmap1 = QPixmap('./HI/11번가_코트{}.jpg'.format(self.coats))
                    pixmap2 = QPixmap('./HI/G마켓_코트{}.jpg'.format(self.coats))
                    pixmap3 = QPixmap('./HI/옥션_코트{}.jpg'.format(self.coats))
                    pixmap4 = QPixmap('./HI/신세계_코트{}.jpg'.format(self.coats))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "패딩":
                    pixmap1 = QPixmap('./HI/11번가_패딩{}.jpg'.format(self.paddings))
                    pixmap2 = QPixmap('./HI/G마켓_패딩{}.jpg'.format(self.paddings))
                    pixmap3 = QPixmap('./HI/옥션_패딩{}.jpg'.format(self.paddings))
                    pixmap4 = QPixmap('./HI/신세계_패딩{}.jpg'.format(self.paddings))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)





            else:
                QMessageBox.information(self, "알림", "마지막페이지입니다.")
        else:
            pass

    def Prev(self):
        if self.doneSerach == True:
            if self.rank >= 2:

                self.Link_1 = ""
                self.Link_2 = ""
                self.Link_3 = ""
                self.Link_4 = ""

                self.rank -= 1
                self.label_top.setText(str(self.rank))

                keyWord = self.comboBox_2.currentText()
                kinds = ""
                if keyWord == "맨투맨" or keyWord == "셔츠":
                    kinds = "shirts"
                elif keyWord == "청바지" or keyWord == "슬랙스":
                    kinds = "pants"
                else:
                    kinds = "outers"
                sql = 'select * from {} where category = "{}" and top1to5 = {}'.format(kinds, keyWord, self.rank)
                cur.execute(sql)
                result = cur.fetchall()
                self.name_1.setText(result[0][3])
                self.name_2.setText(result[1][3])
                self.name_3.setText(result[2][3])
                self.name_4.setText(result[3][3])

                self.price_1.setText(result[0][4])
                self.price_2.setText(result[1][4])
                self.price_3.setText(result[2][4])
                self.price_4.setText(result[3][4])

                self.review_1.setText(result[0][5])
                self.review_2.setText(result[1][5])
                self.review_3.setText(result[2][5])
                self.review_4.setText(result[3][5])

                self.Link_1 = result[0][6]
                self.Link_2 = result[1][6]
                self.Link_3 = result[2][6]
                self.Link_4 = result[3][6]

                self.mantoman -= 1
                self.shirts -= 1
                self.jeans -= 1
                self.slacks -= 1
                self.coats -= 1
                self.paddings -= 1

                if keyWord == "맨투맨":
                    pixmap1 = QPixmap('./HI/11번가_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap2 = QPixmap('./HI/G마켓_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap3 = QPixmap('./HI/옥션_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap4 = QPixmap('./HI/신세계_맨투맨{}.jpg'.format(self.mantoman))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "셔츠":
                    pixmap1 = QPixmap('./HI/11번가_셔츠{}.jpg'.format(self.shirts))
                    pixmap2 = QPixmap('./HI/G마켓_셔츠{}.jpg'.format(self.shirts))
                    pixmap3 = QPixmap('./HI/옥션_셔츠{}.jpg'.format(self.shirts))
                    pixmap4 = QPixmap('./HI/신세계_셔츠{}.jpg'.format(self.shirts))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "청바지":
                    pixmap1 = QPixmap('./HI/11번가_청바지{}.jpg'.format(self.jeans))
                    pixmap2 = QPixmap('./HI/G마켓_청바지{}.jpg'.format(self.jeans))
                    pixmap3 = QPixmap('./HI/옥션_청바지{}.jpg'.format(self.jeans))
                    pixmap4 = QPixmap('./HI/신세계_청바지{}.jpg'.format(self.jeans))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelFourth.setPixmap(pixmap3)
                elif keyWord == "슬랙스":
                    pixmap1 = QPixmap('./HI/11번가_슬랙스{}.jpg'.format(self.slacks))
                    pixmap2 = QPixmap('./HI/G마켓_슬랙스{}.jpg'.format(self.slacks))
                    pixmap3 = QPixmap('./HI/옥션_슬랙스{}.jpg'.format(self.slacks))
                    pixmap4 = QPixmap('./HI/신세계_슬랙스{}.jpg'.format(self.slacks))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "코트":
                    pixmap1 = QPixmap('./HI/11번가_코트{}.jpg'.format(self.coats))
                    pixmap2 = QPixmap('./HI/G마켓_코트{}.jpg'.format(self.coats))
                    pixmap3 = QPixmap('./HI/옥션_코트{}.jpg'.format(self.coats))
                    pixmap4 = QPixmap('./HI/신세계_코트{}.jpg'.format(self.coats))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "패딩":
                    pixmap1 = QPixmap('./HI/11번가_패딩{}.jpg'.format(self.paddings))
                    pixmap2 = QPixmap('./HI/G마켓_패딩{}.jpg'.format(self.paddings))
                    pixmap3 = QPixmap('./HI/옥션_패딩{}.jpg'.format(self.paddings))
                    pixmap4 = QPixmap('./HI/신세계_패딩{}.jpg'.format(self.paddings))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

            else:
                QMessageBox.about(self, "알림", "더이상 앞으로 넘길 수 없습니다.")
        else:
            pass



import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QApplication
from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import socket
import zipfile
import sys
import pymysql
import webbrowser
import matplotlib.pyplot as plt
import os
import shutil





conn = pymysql.connect(host='10.10.21.108', user='root', password='1234', db='clothes', charset='utf8')
cur = conn.cursor()

ui_form = uic.loadUiType("main.ui")[0]
ui_form2 = uic.loadUiType("graph.ui")[0]

class MainWindow(QMainWindow, ui_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.combobox()
        self.comboBox.activated.connect(self.combobox)
        self.pushButton.clicked.connect(self.goToStart)
        self.pushButton_graph.clicked.connect(self.goToGraph)
        self.search_btn.clicked.connect(self.search)
        self.next_btn.clicked.connect(self.Next)
        self.prev_btn.clicked.connect(self.Prev)
        self.doneSerach = False
        self.rank = 1

        self.Link_1 = ""
        self.Link_2 = ""
        self.Link_3 = ""
        self.Link_4 = ""

        self.mantoman = 0
        self.shirts = 5
        self.slacks = 15
        self.jeans = 10
        self.coats = 20
        self.paddings = 25

        # if self.doneSerach == False:
        #     pass
        # else:
        #     self.pushButton_link_1.clicked.connect(lambda: webbrowser.open(self.Link_1))
        #     self.pushButton_link_2.clicked.connect(lambda: webbrowser.open(self.Link_2))
        #     self.pushButton_link_3.clicked.connect(lambda: webbrowser.open(self.Link_3))

        self.pushButton_link_1.clicked.connect(lambda: webbrowser.open(self.Link_1))
        self.pushButton_link_2.clicked.connect(lambda: webbrowser.open(self.Link_2))
        self.pushButton_link_3.clicked.connect(lambda: webbrowser.open(self.Link_3))
        self.pushButton_link_4.clicked.connect(lambda: webbrowser.open(self.Link_4))




    ###############################################################
    ####################    압축파일 받아와서 풀기    ################
    ###############################################################
    def goToStart(self):
        HOST = '10.10.21.102'
        PORT = 5003
        ADDR = (HOST, PORT)
        BUFF_SIZE = 1024

        clientSocket = socket.socket()
        clientSocket.connect(ADDR)
        clientSocket.send('client message'.encode())
        with open('HI.zip', 'wb') as f:
            print('file opened')
            while True:
                print('receiving data...')
                data = clientSocket.recv(BUFF_SIZE)
                print('(data)', data)
                if not data:
                    break
                f.write(data)
        f.close()
        print('Successfully get the file')
        clientSocket.close()
        print('connection closed')
        zipfile.ZipFile('HI.zip').extractall('/home/aiot8/PycharmProjects/pythonProject12/HI')

        self.stackedWidget.setCurrentWidget(self.page)

    def combobox(self):
        first = self.comboBox.currentText()
        if first == "상의":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("맨투맨")
            self.comboBox_2.addItem("셔츠")
        elif first == "하의":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("청바지")
            self.comboBox_2.addItem("슬랙스")
        else:
            self.comboBox_2.clear()
            self.comboBox_2.addItem("코트")
            self.comboBox_2.addItem("패딩")

        self.shop_name_1.setText("11번가")
        self.shop_name_2.setText("G마켓")
        self.shop_name_3.setText("옥션")
        self.shop_name_4.setText("신세계TV쇼핑")

    def goToGraph(self):
        self.sh = GraphWindow()
        self.sh.show()
        self.hide()

    def search(self):
        self.Link_1 = ""
        self.Link_2 = ""
        self.Link_3 = ""
        self.Link_4 = ""

        self.doneSerach = True
        self.rank = 1
        self.label_top.setText(str(self.rank))
        keyWord = self.comboBox_2.currentText()
        kinds = ""
        if keyWord == "맨투맨" or keyWord == "셔츠":
            kinds = "shirts"
        elif keyWord == "청바지" or keyWord == "슬랙스":
            kinds = "pants"
        else :
            kinds = "outers"

        sql = 'select * from {} where top1to5 = 1 and category = "{}"'.format(kinds, keyWord)
        cur.execute(sql)
        result = cur.fetchall()

        self.name_1.setText(result[0][3])
        self.name_2.setText(result[1][3])
        self.name_3.setText(result[2][3])
        self.name_4.setText(result[3][3])


        self.price_1.setText(result[0][4])
        self.price_2.setText(result[1][4])
        self.price_3.setText(result[2][4])
        self.price_4.setText(result[3][4])

        self.review_1.setText(result[0][5])
        self.review_2.setText(result[1][5])
        self.review_3.setText(result[2][5])
        self.review_4.setText(result[3][5])

        self.Link_1 = result[0][6]
        self.Link_2 = result[1][6]
        self.Link_3 = result[2][6]
        self.Link_4 = result[3][6]

        ### 사진넣기 ###

        self.mantoman = 0
        self.shirts = 5
        self.slacks = 15
        self.jeans = 10
        self.coats = 20
        self.paddings = 25
        if keyWord == "맨투맨":
            pixmap1 = QPixmap('./HI/11번가_맨투맨{}.jpg'.format(self.mantoman))
            pixmap2 = QPixmap('./HI/G마켓_맨투맨{}.jpg'.format(self.mantoman))
            pixmap3 = QPixmap('./HI/옥션_맨투맨{}.jpg'.format(self.mantoman))
            pixmap4 = QPixmap('./HI/신세계_맨투맨{}.jpg'.format(self.mantoman))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)

        elif keyWord == "셔츠":


            pixmap1 = QPixmap('./HI/11번가_셔츠{}.jpg'.format(self.shirts))
            pixmap2 = QPixmap('./HI/G마켓_셔츠{}.jpg'.format(self.shirts))
            pixmap3 = QPixmap('./HI/옥션_셔츠{}.jpg'.format(self.shirts))
            pixmap4 = QPixmap('./HI/신세계_셔츠{}.jpg'.format(self.shirts))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)

        elif keyWord == "슬랙스":
            pixmap1 = QPixmap('./HI/11번가_슬랙스{}.jpg'.format(self.slacks))
            pixmap2 = QPixmap('./HI/G마켓_슬랙스{}.jpg'.format(self.slacks))
            pixmap3 = QPixmap('./HI/옥션_슬랙스{}.jpg'.format(self.slacks))
            pixmap4 = QPixmap('./HI/신세계_슬랙스{}.jpg'.format(self.slacks))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)

        elif keyWord == "청바지":
            pixmap1 = QPixmap('./HI/11번가_청바지{}.jpg'.format(self.jeans))
            pixmap2 = QPixmap('./HI/G마켓_청바지{}.jpg'.format(self.jeans))
            pixmap3 = QPixmap('./HI/옥션_청바지{}.jpg'.format(self.jeans))
            pixmap4 = QPixmap('./HI/신세계_청바지{}.jpg'.format(self.jeans))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)

        elif keyWord == "코트":
            pixmap1 = QPixmap('./HI/11번가_코트{}.jpg'.format(self.coats))
            pixmap2 = QPixmap('./HI/G마켓_코트{}.jpg'.format(self.coats))
            pixmap3 = QPixmap('./HI/옥션_코트{}.jpg'.format(self.coats))
            pixmap4 = QPixmap('./HI/신세계_코트{}.jpg'.format(self.coats))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)

        elif keyWord == "패딩":
            pixmap1 = QPixmap('./HI/11번가_패딩{}.jpg'.format(self.paddings))
            pixmap2 = QPixmap('./HI/G마켓_패딩{}.jpg'.format(self.paddings))
            pixmap3 = QPixmap('./HI/옥션_패딩{}.jpg'.format(self.paddings))
            pixmap4 = QPixmap('./HI/신세계_패딩{}.jpg'.format(self.paddings))
            self.labelFirst.setPixmap(pixmap1)
            self.labelSecond.setPixmap(pixmap2)
            self.labelThird.setPixmap(pixmap3)
            self.labelFourth.setPixmap(pixmap4)



    def Next(self):
        if self.doneSerach == True:

            if self.rank <= 4:

                self.Link_1 = ""
                self.Link_2 = ""
                self.Link_3 = ""
                self.Link_4 = ""
                self.rank += 1
                self.label_top.setText(str(self.rank))

                keyWord = self.comboBox_2.currentText()
                kinds = ""
                if keyWord == "맨투맨" or keyWord == "셔츠":
                    kinds = "shirts"
                elif keyWord == "청바지" or keyWord == "슬랙스":
                    kinds = "pants"
                else :
                    kinds = "outers"
                sql = 'select * from {} where category = "{}" and top1to5 = {}'.format(kinds, keyWord, self.rank)
                cur.execute(sql)
                result = cur.fetchall()
                self.name_1.setText(result[0][3])
                self.name_2.setText(result[1][3])
                self.name_3.setText(result[2][3])
                self.name_4.setText(result[3][3])

                self.price_1.setText(result[0][4])
                self.price_2.setText(result[1][4])
                self.price_3.setText(result[2][4])
                self.price_4.setText(result[3][4])

                self.review_1.setText(result[0][5])
                self.review_2.setText(result[1][5])
                self.review_3.setText(result[2][5])
                self.review_4.setText(result[3][5])

                self.Link_1 = result[0][6]
                self.Link_2 = result[1][6]
                self.Link_3 = result[2][6]
                self.Link_4 = result[3][6]

                self.mantoman += 1
                self.shirts += 1
                self.jeans += 1
                self.slacks += 1
                self.coats += 1
                self.paddings += 1

                if keyWord == "맨투맨":
                    pixmap1 = QPixmap('./HI/11번가_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap2 = QPixmap('./HI/G마켓_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap3 = QPixmap('./HI/옥션_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap4 = QPixmap('./HI/신세계_맨투맨{}.jpg'.format(self.mantoman))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "셔츠":
                    pixmap1 = QPixmap('./HI/11번가_셔츠{}.jpg'.format(self.shirts))
                    pixmap2 = QPixmap('./HI/G마켓_셔츠{}.jpg'.format(self.shirts))
                    pixmap3 = QPixmap('./HI/옥션_셔츠{}.jpg'.format(self.shirts))
                    pixmap4 = QPixmap('./HI/신세계_셔츠{}.jpg'.format(self.shirts))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "청바지":
                    pixmap1 = QPixmap('./HI/11번가_청바지{}.jpg'.format(self.jeans))
                    pixmap2 = QPixmap('./HI/G마켓_청바지{}.jpg'.format(self.jeans))
                    pixmap3 = QPixmap('./HI/옥션_청바지{}.jpg'.format(self.jeans))
                    pixmap4 = QPixmap('./HI/신세계_청바지{}.jpg'.format(self.jeans))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)
                elif keyWord == "슬랙스":
                    pixmap1 = QPixmap('./HI/11번가_슬랙스{}.jpg'.format(self.slacks))
                    pixmap2 = QPixmap('./HI/G마켓_슬랙스{}.jpg'.format(self.slacks))
                    pixmap3 = QPixmap('./HI/옥션_슬랙스{}.jpg'.format(self.slacks))
                    pixmap4 = QPixmap('./HI/신세계_슬랙스{}.jpg'.format(self.slacks))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "코트":
                    pixmap1 = QPixmap('./HI/11번가_코트{}.jpg'.format(self.coats))
                    pixmap2 = QPixmap('./HI/G마켓_코트{}.jpg'.format(self.coats))
                    pixmap3 = QPixmap('./HI/옥션_코트{}.jpg'.format(self.coats))
                    pixmap4 = QPixmap('./HI/신세계_코트{}.jpg'.format(self.coats))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "패딩":
                    pixmap1 = QPixmap('./HI/11번가_패딩{}.jpg'.format(self.paddings))
                    pixmap2 = QPixmap('./HI/G마켓_패딩{}.jpg'.format(self.paddings))
                    pixmap3 = QPixmap('./HI/옥션_패딩{}.jpg'.format(self.paddings))
                    pixmap4 = QPixmap('./HI/신세계_패딩{}.jpg'.format(self.paddings))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)





            else:
                QMessageBox.information(self, "알림", "마지막페이지입니다.")
        else:
            pass

    def Prev(self):
        if self.doneSerach == True:
            if self.rank >= 2:

                self.Link_1 = ""
                self.Link_2 = ""
                self.Link_3 = ""
                self.Link_4 = ""

                self.rank -= 1
                self.label_top.setText(str(self.rank))

                keyWord = self.comboBox_2.currentText()
                kinds = ""
                if keyWord == "맨투맨" or keyWord == "셔츠":
                    kinds = "shirts"
                elif keyWord == "청바지" or keyWord == "슬랙스":
                    kinds = "pants"
                else:
                    kinds = "outers"
                sql = 'select * from {} where category = "{}" and top1to5 = {}'.format(kinds, keyWord, self.rank)
                cur.execute(sql)
                result = cur.fetchall()
                self.name_1.setText(result[0][3])
                self.name_2.setText(result[1][3])
                self.name_3.setText(result[2][3])
                self.name_4.setText(result[3][3])

                self.price_1.setText(result[0][4])
                self.price_2.setText(result[1][4])
                self.price_3.setText(result[2][4])
                self.price_4.setText(result[3][4])

                self.review_1.setText(result[0][5])
                self.review_2.setText(result[1][5])
                self.review_3.setText(result[2][5])
                self.review_4.setText(result[3][5])

                self.Link_1 = result[0][6]
                self.Link_2 = result[1][6]
                self.Link_3 = result[2][6]
                self.Link_4 = result[3][6]

                self.mantoman -= 1
                self.shirts -= 1
                self.jeans -= 1
                self.slacks -= 1
                self.coats -= 1
                self.paddings -= 1

                if keyWord == "맨투맨":
                    pixmap1 = QPixmap('./HI/11번가_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap2 = QPixmap('./HI/G마켓_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap3 = QPixmap('./HI/옥션_맨투맨{}.jpg'.format(self.mantoman))
                    pixmap4 = QPixmap('./HI/신세계_맨투맨{}.jpg'.format(self.mantoman))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "셔츠":
                    pixmap1 = QPixmap('./HI/11번가_셔츠{}.jpg'.format(self.shirts))
                    pixmap2 = QPixmap('./HI/G마켓_셔츠{}.jpg'.format(self.shirts))
                    pixmap3 = QPixmap('./HI/옥션_셔츠{}.jpg'.format(self.shirts))
                    pixmap4 = QPixmap('./HI/신세계_셔츠{}.jpg'.format(self.shirts))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "청바지":
                    pixmap1 = QPixmap('./HI/11번가_청바지{}.jpg'.format(self.jeans))
                    pixmap2 = QPixmap('./HI/G마켓_청바지{}.jpg'.format(self.jeans))
                    pixmap3 = QPixmap('./HI/옥션_청바지{}.jpg'.format(self.jeans))
                    pixmap4 = QPixmap('./HI/신세계_청바지{}.jpg'.format(self.jeans))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelFourth.setPixmap(pixmap3)
                elif keyWord == "슬랙스":
                    pixmap1 = QPixmap('./HI/11번가_슬랙스{}.jpg'.format(self.slacks))
                    pixmap2 = QPixmap('./HI/G마켓_슬랙스{}.jpg'.format(self.slacks))
                    pixmap3 = QPixmap('./HI/옥션_슬랙스{}.jpg'.format(self.slacks))
                    pixmap4 = QPixmap('./HI/신세계_슬랙스{}.jpg'.format(self.slacks))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "코트":
                    pixmap1 = QPixmap('./HI/11번가_코트{}.jpg'.format(self.coats))
                    pixmap2 = QPixmap('./HI/G마켓_코트{}.jpg'.format(self.coats))
                    pixmap3 = QPixmap('./HI/옥션_코트{}.jpg'.format(self.coats))
                    pixmap4 = QPixmap('./HI/신세계_코트{}.jpg'.format(self.coats))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

                elif keyWord == "패딩":
                    pixmap1 = QPixmap('./HI/11번가_패딩{}.jpg'.format(self.paddings))
                    pixmap2 = QPixmap('./HI/G마켓_패딩{}.jpg'.format(self.paddings))
                    pixmap3 = QPixmap('./HI/옥션_패딩{}.jpg'.format(self.paddings))
                    pixmap4 = QPixmap('./HI/신세계_패딩{}.jpg'.format(self.paddings))
                    self.labelFirst.setPixmap(pixmap1)
                    self.labelSecond.setPixmap(pixmap2)
                    self.labelThird.setPixmap(pixmap3)
                    self.labelFourth.setPixmap(pixmap4)

            else:
                QMessageBox.about(self, "알림", "더이상 앞으로 넘길 수 없습니다.")
        else:
            pass



class GraphWindow(QMainWindow, ui_form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.kinds = ""
        self.mymy = ["11번가", "G마켓", "옥션", "신세계"]
        self.price = []  #가격
        self.reviewCount = []  #리뷰수

        print("1")
        self.canvas = FigureCanvas(Figure(figsize=(4, 3)))
        print("2")
        self.vbox = QVBoxLayout(self.label)
        print("3")
        self.vbox.addWidget(self.canvas)
        print("4")
        self.ax = self.canvas.figure.subplots()  # xy축 그리기
        print("5")
        self.ax2 = self.ax.twinx()


        self.pushButton_goback.clicked.connect(self.goback)
        self.pushButton_graph1.clicked.connect(self.searchgraph)


    def goback(self):
        self.sh = MainWindow()
        self.sh.show()
        self.close()


    def searchgraph(self):
        Keyword = self.comboBox.currentText()
        print("Keyword : ",Keyword)

        if Keyword == "전체쇼핑몰":
            self.total()

        if Keyword == "맨투맨" or Keyword == "셔츠":
            self.kinds = "shirts"
            print("self.kinds :", self.kinds)
            self.first()

        if Keyword == "청바지" or Keyword == "슬랙스":
            self.kinds = "pants"
            print("self.kinds :", self.kinds)
            self.first()

        if Keyword == "코트" or Keyword == "패딩":
            self.kinds = "outers"
            print("self.kinds :", self.kinds)
            self.first()
    def total(self):
        pass

    def first(self):
        self.ax.clear()
        self.ax2.clear()
        conn = pymysql.connect(host='10.10.21.108', user='root', password='1234', db='clothes', charset='utf8')
        cur = conn.cursor()

        # self.fig = plt.figure()
        # self.canvas22 = FigureCanvas(self.fig)
        # self.graph_layout.addWidget(self.canvas22)



        keyWord = self.comboBox.currentText()
        self.price = []  # 가격 초기화
        self.reviewCount = []  # 리뷰수 초기화
        price_11 = 0       #11번가 평균가격
        price_gm = 0       #지마켓 평균가격
        price_auc = 0      #옥션 평균가격
        price_shin = 0     #신세계 평균가격

        rev_11 = 0
        rev_gm = 0
        rev_auc = 0
        rev_shin = 0

        for i in self.mymy:
            sql = 'select price, reviewCount from {} where company = "{}" and category = "{}"'.format(self.kinds, i, keyWord)
            cur.execute(sql)
            result = cur.fetchall()
            for j in range(0,5):
                space1 = result[j][0].replace(',','')   #가격구하기
                space1 = space1.replace('원','')
                print(i , " 가격 ", j, " : " , space1)
                space1 = int(space1)
                if i == "11번가":
                    price_11 += space1
                elif i == "G마켓":
                    price_gm += space1
                elif i == "옥션":
                    price_auc += space1
                else:
                    price_shin += space1
                space2 = result[j][1].replace(',',"")   #리뷰구하기
                space2 = space2.replace('건',"")
                print(i , " 리뷰 ", j, " : ", space2)
                space2 = int(space2)
                if i == "11번가":
                    rev_11 += space2
                elif i == "G마켓":
                    rev_gm += space2
                elif i == "옥션":
                    rev_auc += space2
                else:
                    rev_shin += space2
        price_11 = int(price_11/5)
        price_gm =   int(price_gm/5)
        price_auc =  int(price_auc/5)
        price_shin = int(price_shin/5)
        print('평균-----------')
        print(price_11)
        print(price_gm)
        print(price_auc)
        print(price_shin)
        rev_11 = int(rev_11/5)
        rev_gm = int(rev_gm/5)
        rev_auc =  int(rev_auc/5)
        rev_shin = int(rev_shin/5)
        print('평균-----------')
        print(rev_11)
        print(rev_gm)
        print(rev_auc)
        print(rev_shin)

        print("111111111111111111111111111111111111111111111111111")


        topics = ['11', 'Gmarket', 'Auc', 'Shin']    # x축 이름정하기
        value_a = [price_11, price_gm, price_auc, price_shin]      # 그래프 1 데이터
        value_b = [rev_11, rev_gm, rev_auc, rev_shin]      # 그래프 2 데이터
        print("22222222222222222222222222222222222222222222222222")
        print("33333333333333333333333333333333333333333333333333")
        # x축 값설정
        # self.df_list_x1 = value_a
        # print(self.df_list_x1)
        # y축 값 설정
        # self.df_list_x2 = value_b
        # print(self.df_list_x2)
        print("4444444444444444444444444444444444444444444444444")
        # 갱신 기능
        # self.ax.clear()
        def create_x(t, w, n, d):  # 그래프 틀만들기?
            return [t * x + w * n for x in range(d)]
        value_a_x = create_x(3, 0.8, 1, 4)  # 그래프 1 데이터로 그래프 그리는 함수 호출
        value_b_x = create_x(3, 0.8, 2, 4)  # 그래프 2 데이터로 그래프 그리는 함수 호출
        # 아마도 배치?


        self.ax.bar(value_a_x, value_a, color='green', label='price')
        print("55555555555555555555555555555555555555555555555555")
        self.ax.legend(loc='upper left')
        print("66666666666666666666666666666666666666666666666666")

        # self.ax2 = self.ax.twinx()
        print("777777777777777777777777777777777777777777777777777")
        self.ax2.bar(value_b_x, value_b, color='deeppink', label='review')
        print("8888888888888888888888888888888888888888888888888888")
        self.ax2.set_ylabel("AVG rieview by company (CLICK)")
        print("9999999999999999999999999999999999999999999999999999999")
        self.ax2.legend(loc='upper right')
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

        middle_x = [(a + b) / 2 for (a, b) in zip(value_a_x, value_b_x)]
        self.ax.set_xticks(middle_x)
        self.ax.set_xticklabels(topics)

        # 그려지는거
        self.ax.figure.canvas.draw()
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()



