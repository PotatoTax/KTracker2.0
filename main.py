import gspread
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

import SheetTools
from LoginPage import LoginPage
from SignupPage import SignupPage
from HomePage import HomePage
from MyActivitiesPage import MyActivitiesPage
from TrainingLogPage import TrainingLogPage
from PageParent import PageParent
from HeaderWidget import Header
from ActivityDataObject import ActivityData
kivy.require("1.10.1")


class KTrackerApp(App):
    def build(self):
        self.activity_data = None
        self.user_data = None

        self.home_page = None
        self.my_activities_page = None

        self.screen_manager = ScreenManager()

        self.login_page = LoginPage(self)
        screen = Screen(name="Login")
        screen.add_widget(self.login_page)
        self.screen_manager.add_widget(screen)

        self.signup_page = SignupPage(self)
        screen = Screen(name="Signup")
        screen.add_widget(self.signup_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def secondary_build(self):
        self.home_page = PageParent(self, Header, HomePage)
        screen = Screen(name="Home")
        screen.add_widget(self.home_page)
        self.screen_manager.add_widget(screen)

        self.my_activities_page = PageParent(self, Header, MyActivitiesPage)
        screen = Screen(name="My Activities")
        screen.add_widget(self.my_activities_page)
        self.screen_manager.add_widget(screen)

        self.training_log_page = PageParent(self, Header, TrainingLogPage)
        screen = Screen(name="Training Log")
        screen.add_widget(self.training_log_page)
        self.screen_manager.add_widget(screen)

    def load_user_data(self):
        self.activity_data = ActivityData()


if __name__ == "__main__":
    main_app = KTrackerApp()
    main_app.run()
