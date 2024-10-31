from database.models.booking import Booking, BookingType
from utils.invoice_caculator import BookingPriceCalculator


class BillCalculator:
    @staticmethod
    def calculate_nights_stayed(checkin_date, checkout_date):
        nights_stayed = (checkout_date.date() - checkin_date.date()).days
        return max(1, nights_stayed - 1)

    @staticmethod
    def calculate_hours_stayed(checkin_date, checkout_date):
        hours_stayed = (checkout_date - checkin_date).total_seconds() / 3600
        return max(1, hours_stayed)

    @staticmethod
    def calculate_service_total(services):
        return round(sum(ser.price for ser in services), 2)

    @staticmethod
    def calculate_room_total(booking, duration):
        if booking.booking_type == BookingType.Daily:
            return booking.room.price * duration
        return booking.room.price * 0.05 / 24 * duration

    @staticmethod
    def calculate_total_price(room_price, service_price, extra_charges=0):
        return room_price + service_price + extra_charges

    @staticmethod
    def calculate_bill_details(booking: Booking):
        if booking.booking_type == BookingType.Daily:
            nights = BillCalculator.calculate_nights_stayed(booking.checkin, booking.checkout)
            extra_charges = BookingPriceCalculator.calculate_extra_charges(booking.checkin, booking.checkout,
                                                                           booking.room.price)[1]
            room_total = BillCalculator.calculate_room_total(booking, nights)
            service_total = BillCalculator.calculate_service_total(booking.services)
            total_price = BillCalculator.calculate_total_price(room_total, service_total, extra_charges)
            duration_text = f"{nights} nights"

        else:  # Hourly booking
            hours = BillCalculator.calculate_hours_stayed(booking.checkin, booking.checkout)
            room_total = BillCalculator.calculate_room_total(booking, hours)
            service_total = BillCalculator.calculate_service_total(booking.services)
            total_price = BillCalculator.calculate_total_price(room_total, service_total)
            duration_text = f"{round(hours, 2)} hours"
        prepaid = round(booking.invoice.prepaid, 2) if booking.invoice else 0
        return {
            'room_price_lb': f"{round(booking.room.price, 2)}",  # Label for room price
            'duration_lb': duration_text,  # Label for duration
            'service_total_price_lb': f"{round(service_total, 2)}",  # Label for service total
            'room_total_price_lb': f"{round(room_total, 2)}",  # Label for room total
            'total_price_lb': f"{round(total_price, 2)}",  # Label for total price
            'prepaid_lb': f"{prepaid}",  # Label for prepaid amount
            'remaining_total_lb': f"{round(total_price - prepaid, 2)}"  # Label for remaining amount
        }

    @staticmethod
    def calculate_pre_checkout_bill_details(booking: Booking):
        # Calculate pre-checkout details based on start_date and end_date
        if booking.booking_type == BookingType.Daily:
            nights = (booking.end_date.date() - booking.start_date.date()).days
            room_total = BillCalculator.calculate_room_total(booking, nights)
            service_total = BillCalculator.calculate_service_total(booking.services)
            total_price = BillCalculator.calculate_total_price(room_total, service_total)

            duration_text = f"{nights} nights"
        else:  # Hourly booking
            # Assuming hours are based on the total period from start_date to end_date
            hours = (booking.end_date - booking.start_date).total_seconds() / 3600
            room_total = BillCalculator.calculate_room_total(booking, hours)
            service_total = BillCalculator.calculate_service_total(booking.services)
            total_price = BillCalculator.calculate_total_price(room_total, service_total)

            duration_text = f"{round(hours, 2)} hours"
        prepaid = round(booking.invoice.prepaid, 2) if booking.invoice else 0

        return {
            'room_price_lb': f"{round(booking.room.price, 2)}",  # Label for room price
            'duration_lb': duration_text,  # Label for duration
            'service_total_price_lb': f"{round(service_total, 2)}",  # Label for service total
            'room_total_price_lb': f"{round(room_total, 2)}",  # Label for room total
            'total_price_lb': f"{round(total_price, 2)}",  # Label for total price
            'prepaid_lb': f"{prepaid}",  # Label for prepaid amount
            'remaining_total_lb': f"{round(total_price - prepaid, 2)}"  # Label for remaining amount
        }
