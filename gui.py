import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Retirement planner'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.textbox_x = 20
        self.textbox_y = 240
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(self.textbox_y, self.textbox_x)
        self.textbox.setObjectName('Starting amount')

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 60)
        self.textbox.resize(self.textbox_y, self.textbox_x)

        self.button = QPushButton('Run monte carlo', self)
        self.button.move(20, 200)

        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        textbox_val = self.textbox.text()
        QMessageBox.question(self, 'MonteCarloMessage',
                             'You typed: %s' % textbox_val,
                             QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
