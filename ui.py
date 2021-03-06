# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# Modified to avoid repetitive tasks 
# Some parameters added for convenience 

from PyQt5 import QtCore, QtGui, QtWidgets

ROW_COUNT = 3
COLUMN_COUNT = 16
NOT_CHECKED = "background-color: #40464d;\nborder: 1px solid white;"
CHECKED = "background-color: #1790BB;\nborder: 1px solid white;"
PLAYING = "background-color: green"
NOT_PLAYING = "background-color: white"

class Ui_Form(object):
    """ The form generated from QtDesigner. 
    """
    def setupUi(self, Form):
        """ Setup the form and add components to it. 
        """
        self.uiMatrix = list()
        for i in range(ROW_COUNT): self.uiMatrix.append(list())
        self.status = list()
        Form.setObjectName("Form")
        Form.resize(690, 368)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 50, 671, 311))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.fileSelector1 = QtWidgets.QPushButton(self.widget)
        self.fileSelector1.setMaximumSize(QtCore.QSize(100, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileSelector1.setIcon(icon)
        self.fileSelector1.setObjectName("fileSelector1")
        self.gridLayout_2.addWidget(self.fileSelector1, 0, 0, 1, 3)
        self.soundButton1 = QtWidgets.QPushButton(self.widget)
        self.soundButton1.setEnabled(True)
        # self.soundButton1.setMinimumSize(QtCore.QSize(0, 0))
        self.soundButton1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/mute.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("images/unmute.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("images/mute.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("images/unmute.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.soundButton1.setCheckable(True)
        self.soundButton1.setChecked(False)
        # self.soundButton1.setIcon(icon1)
        # self.soundButton1.setIconSize(QtCore.QSize(20, 20))
        self.soundButton1.setObjectName("soundButton1")
        self.gridLayout_2.addWidget(self.soundButton1, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 1, 1)
        self.fileSelector2 = QtWidgets.QPushButton(self.widget)
        self.fileSelector2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fileSelector2.setIcon(icon)
        self.fileSelector2.setObjectName("fileSelector2")
        self.gridLayout_3.addWidget(self.fileSelector2, 0, 0, 1, 3)
        self.soundButton2 = QtWidgets.QPushButton(self.widget)
        self.soundButton2.setEnabled(True)
        self.soundButton2.setMinimumSize(QtCore.QSize(30, 30))
        self.soundButton2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/unmute.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("images/mute.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("images/unmute.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap("images/mute.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.soundButton2.setCheckable(True)
        self.soundButton2.setChecked(False)
        # self.soundButton2.setIcon(icon3)
        # self.soundButton2.setIconSize(QtCore.QSize(20, 20))
        self.soundButton2.setObjectName("soundButton2")
        self.gridLayout_3.addWidget(self.soundButton2, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addRow(self.horizontalLayout_3, 2, 16)

        self.gridLayout_4.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addRow(self.horizontalLayout_2, 1, COLUMN_COUNT)

        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addRow(self.horizontalLayout, 0, COLUMN_COUNT)

        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fileSelector0 = QtWidgets.QPushButton(self.widget)
        self.fileSelector0.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fileSelector0.setIcon(icon)
        self.fileSelector0.setObjectName("fileSelector0")
        self.gridLayout.addWidget(self.fileSelector0, 0, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.soundButton0 = QtWidgets.QPushButton(self.widget)
        self.soundButton0.setEnabled(True)
        self.soundButton0.setMinimumSize(QtCore.QSize(30, 30))
        self.soundButton0.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/mute.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("images/unmute.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("images/mute.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("images/unmute.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.soundButton0.setCheckable(True)
        self.soundButton0.setChecked(False)
        # self.soundButton0.setIcon(icon2)
        # self.soundButton0.setIconSize(QtCore.QSize(20, 20))
        self.soundButton0.setObjectName("soundButton0")
        self.gridLayout.addWidget(self.soundButton0, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        for i in range(COLUMN_COUNT):
            cell = QtWidgets.QLabel(self.widget)
            cell.setMaximumSize(QtCore.QSize(16777215, 20))
            cell.setStyleSheet(NOT_PLAYING)
            cell.setText("")
            cell.setObjectName("status"+str(i))
            self.horizontalLayout_6.addWidget(cell)
            self.status.append(cell)

        self.speedTimer = QtWidgets.QDoubleSpinBox()
        self.speedTimer.setMinimum(0.05)
        self.speedTimer.setMaximum(1.0)
        self.speedTimer.setDecimals(2)
        self.speedTimer.setSingleStep(0.1)
        self.speedTimer.setSuffix(" s")
        self.gridLayout_4.addWidget(self.speedTimer, 0, 0)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.gridLayout_4.setRowMinimumHeight(0, 1)
        self.gridLayout_4.setRowMinimumHeight(1, 4)
        self.gridLayout_4.setRowMinimumHeight(2, 4)
        self.gridLayout_4.setRowMinimumHeight(3, 4)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 12)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 4)
        self.gridLayout_4.setRowStretch(2, 4)
        self.gridLayout_4.setRowStretch(3, 4)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 671, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.playButton = QtWidgets.QPushButton(self.widget1)
        self.playButton.setEnabled(True)
        self.playButton.setMinimumSize(QtCore.QSize(20, 20))
        self.playButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/play.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("images/play.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("images/paused.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap("images/paused.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.playButton.setIcon(icon3)
        self.playButton.setCheckable(True)
        self.playButton.setChecked(False)
        self.playButton.setDefault(True)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_4.addWidget(self.playButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.label_55 = QtWidgets.QLabel(self.widget1)
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_4.addWidget(self.label_55)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.soundButton0.raise_()
        self.fileSelector0.raise_()
        self.playButton.raise_()
        self.soundButton0.setFixedSize(0,0)
        self.soundButton1.setFixedSize(0,0)
        self.soundButton2.setFixedSize(0,0)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """ Translate ui components if required. 
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fileSelector1.setToolTip(_translate("Form", "<html><head/><body><p>Set audio source</p></body></html>"))
        self.fileSelector1.setText(_translate("Form", ""))
        self.soundButton1.setToolTip(_translate("Form", "<html><head/><body><p>Mute/Unmute</p></body></html>"))
        self.fileSelector2.setToolTip(_translate("Form", "<html><head/><body><p>Set audio source</p></body></html>"))
        self.fileSelector2.setText(_translate("Form", ""))
        self.soundButton2.setToolTip(_translate("Form", "<html><head/><body><p>Mute/Unmute</p></body></html>"))
        self.fileSelector0.setToolTip(_translate("Form", "<html><head/><body><p>Set audio source</p></body></html>"))
        self.fileSelector0.setText(_translate("Form", ""))
        self.soundButton0.setToolTip(_translate("Form", "<html><head/><body><p>Mute/Unmute</p></body></html>"))
        self.playButton.setToolTip(_translate("Form", "<html><head/><body><p>Play/Pause</p></body></html>"))
        self.label_55.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">PyJam</span></p></body></html>"))

    def addRow(self, layout, index, count):
        """ Create a row and add it to the layout asked. 
        """
        for i in range(count):
            cell = QtWidgets.QPushButton(self.widget)
            cell.setText("")
            cell.setFixedHeight(80)
            cell.setStyleSheet(NOT_CHECKED)
            cell.setCheckable(True)
            cell.setChecked(False)
            cell.setFocusPolicy(QtCore.Qt.NoFocus)
            cell.setObjectName("cell_"+str(index)+"_"+str(i))
            layout.addWidget(cell)
            self.uiMatrix[index].append(cell)
