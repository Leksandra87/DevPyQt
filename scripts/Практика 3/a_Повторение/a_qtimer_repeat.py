"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets, QtCore
from datetime import datetime


# e_simple
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initimer()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """
        self.plainText = QtWidgets.QPlainTextEdit()
        self.spinbox = QtWidgets.QSpinBox()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.plainText)
        layout.addWidget(self.spinbox)

        self.setLayout(layout)



    def initimer(self) -> None:
        """
        Инициализация таймеров

        :return: None
        """

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)  # раз в секунду
        self.timer.start()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.timer.timeout.connect(self.some_func)
        self.spinbox.valueChanged.connect(self.ch_int)

    def ch_int(self, value):
        self.timer.setInterval(value * 100 + 100)

    def some_func(self):
        self.plainText.appendPlainText(str(datetime.now()))

    # def showTime(self) -> None:
    #     """
    #     Слот для отображения в labelTime текущего времени
    #
    #     :return: None
    #     """
    #
    #     time = QtCore.QDateTime.currentDateTime()
    #     timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
    #     self.labelTime.setText(timeDisplay)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
