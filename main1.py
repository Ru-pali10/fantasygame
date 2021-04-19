# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from new import Ui_Form as new_team
from evaluate import Ui_E_MainWindow as evaluate_team

import sqlite3
db1=sqlite3.connect('players.db')
curplay=db1.cursor()


import CRI
class Ui_MainWindow(object):
    def __init__(self):
        self.newTeam=QtWidgets.QWidget()
        self.new_window=new_team()
        self.new_window.setupUi(self.newTeam)
        self.WK=1
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 100, 523, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl2.setFont(font)
        self.lbl2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl2.setObjectName("lbl2")
        self.horizontalLayout.addWidget(self.lbl2)
        self.lbl3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl3.setFont(font)
        self.lbl3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl3.setObjectName("lbl3")
        self.horizontalLayout.addWidget(self.lbl3)
        self.lbl4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl4.setFont(font)
        self.lbl4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl4.setObjectName("lbl4")
        self.horizontalLayout.addWidget(self.lbl4)
        self.lbl5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl5.setFont(font)
        self.lbl5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl5.setObjectName("lbl5")
        self.horizontalLayout.addWidget(self.lbl5)
        self.lbl6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl6.setFont(font)
        self.lbl6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl6.setObjectName("lbl6")
        self.horizontalLayout.addWidget(self.lbl6)
        self.lbl7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl7.setFont(font)
        self.lbl7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl7.setObjectName("lbl7")
        self.horizontalLayout.addWidget(self.lbl7)
        self.lbl8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl8.setFont(font)
        self.lbl8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl8.setObjectName("lbl8")
        self.horizontalLayout.addWidget(self.lbl8)
        self.lbl9 = QtWidgets.QLabel(self.layoutWidget)
        self.lbl9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl9.setObjectName("lbl9")
        self.horizontalLayout.addWidget(self.lbl9)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 270, 231, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.list1 = QtWidgets.QListWidget(self.frame)
        self.list1.setGeometry(QtCore.QRect(10, 60, 191, 191))
        self.list1.setObjectName("list1")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 221, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rb1 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb1.setEnabled(False)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_3.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb2.setEnabled(False)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_3.addWidget(self.rb2)
        self.rb3 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb3.setEnabled(False)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_3.addWidget(self.rb3)
        self.rb4 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb4.setEnabled(False)
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_3.addWidget(self.rb4)
        self.rb2.raise_()
        self.rb4.raise_()
        self.rb1.raise_()
        self.rb3.raise_()
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(310, 270, 231, 261))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lbl14 = QtWidgets.QLabel(self.frame_2)
        self.lbl14.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl14.setFont(font)
        self.lbl14.setObjectName("lbl14")
        self.lbl15 = QtWidgets.QLabel(self.frame_2)
        self.lbl15.setGeometry(QtCore.QRect(120, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl15.setFont(font)
        self.lbl15.setText("")
        self.lbl15.setObjectName("lbl15")
        self.list2 = QtWidgets.QListWidget(self.frame_2)
        self.list2.setGeometry(QtCore.QRect(10, 61, 201, 181))
        self.list2.setObjectName("list2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 380, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 200, 151, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl10 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl10.setFont(font)
        self.lbl10.setObjectName("lbl10")
        self.horizontalLayout_2.addWidget(self.lbl10)
        self.lbl11 = QtWidgets.QLabel(self.layoutWidget2)
        self.lbl11.setObjectName("lbl11")
        self.horizontalLayout_2.addWidget(self.lbl11)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(320, 200, 161, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl12 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl12.setFont(font)
        self.lbl12.setObjectName("lbl12")
        self.horizontalLayout_4.addWidget(self.lbl12)
        self.lbl13 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl13.setFont(font)
        self.lbl13.setObjectName("lbl13")
        self.horizontalLayout_4.addWidget(self.lbl13)
        self.lbl15_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl15_2.setGeometry(QtCore.QRect(40, 10, 81, 71))
        self.lbl15_2.setStyleSheet("image: url(:/newPrefix/CRI.jpg);")
        self.lbl15_2.setText("")
        self.lbl15_2.setTextFormat(QtCore.Qt.RichText)
        self.lbl15_2.setPixmap(QtGui.QPixmap(":/newPrefix/CRI.jpg"))
        self.lbl15_2.setScaledContents(True)
        self.lbl15_2.setObjectName("lbl15_2")
        self.lbl16 = QtWidgets.QLabel(self.centralwidget)
        self.lbl16.setGeometry(QtCore.QRect(150, 10, 421, 61))
        self.lbl16.setObjectName("lbl16")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")
        self.menuhii = QtWidgets.QMenu(self.menubar)
        self.menuhii.setObjectName("menuhii")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionDELETE_Team = QtWidgets.QAction(MainWindow)
        self.actionDELETE_Team.setObjectName("actionDELETE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuhii.addAction(self.actionNEW_Team)
        self.menuhii.addAction(self.actionOPEN_Team)
        self.menuhii.addAction(self.actionSAVE_Team)
        self.menuhii.addAction(self.actionDELETE_Team)
        self.menuhii.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuhii.menuAction())
        
        self.batsMen=0
        self.bowL=0
        self.allR=0
        self.wk=0
        self.av_point=0
        self.used_point=0

        self.new_window.btn1.clicked.connect(self.team_name)
        self.actionNEW_Team.triggered.connect(self.new_team)
        self.actionSAVE_Team.triggered.connect(self.save_team)
        self.actionOPEN_Team.triggered.connect(self.open_Team)
        self.actionDELETE_Team.triggered.connect(self.delete_Team)                                                        
        self.actionEVALUATE_Team.triggered.connect(self.evaluate_Team)
        self.rb1.toggled.connect(self.list)
        self.rb2.toggled.connect(self.list)
        self.rb3.toggled.connect(self.list)
        self.rb4.toggled.connect(self.list)
        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.rb1, self.rb2)
        MainWindow.setTabOrder(self.rb2, self.rb3)
        MainWindow.setTabOrder(self.rb3, self.rb4)
        MainWindow.setTabOrder(self.rb4, self.list1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selection"))
        self.lbl2.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.lbl3.setText(_translate("MainWindow", "0"))
        self.lbl4.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.lbl5.setText(_translate("MainWindow", "0"))
        self.lbl6.setText(_translate("MainWindow", "All Rounder(AR)"))
        self.lbl7.setText(_translate("MainWindow", "0"))
        self.lbl8.setText(_translate("MainWindow", "Wicket Keeper(WK)"))
        self.lbl9.setText(_translate("MainWindow", "0"))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BOW"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.lbl14.setText(_translate("MainWindow", "Team Name"))
        self.label_2.setText(_translate("MainWindow", "     >"))
        self.lbl10.setText(_translate("MainWindow", "Points available "))
        self.lbl11.setText(_translate("MainWindow", "0"))
        self.lbl12.setText(_translate("MainWindow", "Points Used"))
        self.lbl13.setText(_translate("MainWindow", "0"))
        self.lbl16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#1f5ab8;\">FANTASY CRICKET GAME</span></p></body></html>"))
        self.menuhii.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionDELETE_Team.setText(_translate("MainWindow", "DELETE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def team_name(self):
        self.rb1.setEnabled(True)
        self.rb2.setEnabled(True)
        self.rb3.setEnabled(True)
        self.rb4.setEnabled(True)
        self.lbl11.setText(str(1500))
        self.lbl13.setText(str('0'))
        self.batsMen=0
        self.lbl3.setText(str(self.batsMen))
        self.bowL=0
        self.lbl5.setText(str(self.bowL))
        self.allR=0
        self.lbl7.setText(str(self.allR))
        self.wk=0
        self.lbl9.setText(str(self.wk))
        team=self.new_window.tf1.text()
        self.lbl15.setText(str(team))
        return
    def new_team(self):
        self.newTeam.show()
        return
    def save_team(self):
        count=self.list2.count()
        selected=""
        for i in range(count):
            selected+=self.list2.item(i).text()
            if i<count:
                selected+=","
##        print(selected)
        if (self.batsMen+self.bowL+self.allR+self.wk)!=11:
            popup="insufficient players"
            self.show_up(popup)
            return 
        team=self.lbl15.text()
        used_point=self.lbl13.text()
        sq2="SELECT player FROM name='"+team+"';"
        curplay.execute(sq2)
        check=curplay.fetchall()
        for record in check:
            print(record)
        if(check):
            sql="INSERT INTO teams (name,player,value) VALUES ('"+team+"','"+selected+"','"+str(used_point)+"');"
        else:
            sql="UPDATE teams SET player='"+selected+"' WHERE name='"+team+"';"
##        print(team)
##        print(used_point)
        try:
            curplay.execute(sql)
            db1.commit()
            popup="Team saved successfully"
            self.show_up(popup)
            
           
        except:
            db1.rollback()
            popup="Error in Operation"
            self.show_up(popup)

        return
    def list(self):
        if self.rb1.isChecked()==True:
            self.list1.clear()
            sql="SELECT player FROM stats WHERE ctg='BAT';"
            curplay.execute(sql)
            bat=curplay.fetchall()
            for row in bat:
                selected=[]
                for i in range(self.list2.count()):
                    selected.append(self.list2.item(i).text())
                if row[0] not in selected:
                    self.list1.addItem(row[0])
                    
            
        elif self.rb2.isChecked()==True:
            self.list1.clear()
            sql="SELECT player FROM stats WHERE ctg='BWL';"
            curplay.execute(sql)
            bwl=curplay.fetchall()
            for row in bwl:
                selected=[]
                for i in range(self.list2.count()):
                    selected.append(self.list2.item(i).text())
                if row[0] not in selected:
                    self.list1.addItem(row[0])
        elif self.rb3.isChecked()==True:
            self.list1.clear()
            sql="SELECT player FROM stats WHERE ctg='AR';"
            curplay.execute(sql)
            ar=curplay.fetchall()
            for row in ar:
                selected=[]
                for i in range(self.list2.count()):
                    selected.append(self.list2.item(i).text())
                if row[0] not in selected:
                    self.list1.addItem(row[0])
        elif self.rb4.isChecked()==True:
            self.list1.clear()
            sql="SELECT player FROM stats WHERE ctg='WK';"
            curplay.execute(sql)
            wk1=curplay.fetchall()
            for row in wk1:
                selected=[]
                for i in range(self.list2.count()):
                    selected.append(self.list2.item(i).text())
                if row[0] not in selected:
                    self.list1.addItem(row[0])
        return

    def removelist1(self):
        if self.rb4.isChecked()and self.WK != 0 or self.rb1.isChecked() or self.rb2.isChecked() or self.rb3.isChecked():
            item=self.list1.takeItem(self.list1.currentRow())
            self.list2.addItem(item)
            sql="SELECT value FROM stats WHERE player='"+item.text()+"';"
            curplay.execute(sql)
            points=curplay.fetchall()
            av_point=self.lbl11.text()
            av_point=int(av_point)-int(points[0][0])
            self.lbl11.setText(str(av_point))
            used_point=self.lbl13.text()
            us_point=int(used_point)+int(points[0][0])
            self.lbl13.setText(str(us_point))
            print(us_point)
            if av_point<=0:
                popup="your points are exhausted"
                self.show_up(popup)
                
        else:
            popup="you cannot select more than one wicketkeeper"
            self.show_up(popup)
        if self.rb1.isChecked()==True:
            self.batsMen=self.lbl3.text()
            self.batsMen=int(self.batsMen)+1
            self.lbl3.setText(str(self.batsMen))
            if self.batsMen >5:
                popup="batsmen not more than 5"
                self.show_up(popup)
        elif self.rb2.isChecked():   
            self.bowL=self.lbl5.text()
            self.bowL=int(self.bowL)+1
            self.lbl5.setText(str(self.bowL))
        elif self.rb4.isChecked() and self.WK != 0:   
            self.WK=self.WK-1
            self.wk=2
            self.wk=int(self.wk)-1
            self.lbl9.setText(str(self.wk))
        else:    
            self.allR=self.lbl7.text()
            self.allR=int(self.allR)+1
            self.lbl7.setText(str(self.allR))
        return
    def show_up(self,popup):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(popup)
        msg.exec_()
        return
    def removelist2(self):
        item=self.list2.takeItem(self.list2.currentRow())
        curplay.execute("SELECT ctg FROM stats WHERE player='"+item.text()+"'")
        data_type=curplay.fetchall()
        if self.rb1.isChecked() and data_type[0][0]=="BAT":
            self.list1.addItem(item.text())
            self.batsMen=self.lbl3.text()
            self.batsMen=int(self.batsMen)-1
            self.lbl3.setText(str(self.batsMen))
        elif self.rb2.isChecked() and data_type[0][0]=="BWL":
            self.list1.addItem(item.text())
            self.bowL=self.lbl5.text()
            self.bowL=int(self.bowL)-1
            self.lbl5.setText(str(self.bowL))
        elif self.rb3.isChecked() and data_type[0][0]=="AR":
            self.list1.addItem(item.text())
            self.allR=self.lbl7.text()
            self.allR=int(self.allR)-1
            self.lbl7.setText(str(self.allR))
        elif self.rb4.isChecked() and data_type[0][0]=="WK":
            self.list1.addItem(item.text())
            self.wk=self.lbl9.text()
            self.wk=int(self.wk)-1
            self.WK=1
            self.lbl9.setText(str(self.wk))
        item=item.text()
        curplay.execute("SELECT value FROM stats WHERE player='"+item+"'")
        points=curplay.fetchall()
        av_point=self.lbl13.text()
        av_point=int(av_point)-int(points[0][0])
        self.lbl13.setText(str(av_point))
        used_point=self.lbl11.text()
        us_point=int(used_point)+int(points[0][0])
        self.lbl11.setText(str(us_point))
        return
    def open_Team(self):
        self.rb1.setEnabled(True)
        self.rb2.setEnabled(True)
        self.rb3.setEnabled(True)
        self.rb4.setEnabled(True)
    
        sql="select name from teams;"
   
        curplay.execute(sql)
        cur=curplay.fetchall()
        
        teams=[]

        for row in cur:
            teams.append(row[0])
        
        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Open team","Choose A Team",teams,0,False)
        if ok and team:
            self.lbl15.setText(team)
        
        
        sql1="SELECT player,value from teams where name='"+team+"';"
        curplay.execute(sql1)
        row=curplay.fetchone()
        selected=row[0].split(',')
        
        self.list2.addItems(selected)
        self.used_point=row[1]
        
        self.av_point=1500-row[1]
        count=self.list2.count()
        self.lbl13.setText(str(self.used_point))
        self.lbl11.setText(str(self.av_point))

        for i in range(count-1):
            ply=self.list2.item(i).text()
            
            sql="select ctg from stats where player='"+ply+"';"
            
            curplay.execute(sql)
            
            row=curplay.fetchone()
            ctgr=row[0]
            if ctgr=="BAT":
                self.batsMen+=1
                self.lbl3.setText(str(self.batsMen))
            if ctgr=="BWL":
                self.bowL+=1
                self.lbl5.setText(str(self.bowL))
            if ctgr=="AR":
                self.allR+=1
                self.lbl7.setText(str(self.allR))
            if ctgr=="WK":
                self.wk+=1
                self.lbl9.setText(str(self.wk))
        return
    def evaluate_Team(self):
        self.evaluateTeam = QtWidgets.QMainWindow()
        self.evaluate_screen = evaluate_team()
        self.evaluate_screen.setupUi(self.evaluateTeam)
        self.evaluateTeam.show()
        return
    def delete_Team(self):
        print("delete")
        sql="select name from teams;"
   
        curplay.execute(sql)
        cur=curplay.fetchall()
        
        teams=[]

        for row in cur:
            teams.append(row[0])
        
        team, delete=QtWidgets.QInputDialog.getItem(MainWindow,"Open team","Choose A Team",teams,0,False)
        if delete and team:
            sql1="DELETE FROM teams WHERE name='"+team+"';"
            curplay.execute(sql1)
            db1.commit()
            popup="Team deleted successfully"
            self.show_up(popup)
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
