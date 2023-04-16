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
