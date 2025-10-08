# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_container.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Container(object):
    def setupUi(self, Container):
        if not Container.objectName():
            Container.setObjectName(u"Container")
        Container.resize(785, 344)
        self.verticalLayout = QVBoxLayout(Container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_up = QFrame(Container)
        self.frame_up.setObjectName(u"frame_up")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_up.sizePolicy().hasHeightForWidth())
        self.frame_up.setSizePolicy(sizePolicy)
        self.frame_up.setMinimumSize(QSize(0, 30))
        self.frame_up.setMaximumSize(QSize(16777215, 30))
        self.frame_up.setStyleSheet(u"")
        self.frame_up.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_up.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_up)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_rencent_opened = QLabel(self.frame_up)
        self.label_rencent_opened.setObjectName(u"label_rencent_opened")
        font = QFont()
        font.setPointSize(10)
        self.label_rencent_opened.setFont(font)
        self.label_rencent_opened.setStyleSheet(u"QLabel{\n"
"color:rgb(150, 150, 150);\n"
"}")

        self.horizontalLayout.addWidget(self.label_rencent_opened)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.add_button = QPushButton(self.frame_up)
        self.add_button.setObjectName(u"add_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy1)
        self.add_button.setMinimumSize(QSize(25, 25))
        self.add_button.setMaximumSize(QSize(25, 25))
        self.add_button.setStyleSheet(u" QPushButton {\n"
"                background-color: transparent;\n"
"                border: none;\n"
"                border-radius: 3px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgba(50,50,50,127); /* Change to red on hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgba(127.127,127,127); /* Change to brown when pressed */\n"
"            }")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_button.setIcon(icon)
        self.add_button.setIconSize(QSize(22, 22))
        self.add_button.setFlat(True)

        self.horizontalLayout.addWidget(self.add_button)

        self.delete_button = QPushButton(self.frame_up)
        self.delete_button.setObjectName(u"delete_button")
        sizePolicy1.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy1)
        self.delete_button.setMinimumSize(QSize(25, 25))
        self.delete_button.setMaximumSize(QSize(25, 25))
        self.delete_button.setStyleSheet(u"QPushButton {\n"
"                background-color: transparent;\n"
"                border: none;\n"
"                border-radius: 3px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color:rgb(255, 85, 88); /* Change to red on hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: brown; /* Change to brown when pressed */\n"
"            }")
        icon1 = QIcon()
        icon1.addFile(u"icon/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setIconSize(QSize(22, 22))
        self.delete_button.setFlat(True)

        self.horizontalLayout.addWidget(self.delete_button)

        self.horizontalSpacer_right = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_right)


        self.verticalLayout.addWidget(self.frame_up)

        self.frame_down = QFrame(Container)
        self.frame_down.setObjectName(u"frame_down")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_down.sizePolicy().hasHeightForWidth())
        self.frame_down.setSizePolicy(sizePolicy2)
        self.frame_down.setStyleSheet(u"QFrame{\n"
"background-color: transparent;\n"
"border: none;\"\n"
"}")
        self.frame_down.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_down.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_down)

        self.verticalSpacer_down = QSpacerItem(20, 139, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_down)


        self.retranslateUi(Container)

        QMetaObject.connectSlotsByName(Container)
    # setupUi

    def retranslateUi(self, Container):
        Container.setWindowTitle(QCoreApplication.translate("Container", u"Container", None))
        self.label_rencent_opened.setText(QCoreApplication.translate("Container", u"\u6700\u8fd1\u6253\u5f00\u7684\u6587\u4ef6", None))
        self.add_button.setText("")
        self.delete_button.setText("")
    # retranslateUi

