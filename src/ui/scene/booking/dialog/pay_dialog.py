from datetime import datetime

from PyQt5.QtWidgets import QDialog

from database.models.booking import Booking, BookingType
from database.models.customer import Customer
from database.models.invoice import PaymentStatus
from services.booking_service import BookingService
from ui.scene.booking.dialog.ui.ui_pay import Ui_Pay_Dialog
from utils.invoice_caculator import BookingPriceCalculator


class PayDialog(QDialog):
    def get_checkout_result(self):
        return self._booking

    def __init__(self, booking: Booking, parent=None):
        super(PayDialog, self).__init__(parent)
        self._booking = None
        self.ui = Ui_Pay_Dialog()
        self.ui.setupUi(self)
        from components.app import App
        self.resize(int(App.maxWidth * 3 / 4), int(App.maxHeight * 3 / 4))
        self.init_base_ui()
        self.init_personal_info(booking.customer)
        self.init_stay_info(booking)
        self.init_service_info()
        self.init_bill_info(booking)

    def init_base_ui(self):
        self.ui.checkout_btn.setEnabled(False)
        self.ui.checkout_btn.setStyleSheet(" color: gray")
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.confirm_pay_cb.stateChanged.connect(
            lambda: self.update_checkout_button())

    def update_checkout_button(self):
        if self.ui.confirm_pay_cb.isChecked():
            self.ui.checkout_btn.setEnabled(True)
            self.ui.checkout_btn.setStyleSheet(" color: white")
        else:
            self.ui.checkout_btn.setEnabled(False)
            self.ui.checkout_btn.setStyleSheet(" color: gray")

    def init_personal_info(self, customer: Customer):
        self.ui.phone_customer_lb.setText(customer.phone)
        self.ui.name_lb.setText(customer.lastname + " " + customer.firstname)
        self.ui.address_lb.setText(customer.address)
        self.ui.id_lb.setText(customer.uuid)

    def init_stay_info(self, booking: Booking):
        self.ui.type_booking_lb.setText(booking.booking_type.value)
        self.ui.room_id_lb.setText(f"#{booking.room_id} Floor {booking.room.floor_id}")
        self.ui.checkin_lb.setText(str(booking.checkin))
        self.ui.checkout_lb.setText(str(booking.checkout))
        self.ui.num_of_guest_lb.setText(str(booking.num_adults + booking.num_children))
        self.ui.room_type_lb.setText(booking.room.room_type.value)

    def init_service_info(self):
        pass

    def init_bill_info(self, booking: Booking):
        if booking.booking_type == BookingType.Daily:
            self.ui.room_price_lb.setText(f"{round(booking.room.price, 2)} / per night")

            def calculate_nights_stayed(checkin_date, checkout_date):
                nights_stayed = (checkout_date.date() - checkin_date.date()).days
                if nights_stayed > 0:
                    return nights_stayed - 1
                return 1

            nights = calculate_nights_stayed(booking.checkin, booking.checkout)
            self.ui.duration_lb.setText(f"{nights} nights")

            _, extra_charges = BookingPriceCalculator.calculate_extra_charges(booking.checkin, booking.checkout,
                                                                              booking.room.price)

            room_price = booking.room.price * nights
            total_room_price = room_price + extra_charges

            service = 0

            self.ui.service_total_price_lb.setText(str(round(service, 2)))
            self.ui.room_total_price_lb.setText(str(round(total_room_price, 2)))
            total_price = total_room_price + service
            self.ui.total_price_lb.setText(str(round(total_price, 2)))
            self.ui.prepaid_lb.setText(str(round(booking.invoice.prepaid, 2)))

            booking.invoice.total_price = total_price - booking.invoice.prepaid

        else:
            self.ui.room_price_lb.setText(f"{round(booking.room.price * 0.05 / 24, 2)} / per hour")

            def calculate_hours_stayed(checkin_date, checkout_date):
                hours_stayed = (checkout_date - checkin_date).total_seconds() / 3600  # Chuyển đổi giây sang giờ
                return max(1, hours_stayed)

            hours = calculate_hours_stayed(booking.checkin, booking.checkout)
            self.ui.duration_lb.setText(f"{round(hours, 2)} hours")

            # Tính giá phòng dựa trên giờ đã ở
            room_price = booking.room.price * 0.05 / 24 * hours
            service = 0
            self.ui.room_total_price_lb.setText(str(round(room_price, 2)))
            self.ui.service_total_price_lb.setText(str(round(service, 2)))

            total_price = room_price + service
            self.ui.total_price_lb.setText(str(round(total_price, 2)))
            self.ui.prepaid_lb.setText(str(round(booking.invoice.prepaid, 2)))

            booking.invoice.total_price = total_price - booking.invoice.prepaid
        self.ui.checkout_btn.clicked.connect(lambda: self.pay(booking))

    def pay(self, booking: Booking):
        self._booking = booking
        booking.invoice.status = PaymentStatus.Done
        BookingService().update_invoice(booking.invoice)
