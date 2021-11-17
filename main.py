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
        self.pushButton_goback.clicked.connect(self.goback)
        self.pushButton_graph1.clicked.connect(self.graph)

    def goback(self):
        self.sh = MainWindow()
        self.sh.show()
        self.close()
    def graph(self):
        Keyword = self.comboBox.currentText()
        print(Keyword)
        if Keyword == "전체쇼핑몰":
            self.total()
        elif Keyword == "11번가":
            self.first()
        elif Keyword == "G마켓":
            self.second()
        elif Keyword == "옥션":
            self.fourth()
        elif Keyword == "신세계":
            self.fifth()


    def total(self):










        # X1 = [1, 3, 5, 7]       #이좌표에서 각쇼핑몰의 첫막대 그래프가 시작
        # data1 = [1, 2, 3, 4]
        # plt.bar(X1, data1, color='r', width=0.5)
        #
        # X2 = [1 + 0.5, 3 + 0.5, 5 + 0.5, 7 + 0.5]       #이좌표에서 각쇼핑몰의 두번째그래프 시작
        # data2 = [2, 3, 4, 5]
        # plt.bar(X2, data2, color='g', width=0.5)
        #
        # X3 = [1 + 1, 3 + 1, 5 + 1, 7 + 1]               #이좌표에서 각쇼핑몰의 세번째그래프시작
        # data3 = [3, 4, 5, 6]
        # plt.bar(X3, data3, color='b', width=0.5)
        #
        # ticklabel = ['11bunga', 'Gmarket', 'Auction', '?']
        # plt.xticks(X2, ticklabel, fontsize=15, rotation=0)
        # plt.tick_params(
        #     axis='x',
        #     bottom=False)
        # plt.show()



    def first(self):
        pass

    def second(self):
        pass

    def third(self):
        pass

    def fourth(self):
        pass

    def fifth(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()
