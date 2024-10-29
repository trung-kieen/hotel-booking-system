import datetime
from enum import Enum

from utils.logging import app_logger
from database.models.booking import Booking


class BookingStatus(Enum):
    Completed = 'Completed'
    Cancelled = 'Cancelled'
    InActive = 'InActive'
    InComing = 'InComing'
    Late = 'Late'
    Loading = 'Loading'

    def get_status(booking: Booking):
        status = BookingStatus.Loading
        if booking.is_canceled:
            status = BookingStatus.Cancelled
        elif booking.start_date.date() > datetime.date.today():
            status = BookingStatus.InComing
        elif booking.checkout is not None:
            status = BookingStatus.Completed
        elif booking.start_date.date() <= datetime.date.today() <= booking.end_date.date() and booking.checkout is None:
            status = BookingStatus.InActive
        elif datetime.date.today() > booking.end_date.date() and booking.checkout is None:
            status = BookingStatus.Late
        else:
            app_logger.error("Error Handle Status")
        return status
