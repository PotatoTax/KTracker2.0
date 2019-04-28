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

kivy.require("1.10.1")


class KTrackerApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.login_page = LoginPage(self)
        screen = Screen(name="Login")
        screen.add_widget(self.login_page)
        self.screen_manager.add_widget(screen)

        self.signup_page = SignupPage(self)
        screen = Screen(name="Signup")
        screen.add_widget(self.signup_page)
        self.screen_manager.add_widget(screen)

        self.home_page = HomePage(self)
        screen = Screen(name="Home")
        screen.add_widget(self.home_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    main_app = KTrackerApp()
    main_app.run()
