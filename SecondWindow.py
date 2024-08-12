from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from instr import *
from ThirdWindow import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connect()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.name = QLabel(txt_name)
        self.age = QLabel(txt_age)
        self.pulsetest = QLabel(txt_test1)
        self.squat = QLabel(txt_test2)
        self.finaltest = QLabel(txt_test3)
        self.entername = QLineEdit(txt_hintname)
        self.enterage = QLineEdit(txt_hintage)
        self.enterpulse = QLineEdit(txt_hinttest1)
        self.entersquat = QLineEdit(txt_hinttest2)
        self.enterfinal = QLineEdit(txt_hinttest3)
        self.enterfinal2 = QLineEdit(txt_hinttest3)
        self.startpulse = QPushButton(txt_starttest1)
        self.startsquat = QPushButton(txt_starttest2)
        self.startfinal = QPushButton(txt_starttest3)
        self.send = QPushButton(txt_sendresults)
        self.send.setFixedWidth(100)
        self.startpulse.setFixedWidth(100)
        self.startsquat.setFixedWidth(100)
        self.startfinal.setFixedWidth(100)
        self.entername.setFixedWidth(100)
        self.enterage.setFixedWidth(100)
        self.enterpulse.setFixedWidth(100)
        self.entersquat.setFixedWidth(100)
        self.enterfinal.setFixedWidth(100)
        self.enterfinal2.setFixedWidth(100)
        self.timer = QLabel(txt_timer)
        self.l_line.addWidget(self.name)
        self.l_line.addWidget(self.entername)
        self.l_line.addWidget(self.age)
        self.l_line.addWidget(self.enterage)
        self.l_line.addWidget(self.pulsetest)
        self.l_line.addWidget(self.enterpulse)
        self.l_line.addWidget(self.squat)
        self.l_line.addWidget(self.entersquat)
        self.l_line.addWidget(self.finaltest)
        self.l_line.addWidget(self.enterfinal)
        self.l_line.addWidget(self.enterfinal2)
        self.l_line.addWidget(self.send, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.timer)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)


    def connect(self):
        self.send.clicked.connect(self.next_click)
    
    def next_click(self):
        self.hide()
        self.tw = FinalWin()