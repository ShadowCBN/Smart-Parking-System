

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_booking(object):


    def setupUi(self, booking):
        booking.setObjectName("booking")
        booking.setEnabled(True)
        booking.resize(751, 440)
        self.centralwidget = QtWidgets.QWidget(booking)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 751, 441))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(510, 240, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.page)
        self.calendarWidget.setGeometry(QtCore.QRect(90, 150, 281, 191))
        self.calendarWidget.setMinimumDate(QtCore.QDate.currentDate())
        self.calendarWidget.setObjectName("calendarWidget")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(510, 280, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 370, 131, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(1))

        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(250, 70, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.timeEdit = QtWidgets.QTimeEdit(self.page)
        self.timeEdit.setGeometry(QtCore.QRect(510, 190, 121, 21))
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.timeEdit.setMaximumTime(QtCore.QTime(19, 0, 0))
        self.timeEdit.setMinimumTime(QtCore.QTime(6, 0, 0))
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.AmPmSection)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(510, 150, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_31 = QtWidgets.QPushButton(self.page)
        self.pushButton_31.setGeometry(QtCore.QRect(70, 0, 75, 23))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_31.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.pushButton_34 = QtWidgets.QPushButton(self.page)
        self.pushButton_34.setGeometry(QtCore.QRect(280, 0, 75, 23))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_33 = QtWidgets.QPushButton(self.page)
        self.pushButton_33.setGeometry(QtCore.QRect(210, 0, 75, 23))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_33.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

        self.pushButton_32 = QtWidgets.QPushButton(self.page)
        self.pushButton_32.setGeometry(QtCore.QRect(140, 0, 75, 23))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_32.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.pushButton_55 = QtWidgets.QPushButton(self.page)
        self.pushButton_55.setEnabled(False)
        self.pushButton_55.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton_55.setObjectName("pushButton_55")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 441))
        self.label.setText("")
        self.label.setPixmap(QPixmap("abc1.jpg"))
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 200, 71, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_19 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_19.setGeometry(QtCore.QRect(540, 260, 71, 21))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 170, 71, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_35 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_35.setGeometry(QtCore.QRect(70, 0, 75, 23))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_35.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.pushButton_12 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_12.setGeometry(QtCore.QRect(240, 230, 71, 21))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 170, 71, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_38 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_38.setGeometry(QtCore.QRect(140, 0, 75, 23))
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_38.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.pushButton_36 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_36.setGeometry(QtCore.QRect(280, 0, 75, 23))
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(140, 170, 71, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_22.setGeometry(QtCore.QRect(240, 290, 71, 21))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_18 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_18.setGeometry(QtCore.QRect(340, 260, 71, 21))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_15.setGeometry(QtCore.QRect(440, 230, 71, 21))
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_20 = QtWidgets.QLabel(self.page_2)
        self.label_20.setGeometry(QtCore.QRect(220, 70, 321, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_20.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_20.setGeometry(QtCore.QRect(440, 260, 71, 21))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_37 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_37.setGeometry(QtCore.QRect(210, 0, 75, 23))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_37.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

        self.pushButton_25 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_25.setGeometry(QtCore.QRect(440, 290, 71, 21))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 200, 71, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_21.setGeometry(QtCore.QRect(140, 290, 71, 21))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_26 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_26.setGeometry(QtCore.QRect(670, 0, 81, 41))
        self.pushButton_26.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_23 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_23.setGeometry(QtCore.QRect(340, 290, 71, 21))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_14.setGeometry(QtCore.QRect(540, 230, 71, 21))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_29 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_29.setGeometry(QtCore.QRect(140, 230, 71, 21))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_17 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_17.setGeometry(QtCore.QRect(240, 260, 71, 21))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_11.setGeometry(QtCore.QRect(540, 170, 71, 21))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_16.setGeometry(QtCore.QRect(140, 260, 71, 21))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_27 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_27.setEnabled(True)
        self.pushButton_27.setGeometry(QtCore.QRect(310, 350, 131, 61))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_27.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.pushButton_13 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_13.setGeometry(QtCore.QRect(340, 230, 71, 21))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_9.setGeometry(QtCore.QRect(540, 200, 71, 21))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 170, 71, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_10.setGeometry(QtCore.QRect(440, 200, 71, 21))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_24 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_24.setGeometry(QtCore.QRect(540, 290, 71, 21))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_8.setGeometry(QtCore.QRect(340, 200, 71, 21))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_56 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_56.setEnabled(False)
        self.pushButton_56.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton_56.setObjectName("pushButton_56")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 751, 441))
        self.label_6.setText("")
        self.label_6.setPixmap(QPixmap("blue1.png"))
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(30, 370, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_16 = QtWidgets.QLabel(self.page_3)
        self.label_16.setGeometry(QtCore.QRect(200, 220, 141, 21))
        self.label_16.setObjectName("label_16")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(30, 220, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_28 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_28.setGeometry(QtCore.QRect(570, 200, 111, 41))
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(200, 320, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_19 = QtWidgets.QLabel(self.page_3)
        self.label_19.setGeometry(QtCore.QRect(350, 70, 141, 21))
        self.label_19.setObjectName("label_19")
        self.label_18 = QtWidgets.QLabel(self.page_3)
        self.label_18.setGeometry(QtCore.QRect(200, 370, 141, 21))
        self.label_18.setObjectName("label_18")
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setGeometry(QtCore.QRect(200, 170, 141, 21))
        self.label_15.setObjectName("label_15")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(30, 270, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_42 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_42.setGeometry(QtCore.QRect(140, 0, 75, 23))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_42.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(200, 70, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_17 = QtWidgets.QLabel(self.page_3)
        self.label_17.setGeometry(QtCore.QRect(200, 270, 141, 21))
        self.label_17.setObjectName("label_17")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(30, 320, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_41 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_41.setGeometry(QtCore.QRect(210, 0, 75, 23))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_41.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setGeometry(QtCore.QRect(200, 120, 141, 21))
        self.label_14.setObjectName("label_14")
        self.pushButton_30 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_30.setGeometry(QtCore.QRect(670, 0, 81, 41))
        self.pushButton_30.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_30")
        self.label_21 = QtWidgets.QLabel(self.page_3)
        self.label_21.setGeometry(QtCore.QRect(30, 170, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.pushButton_39 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_39.setGeometry(QtCore.QRect(70, 0, 75, 23))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_39.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.pushButton_40 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_40.setGeometry(QtCore.QRect(280, 0, 75, 23))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_57 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_57.setEnabled(False)
        self.pushButton_57.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton_57.setObjectName("pushButton_57")
        self.stackedWidget.addWidget(self.page_3)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_22 = QtWidgets.QLabel(self.page_6)
        self.label_22.setGeometry(QtCore.QRect(0, 0, 751, 441))
        self.label_22.setText("")
        self.label_22.setPixmap(QPixmap("white.png"))
        self.label_22.setObjectName("label_22")
        self.pushButton_44 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_44.setGeometry(QtCore.QRect(280, 0, 75, 23))
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_46 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_46.setGeometry(QtCore.QRect(140, 0, 75, 23))
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_46.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.pushButton_43 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_43.setEnabled(False)
        self.pushButton_43.setGeometry(QtCore.QRect(70, 0, 75, 23))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_45 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_45.setGeometry(QtCore.QRect(210, 0, 75, 23))
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_45.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

        self.label_25 = QtWidgets.QLabel(self.page_6)
        self.label_25.setGeometry(QtCore.QRect(40, 170, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.page_6)
        self.label_26.setGeometry(QtCore.QRect(40, 320, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.page_6)
        self.label_27.setGeometry(QtCore.QRect(210, 370, 141, 21))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.page_6)
        self.label_28.setGeometry(QtCore.QRect(210, 270, 141, 21))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.page_6)
        self.label_29.setGeometry(QtCore.QRect(210, 70, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.page_6)
        self.label_30.setGeometry(QtCore.QRect(40, 220, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.page_6)
        self.label_31.setGeometry(QtCore.QRect(210, 120, 141, 21))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.page_6)
        self.label_32.setGeometry(QtCore.QRect(210, 170, 141, 21))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.page_6)
        self.label_33.setGeometry(QtCore.QRect(210, 220, 141, 21))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.page_6)
        self.label_34.setGeometry(QtCore.QRect(40, 370, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.page_6)
        self.label_35.setGeometry(QtCore.QRect(360, 70, 141, 21))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.page_6)
        self.label_36.setGeometry(QtCore.QRect(40, 120, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.page_6)
        self.label_37.setGeometry(QtCore.QRect(40, 270, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.page_6)
        self.label_38.setGeometry(QtCore.QRect(210, 320, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.page_6)
        self.label_39.setGeometry(QtCore.QRect(550, 220, 141, 21))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.page_6)
        self.label_40.setGeometry(QtCore.QRect(350, 220, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.pushButton_58 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_58.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_58.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.pushButton_48 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_48.setGeometry(QtCore.QRect(280, 0, 75, 23))
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_49.setGeometry(QtCore.QRect(210, 0, 75, 23))
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_49.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

        self.pushButton_50 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_50.setEnabled(False)
        self.pushButton_50.setGeometry(QtCore.QRect(140, 0, 75, 23))
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_47 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_47.setGeometry(QtCore.QRect(70, 0, 75, 23))
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_47.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.pushButton_59 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_59.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_59.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.label_41 = QtWidgets.QLabel(self.page_7)
        self.label_41.setGeometry(QtCore.QRect(40, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.textEdit = QtWidgets.QTextEdit(self.page_7)
        self.textEdit.setGeometry(QtCore.QRect(220, 170, 441, 201))
        self.textEdit.setObjectName("textEdit")
        self.label_23 = QtWidgets.QLabel(self.page_7)
        self.label_23.setGeometry(QtCore.QRect(40, 50, 531, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_42 = QtWidgets.QLabel(self.page_7)
        self.label_42.setGeometry(QtCore.QRect(40, 110, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.pushButton_61 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_61.setGeometry(QtCore.QRect(320, 390, 121, 31))
        self.pushButton_61.setObjectName("pushButton_61")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_24 = QtWidgets.QLabel(self.page_8)
        self.label_24.setGeometry(QtCore.QRect(0, 0, 751, 441))
        self.label_24.setText("")
        self.label_24.setPixmap(QPixmap("white.png"))
        self.label_24.setObjectName("label_24")
        self.pushButton_54 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_54.setGeometry(QtCore.QRect(140, 0, 75, 23))
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_54.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))

        self.pushButton_53 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_53.setEnabled(False)
        self.pushButton_53.setGeometry(QtCore.QRect(210, 0, 75, 23))
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_52 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_52.setGeometry(QtCore.QRect(280, 0, 75, 23))
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_51 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_51.setGeometry(QtCore.QRect(70, 0, 75, 23))
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_51.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.pushButton_60 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_60.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_60.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.label_43 = QtWidgets.QLabel(self.page_8)
        self.label_43.setGeometry(QtCore.QRect(30, 160, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.page_8)
        self.label_44.setGeometry(QtCore.QRect(30, 320, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.page_8)
        self.label_45.setGeometry(QtCore.QRect(30, 240, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.page_8)
        self.label_46.setGeometry(QtCore.QRect(30, 70, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.stackedWidget.addWidget(self.page_8)
        booking.setCentralWidget(self.centralwidget)

        self.retranslateUi(booking)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(booking)

    def retranslateUi(self, booking):
        _translate = QtCore.QCoreApplication.translate
        booking.setWindowTitle(_translate("booking", "MainWindow"))
        self.label_5.setText(_translate("booking", "Select Hours:"))
        self.comboBox.setItemText(0, _translate("booking", "--Select--"))
        self.comboBox.setItemText(1, _translate("booking", "1hr"))
        self.comboBox.setItemText(2, _translate("booking", "2hr"))
        self.comboBox.setItemText(3, _translate("booking", "3hr"))
        self.comboBox.setItemText(4, _translate("booking", "4hr"))
        self.comboBox.setItemText(5, _translate("booking", "5hr"))
        self.comboBox.setItemText(6, _translate("booking", "6hr"))
        self.comboBox.setItemText(7, _translate("booking", "7hr"))
        self.comboBox.setItemText(8, _translate("booking", "8hr"))
        self.comboBox.setItemText(9, _translate("booking", "9hr"))
        self.comboBox.setItemText(10, _translate("booking", "10hr"))
        self.comboBox.setItemText(11, _translate("booking", "11hr"))
        self.comboBox.setItemText(12, _translate("booking", "12hr"))
        self.pushButton_4.setText(_translate("booking", "NEXT"))
        self.label_2.setText(_translate("booking", "SELECT DATE AND TIME"))
        self.label_3.setText(_translate("booking", "DATE:"))
        self.label_4.setText(_translate("booking", "Start Time:"))
        self.pushButton_31.setText(_translate("booking", "View Booking"))
        self.pushButton_34.setText(_translate("booking", "Logout"))
        self.pushButton_33.setText(_translate("booking", "About Us"))
        self.pushButton_32.setText(_translate("booking", "Contact Us"))
        self.pushButton_55.setText(_translate("booking", "Book"))
        self.pushButton_6.setText(_translate("booking", "a2"))
        self.pushButton_19.setText(_translate("booking", "e4"))
        self.pushButton_5.setText(_translate("booking", "d1"))
        self.pushButton_35.setText(_translate("booking", "View Booking"))
        self.pushButton_12.setText(_translate("booking", "b3"))
        self.pushButton_2.setText(_translate("booking", "b1"))
        self.pushButton_38.setText(_translate("booking", "Contact Us"))
        self.pushButton_36.setText(_translate("booking", "Logout"))
        self.pushButton.setText(_translate("booking", "a1"))
        self.pushButton_22.setText(_translate("booking", "b5"))
        self.pushButton_18.setText(_translate("booking", "c4"))
        self.pushButton_15.setText(_translate("booking", "d3"))
        self.label_20.setText(_translate("booking", " SELECT YOUR SLOT"))
        self.pushButton_20.setText(_translate("booking", "d4"))
        self.pushButton_37.setText(_translate("booking", "About Us"))
        self.pushButton_25.setText(_translate("booking", "d5"))
        self.pushButton_7.setText(_translate("booking", "b2"))
        self.pushButton_21.setText(_translate("booking", "a5"))
        self.pushButton_26.setText(_translate("booking", "⬅️"))
        self.pushButton_23.setText(_translate("booking", "c5"))
        self.pushButton_14.setText(_translate("booking", "e3"))
        self.pushButton_29.setText(_translate("booking", "a3"))
        self.pushButton_17.setText(_translate("booking", "b4"))
        self.pushButton_11.setText(_translate("booking", "e1"))
        self.pushButton_16.setText(_translate("booking", "a4"))
        self.pushButton_27.setText(_translate("booking", "BOOK NOW"))
        self.pushButton_13.setText(_translate("booking", "c3"))
        self.pushButton_9.setText(_translate("booking", "e2"))
        self.pushButton_3.setText(_translate("booking", "c1"))
        self.pushButton_10.setText(_translate("booking", "d2"))
        self.pushButton_24.setText(_translate("booking", "e5"))
        self.pushButton_8.setText(_translate("booking", "c2"))
        self.pushButton_56.setText(_translate("booking", "Book"))
        self.label_12.setText(_translate("booking", "Total Cost:"))
        self.label_16.setText(_translate("booking", "3"))
        self.label_7.setText(_translate("booking", "Car number:"))
        self.label_9.setText(_translate("booking", "START TIME:"))
        self.pushButton_28.setText(_translate("booking", "PayBill"))
        self.label_13.setText(_translate("booking", "₹30"))
        self.label_19.setText(_translate("booking", "3"))
        self.label_18.setText(_translate("booking", "3"))
        self.label_15.setText(_translate("booking", "2"))
        self.label_10.setText(_translate("booking", "END TIME:"))
        self.pushButton_42.setText(_translate("booking", "Contact Us"))
        self.label_8.setText(_translate("booking", "User Name:"))
        self.label_17.setText(_translate("booking", "3"))
        self.label_11.setText(_translate("booking", "Cost Per Hour:"))
        self.pushButton_41.setText(_translate("booking", "About Us"))
        self.label_14.setText(_translate("booking", "1"))
        self.pushButton_30.setText(_translate("booking", "⬅️"))
        self.label_21.setText(_translate("booking", "Slot number:"))
        self.pushButton_39.setText(_translate("booking", "View Booking"))
        self.pushButton_40.setText(_translate("booking", "Logout"))
        self.pushButton_57.setText(_translate("booking", "Book"))
        self.pushButton_44.setText(_translate("booking", "Logout"))
        self.pushButton_46.setText(_translate("booking", "Contact Us"))
        self.pushButton_43.setText(_translate("booking", "View Booking"))
        self.pushButton_45.setText(_translate("booking", "About Us"))
        self.label_25.setText(_translate("booking", "Slot number:"))
        self.label_26.setText(_translate("booking", "Cost Per Hour:"))
        self.label_27.setText(_translate("booking", "3"))
        self.label_28.setText(_translate("booking", "3"))
        self.label_29.setText(_translate("booking", "User Name:"))
        self.label_30.setText(_translate("booking", "START TIME:"))
        self.label_31.setText(_translate("booking", "1"))
        self.label_32.setText(_translate("booking", "2"))
        self.label_33.setText(_translate("booking", "3"))
        self.label_34.setText(_translate("booking", "Total Cost:"))
        self.label_35.setText(_translate("booking", "3"))
        self.label_36.setText(_translate("booking", "Car number:"))
        self.label_37.setText(_translate("booking", "END TIME:"))
        self.label_38.setText(_translate("booking", "₹30"))
        self.label_39.setText(_translate("booking", "3"))
        self.label_40.setText(_translate("booking", "#Token_Number:"))
        self.pushButton_58.setText(_translate("booking", "Book"))
        self.pushButton_48.setText(_translate("booking", "Logout"))
        self.pushButton_49.setText(_translate("booking", "About Us"))
        self.pushButton_50.setText(_translate("booking", "Contact Us"))
        self.pushButton_47.setText(_translate("booking", "View Booking"))
        self.pushButton_59.setText(_translate("booking", "Book"))
        self.label_41.setText(_translate("booking", "Your Query:"))
        self.label_23.setText(_translate("booking", "Mail Us At                 :             CarParking@siesgst.ac.in"))
        self.label_42.setText(_translate("booking", "Contact Number       :             1234567890"))
        self.pushButton_61.setText(_translate("booking", "Submit"))
        self.pushButton_54.setText(_translate("booking", "Contact Us"))
        self.pushButton_53.setText(_translate("booking", "About Us"))
        self.pushButton_52.setText(_translate("booking", "Logout"))
        self.pushButton_51.setText(_translate("booking", "View Booking"))
        self.pushButton_60.setText(_translate("booking", "Book"))
        self.label_43.setText(_translate("booking", "Ritvij Iyer                    :             117A3014"))
        self.label_44.setText(_translate("booking", "Rajesh  Jethwa            :             117A3018"))
        self.label_45.setText(_translate("booking", "Shreyas Jaiswal           :             117A3017"))
        self.label_46.setText(_translate("booking", "MANAGED & CREATED BY:-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    booking = QtWidgets.QMainWindow()
    ui = Ui_booking()
    ui.setupUi(booking)
    booking.show()
    sys.exit(app.exec_())

