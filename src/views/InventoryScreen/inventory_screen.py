
import json
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv
from kivy.clock import Clock
from kivymd.uix.list import OneLineListItem

load_kv(__name__)

class InventoryScreen(MDScreen):
    def on_enter(self):
        print("Torno a entrar")
        for i in range(20):
                self.ids["container"].add_widget(
                OneLineListItem(text=f"Single-line item {i}",id=str(i),on_press=self.print)
                )
        self.list_posts()

    def print(self,row):
        print (f"Pressed {row.id}")

    def list_posts(self):
        self.ids["container"].clear_widgets()
        with open('assets/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids["container"].add_widget(
                OneLineListItem(text=f"User {username}",id=username,on_press=self.print)
                )
               