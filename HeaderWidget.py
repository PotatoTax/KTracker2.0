import gspread
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import SheetTools
from LoginPage import LoginPage
from SignupPage import SignupPage


class Header(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.cols = 10
        self.main_app = main_app

        self.home = Button(text="KTracker 2.0")
        self.home.bind(on_press=self.goto_home)
        self.add_widget(self.home)

        self.dashboard = DropDown()
        for item in [["Activity Feed", self.goto_home]]:
            btn = Button(text=item[0], size_hint_y=None, height=30)
            btn.bind(on_press=item[1])
            self.dashboard.add_widget(btn)
        self.dashboard_main = Button(text="Dashboard", valign='top', size_hint=(None, None))
        self.dashboard_main.bind(on_release=self.dashboard.open)
        self.add_widget(self.dashboard_main)

    def goto_home(self, instance):
        self.main_app.screen_manager.current = "Home"
