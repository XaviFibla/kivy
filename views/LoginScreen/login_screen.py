
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv


load_kv(__name__)

class LoginScreen(MDScreen):
    def open(self):
        app = MDApp.get_running_app()
        self.ids.username.focus = True
        app.switch_screen('login')

    def clear(self):
        self.ids.username.text = ""
        self.ids.password.text = ""
    def do_login(self):
        print(self.ids.username.text)
        app = MDApp.get_running_app()
        app.switch_screen('virtualio')
        self.clear()
    

        

    

   
