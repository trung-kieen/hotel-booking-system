"""
Author: Dang Xuan Lam
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QHeaderView, QMenu
from qt_material import apply_stylesheet

from database.models.service import Service
from designer.style import STYLE
from services.service_service import ServiceService
from ui.scene.service.dialog.create_service_dialog import CreateServiceDialog
from ui.scene.service.dialog.edit_dialog import EditServiceDialog
from ui.scene.service.service_adapter import ServiceAdapter
from ui.ui_service_scene import Ui_SerivceScene


class ServiceScene(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.service = ServiceService()
        self.adapter = ServiceAdapter()
        self.ui = Ui_SerivceScene()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.containerQwidget)
        apply_stylesheet(self.ui, theme='light_blue.xml', extra={'font_size': '15px'})
        self.init_ui()
        self.setup_table_view()
        self.init_state()

    def init_ui(self):
        self.ui.create_new_service_btn.clicked.connect(self.add_service)
        self.ui.search_btn.clicked.connect(self.search)
        self.ui.refresh_btn.clicked.connect(self.init_state)

    def init_state(self):
        self.adapter.set_items(list(self.service.get_services()))

    def setup_table_view(self):
        header = self.ui.service_data_table.horizontalHeader()
        header.setStyleSheet(
            "QHeaderView::section { border: none; border-bottom: 2px solid black;  background-color: #FFFFFF }"
        )
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.service_data_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.service_data_table.verticalHeader().hide()
        self.ui.service_data_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.service_data_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.service_data_table.setModel(self.adapter.model)
        self.ui.service_data_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.service_data_table.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, pos):
        model_index: QModelIndex = self.ui.service_data_table.indexAt(pos)

        if model_index.isValid():  # Kiểm tra nếu vị trí nhấp là hợp lệ
            menu = QMenu(self)  # Tạo một menu
            menu.setStyleSheet(STYLE.MENU.value)
            action_edit = menu.addAction("Edit")
            # action_delete = menu.addAction("Delete")
            action_edit.triggered.connect(lambda: self.edit_service(model_index.row()))
            menu.exec_(self.ui.service_data_table.mapToGlobal(pos))  # Hiển thị menu

    def search(self):
        keyword = self.ui.search_ld.text()
        self.adapter.set_items(self.service.search_services(keyword))

    def add_service(self):
        s = CreateServiceDialog(self)
        s.exec_()
        if s.result() == s.Accepted:
            self.init_state()

    def edit_service(self, row):
        service = self.adapter.get_item(row)
        s = EditServiceDialog(self.adapter.get_item(row))
        s.exec_()
        if s.result() == s.Accepted:
            service.name = s.name_input.text()
            service.price = float(s.price_input.text())
            self.service.update_service(service)
            self.init_state()
