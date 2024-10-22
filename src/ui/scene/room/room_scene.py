from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtSql import QSqlQueryModel
from qt_material import apply_stylesheet
from database.repositories.base_repository import Repository
from designer.style import adjust_cmb, apply_theme, adjust_view_table, set_style_button
from ui.scene.room.room_dialog import RoomDialog
from utils.query import query_get_room_by_total_capacity
from database.repositories.floor_repository import FloorRepository
from database.table_model import adjust_size, fill_data
from services.room_service import ComboboxFilterAdapter, floor_members,  query_condition_translator, room_type_members
from ui.ui_room_scene import Ui_RoomScene


class RoomScene( QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RoomScene()
        self.ui.setupUi(self)


        self.floor_cmb_filter = ComboboxFilterAdapter(floor_members() , self.ui.cmbFloor ,  field_name="floor_id" , all_view_value="All floor")
        self.room_type_cmb_filter= ComboboxFilterAdapter(room_type_members() , self.ui.cmbRoomType,  field_name="room_type", all_view_value="All type")
        self.cmb_filter_list = [self.floor_cmb_filter , self.room_type_cmb_filter]

        self._initUi()
        self.model : QSqlQueryModel
        self.refreshRoomTable()
        self._register_event()





    def _initUi(self):
        self.setCentralWidget(self.ui.containerQwidget )


        apply_theme(self.ui.tableView)
        apply_theme(self.ui.cmbRoomType)
        apply_theme(self.ui.cmbFloor)
        adjust_view_table(self.ui.tableView)
        adjust_cmb(self.ui.cmbFloor)
        adjust_cmb(self.ui.cmbRoomType)
        set_style_button(self.ui.btnAddRoom)

    def _register_event(self):
        self.ui.cmbFloor.currentIndexChanged.connect(lambda : self.refreshRoomTable() )
        self.ui.cmbRoomType.currentIndexChanged.connect(lambda : self.refreshRoomTable())
        self.ui.btnEditRoom.clicked.connect(lambda: self._openEditRoomDialog())
        self.ui.btnAddRoom.clicked.connect(lambda: self._openAddRoomDialog())



    def _openAddRoomDialog(self):
        dialog = RoomDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.refreshRoomTable()
            # Dialog was accepted, you can refresh your customer list or perform other actions
            print("Customer added successfully.")
        else:
            print("Customer is not added!")



        pass
    def _openEditRoomDialog(self):
        room_id = self._selected_room_id()
        if not self._selected_room_id():
            # TODO: use msg box or diable button
            print("Please select room to edit")
        # Open to edit current room
        dialog = RoomDialog(room_id)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.refreshRoomTable()
            # Dialog was accepted, you can refresh your customer list or perform other actions
            print("Customer edited successfully.")
        else:
            print("Customer is not edited!")

    def _selected_room_id (self):
        # column_headers = []
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





    ## TODO: Refactor to service layer


    def refreshRoomTable(self):
        conditions = [ ]
        for cmb in self.cmb_filter_list:
            conditions.append(cmb.query_condition())
        conditions_string  = query_condition_translator(*conditions)
        # TODO: Pagination
        PAGE_LIMIT_RESULT = 1000


        stmt = query_get_room_by_total_capacity.format(conditions_string, PAGE_LIMIT_RESULT)
        self.model = fill_data(sql_statement=stmt, view=self.ui.tableView)
        adjust_size(self.ui.tableView)
