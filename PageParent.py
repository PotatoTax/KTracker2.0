from kivy.uix.gridlayout import GridLayout


class PageParent(GridLayout):
    def __init__(self, main_app, header, page, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.main_app = main_app
        self.add_widget(header(self.main_app, size_hint_y=.075))

        self.add_widget(page(self.main_app))
