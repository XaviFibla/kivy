from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView


class ContentNavigationDrawer(MDScrollView):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Virtualio(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        if platform in ['win', 'linux', 'macosx']:
            Window.size = (800, 900)
        self.theme_cls.theme_style = "Light"
        self.icon = "images/virtualioLogo.png"
        self.title ="Virtualio"


if __name__ == '__main__':
    app = MainApp()
    app.run()