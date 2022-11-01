# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiSettings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(600, 419)
        settings.setStyleSheet("")
        self.start = QtWidgets.QPushButton(settings)
        self.start.setGeometry(QtCore.QRect(220, 300, 131, 51))
        self.start.setObjectName("start")
        self.cell_size = QtWidgets.QSpinBox(settings)
        self.cell_size.setGeometry(QtCore.QRect(180, 120, 101, 22))
        self.cell_size.setMinimum(5)
        self.cell_size.setProperty("value", 20)
        self.cell_size.setObjectName("cell_size")
        self.speed = QtWidgets.QSpinBox(settings)
        self.speed.setGeometry(QtCore.QRect(180, 160, 101, 22))
        self.speed.setMaximum(360)
        self.speed.setProperty("value", 25)
        self.speed.setObjectName("speed")
        self.window_h = QtWidgets.QSpinBox(settings)
        self.window_h.setGeometry(QtCore.QRect(180, 70, 101, 22))
        self.window_h.setMaximum(16666)
        self.window_h.setSingleStep(10)
        self.window_h.setProperty("value", 768)
        self.window_h.setObjectName("window_h")
        self.label = QtWidgets.QLabel(settings)
        self.label.setGeometry(QtCore.QRect(40, 30, 113, 19))
        self.label.setStyleSheet("font-size: 14px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(settings)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 96, 17))
        self.label_2.setStyleSheet("font-size: 14px;")
        self.label_2.setObjectName("label_2")
        self.window_w = QtWidgets.QSpinBox(settings)
        self.window_w.setGeometry(QtCore.QRect(180, 30, 101, 22))
        self.window_w.setMaximum(16666)
        self.window_w.setSingleStep(10)
        self.window_w.setProperty("value", 1368)
        self.window_w.setObjectName("window_w")
        self.label_3 = QtWidgets.QLabel(settings)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 138, 17))
        self.label_3.setStyleSheet("font-size: 14px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(settings)
        self.label_4.setGeometry(QtCore.QRect(90, 160, 62, 17))
        self.label_4.setStyleSheet("font-size: 14px;")
        self.label_4.setObjectName("label_4")
        self.cell_color_btn = QtWidgets.QPushButton(settings)
        self.cell_color_btn.setGeometry(QtCore.QRect(410, 30, 111, 51))
        self.cell_color_btn.setObjectName("cell_color_btn")
        self.field_color_btn = QtWidgets.QPushButton(settings)
        self.field_color_btn.setGeometry(QtCore.QRect(410, 140, 111, 51))
        self.field_color_btn.setObjectName("field_color_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(settings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 210, 160, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Settings"))
        self.start.setText(_translate("settings", "Начать симуляцию"))
        self.label.setText(_translate("settings", "<html><head/><body><p><span style=\" font-size:12pt;\">Ширина экрана</span></p></body></html>"))
        self.label_2.setText(_translate("settings", "Высота экрана"))
        self.label_3.setText(_translate("settings", "Размер одной клетки"))
        self.label_4.setText(_translate("settings", "Скорость"))
        self.cell_color_btn.setText(_translate("settings", "Цвет клетки"))
        self.field_color_btn.setText(_translate("settings", "Цвет поля"))
        self.radioButton_2.setText(_translate("settings", "Рандомная симуляция"))
        self.radioButton.setText(_translate("settings", "Изначально пустое поле"))
