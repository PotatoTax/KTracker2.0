from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
import datetime


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
            self.body.add_widget(self.week_view(i))
        self.add_widget(self.body)

    def change_units(self, spinner, text):
        print(text)

    def week_view(self, offset):
        week = GridLayout(cols=8, rows=1)
        week.add_widget(Label(text="Week Totals"))
        current_day = datetime.date.today().toordinal()
        week_day = datetime.date.today().weekday()
        week_start = datetime.date.fromordinal(current_day - week_day)
        print(current_day, week_day, week_start)
        for i in range(7):
            day = []
            for a in self.main_app.activity_data.activity_list:
                if current_day - week_day + i - offset*7 == self.str_to_date(a):
                    day.append(a)
            print(day)
            mileage = sum([a["Distance"] for a in day])
            if mileage == 0:
                if current_day - week_day + i - offset*7 == current_day:
                    week.add_widget(Label(text="Today"))
                elif current_day - week_day + i - offset*7 > current_day:
                    week.add_widget(Label())
                else:
                    week.add_widget(Label(text="Rest"))
            else:
                week.add_widget(Label(text=str(round(mileage, 1))))
        return week

    def str_to_date(self, a):
        d = [int(x) for x in a["Date"].split()[0].split("-")]
        return datetime.date.toordinal(datetime.date(d[0], d[1], d[2]))