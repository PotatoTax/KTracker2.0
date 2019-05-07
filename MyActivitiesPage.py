from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from HeaderWidget import Header


class PageParent(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.main_app = main_app
        self.add_widget(Header(self.main_app, size_hint_y=.075))

        self.add_widget(MyActivitiesPage(self.main_app))


class MyActivitiesPage(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.main_app = main_app
        self.activity_list = self.main_app.activity_data.activity_list
        self.filtered_list = self.activity_list
        self.num_activities = 10

        self.cols = 1
        self.header = GridLayout(cols=2, size_hint_y=.15)
        self.header.add_widget(Label(text="My Activities", size_hint_x=.5))
        self.header.add_widget(Label(size_hint_x=.5))
        self.add_widget(self.header)

        self.search = GridLayout(cols=3, size_hint_y=.1)
        self.search.keywords = TextInput(multiline=False, size_hint_x=.4)
        self.search.add_widget(self.search.keywords)
        self.search.type = Spinner(text='Select Sport', values=('All', 'Run', 'Bike'), size_hint_x=.4)
        self.search.type.bind(text=self.sport_filter)
        self.search.add_widget(self.search.type)
        self.search.search = Button(text="Search", size_hint_x=.2)
        self.search.search.bind(on_press=lambda e: self.filter())
        self.search.add_widget(self.search.search)
        self.add_widget(self.search)

        self.activity_viewer = GridLayout(cols=1, rows=2)
        self.activity_viewer.header = GridLayout(cols=5, size_hint_y=.1)
        self.activity_viewer.header.add_widget(Label(text="Sport", size_hint_x=.17))
        self.activity_viewer.header.add_widget(Label(text="Date", size_hint_x=.17))
        self.activity_viewer.header.add_widget(Label(text="Title"))
        self.activity_viewer.header.add_widget(Label(text="Time", size_hint_x=.17))
        self.activity_viewer.header.add_widget(Label(text="Distance", size_hint_x=.17))
        self.activity_viewer.add_widget(self.activity_viewer.header)
        self.activity_viewer.body = GridLayout(cols=1, rows=self.num_activities)
        self.activity_viewer.add_widget(self.activity_viewer.body)

        self.show_activities()
        self.add_widget(self.activity_viewer)

    def show_activities(self):
        self.activity_viewer.body.clear_widgets()

        for i in range(self.num_activities):
            self.months = {1: 'January', 2: 'Febuary', 3: 'March', 4: 'April', 5: 'May',
                           6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',
                           12: 'December'}
            activity = self.filtered_list[i]
            row = GridLayout(cols=5)

            row.add_widget(Label(text=activity['Type'], size_hint_x=.17))
            date = activity['Date'][:19]
            year = date[:4]
            month = self.months[int(date[5:7])]
            day = int(date[8:10])
            row.add_widget(Label(text=(month + " " + str(day) + ', ' + year), size_hint_x=.17))

            row.add_widget(Label(text=activity['Name']))

            time = activity['Time'] / 60
            if time > 60:
                hours = int(time / 60)
                minutes = int(time - hours * 60)

                time = str(hours) + "h " + str(minutes) + "m"
            else:
                minutes = int(time)
                seconds = int(time % 1 * 60)
                time = str(minutes) + "m " + str(seconds) + "s"
            row.add_widget(Label(text=time, size_hint_x=.17))

            row.add_widget(Label(text=str(activity['Distance']) + " mi", size_hint_x=.17))
            self.activity_viewer.body.add_widget(row)

    def filter(self):
        print("Filtering activities")

        keywords = self.search.keywords.text
        print(keywords)

        new_list = []

        for a in self.activity_list:
            if keywords in a["Name"]:
                new_list.append(a)

        self.filtered_list = new_list
        if len(self.filtered_list) < 10:
            self.num_activities = len(self.filtered_list)
        else:
            self.num_activities = 10
        self.show_activities()

    def sport_filter(self, spinner, text):
        print("Filtering by sport", text)
        print(spinner)

        new_list = []
        translator = {
            "All": "All",
            "Run": "Run",
            "Bike": "Ride",
        }
        type = translator[text]
        if type == "All":
            self.filtered_list = self.activity_list
            self.show_activities()
            return 1
        for a in self.activity_list:
            if type == a["Type"]:
                new_list.append(a)

        self.filtered_list = new_list
        if len(self.filtered_list) < 10:
            self.num_activities = len(self.filtered_list)
        else:
            self.num_activities = 10
        self.show_activities()

