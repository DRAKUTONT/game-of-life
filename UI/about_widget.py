from PyQt5.QtWidgets import QWidget
from UI.about_ui import UiForm


class AboutGame(QWidget, UiForm):
    def __init__(self, back_widget):
        super().__init__()
        self.back_widget = back_widget
        self.initUI()

    def initUI(self) -> None:
        self.setupUi(self)
        self.connect_button(self.back_btn, self.return_to_previous_window)

    def return_to_previous_window(self) -> None:
        """Возвращение к предыдущему окну"""
        self.close()
        self.back_widget.show()

    @staticmethod
    def connect_button(button, handler):
        button.clicked.connect(lambda: handler())

