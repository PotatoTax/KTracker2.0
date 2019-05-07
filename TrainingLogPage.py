from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
import datetime

from HeaderWidget import Header


class PageParent(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.main_app = main_app
        self.add_widget(Header(self.main_app, size_hint_y=.075))

        self.add_widget(TrainingLogPage(self.main_app))


class TrainingLogPage(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.main_app = main_app
        self.cols = 1
        self.rows = 2
        self.months = {1: 'January', 2: 'Febuary', 3: 'March', 4: 'April', 5: 'May',
                       6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',
                       12: 'December'}
        self.curr_month = datetime.date.today().month
        self.curr_year = str(datetime.date.today().year)

        self.heading = GridLayout(cols=3, size_hint_y=.1)
        self.heading.add_widget(Label(text="Training Log"))
        self.heading.sport_select = Spinner(text="Run", values=("Run", "Bike"))
        self.heading.add_widget(self.heading.sport_select)
        self.add_widget(self.heading)

        self.body = GridLayout(cols=1, rows=6)
        self.body.add_widget(Label(text=(self.months[self.curr_month] + " " + self.curr_year)))
        self.body.head = GridLayout(cols=8, rows=1)
        self.body.head.units = Spinner(text="Distance", values=("Distance", "Time"))
        self.body.head.units.bind(text=self.change_units)
        self.body.head.add_widget(self.body.head.units)
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            self.body.head.add_widget(Label(text=day))
        self.body.add_widget(self.body.head)

        for i in range(4):
            self.body.add_widget(self.week_view())
        self.add_widget(self.body)

    def change_units(self, spinner, text):
        print(text)

    def week_view(self):
        week = GridLayout(cols=8, rows=1)
        week.add_widget(Label(text="Week Totals"))
        for i in range(1, 8):
            week.add_widget(Label(text="Day "+str(i)))
        return week