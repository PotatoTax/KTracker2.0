import gspread
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

import SheetTools
from LoginPage import LoginPage
from SignupPage import SignupPage
from HeaderWidget import Header


class HomePage(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.main_app = main_app
        self.add_widget(Header(self.main_app))
