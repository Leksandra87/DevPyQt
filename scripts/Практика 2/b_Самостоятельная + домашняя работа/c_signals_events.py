"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана +
    * На каком экране окно находится
    * Размеры окна +
    * Минимальные размеры окна +
    * Текущее положение (координаты) окна +
    * Координаты центра приложения +
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

from PySide6 import QtWidgets, QtCore, QtGui
from c_from_ui import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.spinBoxX.setMaximum(1999)
        self.ui.spinBoxY.setMaximum(1999)

        self.init_signals()

    def init_signals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        ...

        self.ui.pushButtonLT.clicked.connect(self.move_to_lt)
        self.ui.pushButtonRT.clicked.connect(self.move_to_rt)
        self.ui.pushButtonLB.clicked.connect(self.move_to_lb)
        self.ui.pushButtonRB.clicked.connect(self.move_to_rb)
        self.ui.pushButtonCenter.clicked.connect(self.move_to_center)

        self.ui.pushButtonGetData.clicked.connect(self.get_data)

        self.ui.pushButtonMoveCoords.clicked.connect(self.set_coords)

    def move_to_lt(self) -> None:
        """
        Перемещение окна в левый верхний угол
        """
        self.move(0, 0)

    def move_to_rt(self) -> None:
        """
        Перемещение окна в правый верхний угол
        """
        screen = self.screen().availableSize().toTuple()
        size = self.rect().size().toTuple()
        x = screen[0] - size[0]
        self.move(x, 0)

    def move_to_lb(self) -> None:
        """
        Перемещение окна в левый нижний угол
        """
        size = self.rect().size().toTuple()
        screen = self.screen().availableSize().toTuple()
        y = screen[1] - size[1] - 40
        self.move(0, y)

    def move_to_rb(self) -> None:
        """
        Перемещение окна в правый нижний угол
        """
        screen = self.screen().availableSize().toTuple()
        size = self.rect().size().toTuple()
        x = screen[0] - size[0]
        y = screen[1] - size[1] - 40
        self.move(x, y)

    def move_to_center(self) -> None:
        """
        Перемещение окна в центр
        """
        screen = self.screen().availableSize().toTuple()
        size = self.rect().size().toTuple()
        x = screen[0] // 2 - size[0] // 2
        y = screen[1] // 2 - size[1] // 2
        self.move(x, y)

    def get_data(self) -> None:
        """
        Получение данных о состоянии окна
        """

        the_time = QtCore.QDateTime.currentDateTime().toString("dd.MM.yyyy HH:mm:ss")
        screen = self.screen().availableSize().toTuple()
        size = self.rect().size().toTuple()
        min_size = self.minimumSize().toTuple()
        pos = self.pos().toTuple()
        center = self.rect().center().toTuple()

        self.ui.plainTextEdit.setPlainText(f'{the_time} \n'
                                           f'Разрешение экрана {screen} \n'
                                           f'Размеры окна {size} \n'
                                           f'Минимальные размеры окна {min_size} \n'
                                           f'Текущее положение (координаты) окна {pos} \n'
                                           f'Координаты центра приложения {center} \n')

        #  print(self.geometry().getCoords()) # координаты верхнего левого и нижнего правого угла
        # print(self.pos().toTuple()) # координаты верхнего левого угла в доступной части экрана
        # print(self.rect().size().toTuple()) # размеры окна приложения
        # print(self.rect().center().toTuple()) # координаты центра окна приложения
        # print(self.screen().size()) # размер экрана
        # print(self.screen().availableSize().toTuple())  # размер доступной области экрана
        # print(self.minimumSize().toTuple()) # минимальные размеры окна

    def set_coords(self) -> None:
        """
        Задает координаты окна
        """

        x = int(self.ui.spinBoxX.value())
        y = int(self.ui.spinBoxY.value())
        self.move(x, y)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Событие изменения положения окна

        :param event: QtGui.QMoveEvent
        :return: None
        """

        old = event.oldPos().toTuple()
        new = event.pos().toTuple()
        print(f'{QtCore.QDateTime.currentDateTime().toString("dd.MM.yyyy HH:mm:ss")}\n'
              f'Previous coordinates: {old}'
              f'\nCurrent coordinates: {new}')

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Событие изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """

        print(f'{QtCore.QDateTime.currentDateTime().toString("dd.MM.yyyy HH:mm:ss")} '
              f'Window size: {event.size().toTuple()}')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
