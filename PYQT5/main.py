import sys
import logging
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox,
)
from PyQt5 import QtGui
import random_pass as rp

logging.basicConfig(filename="passwords.txt", format="%(message)s", level=logging.INFO)

# Read showMessage setting
with open("showMessage", "r") as f:
    showM = f.read().strip() == "1"


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 500
        self.y = 500
        self.title = "Password Generator"
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, self.x, self.y)
        self.setWindowTitle(self.title)
        self.setFixedSize(self.x, self.y)
        self.setWindowIcon(QtGui.QIcon("lock.png"))

        self.label1 = QLabel("Characters:", self)
        self.label1.move(190, 50)

        self.charsInput = QLineEdit(self)
        self.charsInput.setText("a,b,c,d")
        self.charsInput.setGeometry(190, 100, 100, 30)

        self.label2 = QLabel("Length:", self)
        self.label2.move(190, 150)

        self.passLength = QLineEdit(self)
        self.passLength.setText("5")
        self.passLength.setGeometry(190, 200, 100, 30)

        self.button1 = QPushButton("Generate Password", self)
        self.button1.setGeometry(170, 240, 150, 30)
        self.button1.clicked.connect(self.generatePassword)

        self.deletePassButton = QPushButton("Delete", self)
        self.deletePassButton.setGeometry(10, 460, 120, 30)
        self.deletePassButton.clicked.connect(self.deletePopUp)

        self.show()

    def generatePassword(self):
        global showM
        chars = self.charsInput.text().split(",")
        passLen = int(self.passLength.text())
        password = rp.randomPass(chars, passLen)
        logging.info(f"password: {password}")

        if showM:
            self.messageBox()

    def messageBox(self):
        message = QMessageBox(self)
        message.setText("The password was written to passwords.txt, show this again?")
        message.setWindowTitle("Password")
        message.setIcon(QMessageBox.Question)
        message.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        message.buttonClicked.connect(self.YesNo)
        message.exec_()

    def YesNo(self, button):
        if button.text() == "&No":
            with open("showMessage", "w") as f:
                f.write("0")

    def deletePasswords(self, button):
        if button.text() == "&Yes":
            try:
                with open("passwords.txt", "w") as f:
                    f.write("")
            except FileNotFoundError:
                QMessageBox.warning(
                    self,
                    "Error",
                    "Password file not found. Please press generate password first.",
                )

    def deletePopUp(self):
        message = QMessageBox(self)
        message.setText("Are you sure you want to delete all the passwords?")
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Cancel)
        message.buttonClicked.connect(self.deletePasswords)
        message.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
