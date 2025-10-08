# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import icon.icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1382, 635)
        MainWindow.setStyleSheet(u"border-radius:4px;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1161, 591))
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_1 = QFrame(self.frame)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setGeometry(QRect(0, 0, 291, 591))
        self.frame_1.setStyleSheet(u"QFrame#frame_1{\n"
"	background-color: rgb(123, 169, 255);\n"
"	border-top-left-radius:32px;\n"
"	border-top-right-radius:0px;\n"
"	border-bottom-right-radius:0px;\n"
"	border-bottom-left-radius:32px;\n"
"}")
        self.frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.inter_tilte = QPushButton(self.frame_1)
        self.inter_tilte.setObjectName(u"inter_tilte")
        self.inter_tilte.setGeometry(QRect(0, 10, 281, 71))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        font.setBold(True)
        font.setKerning(True)
        self.inter_tilte.setFont(font)
        self.inter_tilte.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/svg/namicailiao.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.inter_tilte.setIcon(icon)
        self.inter_tilte.setIconSize(QSize(28, 28))
        self.label_7 = QLabel(self.frame_1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 90, 291, 3))
        self.label_7.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.btn_select_win111111 = QPushButton(self.frame_1)
        self.btn_select_win111111.setObjectName(u"btn_select_win111111")
        self.btn_select_win111111.setGeometry(QRect(0, 480, 291, 61))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setKerning(True)
        self.btn_select_win111111.setFont(font1)
        self.btn_select_win111111.setStyleSheet(u"QPushButton:hover{\n"
"    background-color:rgb(85, 117, 177);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/svg/wenjian-white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_select_win111111.setIcon(icon1)
        self.btn_select_win111111.setIconSize(QSize(20, 20))
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(290, 0, 951, 591))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 951, 41))
        self.frame_4.setStyleSheet(u"background-color: #f7f8ff;\n"
"border-top-right-radius:32px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.min_window = QPushButton(self.frame_4)
        self.min_window.setObjectName(u"min_window")
        self.min_window.setGeometry(QRect(830, 0, 41, 41))
        self.min_window.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.min_window.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius:0px;\n"
"	border-top-right-radius:0px;\n"
"	border-bottom-right-radius:0px;\n"
"	border-bottom-left-radius:0px;\n"
"	color:#928ae1;\n"
"	icon:url(:/svg/zuixiaohua_purple.svg);\n"
"}	\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"	border:none;\n"
"	padding: 3px;\n"
"	color: #FFFFFF;\n"
"	icon:url(:/svg/zuixiaohua_white.svg);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/svg/minwin.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.min_window.setIcon(icon2)
        self.min_window.setIconSize(QSize(26, 26))
        self.max_window = QPushButton(self.frame_4)
        self.max_window.setObjectName(u"max_window")
        self.max_window.setGeometry(QRect(870, 0, 41, 41))
        self.max_window.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius:0px;\n"
"	border-top-right-radius:0px;\n"
"	border-bottom-right-radius:0px;\n"
"	border-bottom-left-radius:0px;\n"
"	color:#928ae1;\n"
"	icon:url(:/svg/zuidahua_purple.svg);\n"
"}	\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"	border:none;\n"
"	padding: 3px;\n"
"	color: #FFFFFF;\n"
"	icon:url(:/svg/zuidahua_white.svg);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/svg/maxwin.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.max_window.setIcon(icon3)
        self.max_window.setIconSize(QSize(26, 26))
        self.close_window = QPushButton(self.frame_4)
        self.close_window.setObjectName(u"close_window")
        self.close_window.setGeometry(QRect(910, 0, 41, 41))
        self.close_window.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius:0px;\n"
"	border-top-right-radius:32px;\n"
"	border-bottom-right-radius:0px;\n"
"	border-bottom-left-radius:0px;\n"
"	color:#928ae1;\n"
"	icon:url(:/svg/guanbi_purple.svg);\n"
"}	\n"
"\n"
"QPushButton:hover{\n"
"	border-top-left-radius:0px;\n"
"	border-top-right-radius:32px;\n"
"	border-bottom-right-radius:0px;\n"
"	border-bottom-left-radius:0px;\n"
"    background-color:rgb(146, 138, 255);\n"
"	border:none;\n"
"	padding: 3px;\n"
"	color: #FFFFFF;\n"
"	icon:url(:/svg/guanbi_white.svg);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/svg/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_window.setIcon(icon4)
        self.close_window.setIconSize(QSize(26, 26))
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, 39, 951, 551))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(951, 551))
        self.frame_2.setStyleSheet(u"border-top-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"background-color: #e7e8f0;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(13)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.file_widget = QWidget(self.frame_2)
        self.file_widget.setObjectName(u"file_widget")
        sizePolicy.setHeightForWidth(self.file_widget.sizePolicy().hasHeightForWidth())
        self.file_widget.setSizePolicy(sizePolicy)
        self.file_widget.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.file_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1382, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.inter_tilte.setText(QCoreApplication.translate("MainWindow", u" \u7eb3\u7c73\u6750\u6599\u529b\u5b66\u6027\u80fd\u5206\u6790", None))
        self.label_7.setText("")
        self.btn_select_win111111.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u65b0\u6587\u4ef6\u563f\u563f\u563f", None))
        self.min_window.setText("")
        self.max_window.setText("")
        self.close_window.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\u7eb3\u7c73\u6750\u6599\u529b\u5b66\u6027\u80fd\u5206\u6790\u7cfb\u7edf", None))
    # retranslateUi

