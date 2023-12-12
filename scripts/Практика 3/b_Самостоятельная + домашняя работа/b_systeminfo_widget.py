"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""


from PySide6 import QtWidgets, QtGui, QtCore
from a_threads import SystemInfo  # Подставьте правильный путь к вашему модулю a_threads

class SystemInfoWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Создаем элементы управления
        self.delay_label = QtWidgets.QLabel("Задержка (сек):")
        self.delay_input = QtWidgets.QLineEdit(self)
        self.cpu_label = QtWidgets.QLabel("Загрузка CPU:")
        self.cpu_value = QtWidgets.QLabel(self)
        self.ram_label = QtWidgets.QLabel("Загрузка RAM:")
        self.ram_value = QtWidgets.QLabel(self)

        # Создаем поток SystemInfo
        self.system_info_thread = SystemInfo()

        # Подключаем сигналы к слотам
        self.system_info_thread.systemInfoReceived.connect(self.update_info)
        self.delay_input.textChanged.connect(self.update_delay)

        # Устанавливаем компоновку
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.delay_label)
        layout.addWidget(self.delay_input)
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.cpu_value)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.ram_value)

        # Запускаем поток
        self.system_info_thread.start()

    @QtCore.Slot(list)
    def update_info(self, data):
        cpu, ram = data
        self.cpu_value.setText(f"{cpu}%")
        self.ram_value.setText(f"{ram}%")

    @QtCore.Slot()
    def update_delay(self):
        try:
            delay = float(self.delay_input.text())
            self.system_info_thread.delay = delay
        except ValueError:
            pass  # Можно добавить обработку ошибок ввода

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = SystemInfoWidget()
    widget.show()
    app.exec()