from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.setWindowTitle('Калькулятор хомячьей электроэнергетики')
window.resize(500,500)

mainline = QVBoxLayout()
window.setLayout(mainline)

line1 = QVBoxLayout()
line2 = QVBoxLayout()
mainline.addLayout(line1)
mainline.addLayout(line2)

text1 = QLabel('P.s. данные для расчета были взяты при средней массе ')

window.show()
app.exec_()
