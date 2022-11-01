from UI.settings_widget import SettingWidget
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    widget = SettingWidget()
    widget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
