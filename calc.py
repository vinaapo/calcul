from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(500,500)
window.setWindowTitle('Калькулятор хомячьей электроэнергетики')

mainline = QVBoxLayout()
window.setLayout(mainline)

inp1 = QLineEdit()
inp1.setPlaceholderText('Введите массу хомяка в кг')

inp2 = QLineEdit()
inp2.setPlaceholderText('Введите диаметр колеса в м')

inp3 = QLineEdit()
inp3.setPlaceholderText('Введите количество хомяков')

def raschet():
    massa = inp1.text()
    dia = inp2.text()
    kol = inp3.text()
    dia = int(dia)
    kol = int(kol)
    massa = int(massa)
    dlina = dia * 3.14
    nrg = massa * 10 * dlina * kol

mainline = QVBoxLayout()

line1 = QHBoxLayout()
mainline.addLayout(line1)

line2 = QHBoxLayout()
mainline.addLayout(line2)

line3 = QHBoxLayout()
mainline.addLayout(line3)

line4 = QHBoxLayout()
mainline.addLayout(line4)

line5 = QHBoxLayout()
mainline.addLayout(line5)

line6 = QHBoxLayout()
mainline.addLayout(line6)


window.show()
app.exec_()
