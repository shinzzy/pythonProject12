# # # ##############################파일 자동전송
# # import socket
# # import zipfile
# # import os
# #
# # HOST = socket.gethostname()
# # PORT = 5002
# # ADDR = (HOST, PORT)
# # BUFF_SIZE = 1024
# #
# # serverSocket = socket.socket()
# #
# # serverSocket.bind(ADDR)
# # serverSocket.listen(5)
# #
# # print ('Server waiting...')
# #
# # while True:
# #     clientSocket, addr = serverSocket.accept()
# #     print ('Connection from', addr)
# #     data = clientSocket.recv(BUFF_SIZE)
# #     print('client : ' + data.decode())
# #     filename='iu1.png'
# #     f = open(filename,'rb')
# #     l = f.read(BUFF_SIZE)
# #     while (l):
# #         print('sending data...')
# #         clientSocket.send(l)
# #         print('(sent)',repr(l))
# #         l = f.read(BUFF_SIZE)
# #     f.close()
# #     print('Done sending')
# #
# # clientSocket.close()
#
#
#
#
#
#
# # ##############################파일 이름입력해서 받기
# # from socket import *
# # from os.path import exists
# # import sys
# # import zipfile
# # import os
# # serverSock = socket(AF_INET, SOCK_STREAM)
# # serverSock.bind(('', 8087))
# # serverSock.listen(1)
# #
# # connectionSock, addr = serverSock.accept()
# #
# # print(str(addr),'에서 접속했습니다')
# #
# # filename = connectionSock.recv(1024) #클라이언트한테 파일이름(이진 바이트 스트림 형태)을 전달 받는다
# # print('받은 데이터 : ', filename.decode('utf-8')) #파일 이름을 일반 문자열로 변환한다
# # data_transferred = 0
# #
# # if not exists(filename):
# #     print("no file")
# #     sys.exit()
# #
# # print("파일 %s 전송 시작" %filename)
# # with open(filename, 'rb') as f:
# #     try:
# #         data = f.read(1024) #1024바이트 읽는다
# #         while data: #데이터가 없을 때까지
# #             data_transferred += connectionSock.send(data) #1024바이트 보내고 크기 저장
# #             data = f.read(1024) #1024바이트 읽음
# #     except Exception as ex:
# #         print(ex)
# # print("전송완료 %s, 전송량 %d" %(filename, data_transferred))
#
#
#
#
#
#
#
#
# # ###############################압축하기
# # import zipfile
# # import os
# #
# # os.chdir('/home/aiot02/PycharmProjects/pythonProject6/iu')
# # # my_zip = zipfile.ZipFile('iu.zip','w')
# # # my_zip.write('iu.txt')
# # # my_zip.close()
# #
# # # file_list = ['iu1.png', 'iu2.png', 'iu3.png', 'iu4.png', 'iu5.png', 'iu6.png', 'iu7.png']
# # file_list = []
# # for i in range(1,8):
# #     file_list.append("iu{}.png".format(i))
# # with zipfile.ZipFile(os.getcwd()+".zip","w")as my_zip:
# #     for i in file_list:
# #         my_zip.write(i)
# #     my_zip.close()
#
#
#
#
#
# #
# #
# # ##############################파일 자동전송 + 압축
# # import socket
# # import zipfile
# # import os
# #
# #
# # os.chdir('/home/aiot02/PycharmProjects/pythonProject6/iu')
# #
# # file_list = []
# # for i in range(1,8):
# #     file_list.append("iu{}.png".format(i))
# #
# # with zipfile.ZipFile(os.getcwd()+".zip","w")as my_zip:
# #     for i in file_list:
# #         my_zip.write(i)
# #     my_zip.close()
# #
# # os.chdir('/home/aiot02/PycharmProjects/pythonProject6')
# # HOST = socket.gethostname()
# # PORT = 5003
# # ADDR = (HOST, PORT)
# # BUFF_SIZE = 1024
# #
# # serverSocket = socket.socket()
# # serverSocket.bind(ADDR)
# # serverSocket.listen(5)
# # print ('Server waiting...')
# # while True:
# #     clientSocket, addr = serverSocket.accept()
# #     print ('Connection from', addr)
# #     data = clientSocket.recv(BUFF_SIZE)
# #     print('client : ' + data.decode())
# #     filename='iu.zip'
# #     #filename='iu1.png'
# #     # f = open(filename,'rb')
# #     with open(filename, 'rb')as f:
# #         try:
# #             l = f.read(BUFF_SIZE)
# #             while (l):
# #                 print('sending data...')
# #                 clientSocket.send(l)
# #                 l = f.read(BUFF_SIZE)
# #             f.close()
# #             print('Done sending')
# #             clientSocket.close()
# #         except Exception as e:
# #             print(e)
#
#
#
#
#
#
#
#
# # # ##############################파일 이름입력해서 받기+압축
# #
# # from socket import *
# # from os.path import exists
# # import sys
# # import zipfile
# # import os
# #
# # os.chdir('/home/aiot02/PycharmProjects/pythonProject6/iu')
# #
# # file_list = []
# # for i in range(1,8):
# #     file_list.append("iu{}.png".format(i))
# #
# # with zipfile.ZipFile(os.getcwd()+".zip","w")as my_zip:
# #     for i in file_list:
# #         my_zip.write(i)
# #     my_zip.close()
# #
# # os.chdir('/home/aiot02/PycharmProjects/pythonProject6')
# # serverSock = socket(AF_INET, SOCK_STREAM)
# # serverSock.bind(('', 8089))
# # serverSock.listen(1)
# #
# # connectionSock, addr = serverSock.accept()
# #
# # print(str(addr),'에서 접속했습니다')
# # filename = connectionSock.recv(1024) #클라이언트한테 파일이름(이진 바이트 스트림 형태)을 전달 받는다
# # print('받은 데이터 : ', filename.decode('utf-8')) #파일 이름을 일반 문자열로 변환한다
# # data_transferred = 0
# #
# # if not exists(filename):
# #     print("no file")
# #     sys.exit()
# #
# # print("파일 %s 전송 시작" %filename)
# # with open(filename, 'rb') as f:
# #     try:
# #         data = f.read(1024) #1024바이트 읽는다
# #         while data: #데이터가 없을 때까지
# #             data_transferred += connectionSock.send(data) #1024바이트 보내고 크기 저장
# #             data = f.read(1024) #1024바이트 읽음
# #     except Exception as ex:
# #         print(ex)
# # print("전송완료 %s, 전송량 %d" %(filename, data_transferred))
#
#
#
#
#
#
# ##############################파일 자동전송 + 압축
import socket
import zipfile
import os




import sys
import requests
import pymysql
from bs4 import BeautifulSoup
from PyQt5.QtGui import QPixmap , QIcon
from PyQt5.QtCore import Qt , QSize
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import threading
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import dload
import datetime
import pymysql
from bs4 import BeautifulSoup
from pprint import pprint
import requests, re,os
from urllib.request import urlretrieve #추가
import os
import zipfile

conn = pymysql.connect(host='10.10.21.108', user='root', password='1234', db='clothes', charset='utf8')
cur = conn.cursor()

sql = 'delete from shirts'
cur.execute(sql)
conn.commit()
sql = 'delete from pants'
cur.execute(sql)
conn.commit()
sql = 'delete from outers'
cur.execute(sql)
conn.commit()

#################################크롤링시작############################
#################################크롤링시작############################
#################################크롤링시작##############################url## -11번가 베스트 기준
#티셔츠 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001841
#후드티 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1059019
#맨투맨 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1059018
#청바지 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001843
#셔츠/남방 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001840
#재킷 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001834
#바지/팬츠 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001844
#가디건 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001837
#점퍼 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001836
#정장/슈트 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001842
#코트 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001835
#니트/스웨터 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001838
#조끼/베스트 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001839
#트레이닝복 - https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001845



#####################11번가######################
#맨투맨
url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1059018"
print(url)
source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")


a = 0
i = 1
num = 0
ing = []         ###########제품 이름 클래스#########
ing2 = []        ###########제품 구매 사이트#########
show_now = []
story33 = []     ##########제품 이름###########
story44 = []     ##########제품 가격###########
story55 = []     ##########제품 평점###########
story66 = []     ##########제품 이미지#########


print("#########################[이름 클래스 받아오는중]#######################")
story22 = soup.findAll('a',{'target':'_top'})
for a in range(0,5):
    print("a ::" , a)
    ing.append("thisClick"+str(story22[a]['class']))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace("prd", "")
    ing[a] = ing[a].replace("'", "")
    print("ing[a] : ", ing[a])

    print("######################[제품 구매 접속 사이트 받아오는중]###########################")
    ing2.append("thisClick" + str(story22[a]['href']))
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace("thisClick", "")
    ing2[a] = ing2[a].replace("'", "")
    print("ing2[a] : ", ing2[a])

print("####################[가져온 갯수만큼 반복하는중]###########################")
for a in range(0,5):

    print("#############################[제품 이름 가져오는중]##########################")
    story33.append(str(soup.select(
            "#{} > div > a > div.pname > p".format(ing[a]))))

    story33[a] = story33[a].replace("[", "")
    story33[a] = story33[a].replace("]", "")
    story33[a] = story33[a].replace("<p>", "")
    story33[a] = story33[a].replace("</p>", "")
    story33[a] = story33[a].replace("  ", "")

    print("#############################[제품 가격 가져오는중]##########################")
    story44.append(str(soup.select(
        "#{} > div > a > div.pname > div.price_info.cfix > span > strong".format(ing[a]))) + "원")

    story44[a] = story44[a].replace("[", "")
    story44[a] = story44[a].replace("]", "")
    story44[a] = story44[a].replace("</strong>", "")
    story44[a] = story44[a].replace('<strong class="sale_price">', "")


    print("story33[a] : ",story33[a])
    print("story44[a] : ", story44[a])

for a in range(0,5):
    url2 = "{}".format(ing2[a])
    print(url2)
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")

    print("##############################[리뷰수 가져오는중]###########################")
    story55.append(str(soup.select(
        "#tabMenuDetail2 > i")))
    story55[a] = story55[a].replace("[", "")
    story55[a] = story55[a].replace("]", "")
    story55[a] = story55[a].replace("(", "")
    story55[a] = story55[a].replace(")", "")
    story55[a] = story55[a].replace("<i>", "")
    story55[a] = story55[a].replace("</i>", "")
    story55[a] = story55[a].replace("'", "")
    story55[a] = story55[a] + "건"
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print("story55 : ", story55[a])
    print(len(story55[a]))



    print("##############################[이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select("#productImg > div > img")))
    story66[a] = story66[a].replace('<img alt="" onerror="this.src=', "")
    story66[a] = story66[a].replace('https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/img/product/no_image.gif', "")
    story66[a] = story66[a].replace("'", "")
    story66[a] = story66[a].replace('src="', "")
    story66[a] = story66[a].replace('"/>', "")
    story66[a] = story66[a].replace(' ', "")
    story66[a] = story66[a].replace('[', "")
    story66[a] = story66[a].replace(']', "")
    story66[a] = story66[a].replace('"', "")
    print("story66[a] : " , story66[a])

    show_now.append(story33[a] + "," + story44[a] + "," + story55[a] + "," + story66[a])
    print("show_now : " , show_now)
    print(ing2[a])
    sql = 'insert into shirts values("11번가", "맨투맨", {}, "{}", "{}", "{}", "{}")'.format(a+1, story33[a], story44[a], story55[a], ing2[a])
    cur.execute(sql)
    conn.commit()

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("stpry66 : " , story66)

print("len(story66) : {}".format(len(story66)))


#이미지 다운로드
try:

    for i in range(0,5):
        img_src = story66[i]
        print(img_src)
        img_src = img_src.split(",")
        print("img_src[0] : ", img_src[0])
        print('img/11번가_{}.jpg'.format(num))
        urlretrieve(img_src[0], '/home/aiot02/PycharmProjects/pythonProject6/HI/11번가_맨투맨{}.jpg'.format(num))
        print("성공")
        num += 1
        print("num : " , num)

except:

    print("실패")
    pass


##########################################################################################################################################################################################
#셔츠
url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001840"
print(url)
source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")


a = 0
i = 1
ing = []         ###########제품 이름 클래스#########
ing2 = []        ###########제품 구매 사이트#########
show_now = []
story33 = []     ##########제품 이름###########
story44 = []     ##########제품 가격###########
story55 = []     ##########제품 평점###########
story66 = []     ##########제품 이미지#########


print("#########################[이름 클래스 받아오는중]#######################")
story22 = soup.findAll('a',{'target':'_top'})
for a in range(0,5):
    print("a ::" , a)
    ing.append("thisClick"+str(story22[a]['class']))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace("prd", "")
    ing[a] = ing[a].replace("'", "")
    print("ing[a] : ", ing[a])

    print("######################[제품 구매 접속 사이트 받아오는중]###########################")
    ing2.append("thisClick" + str(story22[a]['href']))
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace("thisClick", "")
    ing2[a] = ing2[a].replace("'", "")
    print("ing2[a] : ", ing2[a])

print("####################[가져온 갯수만큼 반복하는중]###########################")
for a in range(0,5):

    print("#############################[제품 이름 가져오는중]##########################")
    story33.append(str(soup.select(
            "#{} > div > a > div.pname > p".format(ing[a]))))

    story33[a] = story33[a].replace("[", "")
    story33[a] = story33[a].replace("]", "")
    story33[a] = story33[a].replace("<p>", "")
    story33[a] = story33[a].replace("</p>", "")
    story33[a] = story33[a].replace("  ", "")

    print("#############################[제품 가격 가져오는중]##########################")
    story44.append(str(soup.select(
        "#{} > div > a > div.pname > div.price_info.cfix > span > strong".format(ing[a]))) + "원")

    story44[a] = story44[a].replace("[", "")
    story44[a] = story44[a].replace("]", "")
    story44[a] = story44[a].replace("</strong>", "")
    story44[a] = story44[a].replace('<strong class="sale_price">', "")


    print("story33[a] : ",story33[a])
    print("story44[a] : ", story44[a])


for a in range(0,5):
    url2 = "{}".format(ing2[a])
    print(url2)
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")

    print("##############################[리뷰수 가져오는중]###########################")
    story55.append(str(soup.select(
        "#tabMenuDetail2 > i")))
    story55[a] = story55[a].replace("[", "")
    story55[a] = story55[a].replace("]", "")
    story55[a] = story55[a].replace("(", "")
    story55[a] = story55[a].replace(")", "")
    story55[a] = story55[a].replace("<i>", "")
    story55[a] = story55[a].replace("</i>", "")
    story55[a] = story55[a].replace("'", "")
    story55[a] = story55[a] + "건"
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print("story55 : ", story55)
    print(len(story55[a]))


    print("##############################[이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select("#productImg > div > img")))
    story66[a] = story66[a].replace('<img alt="" onerror="this.src=', "")
    story66[a] = story66[a].replace('https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/img/product/no_image.gif', "")
    story66[a] = story66[a].replace("'", "")
    story66[a] = story66[a].replace('src="', "")
    story66[a] = story66[a].replace('"/>', "")
    story66[a] = story66[a].replace(' ', "")
    story66[a] = story66[a].replace('[', "")
    story66[a] = story66[a].replace(']', "")
    story66[a] = story66[a].replace('"', "")
    print("story66[a] : " , story66[a])


    show_now.append(story33[a] + "," + story44[a] + "," + story55[a] + "," + story66[a])
    print(show_now[a])
    sql = 'insert into shirts values("11번가", "셔츠", {}, "{}", "{}", "{}", "{}")'.format(a+1, story33[a], story44[a], story55[a], ing2[a])
    cur.execute(sql)
    conn.commit()


print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("stpry66 : " , story66[0])
print("len(story66) : {}".format(len(story66)))

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = story66[i]
        print("img_src : " , img_src)
        img_src = img_src.split(",")
        print("img_src[0] : " , img_src[0])
        print('img/11번가_{}.jpg'.format(num))
        urlretrieve(img_src[0] , '/home/aiot02/PycharmProjects/pythonProject6/HI/11번가_셔츠{}.jpg'.format(num))                 # 이미지 저장 경로 / 이미지 이름
        print("성공")
        num += 1

except:

    print("실패")
    pass


#############################################################################################################################################################################################
#청바지
url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001843"
print(url)
source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")


a = 0
i = 1
ing = []         ###########제품 이름 클래스#########
ing2 = []        ###########제품 구매 사이트#########
show_now = []
story33 = []     ##########제품 이름###########
story44 = []     ##########제품 가격###########
story55 = []     ##########제품 평점###########
story66 = []     ##########제품 이미지#########


print("#########################[이름 클래스 받아오는중]#######################")
story22 = soup.findAll('a',{'target':'_top'})
for a in range(0,5):
    print("a ::" , a)
    ing.append("thisClick"+str(story22[a]['class']))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace("prd", "")
    ing[a] = ing[a].replace("'", "")
    print("ing[a] : ", ing[a])

    print("######################[제품 구매 접속 사이트 받아오는중]###########################")
    ing2.append("thisClick" + str(story22[a]['href']))
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace("thisClick", "")
    ing2[a] = ing2[a].replace("'", "")
    print("ing2[a] : ", ing2[a])

print("####################[가져온 갯수만큼 반복하는중]###########################")
for a in range(0,5):

    print("#############################[제품 이름 가져오는중]##########################")
    story33.append(str(soup.select(
            "#{} > div > a > div.pname > p".format(ing[a]))))

    story33[a] = story33[a].replace("[", "")
    story33[a] = story33[a].replace("]", "")
    story33[a] = story33[a].replace("<p>", "")
    story33[a] = story33[a].replace("</p>", "")
    story33[a] = story33[a].replace("  ", "")

    print("#############################[제품 가격 가져오는중]##########################")
    story44.append(str(soup.select(
        "#{} > div > a > div.pname > div.price_info.cfix > span > strong".format(ing[a]))) + "원")

    story44[a] = story44[a].replace("[", "")
    story44[a] = story44[a].replace("]", "")
    story44[a] = story44[a].replace("</strong>", "")
    story44[a] = story44[a].replace('<strong class="sale_price">', "")


    print("story33[a] : ",story33[a])
    print("story44[a] : ", story44[a])


for a in range(0,5):
    url2 = "{}".format(ing2[a])
    print(url2)
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")

    print("##############################[리뷰수 가져오는중]###########################")
    story55.append(str(soup.select(
        "#tabMenuDetail2 > i")))
    story55[a] = story55[a].replace("[", "")
    story55[a] = story55[a].replace("]", "")
    story55[a] = story55[a].replace("(", "")
    story55[a] = story55[a].replace(")", "")
    story55[a] = story55[a].replace("<i>", "")
    story55[a] = story55[a].replace("</i>", "")
    story55[a] = story55[a].replace("'", "")
    story55[a] = story55[a] + "건"
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print("story55 : ", story55)
    print(len(story55[a]))


    print("##############################[이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select("#productImg > div > img")))
    story66[a] = story66[a].replace('<img alt="" onerror="this.src=', "")
    story66[a] = story66[a].replace('https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/img/product/no_image.gif', "")
    story66[a] = story66[a].replace("'", "")
    story66[a] = story66[a].replace('src="', "")
    story66[a] = story66[a].replace('"/>', "")
    story66[a] = story66[a].replace(' ', "")
    story66[a] = story66[a].replace('[', "")
    story66[a] = story66[a].replace(']', "")
    story66[a] = story66[a].replace('"', "")
    print("story66[a] : " , story66[a])


    show_now.append(story33[a] + "," + story44[a] + "," + story55[a] + "," + story66[a])
    print(show_now[a])
    sql = 'insert into pants values("11번가", "청바지", {}, "{}", "{}", "{}", "{}")'.format(a+1, story33[a], story44[a], story55[a], ing2[a])
    cur.execute(sql)
    conn.commit()


print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("stpry66 : " , story66[0])
print("len(story66) : {}".format(len(story66)))

#이미지 다운로드

try:

    for i in range(0,5):
        img_src = story66[i]
        print("img_src : " , img_src)
        img_src = img_src.split(",")
        print("img_src[0] : " , img_src[0])
        print('img/11번가_{}.jpg'.format(num))
        urlretrieve(img_src[0] , '/home/aiot02/PycharmProjects/pythonProject6/HI/11번가_청바지{}.jpg'.format(num))            # 이미지 저장 경로 / 이미지 이름
        print("성공")
        num += 1

except:

    print("실패")
    pass

#############################################################################################################################################################################################
#슬랙스
url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1011986"
print(url)
source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")


a = 0
i = 1
ing = []         ###########제품 이름 클래스#########
ing2 = []        ###########제품 구매 사이트#########
show_now = []
story33 = []     ##########제품 이름###########
story44 = []     ##########제품 가격###########
story55 = []     ##########제품 평점###########
story66 = []     ##########제품 이미지#########


print("#########################[이름 클래스 받아오는중]#######################")
story22 = soup.findAll('a',{'target':'_top'})
for a in range(0,5):
    print("a ::" , a)
    ing.append("thisClick"+str(story22[a]['class']))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace("prd", "")
    ing[a] = ing[a].replace("'", "")
    print("ing[a] : ", ing[a])

    print("######################[제품 구매 접속 사이트 받아오는중]###########################")
    ing2.append("thisClick" + str(story22[a]['href']))
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace("thisClick", "")
    ing2[a] = ing2[a].replace("'", "")
    print("ing2[a] : ", ing2[a])

print("####################[가져온 갯수만큼 반복하는중]###########################")
for a in range(0,5):

    print("#############################[제품 이름 가져오는중]##########################")
    story33.append(str(soup.select(
            "#{} > div > a > div.pname > p".format(ing[a]))))

    story33[a] = story33[a].replace("[", "")
    story33[a] = story33[a].replace("]", "")
    story33[a] = story33[a].replace("<p>", "")
    story33[a] = story33[a].replace("</p>", "")
    story33[a] = story33[a].replace("  ", "")

    print("#############################[제품 가격 가져오는중]##########################")
    story44.append(str(soup.select(
        "#{} > div > a > div.pname > div.price_info.cfix > span > strong".format(ing[a]))) + "원")

    story44[a] = story44[a].replace("[", "")
    story44[a] = story44[a].replace("]", "")
    story44[a] = story44[a].replace("</strong>", "")
    story44[a] = story44[a].replace('<strong class="sale_price">', "")


    print("story33[a] : ",story33[a])
    print("story44[a] : ", story44[a])


for a in range(0,5):
    url2 = "{}".format(ing2[a])
    print(url2)
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")

    print("##############################[리뷰수 가져오는중]###########################")
    story55.append(str(soup.select(
        "#tabMenuDetail2 > i")))
    story55[a] = story55[a].replace("[", "")
    story55[a] = story55[a].replace("]", "")
    story55[a] = story55[a].replace("(", "")
    story55[a] = story55[a].replace(")", "")
    story55[a] = story55[a].replace("<i>", "")
    story55[a] = story55[a].replace("</i>", "")
    story55[a] = story55[a].replace("'", "")
    story55[a] = story55[a] + "건"
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print("story55 : ", story55)
    print(len(story55[a]))


    print("##############################[이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select("#productImg > div > img")))
    story66[a] = story66[a].replace('<img alt="" onerror="this.src=', "")
    story66[a] = story66[a].replace('https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/img/product/no_image.gif', "")
    story66[a] = story66[a].replace("'", "")
    story66[a] = story66[a].replace('src="', "")
    story66[a] = story66[a].replace('"/>', "")
    story66[a] = story66[a].replace(' ', "")
    story66[a] = story66[a].replace('[', "")
    story66[a] = story66[a].replace(']', "")
    story66[a] = story66[a].replace('"', "")
    print("story66[a] : " , story66[a])


    show_now.append(story33[a] + "," + story44[a] + "," + story55[a] + "," + story66[a])
    print(show_now[a])
    sql = 'insert into pants values("11번가", "슬랙스", {}, "{}", "{}", "{}", "{}")'.format(a+1, story33[a], story44[a], story55[a], ing2[a])
    cur.execute(sql)
    conn.commit()


print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("stpry66 : " , story66[0])
print("len(story66) : {}".format(len(story66)))

#이미지 다운로드

try:

    for i in range(0,5):
        img_src = story66[i]
        print("img_src : " , img_src)
        img_src = img_src.split(",")
        print("img_src[0] : " , img_src[0])
        print('img/11번가_{}.jpg'.format(num))
        urlretrieve(img_src[0] , '/home/aiot02/PycharmProjects/pythonProject6/HI//11번가_슬랙스{}.jpg'.format(num))            # 이미지 저장 경로 / 이미지 이름
        print("성공")
        num += 1

except:

    print("실패")
    pass


##########################################################################################################################################################################################
#코트

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1001835"
print(url)
source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")


a = 0
i = 1
ing = []         ###########제품 이름 클래스#########
ing2 = []        ###########제품 구매 사이트#########
show_now = []
story33 = []     ##########제품 이름###########
story44 = []     ##########제품 가격###########
story55 = []     ##########제품 평점###########
story66 = []     ##########제품 이미지#########


print("#########################[이름 클래스 받아오는중]#######################")
story22 = soup.findAll('a',{'target':'_top'})
for a in range(0,5):
    print("a ::" , a)
    ing.append("thisClick"+str(story22[a]['class']))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace("prd", "")
    ing[a] = ing[a].replace("'", "")
    print("ing[a] : ", ing[a])

    print("######################[제품 구매 접속 사이트 받아오는중]###########################")
    ing2.append("thisClick" + str(story22[a]['href']))
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace("thisClick", "")
    ing2[a] = ing2[a].replace("'", "")
    print("ing2[a] : ", ing2[a])

print("####################[가져온 갯수만큼 반복하는중]###########################")
for a in range(0,5):

    print("#############################[제품 이름 가져오는중]##########################")
    story33.append(str(soup.select(
            "#{} > div > a > div.pname > p".format(ing[a]))))

    story33[a] = story33[a].replace("[", "")
    story33[a] = story33[a].replace("]", "")
    story33[a] = story33[a].replace("<p>", "")
    story33[a] = story33[a].replace("</p>", "")
    story33[a] = story33[a].replace("  ", "")

    print("#############################[제품 가격 가져오는중]##########################")
    story44.append(str(soup.select(
        "#{} > div > a > div.pname > div.price_info.cfix > span > strong".format(ing[a]))) + "원")

    story44[a] = story44[a].replace("[", "")
    story44[a] = story44[a].replace("]", "")
    story44[a] = story44[a].replace("</strong>", "")
    story44[a] = story44[a].replace('<strong class="sale_price">', "")


    print("story33[a] : ",story33[a])
    print("story44[a] : ", story44[a])


for a in range(0,5):
    url2 = "{}".format(ing2[a])
    print(url2)
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")

    print("##############################[리뷰수 가져오는중]###########################")
    story55.append(str(soup.select(
        "#tabMenuDetail2 > i")))
    story55[a] = story55[a].replace("[", "")
    story55[a] = story55[a].replace("]", "")
    story55[a] = story55[a].replace("(", "")
    story55[a] = story55[a].replace(")", "")
    story55[a] = story55[a].replace("<i>", "")
    story55[a] = story55[a].replace("</i>", "")
    story55[a] = story55[a].replace("'", "")
    story55[a] = story55[a] + "건"
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print("story55 : ", story55)
    print(len(story55[a]))


    print("##############################[이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select("#productImg > div > img")))
    story66[a] = story66[a].replace('<img alt="" onerror="this.src=', "")
    story66[a] = story66[a].replace('https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/img/product/no_image.gif', "")
    story66[a] = story66[a].replace("'", "")
    story66[a] = story66[a].replace('src="', "")
    story66[a] = story66[a].replace('"/>', "")
    story66[a] = story66[a].replace(' ', "")
    story66[a] = story66[a].replace('[', "")
    story66[a] = story66[a].replace(']', "")
    story66[a] = story66[a].replace('"', "")
    print("story66[a] : " , story66[a])


    show_now.append(story33[a] + "," + story44[a] + "," + story55[a] + "," + story66[a])
    print(show_now[a])
    sql = 'insert into outers values("11번가", "코트", {}, "{}", "{}", "{}", "{}")'.format(a+1, story33[a], story44[a], story55[a], ing2[a])
    cur.execute(sql)
    conn.commit()
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("stpry66 : " , story66[0])
print("len(story66) : {}".format(len(story66)))

#이미지 다운로드

try:

    for i in range(0,5):
        img_src = story66[i]
        print("img_src : " , img_src)
        img_src = img_src.split(",")
        print("img_src[0] : " , img_src[0])
        print('img/11번가_{}.jpg'.format(num))
        urlretrieve(img_src[0] , '/home/aiot02/PycharmProjects/pythonProject6/HI/11번가_코트{}.jpg'.format(num))       # 이미지 저장 경로 / 이미지 이름
        print("성공")
        num += 1

except:

    print("실패")
    pass


##########################################################################################################################################################################################
#패딩

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=2&dispCtgrNo=1012008"
print(url)
source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")


a = 0
i = 1
ing = []         ###########제품 이름 클래스#########
ing2 = []        ###########제품 구매 사이트#########
show_now = []
story33 = []     ##########제품 이름###########
story44 = []     ##########제품 가격###########
story55 = []     ##########제품 평점###########
story66 = []     ##########제품 이미지#########


print("#########################[이름 클래스 받아오는중]#######################")
story22 = soup.findAll('a',{'target':'_top'})
for a in range(0,5):
    print("a ::" , a)
    ing.append("thisClick"+str(story22[a]['class']))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace("prd", "")
    ing[a] = ing[a].replace("'", "")
    print("ing[a] : ", ing[a])

    print("######################[제품 구매 접속 사이트 받아오는중]###########################")
    ing2.append("thisClick" + str(story22[a]['href']))
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace("thisClick", "")
    ing2[a] = ing2[a].replace("'", "")
    print("ing2[a] : ", ing2[a])

print("####################[가져온 갯수만큼 반복하는중]###########################")
for a in range(0,5):

    print("#############################[제품 이름 가져오는중]##########################")
    story33.append(str(soup.select(
            "#{} > div > a > div.pname > p".format(ing[a]))))

    story33[a] = story33[a].replace("[", "")
    story33[a] = story33[a].replace("]", "")
    story33[a] = story33[a].replace("<p>", "")
    story33[a] = story33[a].replace("</p>", "")
    story33[a] = story33[a].replace("  ", "")

    print("#############################[제품 가격 가져오는중]##########################")
    story44.append(str(soup.select(
        "#{} > div > a > div.pname > div.price_info.cfix > span > strong".format(ing[a]))) + "원")

    story44[a] = story44[a].replace("[", "")
    story44[a] = story44[a].replace("]", "")
    story44[a] = story44[a].replace("</strong>", "")
    story44[a] = story44[a].replace('<strong class="sale_price">', "")


    print("story33[a] : ",story33[a])
    print("story44[a] : ", story44[a])


for a in range(0,5):
    url2 = "{}".format(ing2[a])
    print(url2)
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")

    print("##############################[리뷰수 가져오는중]###########################")
    story55.append(str(soup.select(
        "#tabMenuDetail2 > i")))
    story55[a] = story55[a].replace("[", "")
    story55[a] = story55[a].replace("]", "")
    story55[a] = story55[a].replace("(", "")
    story55[a] = story55[a].replace(")", "")
    story55[a] = story55[a].replace("<i>", "")
    story55[a] = story55[a].replace("</i>", "")
    story55[a] = story55[a].replace("'", "")
    story55[a] = story55[a] + "건"
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print("story55 : ", story55)
    print(len(story55[a]))


    print("##############################[이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select("#productImg > div > img")))
    story66[a] = story66[a].replace('<img alt="" onerror="this.src=', "")
    story66[a] = story66[a].replace('https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/img/product/no_image.gif', "")
    story66[a] = story66[a].replace("'", "")
    story66[a] = story66[a].replace('src="', "")
    story66[a] = story66[a].replace('"/>', "")
    story66[a] = story66[a].replace(' ', "")
    story66[a] = story66[a].replace('[', "")
    story66[a] = story66[a].replace(']', "")
    story66[a] = story66[a].replace('"', "")
    print("story66[a] : " , story66[a])

    show_now.append(story33[a] + "," + story44[a] + "," + story55[a] + "," + story66[a])
    print(show_now[a])
    sql = 'insert into outers values("11번가", "패딩", {}, "{}", "{}", "{}", "{}")'.format(a+1, story33[a], story44[a], story55[a], ing2[a])
    cur.execute(sql)
    conn.commit()


print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("stpry66 : " , story66[0])
print("len(story66) : {}".format(len(story66)))

#이미지 다운로드

try:

    for i in range(0,5):
        img_src = story66[i]
        print("img_src : " , img_src)
        img_src = img_src.split(",")
        print("img_src[0] : " , img_src[0])
        print('img/11번가_{}.jpg'.format(num))
        urlretrieve(img_src[0] , '/home/aiot02/PycharmProjects/pythonProject6/HI/11번가_패딩{}.jpg'.format(num))    # 이미지 저장 경로 / 이미지 이름
        print("성공")
        num += 1

except:

    print("실패")
    pass

################################GMARCKET 클롤링############################
################################GMARCKET 클롤링############################


#url## -G마켓 기준
# 맨투맨 - http://browse.gmarket.co.kr/list?category=300023507&v=l&s=8
# 셔츠 - http://browse.gmarket.co.kr/list?category=200000649&s=8
# 청바지 - http://browse.gmarket.co.kr/list?category=200000667&s=8
# 슬랙스 - http://browse.gmarket.co.kr/list?category=300026697&v=l&s=8
# 코트 - http://browse.gmarket.co.kr/list?category=200000493&s=8
# 패딩 - http://browse.gmarket.co.kr/list?category=300006568&s=8

#####################[G마켓]######################

a = 0
i = 1
num = 0
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

######################################################################################################################################################################################
##맨투맨
for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.gmarket.co.kr/list?category=300023507&v=l&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    ing.append(str(story22[a]))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('"', "")
    ing[a] = ing[a].replace('<span class=text__item', "")
    ing[a] = ing[a].replace("title= ", "")
    ing[a] = ing[a].split(">")
    ing[a][0] = ing[a][0].replace('title=', "")
    ing[a] = ing[a][0]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text text__value">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-score > ul > li.list-item.list-item__feedback-count > span.text".format(i))))
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])

    print("######################[제품 번호 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__image > a".format(i))))
    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('data-montelena-page_type="300"', "")
    ing4[a] = ing4[a].replace('data-montelena-page="1"', "")
    ing4[a] = ing4[a].replace('data-montelena-keyword="300023507"', "")
    ing4[a] = ing4[a].replace('data-montelena-tracking_id="e4098p4052r3217m6112d5s1022i{}"'.format(i), "")
    ing4[a] = ing4[a].replace('class="image__item" src="//pics.gmarket.co.kr/pc/single/kr/snowwhite/common/lazyload_image_itemcard_300x300.png"/>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('data-montelena-request_id=', "")
    ing4[a] = ing4[a].replace('data-montelena-tab="a"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier="0"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsevent="click"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsimpression="true"', "")
    ing4[a] = ing4[a].replace('data-montelena-utstype="item"', "")
    ing4[a] = ing4[a].replace('target="_blank"><img alt="이미지로딩중"', "")
    ing4[a] = ing4[a].replace('data-montelena-view_type="l"', "")
    ing4[a] = ing4[a].replace('data-montelena-goodscode=', "")
    ing4[a] = ing4[a].replace('data-montelena-device_type="100"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier_asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('data-montelena-asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('<a class="link__item image--loading" data-montelena-acode="200003323"', "")
    ing4[a] = ing4[a].replace('</span>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")
    ing4[a] = ing4[a].replace('    ', "")
    ing4[a] = ing4[a].replace('   ', "")
    ing4[a] = ing4[a].split('"')

    print("ing4[a] : ", ing4[a])
    print("ing4[a][1] :" ,ing4[a][1])
    print("ing4 ::::: ", ing4[a][5])

    sql = 'insert into shirts values("G마켓", "맨투맨", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a][5])
    cur.execute(sql)
    conn.commit()

    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(ing4[a][1])
    story66[a] = ("https://gdimg.gmarket.co.kr/"+story66[a]+"/still/600")
    print("story66[a] : " ,story66[a])
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = story66[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("G마켓_맨투맨"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass

#######################################################################################################################################################################################
####셔츠
a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

for a in range(0,5):

    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.gmarket.co.kr/list?category=200000649&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    ing.append(str(story22[a]))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('"', "")
    ing[a] = ing[a].replace('<span class=text__item', "")
    ing[a] = ing[a].replace("title= ", "")
    ing[a] = ing[a].split(">")
    ing[a][0] = ing[a][0].replace('title=', "")
    ing[a] = ing[a][0]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text text__value">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-score > ul > li.list-item.list-item__feedback-count > span.text".format(i))))
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])

    print("######################[제품 번호 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__image > a".format(i))))
    ing4.append(story55[a])
    print("ing4 : ", ing4)
    ing4[a] = ing4[a].replace('data-montelena-page_type="300"', "")
    ing4[a] = ing4[a].replace('data-montelena-page="1"', "")
    ing4[a] = ing4[a].replace('data-montelena-keyword="300023507"', "")
    ing4[a] = ing4[a].replace('data-montelena-tracking_id="e4098p4052r3217m6112d5s1022i{}"'.format(i), "")
    ing4[a] = ing4[a].replace('class="image__item" src="//pics.gmarket.co.kr/pc/single/kr/snowwhite/common/lazyload_image_itemcard_300x300.png"/>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('data-montelena-request_id=', "")
    ing4[a] = ing4[a].replace('data-montelena-tab="a"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier="0"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsevent="click"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsimpression="true"', "")
    ing4[a] = ing4[a].replace('data-montelena-utstype="item"', "")
    ing4[a] = ing4[a].replace('target="_blank"><img alt="이미지로딩중"', "")
    ing4[a] = ing4[a].replace('data-montelena-view_type="l"', "")
    ing4[a] = ing4[a].replace('data-montelena-goodscode=', "")
    ing4[a] = ing4[a].replace('data-montelena-device_type="100"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier_asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('data-montelena-asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('<a class="link__item image--loading" data-montelena-acode="200003323"', "")
    ing4[a] = ing4[a].replace('</span>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")
    ing4[a] = ing4[a].replace('    ', "")
    ing4[a] = ing4[a].replace('   ', "")
    ing4[a] = ing4[a].split('"')

    print("ing4[a] : ", ing4[a])
    print("ing4[a][1] :" ,ing4[a][1])
    if a == 2:
        if len(ing4[a]) < 10:
            sql = 'insert into shirts values("G마켓", "셔츠", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a],ing2[a],ing3[a], ing4[a][7])
            cur.execute(sql)
            conn.commit()
        else:
            sql = 'insert into shirts values("G마켓", "셔츠", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a],ing2[a],ing3[a], ing4[a][9])
            cur.execute(sql)
            conn.commit()
    else:
        sql = 'insert into shirts values("G마켓", "셔츠", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a][7])
        cur.execute(sql)
        conn.commit()

    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(ing4[a][1])
    story66[a] = ("https://gdimg.gmarket.co.kr/"+story66[a]+"/still/600")
    print("story66[a] : " ,story66[a])

    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = story66[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("G마켓_셔츠"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass


#######################################################################################################################################################################################
####청바지
a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

for a in range(0,5):

    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.gmarket.co.kr/list?category=200000667&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    ing.append(str(story22[a]))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('"', "")
    ing[a] = ing[a].replace('<span class=text__item', "")
    ing[a] = ing[a].replace("title= ", "")
    ing[a] = ing[a].split(">")
    ing[a][0] = ing[a][0].replace('title=', "")
    ing[a] = ing[a][0]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text text__value">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-score > ul > li.list-item.list-item__feedback-count > span.text".format(i))))
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])

    print("######################[제품 번호 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__image > a".format(i))))
    ing4.append(story55[a])
    print("ing4 : ", ing4)
    ing4[a] = ing4[a].replace('data-montelena-page_type="300"', "")
    ing4[a] = ing4[a].replace('data-montelena-page="1"', "")
    ing4[a] = ing4[a].replace('data-montelena-keyword="300023507"', "")
    ing4[a] = ing4[a].replace('data-montelena-tracking_id="e4098p4052r3217m6112d5s1022i{}"'.format(i), "")
    ing4[a] = ing4[a].replace('class="image__item" src="//pics.gmarket.co.kr/pc/single/kr/snowwhite/common/lazyload_image_itemcard_300x300.png"/>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('data-montelena-request_id=', "")
    ing4[a] = ing4[a].replace('data-montelena-tab="a"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier="0"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsevent="click"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsimpression="true"', "")
    ing4[a] = ing4[a].replace('data-montelena-utstype="item"', "")
    ing4[a] = ing4[a].replace('target="_blank"><img alt="이미지로딩중"', "")
    ing4[a] = ing4[a].replace('data-montelena-view_type="l"', "")
    ing4[a] = ing4[a].replace('data-montelena-goodscode=', "")
    ing4[a] = ing4[a].replace('data-montelena-device_type="100"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier_asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('data-montelena-asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('<a class="link__item image--loading" data-montelena-acode="200003323"', "")
    ing4[a] = ing4[a].replace('</span>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")
    ing4[a] = ing4[a].replace('    ', "")
    ing4[a] = ing4[a].replace('   ', "")
    ing4[a] = ing4[a].split('"')

    print("ing4[a] : ", ing4[a])
    print("ing4[a][1] :" ,ing4[a][1])
    sql = 'insert into pants values("G마켓", "청바지", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a][7])
    cur.execute(sql)
    conn.commit()

    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(ing4[a][1])
    story66[a] = ("https://gdimg.gmarket.co.kr/"+story66[a]+"/still/600")
    print("story66[a] : " ,story66[a])

    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = story66[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("G마켓_청바지"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass

#######################################################################################################################################################################################
####슬랙스
a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

for a in range(0,5):

    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.gmarket.co.kr/list?category=300026697&v=l&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    ing.append(str(story22[a]))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('"', "")
    ing[a] = ing[a].replace('<span class=text__item', "")
    ing[a] = ing[a].replace("title= ", "")
    ing[a] = ing[a].split(">")
    ing[a][0] = ing[a][0].replace('title=', "")
    ing[a] = ing[a][0]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text text__value">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-score > ul > li.list-item.list-item__feedback-count > span.text".format(i))))
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])

    print("######################[제품 번호 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__image > a".format(i))))
    ing4.append(story55[a])
    print("ing4 : ", ing4)
    ing4[a] = ing4[a].replace('data-montelena-page_type="300"', "")
    ing4[a] = ing4[a].replace('data-montelena-page="1"', "")
    ing4[a] = ing4[a].replace('data-montelena-keyword="300023507"', "")
    ing4[a] = ing4[a].replace('data-montelena-tracking_id="e4098p4052r3217m6112d5s1022i{}"'.format(i), "")
    ing4[a] = ing4[a].replace('class="image__item" src="//pics.gmarket.co.kr/pc/single/kr/snowwhite/common/lazyload_image_itemcard_300x300.png"/>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('data-montelena-request_id=', "")
    ing4[a] = ing4[a].replace('data-montelena-tab="a"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier="0"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsevent="click"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsimpression="true"', "")
    ing4[a] = ing4[a].replace('data-montelena-utstype="item"', "")
    ing4[a] = ing4[a].replace('target="_blank"><img alt="이미지로딩중"', "")
    ing4[a] = ing4[a].replace('data-montelena-view_type="l"', "")
    ing4[a] = ing4[a].replace('data-montelena-goodscode=', "")
    ing4[a] = ing4[a].replace('data-montelena-device_type="100"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier_asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('data-montelena-asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('<a class="link__item image--loading" data-montelena-acode="200003323"', "")
    ing4[a] = ing4[a].replace('</span>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")
    ing4[a] = ing4[a].replace('    ', "")
    ing4[a] = ing4[a].replace('   ', "")
    ing4[a] = ing4[a].split('"')

    print("ing4[a] : ", ing4[a])
    print("ing4[a][1] :" ,ing4[a][1])
    sql = 'insert into pants values("G마켓", "슬랙스", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a][7])
    cur.execute(sql)
    conn.commit()

    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(ing4[a][1])
    story66[a] = ("https://gdimg.gmarket.co.kr/"+story66[a]+"/still/600")
    print("story66[a] : " ,story66[a])

    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = story66[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("G마켓_슬랙스"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass


#######################################################################################################################################################################################
####코트
a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

for a in range(0,5):

    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.gmarket.co.kr/list?category=200000493&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    ing.append(str(story22[a]))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('"', "")
    ing[a] = ing[a].replace('<span class=text__item', "")
    ing[a] = ing[a].replace("title= ", "")
    ing[a] = ing[a].split(">")
    ing[a][0] = ing[a][0].replace('title=', "")
    ing[a] = ing[a][0]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text text__value">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-score > ul > li.list-item.list-item__feedback-count > span.text".format(i))))
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])

    print("######################[제품 번호 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__image > a".format(i))))
    ing4.append(story55[a])
    print("ing4 : ", ing4)
    ing4[a] = ing4[a].replace('data-montelena-page_type="300"', "")
    ing4[a] = ing4[a].replace('data-montelena-page="1"', "")
    ing4[a] = ing4[a].replace('data-montelena-keyword="300023507"', "")
    ing4[a] = ing4[a].replace('data-montelena-tracking_id="e4098p4052r3217m6112d5s1022i{}"'.format(i), "")
    ing4[a] = ing4[a].replace('class="image__item" src="//pics.gmarket.co.kr/pc/single/kr/snowwhite/common/lazyload_image_itemcard_300x300.png"/>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('data-montelena-request_id=', "")
    ing4[a] = ing4[a].replace('data-montelena-tab="a"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier="0"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsevent="click"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsimpression="true"', "")
    ing4[a] = ing4[a].replace('data-montelena-utstype="item"', "")
    ing4[a] = ing4[a].replace('target="_blank"><img alt="이미지로딩중"', "")
    ing4[a] = ing4[a].replace('data-montelena-view_type="l"', "")
    ing4[a] = ing4[a].replace('data-montelena-goodscode=', "")
    ing4[a] = ing4[a].replace('data-montelena-device_type="100"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier_asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('data-montelena-asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('<a class="link__item image--loading" data-montelena-acode="200003323"', "")
    ing4[a] = ing4[a].replace('</span>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")
    ing4[a] = ing4[a].replace('    ', "")
    ing4[a] = ing4[a].replace('   ', "")
    ing4[a] = ing4[a].split('"')

    print("ing4[a] : ", ing4[a])
    print("ing4[a][1] :" ,ing4[a][1])
    sql = 'insert into outers values("G마켓", "코트", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a][7])
    cur.execute(sql)
    conn.commit()

    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(ing4[a][1])
    story66[a] = ("https://gdimg.gmarket.co.kr/"+story66[a]+"/still/600")
    print("story66[a] : " ,story66[a])

    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = story66[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("G마켓_코트"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass


#######################################################################################################################################################################################
####패딩
a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

for a in range(0,5):

    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.gmarket.co.kr/list?category=300006568&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    ing.append(str(story22[a]))
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('"', "")
    ing[a] = ing[a].replace('<span class=text__item', "")
    ing[a] = ing[a].replace("title= ", "")
    ing[a] = ing[a].split(">")
    ing[a][0] = ing[a][0].replace('title=', "")
    ing[a] = ing[a][0]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text text__value">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__information > div.box__information-score > ul > li.list-item.list-item__feedback-count > span.text".format(i))))
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])

    print("######################[제품 번호 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section__inner-content-body-container > div:nth-child(2) > div:nth-child({}) > div > div.box__image > a".format(i))))
    ing4.append(story55[a])
    print("ing4 : ", ing4)
    ing4[a] = ing4[a].replace('data-montelena-page_type="300"', "")
    ing4[a] = ing4[a].replace('data-montelena-page="1"', "")
    ing4[a] = ing4[a].replace('data-montelena-keyword="300023507"', "")
    ing4[a] = ing4[a].replace('data-montelena-tracking_id="e4098p4052r3217m6112d5s1022i{}"'.format(i), "")
    ing4[a] = ing4[a].replace('class="image__item" src="//pics.gmarket.co.kr/pc/single/kr/snowwhite/common/lazyload_image_itemcard_300x300.png"/>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('data-montelena-request_id=', "")
    ing4[a] = ing4[a].replace('data-montelena-tab="a"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier="0"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsevent="click"', "")
    ing4[a] = ing4[a].replace('data-montelena-utsimpression="true"', "")
    ing4[a] = ing4[a].replace('data-montelena-utstype="item"', "")
    ing4[a] = ing4[a].replace('target="_blank"><img alt="이미지로딩중"', "")
    ing4[a] = ing4[a].replace('data-montelena-view_type="l"', "")
    ing4[a] = ing4[a].replace('data-montelena-goodscode=', "")
    ing4[a] = ing4[a].replace('data-montelena-device_type="100"', "")
    ing4[a] = ing4[a].replace('data-montelena-tier_asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('data-montelena-asn="{}"'.format(i), "")
    ing4[a] = ing4[a].replace('<a class="link__item image--loading" data-montelena-acode="200003323"', "")
    ing4[a] = ing4[a].replace('</span>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")
    ing4[a] = ing4[a].replace('    ', "")
    ing4[a] = ing4[a].replace('   ', "")
    ing4[a] = ing4[a].split('"')

    print("ing4[a] : ", ing4[a])
    print("ing4[a][1] :" ,ing4[a][1])
    sql = 'insert into outers values("G마켓", "패딩", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a][7])
    cur.execute(sql)
    conn.commit()

    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(ing4[a][1])
    story66[a] = ("https://gdimg.gmarket.co.kr/"+story66[a]+"/still/600")
    print("story66[a] : " ,story66[a])

    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = story66[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("G마켓_패딩"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass
################################GMARCKET 클롤링    끝   ############################
################################GMARCKET 클롤링    끝   ############################


# #url## - 옥션 기준
# 맨투맨 - http://browse.auction.co.kr/list?category=13050900&s=8
# 셔츠 - http://browse.auction.co.kr/list?category=13060000&s=8
# 청바지 - http://browse.auction.co.kr/list?category=13260000&s=8
# 슬랙스 - http://browse.auction.co.kr/list?category=13240100&s=8
# 코트 - http://browse.auction.co.kr/list?category=13130000&s=8
# 패딩 - http://browse.auction.co.kr/list?category=13091000&s=8

#####################[옥션]######################

a = 0
i = 1
num = 0
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

#######################################################################################################################################################################################
###맨투맨
for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.auction.co.kr/list?category=13050900&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_title > span > a > span.text--title".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('<span class="text--title">', "")
    ing[a] = ing[a].replace("</span>", "")
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('<!-- -->', "")
    ing[a] = ing[a]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_price > span.price_seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text--price_seller">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_score > ul > li.item.reviewcnt > span.text--reviewcnt".format(i))))
    if len(story44[a]) == 2 :
        story44[a] = "0"
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text--reviewcnt">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a].replace('후기', "")
    ing3[a] = ing3[a].replace(' ', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_img > a".format(i))))
    print("story55[a] : " ,story55[a])
    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('<a class="link--itemcard image--loading" href=', "")
    ing4[a] = ing4[a].replace('target="_blank"><div class="lazyload-placeholder"', "")
    ing4[a] = ing4[a].replace('style="height:100%">', "")
    ing4[a] = ing4[a].replace('</div>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")


    print("ing4[a] : ", ing4[a])

    sql = 'insert into shirts values("옥션", "맨투맨", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()
    i += 1

    url2 = ing4[a]
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")


    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select(
        "#content > div.item-topinfowrap > div.item-topgallerywrap > div > div.box__viewer-container > ul > li.on > a > img")))
    print("story66[a] :" , story66[a])
    story66[a] = story66[a].split('//')
    ing5.append("https://" + story66[a][3])
    ing5[a] = ing5[a].replace('"', "")
    ing5[a] = ing5[a].replace('/>', "")
    ing5[a] = ing5[a].replace('[', "")
    ing5[a] = ing5[a].replace(']', "")
    print("ing5[a] : " , ing5[a])

    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing5[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("옥션_맨투맨"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass

#######################################################################################################################################################################################
###셔츠

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []


for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.auction.co.kr/list?category=13060000&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_title > span > a > span.text--title".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('<span class="text--title">', "")
    ing[a] = ing[a].replace("</span>", "")
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('<!-- -->', "")
    ing[a] = ing[a]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_price > span.price_seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text--price_seller">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_score > ul > li.item.reviewcnt > span.text--reviewcnt".format(i))))
    if len(story44[a]) == 2 :
        story44[a] = "0"
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text--reviewcnt">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a].replace('후기', "")
    ing3[a] = ing3[a].replace(' ', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_img > a".format(i))))
    print("story55[a] : " ,story55[a])
    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('<a class="link--itemcard image--loading" href=', "")
    ing4[a] = ing4[a].replace('target="_blank"><div class="lazyload-placeholder"', "")
    ing4[a] = ing4[a].replace('style="height:100%">', "")
    ing4[a] = ing4[a].replace('</div>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")


    print("ing4[a] : ", ing4[a])

    sql = 'insert into shirts values("옥션", "셔츠", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()
    i += 1

    url2 = ing4[a]
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")


    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select(
        "#content > div.item-topinfowrap > div.item-topgallerywrap > div > div.box__viewer-container > ul > li.on > a > img")))
    print("story66[a] :" , story66[a])
    story66[a] = story66[a].split('//')
    ing5.append("https://" + story66[a][3])
    ing5[a] = ing5[a].replace('"', "")
    ing5[a] = ing5[a].replace('/>', "")
    ing5[a] = ing5[a].replace('[', "")
    ing5[a] = ing5[a].replace(']', "")
    print("ing5[a] : " , ing5[a])
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing5[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("옥션_셔츠"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass


#######################################################################################################################################################################################
###청바지

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []


for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.auction.co.kr/list?category=13260000&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_title > span > a > span.text--title".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('<span class="text--title">', "")
    ing[a] = ing[a].replace("</span>", "")
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('<!-- -->', "")
    ing[a] = ing[a]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_price > span.price_seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text--price_seller">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_score > ul > li.item.reviewcnt > span.text--reviewcnt".format(i))))
    if len(story44[a]) == 2 :
        story44[a] = "0"
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text--reviewcnt">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a].replace('후기', "")
    ing3[a] = ing3[a].replace(' ', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_img > a".format(i))))
    print("story55[a] : " ,story55[a])
    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('<a class="link--itemcard image--loading" href=', "")
    ing4[a] = ing4[a].replace('target="_blank"><div class="lazyload-placeholder"', "")
    ing4[a] = ing4[a].replace('style="height:100%">', "")
    ing4[a] = ing4[a].replace('</div>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")


    print("ing4[a] : ", ing4[a])

    sql = 'insert into pants values("옥션", "청바지", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()
    i += 1

    url2 = ing4[a]
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")


    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select(
        "#content > div.item-topinfowrap > div.item-topgallerywrap > div > div.box__viewer-container > ul > li.on > a > img")))
    print("story66[a] :" , story66[a])
    story66[a] = story66[a].split('//')
    ing5.append("https://" + story66[a][3])
    ing5[a] = ing5[a].replace('"', "")
    ing5[a] = ing5[a].replace('/>', "")
    ing5[a] = ing5[a].replace('[', "")
    ing5[a] = ing5[a].replace(']', "")
    print("ing5[a] : " , ing5[a])
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing5[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("옥션_청바지"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass


#######################################################################################################################################################################################
###슬랙스

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []


for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.auction.co.kr/list?category=13240100&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_title > span > a > span.text--title".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('<span class="text--title">', "")
    ing[a] = ing[a].replace("</span>", "")
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('<!-- -->', "")
    ing[a] = ing[a]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_price > span.price_seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text--price_seller">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_score > ul > li.item.reviewcnt > span.text--reviewcnt".format(i))))
    if len(story44[a]) == 2 :
        story44[a] = "0"
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text--reviewcnt">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a].replace('후기', "")
    ing3[a] = ing3[a].replace(' ', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_img > a".format(i))))
    print("story55[a] : " ,story55[a])
    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('<a class="link--itemcard image--loading" href=', "")
    ing4[a] = ing4[a].replace('target="_blank"><div class="lazyload-placeholder"', "")
    ing4[a] = ing4[a].replace('style="height:100%">', "")
    ing4[a] = ing4[a].replace('</div>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")


    print("ing4[a] : ", ing4[a])
    sql = 'insert into pants values("옥션", "슬랙스", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()
    i += 1

    url2 = ing4[a]
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")


    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select(
        "#content > div.item-topinfowrap > div.item-topgallerywrap > div > div.box__viewer-container > ul > li.on > a > img")))
    print("story66[a] :" , story66[a])
    story66[a] = story66[a].split('//')
    ing5.append("https://" + story66[a][3])
    ing5[a] = ing5[a].replace('"', "")
    ing5[a] = ing5[a].replace('/>', "")
    ing5[a] = ing5[a].replace('[', "")
    ing5[a] = ing5[a].replace(']', "")
    print("ing5[a] : " , ing5[a])
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing5[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("옥션_슬랙스"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass


#######################################################################################################################################################################################
###코트

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []


for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.auction.co.kr/list?category=13130000&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_title > span > a > span.text--title".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('<span class="text--title">', "")
    ing[a] = ing[a].replace("</span>", "")
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('<!-- -->', "")
    ing[a] = ing[a]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_price > span.price_seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text--price_seller">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_score > ul > li.item.reviewcnt > span.text--reviewcnt".format(i))))
    if len(story44[a]) == 2 :
        story44[a] = "0"
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text--reviewcnt">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a].replace('후기', "")
    ing3[a] = ing3[a].replace(' ', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_img > a".format(i))))
    print("story55[a] : " ,story55[a])
    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('<a class="link--itemcard image--loading" href=', "")
    ing4[a] = ing4[a].replace('target="_blank"><div class="lazyload-placeholder"', "")
    ing4[a] = ing4[a].replace('style="height:100%">', "")
    ing4[a] = ing4[a].replace('</div>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")


    print("ing4[a] : ", ing4[a])
    sql = 'insert into outers values("옥션", "코트", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()
    i += 1

    url2 = ing4[a]
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")


    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select(
        "#content > div.item-topinfowrap > div.item-topgallerywrap > div > div.box__viewer-container > ul > li.on > a > img")))
    print("story66[a] :" , story66[a])
    story66[a] = story66[a].split('//')
    ing5.append("https://" + story66[a][3])
    ing5[a] = ing5[a].replace('"', "")
    ing5[a] = ing5[a].replace('/>', "")
    ing5[a] = ing5[a].replace('[', "")
    ing5[a] = ing5[a].replace(']', "")
    print("ing5[a] : " , ing5[a])
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing5[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("옥션_코트"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass

#######################################################################################################################################################################################
###패딩

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 번호#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []


for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "http://browse.auction.co.kr/list?category=13091000&s=8"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_title > span > a > span.text--title".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('<span class="text--title">', "")
    ing[a] = ing[a].replace("</span>", "")
    ing[a] = ing[a].replace("[", "")
    ing[a] = ing[a].replace("]", "")
    ing[a] = ing[a].replace('<!-- -->', "")
    ing[a] = ing[a]

    print("ing[a] : ", ing[a])


    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_major > div.area--itemcard_price > span.price_seller > strong".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace("[", "")
    ing2[a] = ing2[a].replace("]", "")
    ing2[a] = ing2[a].replace('<strong class="format-price__value">', "")
    ing2[a] = ing2[a].replace('</strong>', "")
    ing2[a] = ing2[a].replace('<strong class="text--price_seller">', "")
    print("ing2[a] : " , ing2[a])

    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_info > div.section--itemcard_info_score > ul > li.item.reviewcnt > span.text--reviewcnt".format(i))))
    if len(story44[a]) == 2 :
        story44[a] = "0"
    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a].replace('<span class="text--reviewcnt">', "")
    ing3[a] = ing3[a].replace("(", "")
    ing3[a] = ing3[a].replace(")", "")
    ing3[a] = ing3[a].replace("<!-- -->", "")
    ing3[a] = ing3[a].replace('</span>', "")
    ing3[a] = ing3[a].replace('후기', "")
    ing3[a] = ing3[a].replace(' ', "")
    ing3[a] = ing3[a] + "건"

    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#section--inner_content_body_container > div:nth-child(2) > div:nth-child({}) > div > div > div.section--itemcard_img > a".format(i))))
    print("story55[a] : " ,story55[a])
    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('<a class="link--itemcard image--loading" href=', "")
    ing4[a] = ing4[a].replace('target="_blank"><div class="lazyload-placeholder"', "")
    ing4[a] = ing4[a].replace('style="height:100%">', "")
    ing4[a] = ing4[a].replace('</div>', "")
    ing4[a] = ing4[a].replace('</a>', "")
    ing4[a] = ing4[a].replace('href=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace('[', "")
    ing4[a] = ing4[a].replace(']', "")


    print("ing4[a] : ", ing4[a])
    sql = 'insert into outers values("옥션", "패딩", {}, "{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()

    i += 1

    url2 = ing4[a]
    source = requests.get(url2).text
    soup = BeautifulSoup(source, "html.parser")


    print("######################[제품 이미지 링크 가져오는중]###########################")
    story66.append(str(soup.select(
        "#content > div.item-topinfowrap > div.item-topgallerywrap > div > div.box__viewer-container > ul > li.on > a > img")))
    print("story66[a] :" , story66[a])
    story66[a] = story66[a].split('//')
    ing5.append("https://" + story66[a][3])
    ing5[a] = ing5[a].replace('"', "")
    ing5[a] = ing5[a].replace('/>', "")
    ing5[a] = ing5[a].replace('[', "")
    ing5[a] = ing5[a].replace(']', "")
    print("ing5[a] : " , ing5[a])
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing5[i]
        print(img_src)
        urlretrieve(img_src , '/home/aiot02/PycharmProjects/pythonProject6/HI/{}.jpg'.format("옥션_패딩"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass



######################[신세계TV]######################
######################[신세계TV]######################
######################[신세계TV]######################


##url## - 신세계TV 기준
#맨투맨 - https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EB%A7%A8%ED%88%AC%EB%A7%A8&trackSearchType=nomal
#셔츠 -  https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EC%85%94%EC%B8%A0&trackSearchType=nomal
#청바지 - https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EB%82%A8%EC%84%B1%EC%B2%AD%EB%B0%94%EC%A7%80&trackSearchType=nomal
#슬랙스 - https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EB%82%A8%EC%84%B1%EC%8A%AC%EB%9E%99%EC%8A%A4&trackSearchType=nomal
#코트 - https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EB%82%A8%EC%84%B1%EC%BD%94%ED%8A%B8&trackSearchType=nomal
#패딩 - https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EB%82%A8%EC%84%B1%ED%8C%A8%EB%94%A9&trackSearchType=nomal

######################[신세계TV]######################
num = 0

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 이미지#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

#######################################################################################################################################################################################
###맨투맨
for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EB%A7%A8%ED%88%AC%EB%A7%A8&trackSearchType=nomal"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    print("story22[a] : " , len(story22[a]))

    if len(story22[a]) == 2:
        print("실패")
        story22[a] = (str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i+1))))
        print("story22 :", story22)
        print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('</span>]', "")
    ing[a] = ing[a].replace('[<span class="_goodsName">', "")
    ing[a] = ing[a].replace("\r", "")
    ing[a] = ing[a].replace("\n", "")
    ing[a] = ing[a].replace("\t", "")
    ing[a] = ing[a].replace('', "")
    ing[a] = ing[a].replace('<span class="_tvDealYn" data-deal="Y">', "")
    ing[a] = ing[a].replace('  ', "")

    print("ing[a] : ", ing[a])




    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    print("len(story33[a] : " ,len(story33[a]))

    if len(story33[a]) == 0:
        print("실패")
        story33[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i+1)))
        print("story33 :", story33)
        print("story33[a] : ", story33[a])


    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace('[<span class="_bestPrice">', "")
    ing2[a] = ing2[a].replace("</span>]", "")

    print("ing2[a] : " , ing2[a])



    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i))))
    print("story44 : " ,story44)
    print("story44[a] : ", story44[a])
    print("len(story44[a] : " ,len(story44[a]))


    if i == 5 and len(story44[a]) == 2:
        print("실패")
        story44[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i+1)))
        print("story44 :", story44)
        print("story44[a] : ", story44[a])

    if len(story44[a]) == 2:
        story44[a] = '0'

    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("<em>", "")
    ing3[a] = ing3[a].replace("</em>", "")
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a] + "건"

    print("ing3 :" , ing3)
    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i))))
    print("story55 : ", story55)
    print("story55[a] : ", story55[a])
    print("len(story55[a] : ", len(story55[a]))

    if i == 5 and len(story55[a]) == 2:
        print("실패")
        story55[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i+1)))
        print("story55 :", story55)
        print("story55[a] : ", story55[a])

    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('[<img alt=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace("'", "")
    ing4[a] = ing4[a].replace("onerror=this.src=/resources/web/img/onerror/s245x245.png", "")
    ing4[a] = ing4[a].replace('class=_image lazy', "")
    ing4[a] = ing4[a].replace('src', "")
    ing4[a] = ing4[a].replace('/>]', "")
    ing4[a] = ing4[a].replace('  ', "")
    ing4[a] = ing4[a].split("=")
    ing4[a] = ing4[a][1]

    print("ing4[a] : ", ing4[a])
    print("ing4 :", ing4)

    sql = 'insert into shirts values("신세계", "맨투맨", {},"{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()



    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing4[i]
        print("img_src : ",img_src)
        print('./img/{}.jpg'.format("신세계_"+str(num)))
        urlretrieve(img_src , './HI/{}.jpg'.format("신세계_맨투맨"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass


#######################################################################################################################################################################################
###셔츠

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 이미지#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EC%85%94%EC%B8%A0&trackSearchType=nomal"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    print("story22[a] : " , len(story22[a]))

    if len(story22[a]) == 2:
        print("실패")
        story22[a] = (str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i+1))))
        print("story22 :", story22)
        print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('</span>]', "")
    ing[a] = ing[a].replace('[<span class="_goodsName">', "")
    ing[a] = ing[a].replace("\r", "")
    ing[a] = ing[a].replace("\n", "")
    ing[a] = ing[a].replace("\t", "")
    ing[a] = ing[a].replace('', "")
    ing[a] = ing[a].replace('<span class="_tvDealYn" data-deal="Y">', "")
    ing[a] = ing[a].replace('  ', "")

    print("ing[a] : ", ing[a])




    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    print("len(story33[a] : " ,len(story33[a]))

    if len(story33[a]) == 0:
        print("실패")
        story33[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i+1)))
        print("story33 :", story33)
        print("story33[a] : ", story33[a])


    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace('[<span class="_bestPrice">', "")
    ing2[a] = ing2[a].replace("</span>]", "")

    print("ing2[a] : " , ing2[a])



    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i))))
    print("story44 : " ,story44)
    print("story44[a] : ", story44[a])
    print("len(story44[a] : " ,len(story44[a]))


    if i == 5 and len(story44[a]) == 2:
        print("실패")
        story44[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i+1)))
        print("story44 :", story44)
        print("story44[a] : ", story44[a])

    if len(story44[a]) == 2:
        story44[a] = '0'

    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("<em>", "")
    ing3[a] = ing3[a].replace("</em>", "")
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a] + "건"

    print("ing3 :" , ing3)
    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i))))
    print("story55 : ", story55)
    print("story55[a] : ", story55[a])
    print("len(story55[a] : ", len(story55[a]))

    if i == 5 and len(story55[a]) == 2:
        print("실패")
        story55[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i+1)))
        print("story55 :", story55)
        print("story55[a] : ", story55[a])

    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('[<img alt=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace("'", "")
    ing4[a] = ing4[a].replace("onerror=this.src=/resources/web/img/onerror/s245x245.png", "")
    ing4[a] = ing4[a].replace('class=_image lazy', "")
    ing4[a] = ing4[a].replace('src', "")
    ing4[a] = ing4[a].replace('/>]', "")
    ing4[a] = ing4[a].replace('  ', "")
    ing4[a] = ing4[a].split("=")
    ing4[a] = ing4[a][1]

    print("ing4[a] : ", ing4[a])
    print("ing4 :", ing4)
    sql = 'insert into shirts values("신세계", "셔츠", {},"{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing4[i]
        print("img_src : ",img_src)
        print('./img/{}.jpg'.format("신세계_"+str(num)))
        urlretrieve(img_src , './HI/{}.jpg'.format("신세계_셔츠"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass


#######################################################################################################################################################################################
###청바지

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 이미지#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EB%82%A8%EC%84%B1%EC%B2%AD%EB%B0%94%EC%A7%80&trackSearchType=nomal"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    print("story22[a] : " , len(story22[a]))

    if len(story22[a]) == 2:
        print("실패")
        story22[a] = (str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i+1))))
        print("story22 :", story22)
        print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('</span>]', "")
    ing[a] = ing[a].replace('[<span class="_goodsName">', "")
    ing[a] = ing[a].replace("\r", "")
    ing[a] = ing[a].replace("\n", "")
    ing[a] = ing[a].replace("\t", "")
    ing[a] = ing[a].replace('', "")
    ing[a] = ing[a].replace('<span class="_tvDealYn" data-deal="Y">', "")
    ing[a] = ing[a].replace('  ', "")

    print("ing[a] : ", ing[a])




    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    print("len(story33[a] : " ,len(story33[a]))

    if len(story33[a]) == 0:
        print("실패")
        story33[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i+1)))
        print("story33 :", story33)
        print("story33[a] : ", story33[a])


    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace('[<span class="_bestPrice">', "")
    ing2[a] = ing2[a].replace("</span>]", "")

    print("ing2[a] : " , ing2[a])



    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i))))
    print("story44 : " ,story44)
    print("story44[a] : ", story44[a])
    print("len(story44[a] : " ,len(story44[a]))


    if i == 5 and len(story44[a]) == 2:
        print("실패")
        story44[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i+1)))
        print("story44 :", story44)
        print("story44[a] : ", story44[a])

    if len(story44[a]) == 2:
        story44[a] = '0'

    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("<em>", "")
    ing3[a] = ing3[a].replace("</em>", "")
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a] + "건"

    print("ing3 :" , ing3)
    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i))))
    print("story55 : ", story55)
    print("story55[a] : ", story55[a])
    print("len(story55[a] : ", len(story55[a]))

    if i == 5 and len(story55[a]) == 2:
        print("실패")
        story55[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i+1)))
        print("story55 :", story55)
        print("story55[a] : ", story55[a])

    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('[<img alt=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace("'", "")
    ing4[a] = ing4[a].replace("onerror=this.src=/resources/web/img/onerror/s245x245.png", "")
    ing4[a] = ing4[a].replace('class=_image lazy', "")
    ing4[a] = ing4[a].replace('src', "")
    ing4[a] = ing4[a].replace('/>]', "")
    ing4[a] = ing4[a].replace('  ', "")
    ing4[a] = ing4[a].split("=")
    ing4[a] = ing4[a][1]

    print("ing4[a] : ", ing4[a])
    print("ing4 :", ing4)
    sql = 'insert into pants values("신세계", "청바지", {},"{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing4[i]
        print("img_src : ",img_src)
        print('./img/{}.jpg'.format("신세계_"+str(num)))
        urlretrieve(img_src , './HI/{}.jpg'.format("신세계_청바지"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass

#######################################################################################################################################################################################
###슬랙스

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 이미지#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EB%82%A8%EC%84%B1%EC%8A%AC%EB%9E%99%EC%8A%A4&trackSearchType=nomal"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    print("story22[a] : " , len(story22[a]))

    if len(story22[a]) == 2:
        print("실패")
        story22[a] = (str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i+1))))
        print("story22 :", story22)
        print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('</span>]', "")
    ing[a] = ing[a].replace('[<span class="_goodsName">', "")
    ing[a] = ing[a].replace("\r", "")
    ing[a] = ing[a].replace("\n", "")
    ing[a] = ing[a].replace("\t", "")
    ing[a] = ing[a].replace('', "")
    ing[a] = ing[a].replace('<span class="_tvDealYn" data-deal="Y">', "")
    ing[a] = ing[a].replace('  ', "")

    print("ing[a] : ", ing[a])




    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    print("len(story33[a] : " ,len(story33[a]))

    if len(story33[a]) == 0:
        print("실패")
        story33[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i+1)))
        print("story33 :", story33)
        print("story33[a] : ", story33[a])


    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace('[<span class="_bestPrice">', "")
    ing2[a] = ing2[a].replace("</span>]", "")

    print("ing2[a] : " , ing2[a])



    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i))))
    print("story44 : " ,story44)
    print("story44[a] : ", story44[a])
    print("len(story44[a] : " ,len(story44[a]))


    if i == 5 and len(story44[a]) == 2:
        print("실패")
        story44[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i+1)))
        print("story44 :", story44)
        print("story44[a] : ", story44[a])

    if len(story44[a]) == 2:
        story44[a] = '0'

    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("<em>", "")
    ing3[a] = ing3[a].replace("</em>", "")
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a] + "건"

    print("ing3 :" , ing3)
    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i))))
    print("story55 : ", story55)
    print("story55[a] : ", story55[a])
    print("len(story55[a] : ", len(story55[a]))

    if i == 5 and len(story55[a]) == 2:
        print("실패")
        story55[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i+1)))
        print("story55 :", story55)
        print("story55[a] : ", story55[a])

    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('[<img alt=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace("'", "")
    ing4[a] = ing4[a].replace("onerror=this.src=/resources/web/img/onerror/s245x245.png", "")
    ing4[a] = ing4[a].replace('class=_image lazy', "")
    ing4[a] = ing4[a].replace('src', "")
    ing4[a] = ing4[a].replace('/>]', "")
    ing4[a] = ing4[a].replace('  ', "")
    ing4[a] = ing4[a].split("=")
    ing4[a] = ing4[a][1]

    print("ing4[a] : ", ing4[a])
    print("ing4 :", ing4)
    sql = 'insert into pants values("신세계", "슬랙스", {},"{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing4[i]
        print("img_src : ",img_src)
        print('./img/{}.jpg'.format("신세계_"+str(num)))
        urlretrieve(img_src , './HI/{}.jpg'.format("신세계_슬랙스"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass


#######################################################################################################################################################################################
###코트

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 이미지#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EB%82%A8%EC%84%B1%EC%BD%94%ED%8A%B8&trackSearchType=nomal"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    print("story22[a] : " , len(story22[a]))

    if len(story22[a]) == 2:
        print("실패")
        story22[a] = (str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i+1))))
        print("story22 :", story22)
        print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('</span>]', "")
    ing[a] = ing[a].replace('[<span class="_goodsName">', "")
    ing[a] = ing[a].replace("\r", "")
    ing[a] = ing[a].replace("\n", "")
    ing[a] = ing[a].replace("\t", "")
    ing[a] = ing[a].replace('', "")
    ing[a] = ing[a].replace('<span class="_tvDealYn" data-deal="Y">', "")
    ing[a] = ing[a].replace('  ', "")

    print("ing[a] : ", ing[a])




    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    print("len(story33[a] : " ,len(story33[a]))

    if len(story33[a]) == 0:
        print("실패")
        story33[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i+1)))
        print("story33 :", story33)
        print("story33[a] : ", story33[a])


    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace('[<span class="_bestPrice">', "")
    ing2[a] = ing2[a].replace("</span>]", "")

    print("ing2[a] : " , ing2[a])



    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i))))
    print("story44 : " ,story44)
    print("story44[a] : ", story44[a])
    print("len(story44[a] : " ,len(story44[a]))


    if i == 5 and len(story44[a]) == 2:
        print("실패")
        story44[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i+1)))
        print("story44 :", story44)
        print("story44[a] : ", story44[a])

    if len(story44[a]) == 2:
        story44[a] = '0'

    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("<em>", "")
    ing3[a] = ing3[a].replace("</em>", "")
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a] + "건"

    print("ing3 :" , ing3)
    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i))))
    print("story55 : ", story55)
    print("story55[a] : ", story55[a])
    print("len(story55[a] : ", len(story55[a]))

    if i == 5 and len(story55[a]) == 2:
        print("실패")
        story55[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i+1)))
        print("story55 :", story55)
        print("story55[a] : ", story55[a])

    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('[<img alt=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace("'", "")
    ing4[a] = ing4[a].replace("onerror=this.src=/resources/web/img/onerror/s245x245.png", "")
    ing4[a] = ing4[a].replace('class=_image lazy', "")
    ing4[a] = ing4[a].replace('src', "")
    ing4[a] = ing4[a].replace('/>]', "")
    ing4[a] = ing4[a].replace('  ', "")
    ing4[a] = ing4[a].split("=")
    ing4[a] = ing4[a][1]

    print("ing4[a] : ", ing4[a])
    print("ing4 :", ing4)
    sql = 'insert into outers values("신세계", "코트", {},"{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing4[i]
        print("img_src : ",img_src)
        print('./img/{}.jpg'.format("신세계_"+str(num)))
        urlretrieve(img_src , './HI/{}.jpg'.format("신세계_코트"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass

#######################################################################################################################################################################################
###패딩

a = 0
i = 1
ing = []         ###########제품 이름#########
ing2 = []        ###########제품 가격#########
ing3 = []        ###########제품 리뷰갯수######
ing4 = []        ###########제품 이미지#########
ing5 = []
show_now = []
story22 = []
story33 = []
story44 = []
story55 = []
story66 = []

for a in range(0,5):
    print("i :", i)
    print("반복횟수 [a] :", a)

    url = "https://www.shinsegaetvshopping.com/goods-search/search?searchKeyword=%EB%82%A8%EC%84%B1%ED%8C%A8%EB%94%A9&trackSearchType=nomal"
    print("url :" ,url)
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")

    print("##########################[제품 이름 받아오는중]##########################")
    story22.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i))))
    print("story22 :", story22)
    print("story22[a] : ", story22[a])
    print("story22[a] : " , len(story22[a]))

    if len(story22[a]) == 2:
        print("실패")
        story22[a] = (str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-product-name > a > span._goodsName".format(i+1))))
        print("story22 :", story22)
        print("story22[a] : ", story22[a])


    ing.append(str(story22[a]))
    ing[a] = ing[a].replace('</span>]', "")
    ing[a] = ing[a].replace('[<span class="_goodsName">', "")
    ing[a] = ing[a].replace("\r", "")
    ing[a] = ing[a].replace("\n", "")
    ing[a] = ing[a].replace("\t", "")
    ing[a] = ing[a].replace('', "")
    ing[a] = ing[a].replace('<span class="_tvDealYn" data-deal="Y">', "")
    ing[a] = ing[a].replace('  ', "")

    print("ing[a] : ", ing[a])




    print("#############################[제품 가격 가져오는중]##########################")
    story33.append(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i)))
    print("story33 : " ,story33)
    print("story33[a] : ", story33[a])
    print("len(story33[a] : " ,len(story33[a]))

    if len(story33[a]) == 0:
        print("실패")
        story33[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-price > span._bestPrice".format(i+1)))
        print("story33 :", story33)
        print("story33[a] : ", story33[a])


    ing2.append(str(story33[a])+"원")
    ing2[a] = ing2[a].replace('[<span class="_bestPrice">', "")
    ing2[a] = ing2[a].replace("</span>]", "")

    print("ing2[a] : " , ing2[a])



    print("######################[제품 리뷰갯수 가져오는중]###########################")
    story44.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i))))
    print("story44 : " ,story44)
    print("story44[a] : ", story44[a])
    print("len(story44[a] : " ,len(story44[a]))


    if i == 5 and len(story44[a]) == 2:
        print("실패")
        story44[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-supporting-text > div.area-score > span.count > em".format(i+1)))
        print("story44 :", story44)
        print("story44[a] : ", story44[a])

    if len(story44[a]) == 2:
        story44[a] = '0'

    ing3.append(story44[a])
    ing3[a] = ing3[a].replace("<em>", "")
    ing3[a] = ing3[a].replace("</em>", "")
    ing3[a] = ing3[a].replace("[", "")
    ing3[a] = ing3[a].replace("]", "")
    ing3[a] = ing3[a] + "건"

    print("ing3 :" , ing3)
    print("ing3[a] : ", ing3[a])



    print("######################[제품 사이트 가져오는중]###########################")
    story55.append(str(soup.select(
        "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i))))
    print("story55 : ", story55)
    print("story55[a] : ", story55[a])
    print("len(story55[a] : ", len(story55[a]))

    if i == 5 and len(story55[a]) == 2:
        print("실패")
        story55[a] = str(soup.select(
            "#shopProducts > div > div > div:nth-child({}) > div.area-richmedia > div:nth-child(1) > a > img".format(i+1)))
        print("story55 :", story55)
        print("story55[a] : ", story55[a])

    ing4.append(story55[a])
    ing4[a] = ing4[a].replace('[<img alt=', "")
    ing4[a] = ing4[a].replace('"', "")
    ing4[a] = ing4[a].replace("'", "")
    ing4[a] = ing4[a].replace("onerror=this.src=/resources/web/img/onerror/s245x245.png", "")
    ing4[a] = ing4[a].replace('class=_image lazy', "")
    ing4[a] = ing4[a].replace('src', "")
    ing4[a] = ing4[a].replace('/>]', "")
    ing4[a] = ing4[a].replace('  ', "")
    ing4[a] = ing4[a].split("=")
    ing4[a] = ing4[a][1]

    print("ing4[a] : ", ing4[a])
    print("ing4 :", ing4)
    sql = 'insert into outers values("신세계", "패딩", {},"{}", "{}", "{}", "{}")'.format(a+1, ing[a], ing2[a], ing3[a], ing4[a])
    cur.execute(sql)
    conn.commit()
    i += 1

#이미지 다운로드
try:

    for i in range(0,5):
        img_src = ing4[i]
        print("img_src : ",img_src)
        print('./img/{}.jpg'.format("신세계_"+str(num)))
        urlretrieve(img_src , './HI/{}.jpg'.format("신세계_패딩"+str(num)))
        print("성공")
        num += 1

except:

    print("실패")
    pass









conn.close()
#################################크롤링끝############################
#################################크롤링끝############################
#################################크롤링끝############################



os.chdir('/home/aiot02/PycharmProjects/pythonProject6/HI')

file_list_1 = []
file_list_2 = []
file_list_3 = []
file_list_4 = []

# for i in range(0,30):
#     file_list_1.append("11번가_{}.jpg".format(i))
#     file_list_2.append("G마켓_{}.jpg".format(i))
#     file_list_3.append("옥션_{}.jpg".format(i))
for i in range(0,5):
    file_list_1.append("11번가_맨투맨{}.jpg".format(i))
    file_list_2.append("G마켓_맨투맨{}.jpg".format(i))
    file_list_3.append("옥션_맨투맨{}.jpg".format(i))
    file_list_4.append("신세계_맨투맨{}.jpg".format(i))
for i in range(5,10):
    file_list_1.append("11번가_셔츠{}.jpg".format(i))
    file_list_2.append("G마켓_셔츠{}.jpg".format(i))
    file_list_3.append("옥션_셔츠{}.jpg".format(i))
    file_list_4.append("신세계_셔츠{}.jpg".format(i))
for i in range(10, 15):
    file_list_1.append("11번가_청바지{}.jpg".format(i))
    file_list_2.append("G마켓_청바지{}.jpg".format(i))
    file_list_3.append("옥션_청바지{}.jpg".format(i))
    file_list_4.append("신세계_청바지{}.jpg".format(i))
for i in range(15, 20):
    file_list_1.append("11번가_슬랙스{}.jpg".format(i))
    file_list_2.append("G마켓_슬랙스{}.jpg".format(i))
    file_list_3.append("옥션_슬랙스{}.jpg".format(i))
    file_list_4.append("신세계_슬랙스{}.jpg".format(i))
for i in range(20, 25):
    file_list_1.append("11번가_코트{}.jpg".format(i))
    file_list_2.append("G마켓_코트{}.jpg".format(i))
    file_list_3.append("옥션_코트{}.jpg".format(i))
    file_list_4.append("신세계_코트{}.jpg".format(i))
for i in range(25, 30):
    file_list_1.append("11번가_패딩{}.jpg".format(i))
    file_list_2.append("G마켓_패딩{}.jpg".format(i))
    file_list_3.append("옥션_패딩{}.jpg".format(i))
    file_list_4.append("신세계_패딩{}.jpg".format(i))

with zipfile.ZipFile(os.getcwd()+".zip","w")as my_zip:
    for i in file_list_1:
        my_zip.write(i)
    for i in file_list_2:
        my_zip.write(i)
    for i in file_list_3:
        my_zip.write(i)
    for i in file_list_4:
        my_zip.write(i)
    my_zip.close()

os.chdir('/home/aiot02/PycharmProjects/pythonProject6')
# HOST = socket.gethostname()
HOST = '10.10.21.102'
PORT = 5003
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

serverSocket = socket.socket()
serverSocket.bind(ADDR)
serverSocket.listen(5)
print ('Server waiting...')
while True:
    clientSocket, addr = serverSocket.accept()
    print ('Connection from', addr)
    data = clientSocket.recv(BUFF_SIZE)
    print('client : ' + data.decode())
    filename='HI.zip'
    #filename='iu1.png'
    # f = open(filename,'rb')
    with open(filename, 'rb')as f:
        try:
            l = f.read(BUFF_SIZE)
            while (l):
                print('sending data...')
                clientSocket.send(l)
                l = f.read(BUFF_SIZE)
            f.close()
            print('Done sending')
            clientSocket.close()
        except Exception as e:
            print(e)



