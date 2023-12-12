"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets

from b_systeminfo_widget import SystemInfoWidget  # Подставьте правильный путь к вашему модулю с SystemInfoWidget
from c_weatherapi_widget1 import WeatherWidget  # Подставьте правильный путь к вашему модулю с WeatherWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем TabWidget
        tab_widget = QtWidgets.QTabWidget(self)

        # Создаем и добавляем виджет SystemInfoWidget на первую вкладку
        system_info_tab = QtWidgets.QWidget()
        system_info_layout = QtWidgets.QVBoxLayout(system_info_tab)
        system_info_widget = SystemInfoWidget()
        system_info_layout.addWidget(system_info_widget)
        tab_widget.addTab(system_info_tab, "System Info")

        # Создаем и добавляем виджет WeatherWidget на вторую вкладку
        weather_tab = QtWidgets.QWidget()
        weather_layout = QtWidgets.QVBoxLayout(weather_tab)
        weather_widget = WeatherWidget()
        weather_layout.addWidget(weather_widget)
        tab_widget.addTab(weather_tab, "Weather")

        # Устанавливаем TabWidget в центр главного окна
        self.setCentralWidget(tab_widget)

class CombinedWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Создаем QGroupBox для SystemInfoWidget
        system_info_group_box = QtWidgets.QGroupBox("Информация о системе", self)

        # Создаем QHBoxLayout для SystemInfoWidget
        system_info_layout = QtWidgets.QHBoxLayout(system_info_group_box)

        # Добавляем виджет SystemInfoWidget
        system_info_widget = SystemInfoWidget()
        system_info_layout.addWidget(system_info_widget)

        # Создаем QGroupBox для WeatherWidget
        weather_group_box = QtWidgets.QGroupBox("Информация о погоде", self)

        # Создаем QHBoxLayout для WeatherWidget
        weather_layout = QtWidgets.QHBoxLayout(weather_group_box)

        # Добавляем виджет WeatherWidget
        weather_widget = WeatherWidget()
        weather_layout.addWidget(weather_widget)

        # Создаем QVBoxLayout для главного окна и добавляем QGroupBox'ы
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addWidget(system_info_group_box)
        main_layout.addWidget(weather_group_box)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    main_window = CombinedWidget()
    main_window.show()
    app.exec()