import os

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import gspread
import SheetTools


class SignupPage(GridLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.main_app = main_app

        self.add_widget(Label(text="Username:"))

        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password:"))

        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label(text="Confirm Password:"))

        self.confirm_password = TextInput(multiline=False)
        self.add_widget(self.confirm_password)

        self.signup = Button(text="Login")
        self.signup.bind(on_press=self.goto_login)
        self.add_widget(self.signup)

        self.login = Button(text="Sign Up")
        self.login.bind(on_press=self.signup_button)
        self.add_widget(self.login)

    def goto_login(self, instance):
        self.main_app.screen_manager.current = "Login"

    def signup_button(self, instance):
        username = self.username.text
        password = self.password.text
        confirm_password = self.confirm_password.text

        if not username or not password or not confirm_password:
            return False

        print(f"Attempted signup with {username}:{password}:{confirm_password}")

        result = SheetTools.add_user(username, password, confirm_password)

        if result == 1:
            None
            # Already User TODO: Inform user of event

        elif result == 2:
            print("Valid Credentials")
            with open("saved_creds.txt", "w") as f:
                f.write(f"{username},{password}")
            self.main_app.screen_manager.current = "Home"

        elif result == 3:
            None
            # Mismatching Passwords TODO: Inform user of event
