# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_E_MainWindow(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow")
        MainWindow2.resize(435, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(370, 140, 20, 191))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.lbl_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_1.setGeometry(QtCore.QRect(60, 20, 331, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_1.setFont(font)
        self.lbl_1.setObjectName("lbl_1")
        self.lw1 = QtWidgets.QListWidget(self.centralwidget)
        self.lw1.setGeometry(QtCore.QRect(30, 140, 151, 192))
        self.lw1.setObjectName("lw1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cb2 = QtWidgets.QComboBox(self.centralwidget)
        self.cb2.setGeometry(QtCore.QRect(240, 50, 141, 22))
        self.cb2.setObjectName("cb2")
        self.cb2.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 80, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lw2 = QtWidgets.QListWidget(self.centralwidget)
        self.lw2.setGeometry(QtCore.QRect(240, 140, 151, 192))
        self.lw2.setObjectName("lw2")
        self.cb1 = QtWidgets.QComboBox(self.centralwidget)
        self.cb1.setGeometry(QtCore.QRect(40, 50, 141, 22))
        self.cb1.setObjectName("cb1")
        self.cb1.addItem("")
        self.bt1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1.setGeometry(QtCore.QRect(170, 350, 75, 23))
        self.bt1.setObjectName("bt1")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 21))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        import sqlite3
        db1=sqlite3.connect('players.db')
        curplay= db1.cursor()
        curplay.execute("SELECT name FROM teams")
        name=curplay.fetchall()
        team=[]
        for row in name:
            self.cb1.addItem(row[0])
        
        self.cb2.addItem("match")
        self.cb2.activated.connect(self.playerShow)
        self.bt1.clicked.connect(self.calculate)
        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)
        MainWindow2.setTabOrder(self.cb1, self.cb2)
        MainWindow2.setTabOrder(self.cb2, self.lw1)
        MainWindow2.setTabOrder(self.lw1, self.lw2)
        MainWindow2.setTabOrder(self.lw2, self.bt1)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_1.setText(_translate("MainWindow", "Evaluate the performance of your Fantasy Team"))
        self.label_2.setText(_translate("MainWindow", "Points"))
        self.cb2.setItemText(0, _translate("MainWindow", "Select Match"))
        self.label.setText(_translate("MainWindow", "Players"))
        self.cb1.setItemText(0, _translate("MainWindow", "Select Team"))
        self.bt1.setText(_translate("MainWindow", "CALCULATE"))

    def playerShow(self):
        import sqlite3
        db1=sqlite3.connect('players.db')
        team=self.cb1.currentText()
        self.lw1.clear()
        sql1="select player,value from teams where name='"+team+"';"
        curlist=db1.cursor()
        curlist.execute(sql1)
        row=curlist.fetchone()
        print(row[0])
        selected=row[0].split(',')
        print(selected[2])
        print(row[1])
        print(selected)
        self.lw1.addItems(selected)
        
        return
    def calculate(self):
        teamttl=0
        match=self.cb2.currentText()
        self.lw2.clear()
        for i in range(self.lw1.count()-1):
            ttl, batscore, bowlscore, fieldscore=0,0,0,0
            nm=self.lw1.item(i).text()
            import sqlite3
            db1=sqlite3.connect('players.db')
            cur1=db1.cursor()
            cur1.execute("select * from match where player='"+nm+"';")
            row=cur1.fetchone()
            cur2=db1.cursor()
            cur2.execute("select runs from stats where player='"+nm+"';")
            row1=cur2.fetchone()
            batscore=int(row1[0]/2)
            if batscore>=50: batscore+=5
            if batscore>=100: batscore+=10
            if row[1]>0:
                skrt=row1[0]/row[2]
                if skrt>=80 and skrt<100:
                    batscore+=2
                if skrt>=100:batscore+=4
            batscore=batscore+row[3]
            batscore=batscore+2*row[4]
            print ("batting score=", batscore)
            bowlscore=row[8]*10
            if row[8]>=3: bowlscore=bowlscore+5
            if row[8]>=5: bowlscore=bowlscore=bowlscore+10
            if row[7]>0:
                ecort=6*row[7]/row[5]
                print ("eco:",ecort)
                if ecort<=2: bowlscore=bowlscore+10
                if ecort>2 and ecort<=3.5: bowlscore=bowlscore+7
                if ecort>3.5 and ecort<=4.5: bowlscore=bowlscore+4
            fieldscore=(row[9]+row[10]+row[11])*10            
            ttl=batscore+bowlscore+fieldscore
            teamttl=teamttl+ttl
            print(ttl)
            self.lw2.addItem(str(ttl))
        print("SSS")
        popup=str(self.teamtt1)
        self.show_up(popup)
    def show_up(self,popup):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("your score is ", popup)
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_E_MainWindow()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
