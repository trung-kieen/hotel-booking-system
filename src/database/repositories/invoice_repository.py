import datetime

from sqlalchemy import func
from database.models.booking import Booking
from database.models.customer import Customer
from database.models.invoice import Invoice, PaymentStatus
from database.repositories.base_repository import Repository
from ui.scene.booking.constant.booking_status import BookingStatus


class InvoiceRepository[T](Repository[T]):

    def filter(self, customer_phone=None, status=None, pay_status=None, completed_date=None):
        query = self.session.query(Invoice).join(Invoice.booking).join(Booking.customer)

        if customer_phone:
            query = query.filter(Customer.phone == customer_phone)

        filters = self.filter_by_booking_status(status)
        if filters:
            query = query.filter(*filters)

        if pay_status and pay_status != "All":
            if pay_status == PaymentStatus.Done.value:
                query = query.filter(Invoice.status == PaymentStatus.Done.value)
            elif pay_status == PaymentStatus.Pending.value:
                query = query.filter(Invoice.status == PaymentStatus.Pending.value)

        if completed_date:
            query = query.filter(func.date(Invoice.completed_at) == completed_date)

        filtered_invoices = query.all()
        return filtered_invoices

    def filter_by_booking_status(self, status):
        filters = []

        if status:
            current_date = datetime.date.today()

            if status == BookingStatus.Completed.value:
                # Booking has been checked out
                filters.append(Booking.checkout.isnot(None))

            elif status == BookingStatus.Cancelled.value:
                # Booking is canceled
                filters.append(Booking.is_canceled.is_(True))

            elif status == BookingStatus.InActive.value:
                # Booking is ongoing (start_date <= today, end_date >= today, not checked out)
                filters.append(Booking.start_date <= current_date)
                filters.append(Booking.end_date >= current_date)
                filters.append(Booking.checkout.is_(None))
                filters.append(Booking.is_canceled.is_(False))  # Ensure it's not canceled

            elif status == BookingStatus.InComing.value:
                # Booking is upcoming (start_date > today, not canceled)
                filters.append(Booking.start_date > current_date)
                filters.append(Booking.is_canceled.is_(False))

            elif status == BookingStatus.Late.value:
                # Booking is late (end_date < today, not checked out, not canceled)
                filters.append(Booking.end_date < current_date)
                filters.append(Booking.checkout.is_(None))
                filters.append(Booking.is_canceled.is_(False))

        return filters

        # Apply all filters to the query
        return filters
