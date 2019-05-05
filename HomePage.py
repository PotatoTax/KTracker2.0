from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

from HeaderWidget import Header


class PageParent(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.main_app = main_app
        self.add_widget(Header(self.main_app, size_hint_y=.075))

        self.add_widget(HomePage(self.main_app))


class HomePage(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.main_app = main_app
        self.cols = 2

        self.add_widget(HomeLeft(self.main_app, size_hint_x=.3))
        self.add_widget(HomeRight(self.main_app, size_hint_x=.7))


class HomeLeft(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.main_app = main_app
        self.rows = 2
        self.add_widget(UserSummary(self.main_app))
        #self.add_widget(GoalParent(self.main_app))


        self.add_widget(GoalParent(self.main_app))
        #self.add_widget(Label(text="Goal Parent"))


class UserSummary(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.main_app = main_app
        self.rows = 4
        self.ools = 1

        self.add_widget(Label(text="Current User"))

        self.followers = GridLayout()
        self.followers.cols = 3
        self.followers.add_widget(Label(text="100"))
        self.followers.add_widget(Label(text="100"))
        self.followers.add_widget(Label(text="1000"))
        self.add_widget(self.followers)

        self.add_widget(Label(text="Latest Activity"))

        self.training_log = Button(text="Training Log")
        self.training_log.bind(on_press=self.goto_training_log)
        self.add_widget(self.training_log)

    def goto_training_log(self, instance):
        self.main_app.screen_manager.current = "Training Log"


class GoalParent(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.main_app = main_app

        self.screen_manager = ScreenManager()

        print("GoalParent")
        self.run = SportParent(self.main_app, self)
        screen = Screen(name="Run")
        screen.add_widget(self.run)
        self.screen_manager.add_widget(screen)

        self.bike = SportParent(self.main_app, self)
        screen = Screen(name="Bike")
        screen.add_widget(self.bike)
        self.screen_manager.add_widget(screen)

        self.swim = SportParent(self.main_app, self)
        screen = Screen(name="Swim")
        screen.add_widget(self.swim)
        self.screen_manager.add_widget(screen)


class SportParent(GridLayout):
    def __init__(self, main_app, parent, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        print("RunParent")
        self.add_widget(GoalsHeader(parent, size_hint_y=.075))
        #self.add_widget(self.header)

        #self.add_widget(SportGoals(main_app))


class GoalsHeader(GridLayout):
    def __init__(self, parent, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.sm = parent

        self.run = Button(text="Run")
        self.run.bind(on_press=self.goto_run)
        self.add_widget(self.run)

        self.bike = Button(text="Bike")
        self.bike.bind(on_press=self.goto_bike)
        self.add_widget(self.bike)

        self.swim = Button(text="Swim")
        self.swim.bind(on_press=self.goto_swim)
        self.add_widget(self.swim)

    def goto_run(self, instance):
        self.sm.screen_manager.current = "Run"

    def goto_bike(self, instance):
        self.sm.screen_manager.current = "Bike"

    def goto_swim(self, instance):
        self.sm.screen_manager.current = "Swim"


class SportGoals(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        print("SportGoals")
        self.main_app = main_app
        self.rows = 1
        self.cols = 1
        self.add_widget(Label(text="DATA HERE"))
        '''
        self.add_widget(Label(text="THIS WEEK"))
        self.add_widget(Label(text="50 mi"))

        self.visuals = GridLayout()
        self.visuals.cols = 2
        self.visuals.add_widget(Label(text="Graph"))  # TODO: Add visuals
        self.visuals.add_widget(Label(text="Circle"))
        self.add_widget(self.visuals)

        self.week_totals = GridLayout()
        self.week_totals.cols = 2
        self.week_totals.add_widget(Label(text="10h10m"))
        self.week_totals.add_widget(Label(text="1,500 ft"))
        self.add_widget(self.week_totals)

        self.add_widget(Label(text="THIS YEAR"))
        self.add_widget(Label(text="Progress Bar"))  # TODO: Progress bar

        self.goals = Button(text="Manage Your Goals")
        self.goals.bind(on_press=self.goto_goals)
        self.add_widget(self.goals)

    def goto_goals(self, instance):
        self.main_app.screen_manager.current = "My Goals"
        '''


class HomeRight(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.main_app = main_app
        self.cols = 1
        self.add_widget(ActivityWidgets(0, self.main_app))
        self.add_widget(ActivityWidgets(1, self.main_app))
        self.add_widget(ActivityWidgets(2, self.main_app))
        self.add_widget(ActivityWidgets(3, self.main_app))


class ActivityWidgets(GridLayout):
    def __init__(self, num, main_app, **kwargs):
        super().__init__(**kwargs)
        self.main_app = main_app
        self.data = self.main_app.activity_data.activity_list[num]
        self.cols = 1
        self.rows = 4

        self.user_date = GridLayout()
        self.user_date.cols = 1
        self.user_date.add_widget(Label(text=self.main_app.user_data['Username']))
        self.user_date.add_widget(Label(text=self.data["Date"]))
        self.add_widget(self.user_date)

        self.name_type = GridLayout()
        self.name_type.cols = 2
        self.name_type.add_widget(Label(text=self.data["Name"]))
        self.name_type.add_widget(Label(text=self.data["Type"]))
        self.add_widget(self.name_type)

        self.activity_data = GridLayout()
        self.activity_data.cols = 3

        self.activity_data.distance = GridLayout()
        self.activity_data.distance.cols = 1
        self.activity_data.distance.add_widget(Label(text="Distance"))
        self.activity_data.distance.add_widget(Label(text=str(self.data["Distance"])))
        self.activity_data.add_widget(self.activity_data.distance)

        self.activity_data.pace = GridLayout()
        self.activity_data.pace.cols = 1
        self.activity_data.pace.add_widget(Label(text="Pace"))
        self.activity_data.pace.add_widget(Label(text="7:00 /mi"))
        self.activity_data.add_widget(self.activity_data.pace)

        self.activity_data.time = GridLayout()
        self.activity_data.time.cols = 1
        self.activity_data.time.add_widget(Label(text="Time"))
        self.activity_data.time.add_widget(Label(text=str(self.data["Time"])))
        self.activity_data.add_widget(self.activity_data.time)

        self.add_widget(self.activity_data)

        self.add_widget(Label())
