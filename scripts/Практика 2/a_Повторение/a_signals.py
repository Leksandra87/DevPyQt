"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets
from taskB import Ui_MainWindow  # Импортируем класс формы


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Создание "прокси" переменной для работы с формой
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_signals()

    def init_signals(self):
        # self.ui.pushButton.clicked.connect(self.revers_text)
        self.ui.lineEdit.textChanged.connect(self.revers_text)

    def revers_text(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit_2.setText(text[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
