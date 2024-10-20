from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtSql import QSqlQueryModel
from qt_material import apply_stylesheet
from database.repositories.base_repository import Repository
from utils.query import query_get_room_by_total_capacity
from database.repositories.floor_repository import FloorRepository
from database.table_model import adjust_size, fill_data
from services.room_service import ComboboxFilter, floor_members,  query_condition_translator, room_type_members
from ui.ui_room_scene import Ui_RoomScene


class RoomScene( QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RoomScene()
        self.ui.setupUi(self)


        self.floor_cmb_items = ComboboxFilter(floor_members() , self.ui.cmbFloor ,  field_name="floor_id" , all_view_value="All floor")
        self.room_type_cmb_items= ComboboxFilter(room_type_members() , self.ui.cmbRoomType,  field_name="room_type", all_view_value="All type")
        self.cmb_filter_list = [self.floor_cmb_items , self.room_type_cmb_items]

        self._initUi()
        self.model : QSqlQueryModel
        self.renderRoomTable()
        self._apply_event()


    def _getRoomType(self):
        # TODO
        pass


    def _initUi(self):
        def view_table_behavior():
            self.ui.tableView.setSelectionMode(QtWidgets.QTableView.SingleSelection)
            self.ui.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        def adjust_cmb (cmb):
            border_offset = 25
            cmb.setFixedWidth(cmb.minimumSizeHint().width() + border_offset )

        def apply_theme(widget):
            apply_stylesheet(widget, theme='light_blue.xml', css_file='custom.css', extra={'font-size': '15px'})

        self.setCentralWidget(self.ui.containerQwidget )

        view_table_behavior()

        apply_theme(self.ui.tableView)
        apply_theme(self.ui.cmbRoomType)
        apply_theme(self.ui.cmbFloor)

        adjust_cmb(self.ui.cmbFloor)
        adjust_cmb(self.ui.cmbRoomType)

    def _apply_event(self):
        self.ui.cmbFloor.currentIndexChanged.connect(lambda : self.renderRoomTable() )
        self.ui.cmbRoomType.currentIndexChanged.connect(lambda : self.renderRoomTable())
        c = self.ui.tableView
        self.ui.btnCreatBooking.clicked.connect(lambda: self._index_table())

    def _index_table(self):


        # column_headers = []
        def model_header_index(header_name):
            column_count = self.model.columnCount()
            for column in range(column_count):
                model = self.ui.tableView.model()
                header = self.model.headerData(column, Qt.Horizontal)
                if str(header).lower().strip() ==  header_name:
                    return column
            return -1
        def get_room_id():
            room_id_index  = model_header_index("room id")
            selected_item: QModelIndex =  self.ui.tableView.currentIndex()

            selected_row = selected_item.row()
            selected_column = room_id_index

            if selected_column == -1:
                return None

            room_id = self.model.data(self.model.index(selected_row, selected_column))
            return room_id

        print(get_room_id())

            # TODO load dialog


    ## TODO: Refactor to service layer


    def renderRoomTable(self):
        conditions = [ ]
        for cmb in self.cmb_filter_list:
            conditions.append(cmb.query_condition())
        conditions_string  = query_condition_translator(*conditions)
        # TODO: Pagination
        PAGE_LIMIT_RESULT = 1000


        stmt = query_get_room_by_total_capacity.format(conditions_string, PAGE_LIMIT_RESULT)
        self.model = fill_data(sql_statement=stmt, view=self.ui.tableView)
        adjust_size(self.ui.tableView)
