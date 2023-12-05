"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

from PySide6 import QtWidgets, QtCore
import requests


class Worker(QtCore.QObject):
    status = QtCore.Signal(int)
    error = QtCore.Signal(bool, str)

    def run(self, url: str) -> None:
        """
        Метод имитирующий долгую задачу

        :return: None
        """

        response = requests.get(url)
        self.status.emit(response.status_code)


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initThread()
        self.initSignals()

    def initUi(self):
        self.setFixedSize(400, 200)

        self.label = QtWidgets.QLabel('Адрес')
        self.lineEdit = QtWidgets.QLineEdit()
        self.label_res = QtWidgets.QLabel('Результат')
        self.button = QtWidgets.QPushButton('Проверить')

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.label_res)

        self.setLayout(main_layout)

    def initThread(self):
        self.thread = Worker()

    def initSignals(self):
        self.button.clicked.connect(self.checkSite)
        self.thread.status.connect(self.setRes)

    def checkSite(self):
        url = self.lineEdit.text()
        self.button.setEnabled(False)
        self.thread.run(url)

    def setRes(self, res):
        self.button.setEnabled(True)
        self.label_res.setText(f'Код ответа {res}')
        ...


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
