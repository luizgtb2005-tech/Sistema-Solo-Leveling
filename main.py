import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

def main():
    app = QApplication(sys.argv)

    ui_file = QFile("solo leveling design/main.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)

    ui_file.close()

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()