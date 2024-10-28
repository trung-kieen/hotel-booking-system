"""
Author: Nguyen Khac Trung Kien
"""
from utils.logging import app_logger
from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtSql import QSqlQueryModel
from qt_material import apply_stylesheet
from components.messagebox.popup import CriticalPopup, ErrorPopup
from database.repositories.base_repository import Repository
from designer.style import adjust_cmb, apply_theme, adjust_view_table, set_style_button
from ui.scene.room.room_dialog import RoomDialog
from utils.decorator import handle_exception
from utils.query import query_get_room_by_total_capacity
from database.repositories.floor_repository import FloorRepository
from database.table_model import adjust_size, fill_data
from services.room_service import ComboboxFilterAdapter, RoomService, floor_members, lock_members,  query_condition_translator, room_type_members
from ui.ui_room_scene import Ui_RoomScene


class RoomScene( QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RoomScene()
        self.ui.setupUi(self)
        self.room_service = RoomService()


        # TODO: create class to manager filter cmb
        self.floor_cmb_filter = ComboboxFilterAdapter(floor_members() , self.ui.cmbFloor ,  field_name="floor_id" , all_view_value="All floor")
        self.room_type_cmb_filter= ComboboxFilterAdapter(room_type_members() , self.ui.cmbRoomType,  field_name="room_type", all_view_value="All type")
        self.lock_status_cmb_filter= ComboboxFilterAdapter(lock_members() , self.ui.cmbLockStatus,  field_name="is_locked")
        self.cmb_filter_list = [self.floor_cmb_filter , self.room_type_cmb_filter, self.lock_status_cmb_filter]

        self._init_ui()

        self.model : QSqlQueryModel
        self.refresh_room_table()
        self._register_event()






    def _init_ui(self):
        apply_stylesheet(self, theme='light_blue.xml', extra={'font_size': '15px'})
        self.setStyleSheet("background-color: #FFFFFF")
        self.setCentralWidget(self.ui.containerQwidget )

        apply_theme(self.ui.tableView)
        apply_theme(self.ui.cmbRoomType)
        apply_theme(self.ui.cmbFloor)
        apply_theme(self.ui.cmbLockStatus)
        adjust_cmb(self.ui.cmbFloor)
        adjust_cmb(self.ui.cmbRoomType)
        adjust_cmb(self.ui.cmbLockStatus)

        set_style_button(self.ui.btnAddRoom)
        set_style_button(self.ui.btnEditRoom)
        set_style_button(self.ui.btnDeleteRoom)

        adjust_view_table(self.ui.tableView)

    def _register_event(self):
        self.ui.cmbFloor.currentIndexChanged.connect(lambda : self.refresh_room_table() )
        self.ui.cmbRoomType.currentIndexChanged.connect(lambda : self.refresh_room_table())
        self.ui.cmbLockStatus.currentIndexChanged.connect(lambda : self.refresh_room_table())
        self.ui.btnEditRoom.clicked.connect(lambda: self._open_edit_room_dialog())
        self.ui.btnAddRoom.clicked.connect(lambda: self._open_add_room_dialog())
        self.ui.btnDeleteRoom.clicked.connect(lambda: self._delete_current_room())



    def _open_add_room_dialog(self):
        dialog = RoomDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.refresh_room_table()
    @handle_exception
    def _delete_current_room(self):
        # TODO: Use business error message
        target_room_id   = self._selected_room_id()
        if self.room_service.exist_booking_with_room(target_room_id):
            CriticalPopup(title="Action not permited", message="Delete this room will losing other important data")
            return

        if not target_room_id: return
        reply = QtWidgets.QMessageBox.question(self, 'Confirm Delete',
                                                f"Are you sure you want to delete room ID {target_room_id}?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply:
            self.room_service.delete_room_by_id(target_room_id)
            self.refresh_room_table()






    def _open_edit_room_dialog(self):
        room_id = self._selected_room_id()
        if not self._selected_room_id():
            # TODO: use msg box or diable button
            app_logger.info("Please select room to edit")
        # Open to edit current room
        dialog = RoomDialog(room_id)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.refresh_room_table()

    def _selected_room_id (self):
        def model_header_index(header_name):
            """
            Return index of header match header_name
            Example:
            Input: "room id"
            Output: 1
            Return -1 if notfound
            """
            column_count = self.model.columnCount()
            for column in range(column_count):
                model = self.ui.tableView.model()
                header = self.model.headerData(column, Qt.Horizontal)
                if str(header).lower().strip() ==  header_name:
                    return column
            return -1
        def room_id_current_row():
            """
            Return room id of current selected row in QTableView
            """
            room_id_index  = model_header_index("room id")
            selected_item: QModelIndex =  self.ui.tableView.currentIndex()

            selected_row = selected_item.row()
            selected_column = room_id_index

            if selected_column == -1:
                return None

            room_id = self.model.data(self.model.index(selected_row, selected_column))
            return room_id

        return room_id_current_row()




    @handle_exception
    def refresh_room_table(self):
        # Boilerplate code to remain table cusor position
        current_index = self.ui.tableView.currentIndex()
        current_row : int = -1
        if current_index:
            current_row = current_index.row()




        conditions = [ ]
        for cmb in self.cmb_filter_list:
            conditions.append(cmb.query_condition())
        conditions_string  = query_condition_translator(*conditions)
        # TODO: Pagination
        PAGE_LIMIT_RESULT = 1000

        stmt = query_get_room_by_total_capacity.format(conditions_string, PAGE_LIMIT_RESULT)
        self.model = fill_data(sql_statement=stmt, view=self.ui.tableView)
        adjust_size(self.ui.tableView)



        # Revert previous selected row
        try:
            self.ui.tableView.selectRow(current_row)
        except:
            pass
