from datetime import datetime, timedelta
from decimal import Decimal

from database.models.booking import Booking
from database.models.invoice import Invoice


class BookingPriceCalculator:
    @staticmethod
    def calculate_total_price(booking: Booking) -> Decimal:
        """
        Calculate the total price of a booking based on check-in and check-out times, 
        and the room's price. Adjusts for early check-out if applicable.
        """
        if not booking.checkin or not booking.checkout:
            raise ValueError("Check-in and check-out times must be set")

        room_price = booking.room.price
        total_price = Decimal(0)

        # Determine the actual checkout date (could be earlier than end_date)
        actual_checkout = min(booking.checkout, booking.end_date)

        # Calculate the duration of stay in days
        stay_duration = actual_checkout - booking.checkin
        full_days = stay_duration.days
        remaining_hours = stay_duration.seconds / 3600

        # Full day price for each full day of stay
        total_price += Decimal(full_days) * room_price

        # Handle partial day charges based on remaining hours
        if remaining_hours > 0:
            if remaining_hours <= 6:  # Early check-out or short stay
                total_price += room_price * Decimal(0.5)
            else:  # Any checkout past 6 hours considered full day
                total_price += room_price

        return total_price


class InvoiceFactory:
    @staticmethod
    def generate_invoice(booking: Booking) -> Invoice:
        calculator = BookingPriceCalculator()
        total_price = calculator.calculate_total_price(booking)

        # Create and return the invoice
        invoice = Invoice(
            total_price=total_price,
            quantity=1,  # Assuming 1 room per booking for simplicity
            booking_id=booking.id
        )
        return invoice
