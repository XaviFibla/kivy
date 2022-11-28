
import json
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDFloatingActionButton

load_kv(__name__)

class InventoryScreen(MDScreen):
 
    def on_enter(self):
        print("Torno a entrar")
        self.ids.box.add_widget(
            MDFloatingActionButton(
                        icon="qrcode",
                        type="standard",
                        theme_icon_color="Custom",
                        md_bg_color="#fefbff",
                        icon_color= "#6851a5",
                        pos_hint= {"center_x": .9, "center_y": .8},
                        on_release=self.camara
                    ))
        for i in range(20):
                self.ids["container"].add_widget(
                OneLineListItem(text=f"Single-line item {i}",id=str(i),on_press=self.print)
                )
        self.list_posts()

    def print(self,row):
        print (f"Pressed {row.id}")
        #app = MDApp.get_running_app()
        #app.switch_screen('login')
    def camara(self, *args):
        print("Obrir Camara")
        app = MDApp.get_running_app()
        app.sm.get_screen('inventory-detail').open("ID_PASSED")
      

    def list_posts(self):
        self.ids["container"].clear_widgets()
        with open('assets/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids["container"].add_widget(
                OneLineListItem(text=f"User {username}",id=username,on_press=self.print)
                )
               