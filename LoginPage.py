import os

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import gspread
import SheetTools


class LoginPage(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.main_app = main_app

        if os.path.isfile("saved_creds.txt"):
            with open("saved_creds.txt", "r") as f:
                d = f.read().split(",")
                prev_username = d[0]
                prev_password = d[1]
        else:
            prev_username = ""
            prev_password = ""

        self.add_widget(Label(text="Username:"))

        self.username = TextInput(text=prev_username, multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password:"))

        self.password = TextInput(text=prev_password, multiline=False)
        self.add_widget(self.password)

        self.signup = Button(text="Sign Up")
        self.signup.bind(on_press=self.goto_signup)
        self.add_widget(self.signup)

        self.login = Button(text="Login")
        self.login.bind(on_press=self.login_button)
        self.add_widget(self.login)

    def goto_signup(self, instance):
        self.main_app.screen_manager.current = "Signup"

    def login_button(self, instance):
        username = self.username.text
        password = self.password.text

        if not username or not password:
            return False

        print(f"Attempted login with {username}:{password}")

        try:
            SheetTools.get_user_data(username)
            if SheetTools.get_password(username) == password:
                print("Valid Credentials")
                with open("saved_creds.txt", "w") as f:
                    f.write(f"{username},{password}")
                self.main_app.screen_manager.current = "Home"
            else:
                print("Invalid Credentials")
        except gspread.exceptions.WorksheetNotFound:
            print("Invalid Credentials")
