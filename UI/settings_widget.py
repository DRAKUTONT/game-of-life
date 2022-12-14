from PyQt5.QtWidgets import QWidget, QColorDialog
from UI.about_widget import AboutGame
from UI.settings_ui import UiSettings
from game.GameOfLife import GameOfLife


class SettingWidget(QWidget, UiSettings):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setupUi(self)
        self.connect_button(self.cell_color_btn, self.choose_cell_color)
        self.connect_button(self.field_color_btn, self.choose_field_color)
        self.connect_button(self.about_game, self.about)
        self.connect_button(self.start, self.start_game)
        self.radioButton_2.setChecked(True)

        self.field_color = (0, 0, 0)
        self.cell_color = (190, 100, 100)
        self.is_random = 'r'

    def about(self) -> None:
        """Об игре"""
        self.hide()
        widget = AboutGame(self)
        widget.show()

    def choose_cell_color(self) -> None:
        """Выбор цвета клетки"""
        color = QColorDialog.getColor()
        self.cell_color = color.getRgb()[:3]

    def choose_field_color(self) -> None:
        """Выбор цвета поля"""
        color = QColorDialog.getColor()
        self.field_color = color.getRgb()[:3]

    def start_game(self) -> None:
        """Старт игры"""
        self.is_random = 'r' if self.radioButton_2.isChecked() else False

        game = GameOfLife(width=self.window_w.value(), height=self.window_h.value(), cell_size=self.cell_size.value(),
                          speed=self.speed.value(), grid=self.is_random,
                          cell_color=self.cell_color, field_color=self.field_color)
        game.run()

    @staticmethod
    def connect_button(button, handler) -> None:
        button.clicked.connect(lambda: handler())

