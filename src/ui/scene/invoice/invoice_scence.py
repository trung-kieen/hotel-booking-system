"""
Author: Dang Xuan Lam
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QHeaderView, QMenu
from qt_material import apply_stylesheet

from database.models.invoice import Invoice
from designer.style import STYLE
from services.invoice_service import InvoiceService
from ui.scene.invoice.dialog.detail_dialog import InvoiceDetailDialog
from ui.scene.invoice.dialog.filter_dialog import InvoiceFilterDialog
from ui.scene.invoice.invoice_adapter import InvoiceAdapter
from ui.ui_invoice_scene import Ui_InvoiceScene


class InvoiceScene(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.adapter = InvoiceAdapter()
        self.ui = Ui_InvoiceScene()
        self.service = InvoiceService()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.containerQwidget)
        apply_stylesheet(self.ui, theme='light_blue.xml', extra={'font_size': '15px'})
        self.init_ui()
        self.init_state()

    def init_ui(self):
        self.ui.filter_btn.clicked.connect(self.filter)
        self.ui.refresh_btn.clicked.connect(self.init_state)
        self.setup_table_view()

    def setup_table_view(self):
        header = self.ui.invoice_data_table.horizontalHeader()
        header.setStyleSheet(
            "QHeaderView::section { border: none; border-bottom: 2px solid black;  background-color: #FFFFFF }"
        )
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.invoice_data_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.invoice_data_table.verticalHeader().hide()
        self.ui.invoice_data_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.invoice_data_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.invoice_data_table.setModel(self.adapter.model)
        self.ui.invoice_data_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.invoice_data_table.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, pos):
        model_index: QModelIndex = self.ui.invoice_data_table.indexAt(pos)

        if model_index.isValid():  # Kiểm tra nếu vị trí nhấp là hợp lệ
            menu = QMenu(self)  # Tạo một menu
            menu.setStyleSheet(STYLE.MENU.value)
            act_detail = menu.addAction("Detail")
            act_detail.triggered.connect(lambda: self.act_detail(model_index.row()))
            # action_edit.triggered.connect(lambda: self.edit_service(model_index.row()))
            menu.exec_(self.ui.invoice_data_table.mapToGlobal(pos))  # Hiển thị menu

    def init_state(self):
        i = self.service.get_all_invoices()
        self.adapter.set_items(i)

    def filter(self):
        i = InvoiceFilterDialog()
        i.exec_()
        if i.result() == QtWidgets.QDialog.Accepted:
            customer_phone, booking_status, pay_status, completed_date = i.get_filter_values()
            i = self.service.filter_invoice(customer_phone, booking_status, pay_status, completed_date)
            self.adapter.set_items(i)

    def act_detail(self, row_index):
        invoice = self.adapter.get_item(row_index)
        invoice_detail_dialog = InvoiceDetailDialog(invoice)
        invoice_detail_dialog.exec_()
