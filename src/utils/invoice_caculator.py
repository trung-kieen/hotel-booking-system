from datetime import datetime, timedelta, time
from decimal import Decimal

from database.models.booking import Booking
from database.models.invoice import Invoice


class BookingPriceCalculator:
    @staticmethod
    def calculate_extra_charges(checkin_datetime, checkout_datetime, room_price):
        # Calculate total nights stayed
        total_nights = (checkout_datetime.date() - checkin_datetime.date()).days
        extra_charge = 0

        # Early check-in conditions
        early_checkin_time = checkin_datetime.time()
        if time(5, 0) <= early_checkin_time <= time(9, 0):
            extra_charge += Decimal('0.5') * room_price  # 50% room price for early check-in
        elif time(9, 0) < early_checkin_time <= time(14, 0):
            extra_charge += Decimal('0.3') * room_price  # 30% room price for early check-in

        # Late checkout conditions
        late_checkout_time = checkout_datetime.time()
        if time(12, 0) <= late_checkout_time <= time(15, 0):
            extra_charge += Decimal('0.3') * room_price  # 30% room price for late check-out
        elif time(15, 0) < late_checkout_time <= time(18, 0):
            extra_charge += Decimal('0.5') * room_price  # 50% room price for late check-out
        elif late_checkout_time > time(18, 0):
            extra_charge += room_price  # 100% room price for late check-out

        return total_nights, extra_charge


class InvoiceFactory:
    @staticmethod
    def generate_invoice(booking: Booking) -> Invoice:
        calculator = BookingPriceCalculator()
        _, total_price = calculator.calculate_extra_charges(booking.checkin, booking.checkout, booking.room.price)

        # Create and return the invoice
        invoice = Invoice(
            total_price=total_price,
            quantity=1,  # Assuming 1 room per booking for simplicity
            booking_id=booking.id
        )
        return invoice
