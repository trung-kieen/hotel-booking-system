from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from utils import query as custom_query
from matplotlib.backends.qt_compat import QtWidgets
import matplotlib.pyplot as plt

from services.home_service import HomeService, extract_result_set
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QLayout, QWidget

class BaseCanvas(FigureCanvas):
    def __init__(self, parent_layout = QtWidgets.QGridLayout, width=3, height=5, dpi = 120):
        fig, self.ax = plt.subplots(figsize=(width, height))
        fig, self.ax = plt.subplots()
        plt.style.use('_mpl-gallery-nogrid')
        super().__init__(fig)

        parent_layout.addWidget(self)
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
    def __init__(self, parent_layout ):
        super().__init__(parent_layout)
        self.service = HomeService()
        self.by_month()
        # self.period = custom_query.MONTH_PERIOD

    def _plot(self):
        """Plots the data on the income canvas."""
        self.ax.clear()
        bars = self.ax.bar(self.labels, self.values)

        self._set_label_by_period(self.period)
        # Annotate each bar with its value
        for bar in bars:
            height = bar.get_height()
            self.ax.text(
                bar.get_x() + bar.get_width() / 2,  # x position: center of the bar
                height,  # y position: height of the bar
                f'{height:.2f}',  # format the value
                ha='center',  # horizontal alignment
                va='bottom'  # vertical alignment
            )

        self.draw()


    def by_day(self):
        self.period = custom_query.DAY_PERIOD
        self._set_data(*self.service.income_by_period(self.period))
        self._plot()

    def by_month(self):
        self.period = custom_query.MONTH_PERIOD
        self._set_data(*self.service.income_by_period(self.period))
        self._plot()

    def _set_label_by_period(self, period):
        period_to_represent = {
            "d": "Day",
            "q": "Quarter",
            "m": "Month",
            "y": "Year"
        }

        y_label = "Income"
        x_label = period_to_represent[period]
        # Add titles and labels
        self.ax.set_title(f"Revenue")
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)


class BookingCanvas(BaseCanvas):
    def __init__(self, parent_layout):
        super().__init__(parent_layout)
        self.service = HomeService()
        # status = ['CANCELED', 'INCOMING', 'IN TIME', 'OVERDUE']
        status = None
        self._set_data(*extract_result_set(self.service.today_booking_by_status(), status))
        self._plot()
    def _plot(self):
        """Plots the data on the booking canvas."""
        self.ax.clear()
        total = sum(self.values)
        self.ax.pie(
            self.values,
            labels=self.labels,
            autopct='%.1f%%',
            # startangle=100,
            radius=0.5
        )

        # Display a summary to the right of the chart
        summary_text = "\n".join(f"{label}: {value}" for label, value in zip(self.labels, self.values))
        self.ax.text(0.9, 0.4, summary_text,
                     ha='left',
                     horizontalalignment='center',
                     verticalalignment='center',
                     transform=self.ax.transAxes)
        self.ax.axis('equal')

        self.ax.set_title(f"Current booking status", loc  = "left")
        self.draw()
