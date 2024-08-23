from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from instr import *
from ThirdWindow import *

class Experiment():
    def __init__(self, age, pulse, final1, final2):
        self.age = age
        self.t1 = pulse
        self.t2 = final1
        self.t3 = final2

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
        self.entername = QLineEdit()
        self.entername.setPlaceholderText(txt_hintname)
        self.enterage = QLineEdit()
        self.enterage.setPlaceholderText(txt_hintage)
        self.enterpulse = QLineEdit()
        self.enterpulse.setPlaceholderText(txt_hinttest1)
        self.enterfinal = QLineEdit()
        self.enterfinal.setPlaceholderText(txt_hinttest3)
        self.enterfinal2 = QLineEdit()
        self.enterfinal2.setPlaceholderText(txt_hinttest3)
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
        self.enterfinal.setFixedWidth(100)
        self.enterfinal2.setFixedWidth(100)
        self.txt_timer = QLabel(txt_timer)
        self.l_line.addWidget(self.name)
        self.l_line.addWidget(self.entername)
        self.l_line.addWidget(self.age)
        self.l_line.addWidget(self.enterage)
        self.l_line.addWidget(self.pulsetest)
        self.l_line.addWidget(self.startpulse)
        self.l_line.addWidget(self.enterpulse)
        self.l_line.addWidget(self.squat)
        self.l_line.addWidget(self.startsquat)
        self.l_line.addWidget(self.finaltest)
        self.l_line.addWidget(self.startfinal)
        self.l_line.addWidget(self.enterfinal)
        self.l_line.addWidget(self.enterfinal2)
        self.l_line.addWidget(self.send, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.txt_timer)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def timerpulse(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timertest.stop()

    def timersquat(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timertest.stop()

    def timerfinal(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if int(time.toString("hh:mm:ss")[6:8]) >= 45 or int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.txt_timer.setStyleSheet("color: rgb(0, 255, 0)")
        else:
            self.txt_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timertest.stop()

    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timertest = QTimer()
        self.timertest.timeout.connect(self.timerpulse)
        self.timertest.start(1000)

    def timer_test2(self):
        global time
        time = QTime(0, 0, 31)
        self.timertest = QTimer()
        self.timertest.timeout.connect(self.timersquat)
        self.timertest.start(1500)

    def timer_test3(self):
        global time
        time = QTime(0, 1, 0)
        self.timertest = QTimer()
        self.timertest.timeout.connect(self.timerfinal)
        self.timertest.start(1000)

    def connect(self):
        self.send.clicked.connect(self.next_click)
        self.startpulse.clicked.connect(self.timer_test)
        self.startsquat.clicked.connect(self.timer_test2)
        self.startfinal.clicked.connect(self.timer_test3)
    
    def next_click(self):
        self.hide()
        self.exp = Experiment(
            int(self.enterage.text()),
            int(self.enterpulse.text()),
            int(self.enterfinal.text()),
            int(self.enterfinal2.text())
        )
        self.tw = FinalWin(self.exp)