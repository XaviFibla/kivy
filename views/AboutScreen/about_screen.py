
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv
from kivy.clock import Clock
from kivymd.uix.list import OneLineListItem

load_kv(__name__)

class AboutScreen(MDScreen):
   def on_enter(self):
       for i in range(20):
            self.ids.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )

    

   
