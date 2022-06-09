from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QStyle, QHBoxLayout, QSizePolicy


class ImageWidget(QWidget):

    def __init__(self, letter, buttons_dict, alphabet_str):
        super().__init__()
        # self.setAttribute(Qt.WA_DeleteOnClose)
        # self.setWindowFlags(Qt.FramelessWindowHint)

        self.title = letter
        self.buttons_dict = buttons_dict
        self.alphabet_str = alphabet_str

        self.setWindowTitle(self.title)

        layout = QHBoxLayout()

        # <a href="https://www.flaticon.com/free-icons/next" title="next icons">
        # Next icons created by Roundicons - Flaticon</a>
        left_arrow_button = QPushButton('', self)
        left_arrow_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        left_arrow_button.setIcon(QIcon('.resources/left-arrow.png'))
        left_arrow_button.setStyleSheet('background-color: white')
        left_arrow_button.setFocusPolicy(Qt.NoFocus)
        # noinspection PyUnresolvedReferences
        left_arrow_button.clicked.connect(self.on_left_arrow_button_click)

        right_arrow_button = QPushButton('', self)
        right_arrow_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_arrow_button.setIcon(QIcon('.resources/right-arrow.png'))
        right_arrow_button.setStyleSheet('background-color: white')
        right_arrow_button.setFocusPolicy(Qt.NoFocus)
        # noinspection PyUnresolvedReferences
        right_arrow_button.clicked.connect(self.on_right_arrow_button_click)

        app_size = QApplication.primaryScreen().availableSize()
        title_bar_height = QApplication.style().pixelMetric(QStyle.PM_TitleBarHeight)

        label = QLabel(self)
        pixmap = QPixmap('.resources/.images/{}.png'.format(self.title))
        pixmap = pixmap.scaledToHeight(app_size.height() - title_bar_height)
        label.setPixmap(pixmap)

        layout.addWidget(left_arrow_button)
        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(right_arrow_button)

        self.setLayout(layout)
        self.setFixedSize(app_size.width(), app_size.height() - title_bar_height)
        self.setWindowModality(Qt.ApplicationModal)
        self.setStyleSheet('background-color: white')

        self.showMaximized()

        left_arrow_button.setIconSize(QSize(left_arrow_button.width() / 2, left_arrow_button.width() / 2))
        right_arrow_button.setIconSize(QSize(right_arrow_button.width() / 2, right_arrow_button.width() / 2))

    def on_left_arrow_button_click(self):
        self.buttons_dict[self.alphabet_str[self.alphabet_str.index(self.title) - 1]].click()

    def on_right_arrow_button_click(self):
        idx = self.alphabet_str.index(self.title)
        self.buttons_dict[self.alphabet_str[idx + 1 if idx < len(self.alphabet_str) - 1 else 0]].click()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.on_left_arrow_button_click()
        elif event.key() == Qt.Key_Right:
            self.on_right_arrow_button_click()
