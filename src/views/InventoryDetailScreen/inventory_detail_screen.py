

       
import json
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from utils import load_kv
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDFloatingActionButton

load_kv(__name__)

class InventoryDetailScreen(MDScreen):

    def on_enter(self):
        for i in range(20):
                self.ids["container"].add_widget(
                OneLineListItem(text=f"Single-line item {i}",on_press=self.print)
                )
    def print(self,row):
        print (f"Pressed {row.id}")
     
    def close(self,*args):
        print (f"Pressed CLOSE")
        app = MDApp.get_running_app()
        app.switch_screen('virtualio')
 

  

    