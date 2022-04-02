# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.SettingsWidjet = QWidget(self.centralwidget)
        self.SettingsWidjet.setObjectName(u"SettingsWidjet")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SettingsWidjet.sizePolicy().hasHeightForWidth())
        self.SettingsWidjet.setSizePolicy(sizePolicy1)
        self.SettingsWidjet.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.SettingsWidjet)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.OpenFileButton = QPushButton(self.SettingsWidjet)
        self.OpenFileButton.setObjectName(u"OpenFileButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.OpenFileButton.sizePolicy().hasHeightForWidth())
        self.OpenFileButton.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.OpenFileButton)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.label_3 = QLabel(self.SettingsWidjet)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.WidthAndHeightSpinBox = QSpinBox(self.SettingsWidjet)
        self.WidthAndHeightSpinBox.setObjectName(u"WidthAndHeightSpinBox")
        self.WidthAndHeightSpinBox.setMinimumSize(QSize(55, 30))
        self.WidthAndHeightSpinBox.setMaximum(512)
        self.WidthAndHeightSpinBox.setSingleStep(2)
        self.WidthAndHeightSpinBox.setValue(64)

        self.horizontalLayout_3.addWidget(self.WidthAndHeightSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.BlackWhiteModeButton = QCheckBox(self.SettingsWidjet)
        self.BlackWhiteModeButton.setObjectName(u"BlackWhiteModeButton")
        sizePolicy2.setHeightForWidth(self.BlackWhiteModeButton.sizePolicy().hasHeightForWidth())
        self.BlackWhiteModeButton.setSizePolicy(sizePolicy2)
        self.BlackWhiteModeButton.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_2.addWidget(self.BlackWhiteModeButton)

        self.InvertedColorButton = QCheckBox(self.SettingsWidjet)
        self.InvertedColorButton.setObjectName(u"InvertedColorButton")
        self.InvertedColorButton.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_2.addWidget(self.InvertedColorButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.label = QLabel(self.SettingsWidjet)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label)

        self.ContrastValueSpinBox = QDoubleSpinBox(self.SettingsWidjet)
        self.ContrastValueSpinBox.setObjectName(u"ContrastValueSpinBox")
        sizePolicy2.setHeightForWidth(self.ContrastValueSpinBox.sizePolicy().hasHeightForWidth())
        self.ContrastValueSpinBox.setSizePolicy(sizePolicy2)
        self.ContrastValueSpinBox.setMinimumSize(QSize(55, 30))
        self.ContrastValueSpinBox.setMaximum(100.000000000000000)
        self.ContrastValueSpinBox.setSingleStep(0.500000000000000)
        self.ContrastValueSpinBox.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.ContrastValueSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.label_2 = QLabel(self.SettingsWidjet)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.ColorCountSpinBox = QSpinBox(self.SettingsWidjet)
        self.ColorCountSpinBox.setObjectName(u"ColorCountSpinBox")
        self.ColorCountSpinBox.setMinimumSize(QSize(55, 30))
        self.ColorCountSpinBox.setMinimum(1)
        self.ColorCountSpinBox.setMaximum(256)
        self.ColorCountSpinBox.setValue(5)

        self.horizontalLayout_2.addWidget(self.ColorCountSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.SettingsWidjet, 0, 0, 1, 1)

        self.ImageView = QGraphicsView(self.centralwidget)
        self.ImageView.setObjectName(u"ImageView")
        sizePolicy2.setHeightForWidth(self.ImageView.sizePolicy().hasHeightForWidth())
        self.ImageView.setSizePolicy(sizePolicy2)
        self.ImageView.setMinimumSize(QSize(520, 520))
        self.ImageView.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.ImageView, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.OpenFileButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430/\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.BlackWhiteModeButton.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0451\u0440\u043d\u043e-\u0431\u0435\u043b\u044b\u0439 \u0440\u0435\u0436\u0438\u043c", None))
        self.InvertedColorButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0446\u0432\u0435\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0441\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0446\u0432\u0435\u0442\u043e\u0432", None))
    # retranslateUi

