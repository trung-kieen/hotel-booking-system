"""
Author: Dang Xuan Lam
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import ui.main.resource.resource_rc


class Ui_MainWindow(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(2700, 1550)
        window.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        window.setFont(font)
        window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")

        self.sidebar = QtWidgets.QWidget(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(50, 110, 351, 1391))
        self.sidebar.setStyleSheet("background-color: rgb(248, 250, 252);\n"
                                   "border-radius: 25px;")
        self.sidebar.setObjectName("sidebar")

        self.home_btn = self._create_button("Home", ":/images/home-icon.png", 0, 40)
        self.guest_btn = self._create_button("Guest", ":/images/guest-icon.png", 0, 170)
        self.reservation_btn = self._create_button("Reservation", ":/images/daily-schedule-icon.png", 0, 300)
        self.room_btn = self._create_button("Room", ":/images/house-icon.png", 0, 430)
        self.service_btn = self._create_button("Service", ":/images/services-icon.png", 0, 560)
        self.setting_btn = self._create_button("Setting", ":/images/setting-icon.png", 0, 690)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 10, 2571, 111))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.hotel_logo = QtWidgets.QLabel(self.widget)
        self.hotel_logo.setGeometry(QtCore.QRect(0, 0, 251, 111))
        self.hotel_logo.setPixmap(QtGui.QPixmap(":/images/hotel-logo.png"))
        self.hotel_logo.setScaledContents(True)
        self.hotel_logo.setObjectName("hotel_logo")

        self.scene = QtWidgets.QStackedWidget(self.centralwidget)
        self.scene.setGeometry(QtCore.QRect(440, 110, 2221, 1391))
        self.scene.setStyleSheet("background-color: rgb(248, 250, 252);\n"
                                            " border-radius: 25px;")
        self.scene.setObjectName("scence_container")

        window.setCentralWidget(self.centralwidget)
        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

        self._listener()

    def _create_button(self, label, icon_path, x, y):
        button = QtWidgets.QPushButton(self.sidebar)
        button.setGeometry(QtCore.QRect(x, y, 321, 81))
        button.setObjectName(f"{label.lower()}_btn")
        icon = QtWidgets.QLabel(button)
        icon.setGeometry(QtCore.QRect(60, 20, 41, 41))
        icon.setPixmap(QtGui.QPixmap(icon_path))
        icon.setScaledContents(True)
        icon.setObjectName(f"{label.lower()}_icon")
        label_widget = QtWidgets.QLabel(button)
        label_widget.setGeometry(QtCore.QRect(130, 0, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        label_widget.setFont(font)
        label_widget.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        label_widget.setText(label)
        label_widget.setObjectName(f"{label.lower()}_lb")
        return button

    def add_scene(self, scenes):
        for scene in scenes:
            self.scene.addWidget(scene)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Hotel Management"))

    def _listener(self):
        curr_btn = None  # Variable to track the currently active button

        def reset_button(button):
            button.setStyleSheet("")  # Reset the button to its default style

        def set_button_style(button):
            nonlocal curr_btn  # Allow access to the curr_btn variable
            if curr_btn:  # Check if there's a currently active button
                reset_button(curr_btn)  # Reset the current button
            button.setStyleSheet("background-color: rgb(100, 200, 255);")  # Set the clicked button's style
            curr_btn = button  # Update the current button

        def change_scene(scene_index):
            self.scene.setCurrentIndex(scene_index)

        def home_clicked():
            set_button_style(self.home_btn)
            change_scene(0)  # Change to home scene
            print("home button clicked!")

        def guest_clicked():
            set_button_style(self.guest_btn)
            change_scene(1)  # Change to Guest scene
            print("Guest button clicked!")

        def reservation_clicked():
            set_button_style(self.reservation_btn)
            change_scene(2)  # Change to Reservation scene
            print("Reservation button clicked!")

        def room_clicked():
            set_button_style(self.room_btn)
            change_scene(3)  # Change to Room scene
            print("Room button clicked!")

        def service_clicked():
            set_button_style(self.service_btn)
            change_scene(4)  # Change to Service scene
            print("Service button clicked!")

        def setting_clicked():
            set_button_style(self.setting_btn)
            change_scene(5)  # Change to Setting scene
            print("Setting button clicked!")

        self.home_btn.clicked.connect(home_clicked)
        self.guest_btn.clicked.connect(guest_clicked)
        self.reservation_btn.clicked.connect(reservation_clicked)
        self.room_btn.clicked.connect(room_clicked)
        self.service_btn.clicked.connect(service_clicked)
        self.setting_btn.clicked.connect(setting_clicked)
