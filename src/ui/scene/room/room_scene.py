from PyQt5 import QtWidgets
from qt_material import apply_stylesheet
from database.models.floor import Floor
from database.repositories.base_repository import Repository
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
        self.renderRoomTable()
        self._initUi()
        floor = Repository[Floor]().get_all()


    def _getRoomType(self):
        # TODO
        pass


    def _initUi(self):

        def adjust_cmb (cmb):
            border_offset = 25
            cmb.setFixedWidth(cmb.minimumSizeHint().width() + border_offset )

        def apply_theme(widget):
            apply_stylesheet(widget, theme='light_blue.xml', css_file='custom.css', extra={'font-size': '15px'})

        self.setCentralWidget(self.ui.containerQwidget )

        self.ui.cmbFloor.currentIndexChanged.connect(lambda : self.renderRoomTable() )
        self.ui.cmbRoomType.currentIndexChanged.connect(lambda : self.renderRoomTable())

        apply_theme(self.ui.tableView)
        apply_theme(self.ui.cmbRoomType)
        apply_theme(self.ui.cmbFloor)

        adjust_cmb(self.ui.cmbFloor)
        adjust_cmb(self.ui.cmbRoomType)







    ## TODO: Refactor to service layer


    def renderRoomTable(self):
        cmb_filter_list = [self.floor_cmb_items , self.room_type_cmb_items]
        conditions = [ ]
        for cmb in cmb_filter_list:
            conditions.append(cmb.query_condition())

        conditions_string  = query_condition_translator(*conditions)
        # TODO: Pagination
        PAGE_LIMIT_RESULT = 1000

        query_get_room_by_total_capacity  = """
SELECT
  room_id AS 'room id',
  SUM(capacity) as capacity,
  floor_id as 'floor id',
  is_locked as 'is locked',
  price as 'PRICE',
  room_type as 'room type'
FROM
  (
    SELECT
      A.id as room_id,
      room_type,
      floor_id,
      is_locked,
      price,
      bed_type_id,
      name,
      (T.capacity * bed_amount) as capacity
    FROM
      (SELECT * FROM  rooms WHERE {0} LIMIT {1} )  AS A
      INNER JOIN bed_rooms AS B
      INNER JOIN bed_types AS T
    WHERE
      A.id = B.room_id
      AND T.id = B.bed_type_id
  )
GROUP BY
  room_id
        """

        stmt = query_get_room_by_total_capacity.format(conditions_string, PAGE_LIMIT_RESULT)
        # fill_data(sql_statement="SELECT  id || floor_id as 'Room' , room_type as 'Room Type', price   FROM rooms LIMIT 10", view=self.ui.tableView)
        fill_data(sql_statement=stmt, view=self.ui.tableView)
        adjust_size(self.ui.tableView)
        # layout = QtWidgets.QVBoxLayout(self)
        # label = QtWidgets.QLabel("Room Scene")
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # layout.addWidget(label)
