import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QSizePolicy

from ImageWidget import ImageWidget
from QIconButton import QIconButton


class MainApplication(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Алфавит'

        self.alphabet_str = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.eng_str = "`qwertyuiop[]asdfghjkl;'zxcvbnm,."
        self.rus_str = "ёйцукенгшщзхъфывапролджэячсмитьбю"
        self.translation = str.maketrans(dict(zip(self.eng_str, self.rus_str)))
        self.buttons_dict = {}
        self._ = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)

        grid = QGridLayout()
        self.setLayout(grid)

        positions = [(i, j) for i in range(3) for j in range(11)]

        for position, letter in zip(positions, self.alphabet_str):
            button = QIconButton('', self)
            self.buttons_dict[letter] = button

            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # noinspection PyUnresolvedReferences
            button.clicked.connect(lambda state, x=letter: self.on_click(x))

            button.setIcon(QIcon('.resources/.letters/{}.png'.format(letter)))
            button.setStyleSheet('background-color: white')
            button.setFocusPolicy(Qt.NoFocus)

            grid.addWidget(button, *position)

        self.showMaximized()

    def on_click(self, letter):
        self._ = ImageWidget(letter, self.buttons_dict, self.alphabet_str)

    def keyPressEvent(self, event):
        # language independent
        if event.text() != '':
            if event.text() in self.rus_str:
                self.buttons_dict[event.text().upper()].click()
            elif event.text() in self.eng_str:
                self.buttons_dict[event.text().translate(self.translation).upper()].click()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    MainApplication()
    sys.exit(app.exec_())
