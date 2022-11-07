from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView

from ctypes import windll, c_int64
windll.user32.SetProcessDpiAwarenessContext(c_int64(-4))


class ContentNavigationDrawer(MDScrollView):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Virtualio(MDScreen):
    pass

class MainApp(MDApp):
    
    sm = None
    
    def build(self):
        if platform in ['win', 'linux', 'macosx']:
            Window.size = (800, 900)
        self.theme_cls.theme_style = "Light"
        self.icon = "images/virtualioLogo.png"
        self.title ="Virtualio"
        self.sm = self.root
        return self.switch_screen('login')

    def switch_screen(self, screen_name='login'):
         self.sm.current = screen_name
    

if __name__ == '__main__':
    app = MainApp()
    app.run()