"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль.
При выводе события указывать время, когда произошло событие.
"""

from PySide6 import QtWidgets, QtCore, QtGui
from taskA import Ui_MainWindow  # Импортируем класс формы


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

    # def event(self, event: QtCore.QEvent) -> bool:
    #     print(event)
    #     return super().event(event)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        print(event.text(), event.key(), event.keyCombination())
        if event.text() == 'r':
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit.clear()
        return super().keyPressEvent(event)
    
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        print(event)
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.ui.lineEdit.setText('RightButton')
        return super().mousePressEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
