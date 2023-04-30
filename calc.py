from PyQt5.QtWidgets import *
from PyQt5.QtGui import*

app = QApplication([])
window = QWidget()
window.setWindowTitle('Калькулятор хомячьей электроэнергетики')
window.setStyleSheet('''QWidget{
background: qlineargradient( x1:0 y1:0, x2:1 y2:0
stop:0	rgb(72,209,204), stop:1 rgb(0,139,139)	
);}''')

mainline = QVBoxLayout()
window.setLayout(mainline)

inp1 = QLineEdit()
inp1.setPlaceholderText('Введите массу хомяка в кг')
inp1.setStyleSheet('''QLineEdit{font-size:16px; background:rgb(95,158,160);}''')

inp2 = QLineEdit()
inp2.setPlaceholderText('Введите диаметр колеса в м')
inp2.setStyleSheet('''QLineEdit{font-size:16px; background:rgb(95,158,160);}''')

inp3 = QLineEdit()
inp3.setPlaceholderText('Введите количество хомяков')
inp3.setStyleSheet('''QLineEdit{font-size:16px; background:rgb(95,158,160);}''')

text1 = QLabel('''Для подсчета итогового кооличества вырабатываемой энергии введите данные в полях. 
P.s. результат считался по формуле N = mgS. (N - энергия, m - масса, g - ускорение, S - путь. Путь (S) = диаметр колеса * 3,14 (число ПИ)''')
text1.setStyleSheet('''QLabel{font-size:14px;}''')

button1 = QPushButton('Произвести расчёты')
button1.setStyleSheet('''QPushButton{font-size:16px;background:rgb(102,205,170);}''')

text2 = QLabel('Результат:')


def calculate():
    massa = inp1.text()
    dia = inp2.text()
    kol = inp3.text()
    dia = float(dia)
    kol = float(kol)
    massa = float(massa)
    dlina = dia * 3.14
    nrg = massa * 10 * dlina * kol
    nrg = round(nrg, 2)
    result = 'Результат: '+str(nrg)+' Ватт'
    text2 = QLabel(result)
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

button1.clicked.connect(calculate)

window.show()
app.exec_()

