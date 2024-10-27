from typing import overload
from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from services.home_service import HomeService, extract_period_from_result_set
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget

class BaseCanvas(FigureCanvas):
    def __init__(self, parent: QtWidgets.QGridLayout | None = None):
        fig, self.ax = plt.subplots()
        plt.style.use('_mpl-gallery-nogrid')
        super().__init__(fig)
        if parent:
            parent.addWidget(self)

        self.labels = []
        self.values = []

    def _set_data(self, labels, values):
        self.labels = labels
        self.values = values
        self._plot()


    def _plot(self):
        """Method to be overridden by subclasses for specific plotting."""
        raise NotImplementedError("Subclasses must implement this method.")


class IncomeCanvas(BaseCanvas):
    def __init__(self, parent: QtWidgets.QGridLayout | None = None):
        super().__init__(parent)
        self.service = HomeService()
        self.by_month()
    def _plot(self):
        """Plots the data on the income canvas."""
        self.ax.clear()
        self.ax.bar(self.labels, self.values)
        self.draw()

    def by_month(self):
        period = "m"
        self._set_data( *self.service.income_by_month())
        self._set_label_by_period(period)
        self._plot()

    def _set_label_by_period(self, period):
        period_to_represent = {
            "d": "Day",
            "q": "Quarter",
            "m": "Month",
            "y": "Year"
        }

        y_label = "Income"  # This can be overridden in subclasses if needed
        x_label = period_to_represent[period]
        # Add titles and labels
        self.ax.set_title(f"{y_label} by {x_label.lower()}")
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)


class BookingCanvas(BaseCanvas):
    def __init__(self, parent: QtWidgets.QGridLayout | None = None):
        super().__init__(parent)
        self.service = HomeService()
        status = ['CANCELED', 'INCOMING', 'IN TIME', 'OVERDUE']
        # status = None
        self._set_data(*extract_period_from_result_set(self.service.today_booking_by_status(), status))
        self._plot()
    def _plot(self):
        """Plots the data on the booking canvas."""
        self.ax.clear()
        self.ax.pie(self.values, labels=self.labels)  # Correctly use labels for pie chart
        self.draw()
