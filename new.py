# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(361, 140)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 301, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lbl_1.setFont(font)
        self.lbl_1.setObjectName("lbl_1")
        self.horizontalLayout.addWidget(self.lbl_1)
        self.tf1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.tf1.setObjectName("tf1")
        self.horizontalLayout.addWidget(self.tf1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 90, 301, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn1.clicked.connect(self.team)
        self.btn1.setObjectName("btn1")
        self.horizontalLayout_2.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn2.setObjectName("btn2")
        self.horizontalLayout_2.addWidget(self.btn2)

        self.retranslateUi(Form)
        self.btn2.clicked.connect(self.tf1.clear)
        self.btn1.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_1.setText(_translate("Form", "Enter Team Name:"))
        self.btn1.setText(_translate("Form", "ok"))
        self.btn2.setText(_translate("Form", "clear"))
    def team(self):
        name=self.tf1.text()
        return name

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
