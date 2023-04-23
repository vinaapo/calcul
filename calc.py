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

text1 = QLabel('''Для подсчета итогового кооличества вырабатываемой энергии введите данные в полях. 
P.s. результат считался по формуле N = mgS. (N - энергия, m - масса, g - ускорение, S - путь. Путь (S) = диаметр колеса * 3,14 (число ПИ)''')

button1 = QPushButton('Произвести расчёты')

text2 = QLabel('Результат:')


def calculate():
    massa = inp1.text()
    dia = inp2.text()
    kol = inp3.text()
    dia = int(dia)
    kol = int(kol)
    massa = int(massa)
    dlina = dia * 3.14
    nrg = massa * 10 * dlina * kol
    text2 = QLabel('Результат:', nrg, 'Ватт')
    line6.addWidget(text2)

line1 = QHBoxLayout()
mainline.addLayout(line1)
line1.addWidget(text1)

line2 = QHBoxLayout()
mainline.addLayout(line2)
line2.addWidget(inp1)

line3 = QHBoxLayout()
mainline.addLayout(line3)
line3.addWidget(inp2)

line4 = QHBoxLayout()
mainline.addLayout(line4)
line4.addWidget(inp3)

line5 = QHBoxLayout()
mainline.addLayout(line5)
line5.addWidget(button1)

line6 = QHBoxLayout()
mainline.addLayout(line6)
line6.addWidget(text2)

window.show()
app.exec_()
