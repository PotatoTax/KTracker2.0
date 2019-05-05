from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Header(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.cols = 6
        self.main_app = main_app

        self.home = Button(text="KTracker 2.0")
        self.home.bind(on_press=self.goto_home)
        self.add_widget(self.home)

        self.dashboard = DropDown()
        for item in [["Activity Feed", self.goto_home], ["My Goals", self.goto_goals]]:
            btn = Button(text=item[0], size_hint_y=None, height=40)
            btn.bind(on_press=item[1])
            self.dashboard.add_widget(btn)
        self.dashboard_main = Button(text="Dashboard")
        self.dashboard_main.bind(on_release=self.dashboard.open)
        self.add_widget(self.dashboard_main)

        self.training = DropDown()
        for item in [["Training Log", self.goto_training_log], ["My Activities", self.goto_my_activities]]:
            btn = Button(text=item[0], size_hint_y=None, height=40)
            btn.bind(on_press=item[1])
            self.training.add_widget(btn)
        self.training_main = Button(text="Training")
        self.training_main.bind(on_release=self.training.open)
        self.add_widget(self.training_main)

        self.add_widget(Label())

        self.profile = DropDown()
        for item in [["My Profile", self.goto_profile], ["Settings", self.goto_settings]]:
            btn = Button(text=item[0], size_hint_y=None, height=40)
            btn.bind(on_press=item[1])
            self.profile.add_widget(btn)
        self.profile_main = Button(text="Profile")
        self.profile_main.bind(on_release=self.profile.open)
        self.add_widget(self.profile_main)

        self.add = DropDown()
        for item in [["Upload Activity", self.goto_upload_activity], ["Create Post", self.goto_create_post]]:
            btn = Button(text=item[0], size_hint_y=None, height=40)
            btn.bind(on_press=item[1])
            self.add.add_widget(btn)
        self.add_main = Button(text="Add")
        self.add_main.bind(on_release=self.add.open)
        self.add_widget(self.add_main)

    def goto_home(self, instance):
        self.main_app.screen_manager.current = "Home"

    def goto_goals(self, instance):
        self.main_app.screen_manager.current = "My Goals"

    def goto_training_log(self, instance):
        self.main_app.screen_manager.current = "Training Log"

    def goto_my_activities(self, instance):
        self.main_app.screen_manager.current = "My Activities"

    def goto_profile(self, instance):
        self.main_app.screen_manager.current = "Profile"

    def goto_settings(self, instance):
        self.main_app.screen_manager.current = "Settings"

    def goto_upload_activity(self, instance):
        self.main_app.screen_manager.current = "Upload Activity"

    def goto_create_post(self, instance):
        self.main_app.screen_manager.current = "Create Post"
