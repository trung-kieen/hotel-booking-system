from datetime import datetime

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog

from database.models.booking import BookingType
from services.booking_service import BookingService
from ui.scene.booking.dialog.ui.ui_booking import Ui_Booking_Dialog
from utils.room_information import get_room_location, get_base_information


class BookingDialog(QDialog):

    def __init__(self, room_id=None, parent=None):
        super().__init__(parent)
        self.booking = None
        self.current_user = None
        self.booking_service = BookingService()
        self.setWindowTitle("Booking Dialog")
        self.ui = Ui_Booking_Dialog()
        self.ui.setupUi(self)
        self.init_base_ui()
        if room_id is not None:
            self.init_ui_w_room_data(room_id)
        else:
            self.init_ui_w_out_room_data()

    def init_ui_w_out_room_data(self):
        self.ui.room_information_container.setVisible(False)
        beds = self.booking_service.get_all_type_bed()
        self.ui.type_room_cb.addItems(self.booking_service.get_all_type_room())
        self.ui.type_bed_cb.addItems([x.name for x in beds])
        self.ui.create_booking_btn.clicked.connect(self.create_booking)
        self.ui.filter_room_btn.clicked.connect(self.filter_room)
        self.ui.rooms_cb.currentTextChanged.connect(self.show_room_information)

    def init_base_ui(self):
        self.ui.message_personal_infor_lb.setVisible(False)

        self.ui.type_booking_cb.addItem(BookingType.DAILY.value)
        self.ui.type_booking_cb.addItem(BookingType.HOURLY.value)

        self.ui.start_date_picker.setMinimumDate(datetime.now())
        self.ui.end_date_picker.setMinimumDate(datetime.now())

        self.ui.num_adult_et.setValidator(QIntValidator(0, 10, self))
        self.ui.num_adult_et.textChanged.connect(
            lambda: self.ui.num_adult_et.setText('0') if self.ui.num_adult_et.text().strip() == "" else None)
        self.ui.num_child_et.setValidator(QIntValidator(0, 10, self))
        self.ui.num_child_et.textChanged.connect(
            lambda: self.ui.num_child_et.setText('0') if self.ui.num_child_et.text().strip() == "" else None)

        self.ui.cancel_btn.clicked.connect(lambda: self.close())
        self.ui.get_user_btn.clicked.connect(self.on_phone_et_change)

        self.ui.price_min_et.setValidator(QIntValidator(0, 1000000, self))
        self.ui.price_min_et.textChanged.connect(
            lambda: self.ui.price_min_et.setText('0') if self.ui.price_min_et.text().strip() == "" else None)

        self.ui.price_max_et.setValidator(QIntValidator(0, 1000000, self))
        self.ui.price_max_et.textChanged.connect(
            lambda: self.ui.price_max_et.setText("0") if self.ui.price_max_et.text().strip() == "" else None)

    def on_phone_et_change(self):
        cus = self.booking_service.get_infor_customer(self.ui.phone_et.text().strip())
        if cus is not None:
            self.current_user = cus
            self.ui.message_personal_infor_lb.setVisible(False)
            self.ui.address_lb.setText(cus.address)
            self.ui.name_lb.setText(cus.lastname + " " + cus.firstname)
            self.ui.id_lb.setText(str(cus.id))
        else:
            self.ui.message_personal_infor_lb.setVisible(True)
            self.ui.message_personal_infor_lb.setText("User Not Found")
            self.ui.address_lb.setText("")
            self.ui.name_lb.setText("")
            self.ui.id_lb.setText(str(""))

    def init_ui_w_room_data(self, room_id):
        self.ui.room_filter_container.setVisible(False)
        room = self.booking_service.get_room_by_id(room_id)
        if room is not None:
            self.ui.type_room_lb.setText(str(room.room_type))
            self.ui.price_lb.setText(str(round(room.price, 2)))
            self.ui.room_lb.setText(
                f"{get_room_location(room_id, room.floor_id)}")
            self.ui.type_bed_lb.setText(" ".join([x.name for x in room.bed_types]))
            self.ui.maxinum_people_lb.setText(str(sum([x.capacity for x in room.bed_types])))
        self.ui.create_booking_btn.clicked.connect(self.create_booking_w_room(room))

    def create_booking(self):
        if self.validate_base_data():
            self.booking = self.booking_service.create_booking(
                cus_id=self.current_user.id,
                type_booking=BookingType(self.ui.type_booking_cb.currentText()),
                start_date=self.ui.start_date_picker.date().toPyDate(),
                end_date=self.ui.end_date_picker.date().toPyDate(),
                num_adult=self.ui.num_adult_et.text(),
                num_child=self.ui.num_child_et.text(),
                room_id=self.ui.rooms_cb.currentData().id,
            )
            self.close()

    def create_booking_w_room(self, room):
        if int(self.ui.num_adult_et) + int(self.ui.num_child_et) <= sum([x.capacity for x in room.bed_types]):
            self.ui.message_stay_infor_lb.setVisible(True)
            self.ui.message_stay_infor_lb.setText("Number of guest must be greater than 0")
            return
        if self.validate_base_data() and self.booking_service.check_room_available(room.id,
                                                                                   self.ui.start_date_picker.date().toPyDate(),
                                                                                   self.ui.end_date_picker.date().toPyDate()):
            self.booking = self.booking_service.create_booking(
                cus_id=self.current_user.id,
                type_booking=BookingType(self.ui.type_booking_cb.currentText()),
                start_date=self.ui.start_date_picker.date().toPyDate(),
                end_date=self.ui.end_date_picker.date().toPyDate(),
                num_adult=self.ui.num_adult_et.text(),
                num_child=self.ui.num_child_et.text(),
                room_id=room.id,
            )
            self.close()

    def validate_base_data(self) -> bool:
        if self.ui.phone_et.text() == "":
            self.ui.message_personal_infor_lb.setVisible(True)
            self.ui.message_personal_infor_lb.setText("Please enter phone number")
            return False
        if not self.validate_sum(self.ui.num_adult_et.text(), self.ui.num_child_et.text()):
            self.ui.message_stay_infor_lb.setVisible(True)
            self.ui.message_stay_infor_lb.setText("Number of guest must be greater than 0")
            return False
        if self.ui.start_date_picker.date() > self.ui.end_date_picker.date():
            self.ui.message_stay_infor_lb.setVisible(True)
            self.ui.message_stay_infor_lb.setText("End date must be greater than start date")
            return False
        if int(self.ui.price_min_et.text()) > int(self.ui.price_max_et.text()):
            self.ui.message_stay_infor_lb.setVisible(True)
            self.ui.message_stay_infor_lb.setText("Price max must be greater than price min")
            return False
        return True

    def filter_room(self):
        type_bed = self.ui.type_bed_cb.currentText()
        type_room = self.ui.type_room_cb.currentText()
        price_min = int(self.ui.price_min_et.text())
        price_max = int(self.ui.price_max_et.text())
        num_of_customer = int(self.ui.num_adult_et.text()) + int(self.ui.num_child_et.text())
        start_date = self.ui.start_date_picker.date().toPyDate()
        end_date = self.ui.end_date_picker.date().toPyDate()
        rooms = self.booking_service.filter_room(type_bed, type_room, price_min, price_max, num_of_customer,
                                                 start_date, end_date)
        self.ui.rooms_cb.clear()
        for room in rooms:
            self.ui.rooms_cb.addItem(get_base_information(room), room)

    def show_room_information(self):
        room = self.ui.rooms_cb.currentData()
        self.ui.room_information_container.setVisible(True)
        self.ui.type_room_lb.setText(str(room.room_type))
        self.ui.price_lb.setText(str(round(room.price, 2)))
        self.ui.room_lb.setText(
            f"{get_room_location(room.id, room.floor_id)}")
        self.ui.type_bed_lb.setText(" ".join([x.name for x in room.bed_types]))
        self.ui.maxinum_people_lb.setText(str(sum([x.capacity for x in room.bed_types])))

    @staticmethod
    def validate_sum(a: str, b: str) -> bool:
        try:
            num_a = int(a) if a else 0
            num_b = int(b) if b else 0

            return (num_a + num_b) > 0

        except ValueError:
            return False
